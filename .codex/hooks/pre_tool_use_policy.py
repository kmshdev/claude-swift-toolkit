#!/usr/bin/env python3
"""Apply repo-local Codex PreToolUse policies for Bash commands."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.hook_policy import (  # noqa: E402
    RuleParseError,
    choose_outcome,
    evaluate_rules,
    load_rule_file,
)

POLICY_FILES = (ROOT / ".codex" / "hooks" / "policies" / "bash-safety.md",)


def load_rules(event: str) -> tuple[list[object], list[str]]:
    """Load policy files and accumulate per-file warnings."""
    rules: list[object] = []
    warnings: list[str] = []
    for path in POLICY_FILES:
        try:
            rule = load_rule_file(path)
        except (OSError, RuleParseError, UnicodeDecodeError) as exc:
            warnings.append(f"Skipped {path.name}: {exc}")
            continue
        if rule.enabled and rule.event in {"all", event}:
            rules.append(rule)
    return rules, warnings


def normalize_input(payload: dict[str, object]) -> dict[str, str]:
    """Normalize Codex PreToolUse payloads into string fields."""
    tool_input = payload.get("tool_input")
    command = ""
    if isinstance(tool_input, dict):
        raw_command = tool_input.get("command")
        if raw_command is not None:
            command = str(raw_command)
    return {
        "tool_name": str(payload.get("tool_name") or ""),
        "command": command,
    }


def main() -> int:
    """Evaluate Bash pre-tool policies and fail open on internal errors."""
    try:
        payload = json.load(sys.stdin)
        if payload.get("tool_name") != "Bash":
            print(json.dumps({}))
            return 0

        rules, warnings = load_rules("bash")
        decision = choose_outcome(evaluate_rules(rules, normalize_input(payload)))
        messages = list(warnings)
        if decision.matched and decision.message:
            messages.append(decision.message)

        if decision.action == "block":
            print(
                json.dumps(
                    {
                        "hookSpecificOutput": {
                            "hookEventName": "PreToolUse",
                            "permissionDecision": "deny",
                            "permissionDecisionReason": "\n\n".join(messages),
                        },
                        "systemMessage": "\n\n".join(messages),
                    }
                )
            )
            return 0

        if messages:
            print(json.dumps({"systemMessage": "\n\n".join(messages)}))
            return 0

        print(json.dumps({}))
        return 0
    except Exception as exc:  # pragma: no cover - defensive fail-open hook path
        print(json.dumps({"systemMessage": f"Codex pre-tool policy failed open: {exc}"}))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
