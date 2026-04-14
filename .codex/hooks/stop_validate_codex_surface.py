#!/usr/bin/env python3
"""Validate the canonical Codex surface before a turn stops."""

from __future__ import annotations

import json
import subprocess
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.hook_policy import choose_outcome, evaluate_rules, load_rule_file  # noqa: E402

PARITY_SOURCE_PATH = ROOT / ".codex" / "parity-source.toml"
GENERATOR_PATH = ROOT / "scripts" / "generate_codex_parity_contract.py"
VALIDATOR_PATH = ROOT / "scripts" / "validate-codex-support.py"
STOP_POLICY_PATH = ROOT / ".codex" / "hooks" / "policies" / "stop-completion.md"


def load_validation_targets() -> list[str]:
    """Load the canonical validation target paths from parity source."""
    payload = tomllib.loads(PARITY_SOURCE_PATH.read_text())
    targets = payload.get("validation_targets", [])
    return [target for target in targets if isinstance(target, str) and target]


def working_tree_touches_targets(targets: list[str]) -> bool:
    """Return True when tracked or untracked changes touch any canonical target."""
    result = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all", "--", *targets],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return bool(result.stdout.strip())


def run_check(command: list[str]) -> tuple[bool, str]:
    """Run a check command and capture stderr/stdout for hook feedback."""
    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    output = (result.stderr or result.stdout).strip()
    return result.returncode == 0, output


def emit_stop(message: str) -> int:
    """Emit a stop payload that continues the turn with a remediation prompt."""
    print(
        json.dumps(
            {
                "decision": "block",
                "reason": message,
                "systemMessage": message,
            }
        )
    )
    return 0


def build_stop_message(command_name: str, command_output: str) -> str:
    """Build the authoritative completion-gate message for Stop failures."""
    message = (
        "Canonical Codex files changed, but the parity contract or validator is not "
        "passing."
    )
    try:
        rule = load_rule_file(STOP_POLICY_PATH)
    except Exception:
        rule = None

    if rule and rule.enabled and rule.event in {"all", "stop"}:
        decision = choose_outcome(
            evaluate_rules(
                [rule],
                {
                    "changed_targets": "true",
                    "validation_failure": "true",
                    "failed_command": command_name,
                    "validation_output": command_output,
                },
            )
        )
        if decision.matched and decision.message:
            message = decision.message

    if command_output:
        return f"{message}\n\n{command_name} output:\n{command_output}"
    return message


def main() -> int:
    """Run generator and validator when canonical Codex files changed."""
    if not PARITY_SOURCE_PATH.is_file():
        return 0

    targets = load_validation_targets()
    if not targets or not working_tree_touches_targets(targets):
        return 0

    generator_command = [sys.executable, str(GENERATOR_PATH)]
    generator_ok, generator_output = run_check(generator_command)
    if not generator_ok:
        return emit_stop(build_stop_message("generate_codex_parity_contract.py", generator_output))

    check_command = [sys.executable, str(GENERATOR_PATH), "--check"]
    check_ok, check_output = run_check(check_command)
    if not check_ok:
        return emit_stop(build_stop_message("generate_codex_parity_contract.py --check", check_output))

    validator_command = [sys.executable, str(VALIDATOR_PATH)]
    validator_ok, validator_output = run_check(validator_command)
    if not validator_ok:
        return emit_stop(build_stop_message("validate-codex-support.py", validator_output))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
