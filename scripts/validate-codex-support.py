#!/usr/bin/env python3
"""Validate the canonical repo-scoped Codex operating layer."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.hook_policy.loader import extract_frontmatter as extract_markdown_frontmatter  # noqa: E402
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
README_PATH = ROOT / "README.md"
OPERATING_LAYER_SKILL_PATH = ROOT / ".codex" / "skills" / PRIMARY_SKILL_NAME / "SKILL.md"
LEGACY_XCODE_BRIDGE = "xcode" "buildmcp"
LEGACY_XCODE_BRIDGE_TITLE = "Xcode" "BuildMCP"
LEGACY_XCODE_TOOL_PREFIX = "mcp__xcode" "buildmcp__"
SUPPORTED_HOOK_EVENTS = {"SessionStart", "PreToolUse", "PostToolUse", "Stop"}
NEGATION_PATTERN = re.compile(r"\b(?:do(?:es)? not|must not|cannot|can not|never|without|not)\b", re.IGNORECASE)
README_REQUIRED_PHRASES = (
    "Hooks are repo-scoped and experimental.",
    "`PreToolUse` and `PostToolUse` apply only to `Bash`.",
    "`Stop` remains the authoritative completion gate.",
    "`codex-runtime-doctor` is the diagnosis-only readiness entrypoint.",
)
AGENTS_REQUIRED_PHRASES = (
    "experimental, Bash-only hook policy pack",
    "Use `codex-runtime-doctor` as the diagnosis-only readiness entrypoint",
)
OPERATING_LAYER_REQUIRED_PHRASES = (
    "`codex-runtime-doctor`",
    "experimental, Bash-only for `PreToolUse` / `PostToolUse`",
    "Route runtime readiness questions through `codex-runtime-doctor`",
)
MANIFEST_REQUIRED_PHRASES = (
    "experimental Bash-only hook policy pack",
    "authoritative completion gate",
    "codex-runtime-doctor",
    "diagnosis-only readiness entrypoint",
)


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
    payload, body = extract_markdown_frontmatter(path.read_text(), path=path)
    if not payload:
        raise ValueError(f"{path}: missing frontmatter block")
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: frontmatter must be a top-level mapping")

    frontmatter: dict[str, str] = {}
    for key, value in payload.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{path}: frontmatter '{key}' must be a non-empty string")
        frontmatter[key] = value
    return frontmatter, body



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
    matches = re.findall(r"\.codex/[A-Za-z0-9_./-]+\.(?:py|sh)", command)
    return [ROOT / match for match in matches]


def validate_repo_hook_script_command(command: str, script_paths: list[Path]) -> list[str]:
    """Validate how repo-local hook commands launch their scripts."""
    errors: list[str] = []
    if not script_paths:
        return errors
    if re.search(r"/usr/bin/python3\s+(?!-c\b)", command):
        errors.append(
            f"{HOOKS_PATH}: repo-local hook commands must not pin /usr/bin/python3; "
            "route through the repo-local launcher or another Python 3.11+ entrypoint"
        )
    if "git rev-parse --show-toplevel" in command:
        errors.append(
            f"{HOOKS_PATH}: repo-local hook commands must not resolve the repo root from "
            "process cwd with git rev-parse; use the hook payload cwd instead"
        )
    for script_path in script_paths:
        if not script_path.is_file():
            continue
        if not os.access(script_path, os.X_OK):
            errors.append(f"{HOOKS_PATH}: repo-local hook script must be executable: {script_path}")
            continue
        contents = script_path.read_text()
        first_line = contents.splitlines()[0] if contents else ""
        expected_shebang = "#!/usr/bin/env python3"
        if script_path.suffix == ".sh":
            expected_shebang = "#!/usr/bin/env bash"
        if first_line != expected_shebang:
            errors.append(
                f"{HOOKS_PATH}: repo-local hook script must use '{expected_shebang}': {script_path}"
            )
    return errors



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
        if event_name not in SUPPORTED_HOOK_EVENTS:
            errors.append(f"{HOOKS_PATH}: unsupported hook event '{event_name}'")
        if not isinstance(groups, list) or not groups:
            errors.append(f"{HOOKS_PATH}: hooks.{event_name} must be a non-empty list")
            continue
        if event_name in {"SessionStart", "PreToolUse", "PostToolUse", "Stop"} and len(groups) != 1:
            errors.append(f"{HOOKS_PATH}: hooks.{event_name} must use exactly one group")
        for group in groups:
            if not isinstance(group, dict):
                errors.append(f"{HOOKS_PATH}: matcher groups must be objects")
                continue
            matcher = group.get("matcher")
            group_hooks = group.get("hooks")
            if not isinstance(group_hooks, list) or not group_hooks:
                errors.append(f"{HOOKS_PATH}: hooks.{event_name} group missing hooks list")
                continue
            if event_name == "SessionStart" and matcher != "startup|resume":
                errors.append(
                    f"{HOOKS_PATH}: hooks.SessionStart matcher must be 'startup|resume'"
                )
            if event_name in {"PreToolUse", "PostToolUse"} and matcher != "Bash":
                errors.append(f"{HOOKS_PATH}: hooks.{event_name} matcher must be 'Bash'")
            if event_name == "Stop" and matcher is not None:
                errors.append(f"{HOOKS_PATH}: hooks.Stop must not declare matcher")
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
                script_paths = extract_repo_script_paths(command)
                errors.extend(validate_repo_hook_script_command(command, script_paths))
                for script_path in script_paths:
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

    runtime_doctor = payload.get("runtime_doctor")
    if not isinstance(runtime_doctor, dict):
        errors.append(f"{PARITY_SOURCE_PATH}: runtime_doctor must be a table")
    else:
        skill_name = runtime_doctor.get("skill")
        role = runtime_doctor.get("role")
        checks = runtime_doctor.get("checks")
        limitations = runtime_doctor.get("limitations")
        if not isinstance(skill_name, str) or skill_name not in skill_dirs:
            errors.append(f"{PARITY_SOURCE_PATH}: runtime_doctor.skill must be configured")
        elif skill_name != "codex-runtime-doctor":
            errors.append(
                f"{PARITY_SOURCE_PATH}: runtime_doctor.skill must be codex-runtime-doctor"
            )
        if role != "diagnosis_only":
            errors.append(f"{PARITY_SOURCE_PATH}: runtime_doctor.role must be 'diagnosis_only'")
        if not isinstance(checks, list) or any(not isinstance(item, str) or not item for item in checks):
            errors.append(f"{PARITY_SOURCE_PATH}: runtime_doctor.checks must be a non-empty string array")
        if not isinstance(limitations, list) or any(
            not isinstance(item, str) or not item for item in limitations
        ):
            errors.append(
                f"{PARITY_SOURCE_PATH}: runtime_doctor.limitations must be a non-empty string array"
            )

    hook_support = payload.get("hook_support")
    if not isinstance(hook_support, list) or not hook_support:
        errors.append(f"{PARITY_SOURCE_PATH}: hook_support must be a non-empty array")
    else:
        configured_events: set[str] = set()
        if HOOKS_PATH.is_file():
            try:
                hooks_payload = load_json(HOOKS_PATH)
            except ValueError as exc:
                errors.append(str(exc))
                hooks_payload = {}
            hooks = hooks_payload.get("hooks") if isinstance(hooks_payload, dict) else {}
            if isinstance(hooks, dict):
                configured_events = set(hooks)

        seen_events: set[str] = set()
        for item in hook_support:
            if not isinstance(item, dict):
                errors.append(f"{PARITY_SOURCE_PATH}: hook_support entries must be tables")
                continue
            event = item.get("event")
            configured = item.get("configured")
            matcher_behavior = item.get("matcher_behavior")
            status = item.get("status")
            handler = item.get("handler")
            policy_files = item.get("policy_files", [])
            support_tags = item.get("support_tags")
            limitations = item.get("limitations")
            if not isinstance(event, str) or not event:
                errors.append(f"{PARITY_SOURCE_PATH}: hook_support.event must be a string")
                continue
            if event in seen_events:
                errors.append(f"{PARITY_SOURCE_PATH}: duplicate hook_support event '{event}'")
                continue
            seen_events.add(event)
            if event not in SUPPORTED_HOOK_EVENTS | {"UserPromptSubmit"}:
                errors.append(f"{PARITY_SOURCE_PATH}: unsupported hook_support event '{event}'")
            if not isinstance(configured, bool):
                errors.append(f"{PARITY_SOURCE_PATH}: hook_support.{event} configured must be boolean")
            if not isinstance(matcher_behavior, str) or not matcher_behavior:
                errors.append(
                    f"{PARITY_SOURCE_PATH}: hook_support.{event} matcher_behavior must be a string"
                )
            if not isinstance(status, str) or not status:
                errors.append(f"{PARITY_SOURCE_PATH}: hook_support.{event} status must be a string")
            if handler is not None and (not isinstance(handler, str) or not handler):
                errors.append(f"{PARITY_SOURCE_PATH}: hook_support.{event} handler must be a string")
            elif isinstance(handler, str) and not (ROOT / handler).is_file():
                errors.append(
                    f"{PARITY_SOURCE_PATH}: hook_support.{event} handler missing: {ROOT / handler}"
                )
            if not isinstance(policy_files, list) or any(
                not isinstance(file_path, str) or not file_path for file_path in policy_files
            ):
                errors.append(
                    f"{PARITY_SOURCE_PATH}: hook_support.{event} policy_files must be a string array"
                )
            else:
                for policy_path in policy_files:
                    if not (ROOT / policy_path).is_file():
                        errors.append(
                            f"{PARITY_SOURCE_PATH}: hook_support.{event} policy missing: {ROOT / policy_path}"
                        )
            if not isinstance(support_tags, list) or any(
                not isinstance(tag, str) or not tag for tag in support_tags
            ):
                errors.append(
                    f"{PARITY_SOURCE_PATH}: hook_support.{event} support_tags must be a string array"
                )
            if not isinstance(limitations, list) or any(
                not isinstance(text, str) or not text for text in limitations
            ):
                errors.append(
                    f"{PARITY_SOURCE_PATH}: hook_support.{event} limitations must be a string array"
                )
            if configured is True and event not in configured_events:
                errors.append(
                    f"{PARITY_SOURCE_PATH}: hook_support.{event} must exist in hooks.json when configured"
                )
            if configured is False and event in configured_events and event != "UserPromptSubmit":
                errors.append(
                    f"{PARITY_SOURCE_PATH}: hook_support.{event} must mark configured=true"
                )
            if event in {"PreToolUse", "PostToolUse"} and matcher_behavior != "bash_only":
                errors.append(
                    f"{PARITY_SOURCE_PATH}: hook_support.{event} must be marked bash_only"
                )
            if event == "Stop" and matcher_behavior != "matcher_ignored":
                errors.append(f"{PARITY_SOURCE_PATH}: hook_support.Stop must be matcher_ignored")
            if event == "UserPromptSubmit":
                if configured is not False:
                    errors.append(
                        f"{PARITY_SOURCE_PATH}: hook_support.UserPromptSubmit must remain unconfigured"
                    )
                if matcher_behavior != "matcher_ignored":
                    errors.append(
                        f"{PARITY_SOURCE_PATH}: hook_support.UserPromptSubmit must be matcher_ignored"
                    )
            if event == "SessionStart" and matcher_behavior != "startup_resume_only":
                errors.append(
                    f"{PARITY_SOURCE_PATH}: hook_support.SessionStart must be startup_resume_only"
                )
            if event == "Stop" and (
                not isinstance(support_tags, list)
                or "authoritative_stop_gate" not in support_tags
            ):
                errors.append(
                    f"{PARITY_SOURCE_PATH}: hook_support.Stop must include authoritative_stop_gate"
                )

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



def iter_text_chunks(text: str) -> list[str]:
    """Split prose into sentence- and line-like chunks for simple policy checks."""
    chunks = re.split(r"(?:\n+|(?<=[.!?])\s+)", text)
    return [chunk.strip() for chunk in chunks if chunk.strip()]



def validate_document_truth(path: Path, required_phrases: tuple[str, ...]) -> list[str]:
    """Require exact runtime-truth phrases in a user-facing document."""
    if not path.is_file():
        return [f"{path}: missing truth-tracked document"]

    text = path.read_text()
    errors: list[str] = []
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"{path}: missing required truth phrase: {phrase}")
    return errors



def has_local_negation(text: str, start: int) -> bool:
    """Return whether a match is locally preceded by explicit negation."""
    window = text[max(0, start - 16) : start]
    return NEGATION_PATTERN.search(window) is not None



def validate_unsupported_hook_claims(path: Path) -> list[str]:
    """Reject doc claims that overstate current Codex hook interception."""
    if not path.is_file():
        return [f"{path}: missing truth-tracked document"]

    errors: list[str] = []
    for chunk in iter_text_chunks(path.read_text()):
        if not re.search(r"\bPreToolUse\b|\bPostToolUse\b", chunk):
            continue
        general_match = re.search(
            r"\b(?:intercept|apply|applies|match|matches|cover|covers|handle|handles|run|runs|trigger|triggers)\b"
            r".{0,24}\b(?:any|all|every|general)\b.{0,24}\btool",
            chunk,
            re.IGNORECASE,
        )
        if general_match and not has_local_negation(chunk, general_match.start()):
            errors.append(f"{path}: unsupported general hook claim: {chunk}")
            continue
        non_bash_match = re.search(
            r"\b(?:intercept|apply|applies|match|matches|cover|covers|handle|handles|run|runs|trigger|triggers)\b"
            r".{0,24}\b(?:Edit|Write|Read|MCP|WebSearch|WebFetch|non-Bash)\b",
            chunk,
            re.IGNORECASE,
        )
        if non_bash_match and not has_local_negation(chunk, non_bash_match.start()):
            errors.append(f"{path}: unsupported non-Bash hook claim: {chunk}")
    return errors



def validate_runtime_doctor_scope(path: Path) -> list[str]:
    """Reject docs that overclaim the runtime doctor as a repair workflow."""
    if not path.is_file():
        return [f"{path}: missing truth-tracked document"]

    errors: list[str] = []
    for chunk in iter_text_chunks(path.read_text()):
        if not re.search(r"codex-runtime-doctor|runtime doctor", chunk, re.IGNORECASE):
            continue
        scope_matches = re.finditer(
            r"\b(?:install|repair|fix|setup|set up|start background|open xcode|build|preview|test|boot|launch)\b",
            chunk,
            re.IGNORECASE,
        )
        for scope_match in scope_matches:
            if not has_local_negation(chunk, scope_match.start()):
                errors.append(f"{path}: runtime doctor must remain diagnosis-only: {chunk}")
                break
    return errors



def validate_contract_truth() -> list[str]:
    """Validate that the generated contract and runtime-facing docs agree."""
    errors: list[str] = []
    try:
        payload = load_json(CONTRACT_PATH)
    except ValueError as exc:
        return [str(exc)]

    if not isinstance(payload, dict):
        return [f"{CONTRACT_PATH}: expected JSON object"]

    runtime = payload.get("runtime")
    if not isinstance(runtime, dict):
        return [f"{CONTRACT_PATH}: missing runtime object"]

    hook_support = runtime.get("hookSupport")
    if not isinstance(hook_support, list) or not hook_support:
        errors.append(f"{CONTRACT_PATH}: runtime.hookSupport must be a non-empty array")
        support_lookup: dict[str, dict[str, object]] = {}
    else:
        support_lookup = {
            item.get("event"): item
            for item in hook_support
            if isinstance(item, dict) and isinstance(item.get("event"), str)
        }

    for event_name in ("SessionStart", "PreToolUse", "PostToolUse", "UserPromptSubmit", "Stop"):
        if event_name not in support_lookup:
            errors.append(f"{CONTRACT_PATH}: runtime.hookSupport missing {event_name}")

    pre_tool_use = support_lookup.get("PreToolUse", {})
    if pre_tool_use.get("matcherBehavior") != "bash_only":
        errors.append(f"{CONTRACT_PATH}: PreToolUse must be marked bash_only")
    if pre_tool_use.get("configured") is not True:
        errors.append(f"{CONTRACT_PATH}: PreToolUse must be configured")

    post_tool_use = support_lookup.get("PostToolUse", {})
    if post_tool_use.get("matcherBehavior") != "bash_only":
        errors.append(f"{CONTRACT_PATH}: PostToolUse must be marked bash_only")
    if post_tool_use.get("configured") is not True:
        errors.append(f"{CONTRACT_PATH}: PostToolUse must be configured")

    user_prompt_submit = support_lookup.get("UserPromptSubmit", {})
    if user_prompt_submit.get("configured") is not False:
        errors.append(f"{CONTRACT_PATH}: UserPromptSubmit must remain documented but unconfigured")
    if user_prompt_submit.get("matcherBehavior") != "matcher_ignored":
        errors.append(f"{CONTRACT_PATH}: UserPromptSubmit must be marked matcher_ignored")

    stop_hook = support_lookup.get("Stop", {})
    stop_tags = stop_hook.get("supportTags", [])
    if stop_hook.get("matcherBehavior") != "matcher_ignored":
        errors.append(f"{CONTRACT_PATH}: Stop must be marked matcher_ignored")
    if not isinstance(stop_tags, list) or "authoritative_stop_gate" not in stop_tags:
        errors.append(f"{CONTRACT_PATH}: Stop must include authoritative_stop_gate")

    readiness = runtime.get("readiness")
    if not isinstance(readiness, dict):
        errors.append(f"{CONTRACT_PATH}: runtime.readiness must be present")
    else:
        role = readiness.get("role")
        if role != "diagnosis_only":
            errors.append(f"{CONTRACT_PATH}: runtime.readiness.role must be diagnosis_only")
        skill = readiness.get("skill")
        if not isinstance(skill, dict) or skill.get("name") != "codex-runtime-doctor":
            errors.append(
                f"{CONTRACT_PATH}: runtime.readiness.skill.name must be codex-runtime-doctor"
            )

    errors.extend(validate_document_truth(README_PATH, README_REQUIRED_PHRASES))
    errors.extend(
        validate_document_truth(OPERATING_LAYER_SKILL_PATH, OPERATING_LAYER_REQUIRED_PHRASES)
    )
    errors.extend(validate_document_truth(ROOT / "AGENTS.md", AGENTS_REQUIRED_PHRASES))
    errors.extend(validate_unsupported_hook_claims(README_PATH))
    errors.extend(validate_unsupported_hook_claims(OPERATING_LAYER_SKILL_PATH))
    errors.extend(validate_unsupported_hook_claims(ROOT / "AGENTS.md"))
    errors.extend(validate_runtime_doctor_scope(README_PATH))
    errors.extend(validate_runtime_doctor_scope(OPERATING_LAYER_SKILL_PATH))
    errors.extend(validate_runtime_doctor_scope(ROOT / "AGENTS.md"))

    try:
        manifest = load_json(MANIFEST_PATH)
    except ValueError as exc:
        errors.append(str(exc))
        manifest = None
    if isinstance(manifest, dict):
        interface = manifest.get("interface")
        manifest_text = json.dumps(interface, sort_keys=True) if isinstance(interface, dict) else ""
        for phrase in MANIFEST_REQUIRED_PHRASES:
            if phrase not in manifest_text:
                errors.append(f"{MANIFEST_PATH}: missing required runtime-truth phrase: {phrase}")

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
    errors.extend(validate_contract_truth())

    if errors:
        print("Codex support validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Codex support validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
