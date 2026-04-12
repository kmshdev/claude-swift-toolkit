#!/usr/bin/env python3
"""Validate the canonical repo-scoped Codex operating layer."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE_PATH = ROOT / ".agents" / "plugins" / "marketplace.json"
MCP_PATH = ROOT / ".mcp.json"
CONFIG_PATH = ROOT / ".codex" / "config.toml"
HOOKS_PATH = ROOT / ".codex" / "hooks.json"
AGENTS_DIR = ROOT / ".codex" / "agents"
PARITY_SOURCE_PATH = ROOT / ".codex" / "parity-source.toml"
CONTRACT_GENERATOR_PATH = ROOT / "scripts" / "generate_codex_parity_contract.py"
CONTRACT_PATH = ROOT / ".codex" / "contracts" / "parity-contract.json"
ALLOWED_FRONTMATTER_KEYS = {"name", "description"}
TOKEN_CHARS = r"A-Za-z0-9_"
PRIMARY_SKILL_NAME = "codex-operating-layer"
LEGACY_XCODE_BRIDGE = "xcode" "buildmcp"
LEGACY_XCODE_BRIDGE_TITLE = "Xcode" "BuildMCP"
LEGACY_XCODE_TOOL_PREFIX = "mcp__xcode" "buildmcp__"


def compile_token_pattern(
    *tokens: str, leading_chars: str = TOKEN_CHARS, trailing_chars: str = TOKEN_CHARS
) -> re.Pattern[str]:
    """Compile a token-aware regex pattern."""
    escaped = "|".join(re.escape(token) for token in tokens)
    return re.compile(rf"(?<![{leading_chars}])(?:{escaped})(?![{trailing_chars}])")


UNSAFE_PATTERNS = (
    compile_token_pattern(
        "/brainstorm",
        "/write-plan",
        "/execute-plan",
        "/build",
        "/fix-build",
        "/run-app",
        "/review",
        "/review-ui",
        "/refactor-view",
        "/swift-style",
        "/test",
        trailing_chars=TOKEN_CHARS + "-",
    ),
    compile_token_pattern(
        "macos-architect",
        "code-architect",
        "code-explorer",
        "ui-developer",
        "ios-developer",
        "swift-reviewer",
        "code-reviewer",
        leading_chars=TOKEN_CHARS + "-",
        trailing_chars=TOKEN_CHARS + "-",
    ),
    compile_token_pattern(LEGACY_XCODE_BRIDGE, LEGACY_XCODE_BRIDGE_TITLE),
    re.compile(re.escape(LEGACY_XCODE_TOOL_PREFIX)),
    compile_token_pattern(
        "session_show_defaults",
        "session_set_defaults",
        "build_run_sim",
        "build_sim",
        "test_sim",
        "launch_app_sim",
        "stop_app_sim",
        "discover_projs",
        "list_sims",
        "snapshot_ui",
        "start_sim_log_cap",
        "stop_sim_log_cap",
        "debug_attach_sim",
    ),
    re.compile(rf"(?<![{TOKEN_CHARS}])xcodebuild\s+-list(?![{TOKEN_CHARS}])"),
)


def load_json(path: Path) -> object:
    """Load JSON with a stable error message."""
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        raise ValueError(f"{path}: invalid JSON ({exc})") from exc



def load_toml(path: Path) -> dict[str, object]:
    """Load TOML with a stable error message."""
    try:
        return tomllib.loads(path.read_text())
    except Exception as exc:
        raise ValueError(f"{path}: invalid TOML ({exc})") from exc



def ensure_repo_relative_path(base_dir: Path, path_value: str) -> tuple[Path | None, list[str]]:
    """Resolve a relative path and ensure it stays inside the repo."""
    errors: list[str] = []
    if not path_value.startswith("./"):
        errors.append(f"{base_dir}: path '{path_value}' must start with './'")
        return None, errors
    resolved = (base_dir / path_value).resolve()
    try:
        resolved.relative_to(ROOT.resolve())
    except ValueError:
        errors.append(f"{base_dir}: path '{path_value}' escapes the repository root")
        return None, errors
    if not resolved.exists():
        errors.append(f"{base_dir}: path '{path_value}' does not exist")
        return None, errors
    return resolved, errors



def parse_yaml_scalar(value: str, *, path: Path, line_number: int) -> object:
    """Parse a restricted scalar subset used by repo metadata files."""
    if value.startswith(("'", '"')):
        quote = value[0]
        if len(value) < 2 or not value.endswith(quote):
            raise ValueError(f"{path}:{line_number}: unterminated quoted scalar")
        return value[1:-1]
    if value == "null":
        return None
    if value == "true":
        return True
    if value == "false":
        return False
    return value



def load_simple_yaml_text(text: str, *, path: Path, start_line: int = 1) -> object:
    """Parse the small YAML subset used in SKILL frontmatter and openai.yaml."""
    entries: list[tuple[int, str, int]] = []
    for line_number, raw_line in enumerate(text.splitlines(), start=start_line):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        if indent % 2 != 0:
            raise ValueError(f"{path}:{line_number}: indentation must use multiples of 2 spaces")
        entries.append((indent, stripped, line_number))

    if not entries:
        raise ValueError(f"{path}: empty YAML file")

    def parse_block(index: int, indent: int) -> tuple[object, int]:
        is_list = entries[index][1].startswith("- ")
        if is_list:
            items: list[object] = []
            while index < len(entries):
                current_indent, stripped, line_number = entries[index]
                if current_indent < indent:
                    break
                if current_indent != indent:
                    raise ValueError(f"{path}:{line_number}: unexpected indentation")
                if not stripped.startswith("- "):
                    raise ValueError(f"{path}:{line_number}: mixed YAML collection types")
                item, index = parse_list_item(index, indent)
                items.append(item)
            return items, index

        mapping: dict[str, object] = {}
        while index < len(entries):
            current_indent, stripped, line_number = entries[index]
            if current_indent < indent:
                break
            if current_indent != indent:
                raise ValueError(f"{path}:{line_number}: unexpected indentation")
            if stripped.startswith("- "):
                raise ValueError(f"{path}:{line_number}: mixed YAML collection types")
            key, value, index = parse_mapping_entry(index, indent)
            if key in mapping:
                raise ValueError(f"{path}:{line_number}: duplicate key '{key}'")
            mapping[key] = value
        return mapping, index

    def parse_mapping_entry(index: int, indent: int) -> tuple[str, object, int]:
        _, stripped, line_number = entries[index]
        key, separator, raw_value = stripped.partition(":")
        if separator != ":" or not key.strip():
            raise ValueError(f"{path}:{line_number}: invalid mapping entry")
        key = key.strip()
        raw_value = raw_value.lstrip()
        index += 1
        if raw_value:
            return key, parse_yaml_scalar(raw_value, path=path, line_number=line_number), index
        if index < len(entries) and entries[index][0] > indent:
            child_indent = entries[index][0]
            if child_indent != indent + 2:
                raise ValueError(f"{path}:{entries[index][2]}: invalid nested indentation")
            value, index = parse_block(index, child_indent)
            return key, value, index
        return key, None, index

    def parse_list_item(index: int, indent: int) -> tuple[object, int]:
        _, stripped, line_number = entries[index]
        item_text = stripped[2:].strip()
        index += 1
        if not item_text:
            if index < len(entries) and entries[index][0] > indent:
                child_indent = entries[index][0]
                if child_indent != indent + 2:
                    raise ValueError(f"{path}:{entries[index][2]}: invalid nested indentation")
                return parse_block(index, child_indent)
            return None, index

        key, separator, raw_value = item_text.partition(":")
        if separator != ":":
            return parse_yaml_scalar(item_text, path=path, line_number=line_number), index

        item: dict[str, object] = {}
        key = key.strip()
        raw_value = raw_value.lstrip()
        if raw_value:
            item[key] = parse_yaml_scalar(raw_value, path=path, line_number=line_number)
            if index < len(entries) and entries[index][0] > indent:
                child_indent = entries[index][0]
                if child_indent != indent + 2:
                    raise ValueError(f"{path}:{entries[index][2]}: invalid nested indentation")
                nested, index = parse_block(index, child_indent)
                if not isinstance(nested, dict):
                    raise ValueError(
                        f"{path}:{entries[index - 1][2]}: list item metadata must be a mapping"
                    )
                for nested_key, nested_value in nested.items():
                    if nested_key in item:
                        raise ValueError(
                            f"{path}:{entries[index - 1][2]}: duplicate key '{nested_key}'"
                        )
                    item[nested_key] = nested_value
            return item, index

        if index < len(entries) and entries[index][0] > indent:
            child_indent = entries[index][0]
            if child_indent != indent + 2:
                raise ValueError(f"{path}:{entries[index][2]}: invalid nested indentation")
            value, index = parse_block(index, child_indent)
            item[key] = value
            return item, index

        item[key] = None
        return item, index

    if entries[0][0] != 0:
        raise ValueError(f"{path}:{entries[0][2]}: top-level keys must start at column 1")
    payload, next_index = parse_block(0, 0)
    if next_index != len(entries):
        raise ValueError(f"{path}:{entries[next_index][2]}: trailing YAML content")
    return payload



def load_simple_yaml(path: Path) -> object:
    """Load a YAML file using the limited parser."""
    return load_simple_yaml_text(path.read_text(), path=path)



def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    """Parse skill frontmatter and body."""
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter block")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"{path}: unterminated frontmatter block")
    payload = load_simple_yaml_text(text[4:end], path=path, start_line=2)
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: frontmatter must be a top-level mapping")

    frontmatter: dict[str, str] = {}
    for key, value in payload.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{path}: frontmatter '{key}' must be a non-empty string")
        frontmatter[key] = value
    return frontmatter, text[end + 5 :]



def validate_skill_file(path: Path) -> tuple[list[str], str | None]:
    """Validate a single SKILL.md file and return its name when valid."""
    errors: list[str] = []
    try:
        frontmatter, body = parse_frontmatter(path)
    except ValueError as exc:
        return [str(exc)], None

    missing = sorted(ALLOWED_FRONTMATTER_KEYS - frontmatter.keys())
    if missing:
        errors.append(f"{path}: missing required frontmatter keys: {', '.join(missing)}")

    extras = sorted(set(frontmatter) - ALLOWED_FRONTMATTER_KEYS)
    if extras:
        errors.append(
            f"{path}: unsupported frontmatter keys for Codex skill: {', '.join(extras)}"
        )

    for pattern in UNSAFE_PATTERNS:
        match = pattern.search(body)
        if match:
            errors.append(f"{path}: contains Codex-unsafe reference '{match.group(0)}'")
    return errors, frontmatter.get("name")



def validate_openai_metadata(path: Path) -> list[str]:
    """Validate `agents/openai.yaml` files."""
    errors: list[str] = []
    try:
        payload = load_simple_yaml(path)
    except ValueError as exc:
        return [str(exc)]

    if not isinstance(payload, dict):
        return [f"{path}: expected top-level YAML mapping"]

    interface = payload.get("interface")
    if not isinstance(interface, dict):
        return [f"{path}: missing top-level interface block"]

    display_name = interface.get("display_name")
    if not isinstance(display_name, str) or not display_name.strip():
        errors.append(f"{path}: missing interface.display_name")

    short_description = interface.get("short_description")
    if not isinstance(short_description, str) or not short_description.strip():
        errors.append(f"{path}: missing interface.short_description")

    default_prompt = interface.get("default_prompt")
    if default_prompt is not None and (
        not isinstance(default_prompt, str) or not default_prompt.strip()
    ):
        errors.append(f"{path}: interface.default_prompt must be a non-empty string")

    dependencies = payload.get("dependencies")
    if dependencies is None:
        return errors
    if not isinstance(dependencies, dict):
        return errors + [f"{path}: dependencies must be a mapping when present"]

    tools = dependencies.get("tools")
    if tools is None:
        return errors
    if not isinstance(tools, list):
        return errors + [f"{path}: dependencies.tools must be a list when present"]

    for tool in tools:
        if not isinstance(tool, dict):
            errors.append(f"{path}: each dependencies.tools entry must be a mapping")
            continue
        tool_type = tool.get("type")
        tool_value = tool.get("value")
        if not isinstance(tool_type, str) or not tool_type.strip():
            errors.append(f"{path}: dependencies.tools entries must include type")
        if not isinstance(tool_value, str) or not tool_value.strip():
            errors.append(f"{path}: dependencies.tools entries must include value")
    return errors



def validate_mcp_config(path: Path) -> list[str]:
    """Validate a Codex MCP config file."""
    errors: list[str] = []
    try:
        payload = load_json(path)
    except ValueError as exc:
        return [str(exc)]
    if not isinstance(payload, dict):
        return [f"{path}: expected JSON object"]

    servers = payload.get("mcpServers")
    if not isinstance(servers, dict) or not servers:
        return [f"{path}: expected a non-empty 'mcpServers' object"]

    for server_name, server_config in servers.items():
        if not isinstance(server_name, str) or not server_name:
            errors.append(f"{path}: MCP server names must be non-empty strings")
            continue
        if not isinstance(server_config, dict):
            errors.append(f"{path}: MCP server '{server_name}' must be an object")
            continue
        command = server_config.get("command")
        if not isinstance(command, str) or not command:
            errors.append(f"{path}: MCP server '{server_name}' is missing a string command")
        args = server_config.get("args")
        if args is not None and (
            not isinstance(args, list) or any(not isinstance(arg, str) for arg in args)
        ):
            errors.append(f"{path}: MCP server '{server_name}' args must be an array of strings")
        env = server_config.get("env")
        if env is not None and (
            not isinstance(env, dict)
            or any(not isinstance(key, str) or not isinstance(value, str) for key, value in env.items())
        ):
            errors.append(f"{path}: MCP server '{server_name}' env must be string pairs")
    return errors



def validate_root_manifest() -> tuple[list[str], dict[str, object] | None]:
    """Validate the canonical root plugin manifest."""
    errors: list[str] = []
    if not MANIFEST_PATH.is_file():
        return [f"{MANIFEST_PATH}: missing root Codex plugin manifest"], None
    try:
        payload = load_json(MANIFEST_PATH)
    except ValueError as exc:
        return [str(exc)], None
    if not isinstance(payload, dict):
        return [f"{MANIFEST_PATH}: expected JSON object"], None

    name = payload.get("name")
    if not isinstance(name, str) or not name.strip():
        errors.append(f"{MANIFEST_PATH}: missing name")
    skills_path = payload.get("skills")
    if not isinstance(skills_path, str):
        errors.append(f"{MANIFEST_PATH}: missing skills path")
    else:
        _, path_errors = ensure_repo_relative_path(ROOT, skills_path)
        errors.extend(path_errors)
    mcp_servers = payload.get("mcpServers")
    if not isinstance(mcp_servers, str):
        errors.append(f"{MANIFEST_PATH}: missing mcpServers path")
    else:
        _, path_errors = ensure_repo_relative_path(ROOT, mcp_servers)
        errors.extend(path_errors)
    interface = payload.get("interface")
    if not isinstance(interface, dict):
        errors.append(f"{MANIFEST_PATH}: missing interface block")
    else:
        for key in ("displayName", "shortDescription", "longDescription"):
            value = interface.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{MANIFEST_PATH}: missing interface.{key}")
        for key in ("developerName", "category", "websiteURL", "brandColor"):
            value = interface.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{MANIFEST_PATH}: missing interface.{key}")

        capabilities = interface.get("capabilities")
        if not isinstance(capabilities, list) or not capabilities:
            errors.append(f"{MANIFEST_PATH}: interface.capabilities must be a non-empty array")
        elif any(not isinstance(item, str) or not item.strip() for item in capabilities):
            errors.append(f"{MANIFEST_PATH}: interface.capabilities entries must be strings")

        default_prompt = interface.get("defaultPrompt")
        if not isinstance(default_prompt, list) or not default_prompt:
            errors.append(f"{MANIFEST_PATH}: interface.defaultPrompt must be a non-empty array")
        elif any(not isinstance(item, str) or not item.strip() for item in default_prompt):
            errors.append(f"{MANIFEST_PATH}: interface.defaultPrompt entries must be strings")
    return errors, payload



def validate_marketplace(expected_name: str | None) -> list[str]:
    """Validate the repo-root marketplace wrapper."""
    errors: list[str] = []
    if not MARKETPLACE_PATH.is_file():
        return [f"{MARKETPLACE_PATH}: missing marketplace file"]
    try:
        payload = load_json(MARKETPLACE_PATH)
    except ValueError as exc:
        return [str(exc)]
    if not isinstance(payload, dict):
        return [f"{MARKETPLACE_PATH}: expected JSON object"]

    interface = payload.get("interface")
    if not isinstance(interface, dict):
        errors.append(f"{MARKETPLACE_PATH}: missing top-level interface object")
    else:
        display_name = interface.get("displayName")
        if not isinstance(display_name, str) or not display_name.strip():
            errors.append(f"{MARKETPLACE_PATH}: missing interface.displayName")

    plugins = payload.get("plugins")
    if not isinstance(plugins, list):
        return errors + [f"{MARKETPLACE_PATH}: plugins must be an array"]
    if len(plugins) != 1:
        errors.append(f"{MARKETPLACE_PATH}: marketplace must expose exactly one canonical plugin")
        return errors

    plugin = plugins[0]
    if not isinstance(plugin, dict):
        return errors + [f"{MARKETPLACE_PATH}: plugin entry must be an object"]
    name = plugin.get("name")
    if expected_name and name != expected_name:
        errors.append(f"{MARKETPLACE_PATH}: plugin name must match root manifest name")
    source = plugin.get("source")
    if not isinstance(source, dict):
        errors.append(f"{MARKETPLACE_PATH}: plugin entry missing source object")
    else:
        if source.get("source") != "local":
            errors.append(f"{MARKETPLACE_PATH}: source.source must be 'local'")
        if source.get("path") != "./":
            errors.append(f"{MARKETPLACE_PATH}: canonical plugin path must be './'")
    policy = plugin.get("policy")
    if not isinstance(policy, dict):
        errors.append(f"{MARKETPLACE_PATH}: plugin entry missing policy object")
    else:
        installation = policy.get("installation")
        authentication = policy.get("authentication")
        if not isinstance(installation, str) or not installation:
            errors.append(f"{MARKETPLACE_PATH}: plugin entry missing policy.installation")
        if not isinstance(authentication, str) or not authentication:
            errors.append(f"{MARKETPLACE_PATH}: plugin entry missing policy.authentication")
    category = plugin.get("category")
    if not isinstance(category, str) or not category.strip():
        errors.append(f"{MARKETPLACE_PATH}: plugin entry missing category")
    return errors



def resolve_configured_skill_dirs() -> tuple[list[str], dict[str, Path]]:
    """Resolve enabled skill directories from config.toml."""
    errors: list[str] = []
    try:
        payload = load_toml(CONFIG_PATH)
    except ValueError as exc:
        return [str(exc)], {}

    features = payload.get("features")
    if not isinstance(features, dict) or features.get("codex_hooks") is not True:
        errors.append(f"{CONFIG_PATH}: features.codex_hooks must be true")

    agents = payload.get("agents")
    if not isinstance(agents, dict):
        errors.append(f"{CONFIG_PATH}: missing agents table")
    else:
        max_threads = agents.get("max_threads")
        max_depth = agents.get("max_depth")
        if not isinstance(max_threads, int) or max_threads < 1:
            errors.append(f"{CONFIG_PATH}: agents.max_threads must be a positive integer")
        if not isinstance(max_depth, int) or max_depth < 1:
            errors.append(f"{CONFIG_PATH}: agents.max_depth must be a positive integer")

    skills_section = payload.get("skills")
    if not isinstance(skills_section, dict):
        return errors + [f"{CONFIG_PATH}: missing skills table"], {}
    entries = skills_section.get("config")
    if not isinstance(entries, list) or not entries:
        return errors + [f"{CONFIG_PATH}: skills.config must be a non-empty array"], {}

    skill_dirs: dict[str, Path] = {}
    seen_paths: set[Path] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append(f"{CONFIG_PATH}: each skills.config entry must be a table")
            continue
        if entry.get("enabled") is False:
            continue
        path_value = entry.get("path")
        if not isinstance(path_value, str) or not path_value:
            errors.append(f"{CONFIG_PATH}: enabled skill paths must be non-empty strings")
            continue
        if Path(path_value).is_absolute():
            errors.append(f"{CONFIG_PATH}: enabled skill paths must be relative")
            continue
        skill_dir = (CONFIG_PATH.parent / path_value).resolve()
        try:
            skill_dir.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{CONFIG_PATH}: skill path '{path_value}' escapes the repository root")
            continue
        if skill_dir in seen_paths:
            errors.append(f"{CONFIG_PATH}: duplicate skill path '{path_value}'")
            continue
        seen_paths.add(skill_dir)
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.is_file():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        skill_errors, skill_name = validate_skill_file(skill_path)
        errors.extend(skill_errors)
        if skill_name is None:
            continue
        if skill_name in skill_dirs:
            errors.append(f"{CONFIG_PATH}: duplicate skill name '{skill_name}'")
            continue
        metadata_path = skill_dir / "agents" / "openai.yaml"
        if metadata_path.is_file():
            errors.extend(validate_openai_metadata(metadata_path))
        elif skill_name == PRIMARY_SKILL_NAME:
            errors.append(f"{metadata_path}: primary skill must include openai metadata")
        skill_dirs[skill_name] = skill_dir
    return errors, skill_dirs



def extract_repo_script_paths(command: str) -> list[Path]:
    """Extract repo-local script paths from a hook command string."""
    matches = re.findall(r"\.codex/[A-Za-z0-9_./-]+\.py", command)
    return [ROOT / match for match in matches]



def validate_hooks() -> list[str]:
    """Validate `.codex/hooks.json` and its referenced scripts."""
    errors: list[str] = []
    if not HOOKS_PATH.is_file():
        return [f"{HOOKS_PATH}: missing hooks config"]
    try:
        payload = load_json(HOOKS_PATH)
    except ValueError as exc:
        return [str(exc)]
    if not isinstance(payload, dict):
        return [f"{HOOKS_PATH}: expected JSON object"]

    hooks = payload.get("hooks")
    if not isinstance(hooks, dict) or not hooks:
        return [f"{HOOKS_PATH}: missing hooks object"]

    for event_name, groups in hooks.items():
        if not isinstance(groups, list) or not groups:
            errors.append(f"{HOOKS_PATH}: hooks.{event_name} must be a non-empty list")
            continue
        for group in groups:
            if not isinstance(group, dict):
                errors.append(f"{HOOKS_PATH}: matcher groups must be objects")
                continue
            group_hooks = group.get("hooks")
            if not isinstance(group_hooks, list) or not group_hooks:
                errors.append(f"{HOOKS_PATH}: hooks.{event_name} group missing hooks list")
                continue
            for hook in group_hooks:
                if not isinstance(hook, dict):
                    errors.append(f"{HOOKS_PATH}: hook entries must be objects")
                    continue
                hook_type = hook.get("type")
                command = hook.get("command")
                if hook_type != "command":
                    errors.append(f"{HOOKS_PATH}: only command hooks are supported in this repo")
                if not isinstance(command, str) or not command.strip():
                    errors.append(f"{HOOKS_PATH}: command hook missing command string")
                    continue
                for script_path in extract_repo_script_paths(command):
                    if not script_path.is_file():
                        errors.append(f"{HOOKS_PATH}: referenced script missing: {script_path}")
    return errors



def validate_custom_agents() -> tuple[list[str], set[str]]:
    """Validate `.codex/agents/*.toml`."""
    errors: list[str] = []
    if not AGENTS_DIR.is_dir():
        return [f"{AGENTS_DIR}: missing custom agents directory"], set()

    agent_names: set[str] = set()
    agent_files = sorted(AGENTS_DIR.glob("*.toml"))
    if not agent_files:
        errors.append(f"{AGENTS_DIR}: expected at least one custom agent file")
        return errors, agent_names

    for agent_path in agent_files:
        try:
            payload = load_toml(agent_path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        name = payload.get("name")
        description = payload.get("description")
        developer_instructions = payload.get("developer_instructions")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{agent_path}: missing name")
            continue
        if name in agent_names:
            errors.append(f"{agent_path}: duplicate agent name '{name}'")
            continue
        agent_names.add(name)
        if not isinstance(description, str) or not description.strip():
            errors.append(f"{agent_path}: missing description")
        if not isinstance(developer_instructions, str) or not developer_instructions.strip():
            errors.append(f"{agent_path}: missing developer_instructions")
    return errors, agent_names



def validate_parity_source(skill_dirs: dict[str, Path], agent_names: set[str]) -> list[str]:
    """Validate `.codex/parity-source.toml`."""
    errors: list[str] = []
    if not PARITY_SOURCE_PATH.is_file():
        return [f"{PARITY_SOURCE_PATH}: missing parity source file"]
    try:
        payload = load_toml(PARITY_SOURCE_PATH)
    except ValueError as exc:
        return [str(exc)]

    primary_skill = payload.get("primary_skill")
    if not isinstance(primary_skill, str) or primary_skill not in skill_dirs:
        errors.append(f"{PARITY_SOURCE_PATH}: primary_skill must name a configured skill")

    validation_targets = payload.get("validation_targets")
    if not isinstance(validation_targets, list) or not validation_targets:
        errors.append(f"{PARITY_SOURCE_PATH}: validation_targets must be a non-empty array")
    else:
        for target in validation_targets:
            if not isinstance(target, str) or not target:
                errors.append(f"{PARITY_SOURCE_PATH}: validation_targets entries must be strings")
                continue
            if not (ROOT / target).exists():
                errors.append(f"{PARITY_SOURCE_PATH}: validation target missing: {ROOT / target}")

    outcomes = payload.get("outcomes")
    if not isinstance(outcomes, list) or not outcomes:
        return errors + [f"{PARITY_SOURCE_PATH}: outcomes must be a non-empty array"]

    for outcome in outcomes:
        if not isinstance(outcome, dict):
            errors.append(f"{PARITY_SOURCE_PATH}: outcomes must contain tables")
            continue
        for key in ("id", "label", "description"):
            value = outcome.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{PARITY_SOURCE_PATH}: outcome missing {key}")
        skills = outcome.get("skills")
        agents = outcome.get("agents")
        if not isinstance(skills, list) or not skills:
            errors.append(f"{PARITY_SOURCE_PATH}: outcome skills must be a non-empty array")
        else:
            for skill_name in skills:
                if not isinstance(skill_name, str) or skill_name not in skill_dirs:
                    errors.append(
                        f"{PARITY_SOURCE_PATH}: unknown outcome skill '{skill_name}'"
                    )
        if not isinstance(agents, list) or not agents:
            errors.append(f"{PARITY_SOURCE_PATH}: outcome agents must be a non-empty array")
        else:
            for agent_name in agents:
                if not isinstance(agent_name, str) or agent_name not in agent_names:
                    errors.append(
                        f"{PARITY_SOURCE_PATH}: unknown outcome agent '{agent_name}'"
                    )
    return errors



def validate_contract_generation() -> list[str]:
    """Ensure the committed parity contract is current."""
    if not CONTRACT_GENERATOR_PATH.is_file():
        return [f"{CONTRACT_GENERATOR_PATH}: missing parity contract generator"]
    if not CONTRACT_PATH.is_file():
        return [f"{CONTRACT_PATH}: missing generated parity contract"]

    result = subprocess.run(
        [sys.executable, str(CONTRACT_GENERATOR_PATH), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        return []
    output = (result.stderr or result.stdout).strip()
    return [f"{CONTRACT_PATH}: stale or invalid parity contract ({output})"]



def main() -> int:
    """Run Codex operating-layer validation."""
    errors: list[str] = []

    manifest_errors, manifest = validate_root_manifest()
    errors.extend(manifest_errors)
    manifest_name = manifest.get("name") if isinstance(manifest, dict) else None

    errors.extend(validate_marketplace(manifest_name if isinstance(manifest_name, str) else None))
    errors.extend(validate_mcp_config(MCP_PATH))

    config_errors, skill_dirs = resolve_configured_skill_dirs()
    errors.extend(config_errors)
    errors.extend(validate_hooks())

    agent_errors, agent_names = validate_custom_agents()
    errors.extend(agent_errors)
    errors.extend(validate_parity_source(skill_dirs, agent_names))
    errors.extend(validate_contract_generation())

    if errors:
        print("Codex support validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Codex support validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
