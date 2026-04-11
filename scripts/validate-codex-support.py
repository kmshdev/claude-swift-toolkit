#!/usr/bin/env python3
"""Validate the repo-scoped Codex plugin surface."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = ROOT / ".agents" / "plugins" / "marketplace.json"
ALLOWED_FRONTMATTER_KEYS = {"name", "description"}
TOKEN_CHARS = r"A-Za-z0-9_"
REQUIRED_METADATA_FILES = (
    ROOT
    / "plugins"
    / "apple-app-architect"
    / "codex-skills"
    / "app-development-workflow"
    / "agents"
    / "openai.yaml",
    ROOT
    / "plugins"
    / "apple-app-architect"
    / "codex-skills"
    / "macos-development"
    / "agents"
    / "openai.yaml",
    ROOT
    / "plugins"
    / "apple-app-builder"
    / "codex-skills"
    / "autonomous-ui-workflow"
    / "agents"
    / "openai.yaml",
    ROOT
    / "plugins"
    / "apple-app-builder"
    / "codex-skills"
    / "xcode-mcp"
    / "agents"
    / "openai.yaml",
    ROOT
    / "plugins"
    / "apple-app-quality"
    / "codex-skills"
    / "code-analyzer"
    / "agents"
    / "openai.yaml",
    ROOT
    / "plugins"
    / "apple-app-quality"
    / "codex-skills"
    / "ios-testing"
    / "agents"
    / "openai.yaml",
    ROOT
    / "plugins"
    / "apple-app-quality"
    / "codex-skills"
    / "swiftui-view-refactor"
    / "agents"
    / "openai.yaml",
    ROOT
    / "plugins"
    / "apple-design-system"
    / "skills"
    / "swiftui-ui-patterns"
    / "agents"
    / "openai.yaml",
)
LEGACY_XCODE_BRIDGE = "xcode" "buildmcp"
LEGACY_XCODE_BRIDGE_TITLE = "Xcode" "BuildMCP"
LEGACY_XCODE_TOOL_PREFIX = "mcp__xcode" "buildmcp__"


def compile_token_pattern(
    *tokens: str, leading_chars: str = TOKEN_CHARS, trailing_chars: str = TOKEN_CHARS
) -> re.Pattern[str]:
    escaped = "|".join(re.escape(token) for token in tokens)
    return re.compile(
        rf"(?<![{leading_chars}])(?:{escaped})(?![{trailing_chars}])"
    )


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
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        raise ValueError(f"{path}: invalid JSON ({exc})") from exc


def ensure_relative_plugin_path(path_value: str, plugin_dir: Path) -> list[str]:
    errors: list[str] = []
    if not path_value.startswith("./"):
        errors.append(f"{plugin_dir}: manifest path '{path_value}' must start with './'")
        return errors

    resolved = (plugin_dir / path_value).resolve()
    try:
        resolved.relative_to(plugin_dir.resolve())
    except ValueError:
        errors.append(f"{plugin_dir}: manifest path '{path_value}' escapes the plugin root")
        return errors

    if not resolved.exists():
        errors.append(f"{plugin_dir}: manifest path '{path_value}' does not exist")
    return errors


def parse_yaml_scalar(value: str, *, path: Path, line_number: int) -> object:
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
    return load_simple_yaml_text(path.read_text(), path=path)


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter block")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"{path}: unterminated frontmatter block")

    frontmatter_block = text[4:end]
    body = text[end + 5 :]
    payload = load_simple_yaml_text(frontmatter_block, path=path, start_line=2)
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: frontmatter must be a top-level mapping")

    frontmatter: dict[str, str] = {}
    for key, value in payload.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{path}: frontmatter '{key}' must be a non-empty string")
        frontmatter[key] = value
    return frontmatter, body


def validate_skill_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        frontmatter, body = parse_frontmatter(path)
    except ValueError as exc:
        return [str(exc)]

    missing = sorted(ALLOWED_FRONTMATTER_KEYS - frontmatter.keys())
    if missing:
        errors.append(f"{path}: missing required frontmatter keys: {', '.join(missing)}")

    extras = sorted(set(frontmatter) - ALLOWED_FRONTMATTER_KEYS)
    if extras:
        errors.append(
            f"{path}: unsupported frontmatter keys for Codex-exposed skill: {', '.join(extras)}"
        )

    for pattern in UNSAFE_PATTERNS:
        match = pattern.search(body)
        if match:
            errors.append(f"{path}: contains Codex-unsafe reference '{match.group(0)}'")
    return errors


def validate_openai_metadata(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        payload = load_simple_yaml(path)
    except ValueError as exc:
        return [str(exc)]

    if not isinstance(payload, dict):
        return [f"{path}: expected top-level YAML mapping"]

    interface = payload.get("interface")
    if not isinstance(interface, dict):
        errors.append(f"{path}: missing top-level interface block")
        return errors

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
    if dependencies is not None:
        if not isinstance(dependencies, dict):
            errors.append(f"{path}: dependencies must be a mapping when present")
            return errors
        tools = dependencies.get("tools")
        if tools is not None:
            if not isinstance(tools, list):
                errors.append(f"{path}: dependencies.tools must be a list when present")
            else:
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
            errors.append(f"{path}: MCP server '{server_name}' env must be an object of string pairs")
    return errors


def validate_plugin(plugin_dir: Path) -> list[str]:
    errors: list[str] = []
    manifest_path = plugin_dir / ".codex-plugin" / "plugin.json"
    if not manifest_path.exists():
        return [f"{plugin_dir}: missing .codex-plugin/plugin.json"]

    try:
        manifest = load_json(manifest_path)
    except ValueError as exc:
        return [str(exc)]

    if not isinstance(manifest, dict):
        return [f"{manifest_path}: expected JSON object"]

    for key in ("skills", "mcpServers", "apps"):
        value = manifest.get(key)
        if value is None:
            continue
        if not isinstance(value, str):
            errors.append(f"{manifest_path}: '{key}' must be a string path")
            continue
        errors.extend(ensure_relative_plugin_path(value, plugin_dir))

    mcp_path_value = manifest.get("mcpServers")
    if isinstance(mcp_path_value, str):
        mcp_path = (plugin_dir / mcp_path_value).resolve()
        if mcp_path.exists():
            errors.extend(validate_mcp_config(mcp_path))

    skills_path_value = manifest.get("skills")
    if isinstance(skills_path_value, str):
        skills_root = (plugin_dir / skills_path_value).resolve()
        if skills_root.exists():
            for skill_file in sorted(skills_root.rglob("SKILL.md")):
                errors.extend(validate_skill_file(skill_file))
                agents_dir = skill_file.parent / "agents"
                metadata_path = agents_dir / "openai.yaml"
                if agents_dir.exists():
                    if not metadata_path.is_file():
                        errors.append(f"{metadata_path}: expected a file")
                    else:
                        errors.extend(validate_openai_metadata(metadata_path))

    return errors


def main() -> int:
    errors: list[str] = []

    if not MARKETPLACE_PATH.exists():
        print(f"Missing marketplace: {MARKETPLACE_PATH}", file=sys.stderr)
        return 1

    try:
        marketplace = load_json(MARKETPLACE_PATH)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if not isinstance(marketplace, dict):
        print(f"{MARKETPLACE_PATH}: expected JSON object", file=sys.stderr)
        return 1

    interface = marketplace.get("interface")
    if not isinstance(interface, dict):
        print(f"{MARKETPLACE_PATH}: missing top-level interface object", file=sys.stderr)
        return 1
    display_name = interface.get("displayName")
    if not isinstance(display_name, str) or not display_name.strip():
        print(f"{MARKETPLACE_PATH}: missing interface.displayName", file=sys.stderr)
        return 1

    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list):
        print(f"{MARKETPLACE_PATH}: 'plugins' must be an array", file=sys.stderr)
        return 1

    for plugin in plugins:
        if not isinstance(plugin, dict):
            errors.append(f"{MARKETPLACE_PATH}: each plugin entry must be an object")
            continue
        source = plugin.get("source")
        name = plugin.get("name", "<unknown>")
        if not isinstance(source, dict):
            errors.append(f"{MARKETPLACE_PATH}: plugin '{name}' is missing a source object")
            continue
        policy = plugin.get("policy")
        if not isinstance(policy, dict):
            errors.append(f"{MARKETPLACE_PATH}: plugin '{name}' is missing a policy object")
        else:
            installation = policy.get("installation")
            if not isinstance(installation, str) or not installation:
                errors.append(
                    f"{MARKETPLACE_PATH}: plugin '{name}' is missing policy.installation"
                )
            authentication = policy.get("authentication")
            if not isinstance(authentication, str) or not authentication:
                errors.append(
                    f"{MARKETPLACE_PATH}: plugin '{name}' is missing policy.authentication"
                )
        category = plugin.get("category")
        if not isinstance(category, str) or not category.strip():
            errors.append(f"{MARKETPLACE_PATH}: plugin '{name}' is missing category")
        source_path = source.get("path")
        if not isinstance(source_path, str) or not source_path.startswith("./"):
            errors.append(
                f"{MARKETPLACE_PATH}: plugin '{name}' must use a './'-prefixed source.path"
            )
            continue

        plugin_dir = (ROOT / source_path).resolve()
        try:
            plugin_dir.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{MARKETPLACE_PATH}: plugin '{name}' path escapes the repository root")
            continue
        if not plugin_dir.exists():
            errors.append(f"{MARKETPLACE_PATH}: plugin '{name}' path does not exist: {source_path}")
            continue
        errors.extend(validate_plugin(plugin_dir))

    for metadata_path in REQUIRED_METADATA_FILES:
        if not metadata_path.is_file():
            errors.append(f"{metadata_path}: required entry-point metadata file is missing")

    if errors:
        print("Codex support validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Codex support validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
