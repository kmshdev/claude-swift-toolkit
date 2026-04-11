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
UNSAFE_PATTERNS = (
    re.compile(r"/(brainstorm|write-plan|execute-plan|build|fix-build|run-app|review|review-ui|refactor-view|swift-style|test)\\b"),
    re.compile(r"\\b(macos-architect|code-architect|code-explorer|ui-developer|ios-developer|swift-reviewer|code-reviewer)\\b"),
    re.compile(
        rf"\\b({re.escape(LEGACY_XCODE_BRIDGE)}|{re.escape(LEGACY_XCODE_BRIDGE_TITLE)}|"
        rf"{re.escape(LEGACY_XCODE_TOOL_PREFIX)})\\b"
    ),
    re.compile(
        r"\\b(session_show_defaults|session_set_defaults|build_run_sim|build_sim|test_sim|"
        r"launch_app_sim|stop_app_sim|discover_projs|list_sims|snapshot_ui|"
        r"start_sim_log_cap|stop_sim_log_cap|debug_attach_sim)\\b"
    ),
    re.compile(r"\\bxcodebuild\\s+-list\\b"),
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


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter block")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"{path}: unterminated frontmatter block")

    frontmatter_block = text[4:end]
    body = text[end + 5 :]
    frontmatter: dict[str, str] = {}
    for line in frontmatter_block.splitlines():
        match = re.match(r"([A-Za-z0-9_-]+):\s*(.*)", line)
        if match:
            frontmatter[match.group(1)] = match.group(2)
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
    text = path.read_text()
    if "interface:" not in text:
        errors.append(f"{path}: missing top-level interface block")
    if "display_name:" not in text:
        errors.append(f"{path}: missing interface.display_name")
    if "short_description:" not in text:
        errors.append(f"{path}: missing interface.short_description")
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
