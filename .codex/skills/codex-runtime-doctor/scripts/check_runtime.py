#!/usr/bin/env python3
"""Diagnose the repo-scoped Codex runtime and root Xcode bridge readiness."""

from __future__ import annotations

import json
import platform
import subprocess
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
CONFIG_PATH = ROOT / ".codex" / "config.toml"
HOOKS_PATH = ROOT / ".codex" / "hooks.json"
PARITY_SOURCE_PATH = ROOT / ".codex" / "parity-source.toml"
CONTRACT_PATH = ROOT / ".codex" / "contracts" / "parity-contract.json"
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"
MCP_PATH = ROOT / ".mcp.json"
VALIDATOR_PATH = ROOT / "scripts" / "validate-codex-support.py"
POLICY_DIR = ROOT / ".codex" / "hooks" / "policies"
REQUIRED_POLICY_FILES = (
    POLICY_DIR / "bash-safety.md",
    POLICY_DIR / "bash-post-review.md",
    POLICY_DIR / "stop-completion.md",
)
REQUIRED_HOOK_EVENTS = ("SessionStart", "PreToolUse", "PostToolUse", "Stop")


def run_command(command: list[str], *, timeout: int = 5) -> subprocess.CompletedProcess[str]:
    """Run a low-cost subprocess probe."""
    return subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=timeout,
    )


def load_json(path: Path) -> object:
    """Load a JSON file with a stable error."""
    return json.loads(path.read_text())


def load_toml(path: Path) -> dict[str, object]:
    """Load a TOML file with a stable error."""
    return tomllib.loads(path.read_text())


def section(status: str, evidence: list[str], remediation: list[str]) -> dict[str, object]:
    """Create a normalized doctor section."""
    return {
        "status": status,
        "evidence": evidence,
        "remediation": remediation,
    }


def check_canonical_surface() -> dict[str, object]:
    """Validate that the repo-owned Codex runtime surface is internally coherent."""
    evidence: list[str] = []
    remediation: list[str] = []
    required_files = (
        CONFIG_PATH,
        HOOKS_PATH,
        PARITY_SOURCE_PATH,
        CONTRACT_PATH,
        MANIFEST_PATH,
        MCP_PATH,
    )
    for path in required_files:
        if not path.is_file():
            remediation.append(f"Restore missing canonical file: {path}")
            return section("degraded", evidence, remediation)

    try:
        load_toml(CONFIG_PATH)
        load_json(HOOKS_PATH)
        load_toml(PARITY_SOURCE_PATH)
        load_json(CONTRACT_PATH)
        load_json(MANIFEST_PATH)
        load_json(MCP_PATH)
    except Exception as exc:
        remediation.append("Fix the malformed canonical Codex file and rerun the doctor.")
        return section("degraded", [f"Canonical file parsing failed: {exc}"], remediation)

    evidence.append("Canonical repo-local Codex files parse successfully.")
    validator = run_command([sys.executable, str(VALIDATOR_PATH)], timeout=30)
    if validator.returncode != 0:
        output = (validator.stderr or validator.stdout).strip()
        evidence.append(f"Validator failed: {output}")
        remediation.append("Run `python3 scripts/validate-codex-support.py` and fix the reported drift.")
        return section("degraded", evidence, remediation)

    evidence.append("`scripts/validate-codex-support.py` passed.")
    return section("ready", evidence, remediation)


def check_repo_hooks() -> dict[str, object]:
    """Classify repo-local hook readiness and supported-event shape."""
    evidence: list[str] = []
    remediation: list[str] = []

    if platform.system() == "Windows":
        evidence.append("Codex hooks are currently disabled on Windows.")
        remediation.append("Use a non-Windows environment before relying on repo-local hooks.")
        return section("unavailable", evidence, remediation)

    try:
        config = load_toml(CONFIG_PATH)
        hooks_payload = load_json(HOOKS_PATH)
    except Exception as exc:
        remediation.append("Fix `.codex/config.toml` or `.codex/hooks.json` and rerun the doctor.")
        return section("degraded", [f"Hook config parse failed: {exc}"], remediation)

    features = config.get("features")
    if not isinstance(features, dict) or features.get("codex_hooks") is not True:
        evidence.append("`features.codex_hooks` is not enabled in `.codex/config.toml`.")
        remediation.append("Set `features.codex_hooks = true` in `.codex/config.toml`.")
        return section("unavailable", evidence, remediation)

    hooks = hooks_payload.get("hooks") if isinstance(hooks_payload, dict) else None
    if not isinstance(hooks, dict):
        remediation.append("Restore the top-level `hooks` object in `.codex/hooks.json`.")
        return section("degraded", evidence, remediation)

    missing_events = [event for event in REQUIRED_HOOK_EVENTS if event not in hooks]
    if missing_events:
        evidence.append(f"Missing hook events: {', '.join(missing_events)}")
        remediation.append("Restore the supported repo-local hook events in `.codex/hooks.json`.")
        return section("degraded", evidence, remediation)

    session_groups = hooks.get("SessionStart")
    pre_groups = hooks.get("PreToolUse")
    post_groups = hooks.get("PostToolUse")
    stop_groups = hooks.get("Stop")
    if not isinstance(session_groups, list) or len(session_groups) != 1:
        evidence.append("`SessionStart` must use exactly one startup/resume handler group.")
        remediation.append("Keep one `SessionStart` handler in `.codex/hooks.json`.")
        return section("degraded", evidence, remediation)
    if not isinstance(pre_groups, list) or len(pre_groups) != 1:
        evidence.append("`PreToolUse` must use exactly one repo-local handler group.")
        remediation.append("Keep one Bash-only `PreToolUse` handler in `.codex/hooks.json`.")
        return section("degraded", evidence, remediation)
    if not isinstance(post_groups, list) or len(post_groups) != 1:
        evidence.append("`PostToolUse` must use exactly one repo-local handler group.")
        remediation.append("Keep one Bash-only `PostToolUse` handler in `.codex/hooks.json`.")
        return section("degraded", evidence, remediation)
    if not isinstance(stop_groups, list) or len(stop_groups) != 1:
        evidence.append("`Stop` must use exactly one authoritative completion gate.")
        remediation.append("Keep one repo-local `Stop` handler in `.codex/hooks.json`.")
        return section("degraded", evidence, remediation)

    if session_groups[0].get("matcher") != "startup|resume":
        evidence.append("`SessionStart` must stay scoped to startup/resume only.")
        remediation.append("Set the `SessionStart` matcher to `startup|resume`.")
        return section("degraded", evidence, remediation)

    if pre_groups[0].get("matcher") != "Bash" or post_groups[0].get("matcher") != "Bash":
        evidence.append("`PreToolUse` and `PostToolUse` must remain Bash-only in this repo.")
        remediation.append("Set the hook matcher to `Bash` for `PreToolUse` and `PostToolUse`.")
        return section("degraded", evidence, remediation)

    if "matcher" in stop_groups[0]:
        evidence.append("`Stop` must not rely on matcher semantics in this repo.")
        remediation.append("Remove the `matcher` field from the `Stop` hook group.")
        return section("degraded", evidence, remediation)

    missing_policies = [path.name for path in REQUIRED_POLICY_FILES if not path.is_file()]
    if missing_policies:
        evidence.append(f"Missing policy files: {', '.join(missing_policies)}")
        remediation.append("Restore the repo-local hook policy files under `.codex/hooks/policies/`.")
        return section("degraded", evidence, remediation)

    evidence.append("Repo-local hooks are enabled and scoped to supported Codex events.")
    evidence.append("`SessionStart` remains scoped to startup/resume only.")
    evidence.append("`PreToolUse` and `PostToolUse` remain Bash-only, and `Stop` stays matcher-free.")
    return section("ready", evidence, remediation)


def check_external_hook_overlay() -> dict[str, object]:
    """Report whether a user-level hooks overlay exists outside the repo."""
    overlay_path = Path.home() / ".codex" / "hooks.json"
    if overlay_path.is_file():
        return section(
            "present",
            [f"Found external hook overlay at {overlay_path}."],
            [
                "Observed hook behavior may differ from the repo-local contract while that overlay exists."
            ],
        )
    return section("absent", ["No user-level `~/.codex/hooks.json` overlay found."], [])


def check_xcode_bridge() -> dict[str, object]:
    """Classify root Xcode bridge wiring and low-cost command availability."""
    evidence: list[str] = []
    remediation: list[str] = []

    try:
        mcp_payload = load_json(MCP_PATH)
    except Exception as exc:
        remediation.append("Fix `.mcp.json` so the repo declares the root Xcode MCP bridge cleanly.")
        return section("degraded", [f"Failed to parse `.mcp.json`: {exc}"], remediation)

    xcode_server = None
    if isinstance(mcp_payload, dict):
        servers = mcp_payload.get("mcpServers")
        if isinstance(servers, dict):
            xcode_server = servers.get("xcode")
    if not isinstance(xcode_server, dict):
        remediation.append("Declare the root Xcode bridge as `mcpServers.xcode` in `.mcp.json`.")
        return section("degraded", evidence, remediation)

    command = xcode_server.get("command")
    args = xcode_server.get("args")
    if command != "xcrun" or args != ["mcpbridge"]:
        evidence.append("The root `.mcp.json` no longer points to `xcrun mcpbridge`.")
        remediation.append("Restore `.mcp.json` to the repo-owned `xcrun mcpbridge` declaration.")
        return section("degraded", evidence, remediation)

    evidence.append("Root `.mcp.json` declares `xcrun mcpbridge`.")

    xcrun_probe = run_command(["xcrun", "--find", "xcodebuild"])
    if xcrun_probe.returncode != 0:
        output = (xcrun_probe.stderr or xcrun_probe.stdout).strip()
        evidence.append(f"`xcrun` probe failed: {output}")
        remediation.append("Install Xcode command line tools so `xcrun` can resolve Apple tooling.")
        return section("unavailable", evidence, remediation)

    evidence.append("`xcrun --find xcodebuild` succeeded.")
    bridge_probe = run_command(["xcrun", "--find", "mcpbridge"])
    if bridge_probe.returncode != 0:
        output = (bridge_probe.stderr or bridge_probe.stdout).strip()
        evidence.append(f"`xcrun --find mcpbridge` failed: {output}")
        remediation.append("Install or update Xcode so `mcpbridge` is available to `xcrun`.")
        return section("degraded", evidence, remediation)

    evidence.append("`xcrun --find mcpbridge` succeeded.")
    return section("ready", evidence, remediation)


def summarize_status(sections: dict[str, dict[str, object]]) -> str:
    """Return an overall readiness summary from section statuses."""
    statuses = [str(section["status"]) for section in sections.values()]
    if "unavailable" in statuses:
        return "unavailable"
    if "degraded" in statuses or "present" in statuses:
        return "degraded"
    return "ready"


def build_report() -> dict[str, object]:
    """Build the full runtime doctor report."""
    sections = {
        "canonical_surface": check_canonical_surface(),
        "repo_hooks": check_repo_hooks(),
        "external_hook_overlay": check_external_hook_overlay(),
        "xcode_bridge": check_xcode_bridge(),
    }
    return {
        "summary": summarize_status(sections),
        "sections": sections,
    }


def main() -> int:
    """Print the runtime doctor report as JSON."""
    print(json.dumps(build_report(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
