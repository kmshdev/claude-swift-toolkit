#!/usr/bin/env python3
"""Apply repo-local Codex PostToolUse policies for Bash commands."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.hook_policy import (  # noqa: E402
    RuleParseError,
    choose_outcome,
    evaluate_rules,
    load_rule_file,
)

POLICY_FILES = (ROOT / ".codex" / "hooks" / "policies" / "bash-post-review.md",)


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


def stringify(value: Any) -> str:
    """Convert hook payload values into strings for rule evaluation."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def flatten_tool_response(value: Any, fields: dict[str, str], *, prefix: str = "") -> None:
    """Flatten a JSON-like tool response into string fields."""
    if isinstance(value, dict):
        for key, nested in value.items():
            flatten_tool_response(nested, fields, prefix=f"{prefix}{key}_")
        return
    if isinstance(value, list):
        fields[prefix.rstrip("_") or "tool_response_text"] = "\n".join(
            stringify(item) for item in value
        )
        return
    if prefix:
        fields[prefix.rstrip("_")] = stringify(value)


def normalize_input(payload: dict[str, object]) -> dict[str, str]:
    """Normalize Codex PostToolUse payloads into string fields."""
    tool_input = payload.get("tool_input")
    command = ""
    if isinstance(tool_input, dict):
        raw_command = tool_input.get("command")
        if raw_command is not None:
            command = str(raw_command)

    fields = {
        "tool_name": str(payload.get("tool_name") or ""),
        "command": command,
    }
    tool_response = payload.get("tool_response")
    fields["tool_response_text"] = stringify(tool_response)

    parsed_response = tool_response
    if isinstance(tool_response, str):
        try:
            parsed_response = json.loads(tool_response)
        except json.JSONDecodeError:
            parsed_response = tool_response
    flatten_tool_response(parsed_response, fields)
    return fields


def main() -> int:
    """Evaluate Bash post-tool policies and fail open on internal errors."""
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
        if not messages:
            print(json.dumps({}))
            return 0

        message = "\n\n".join(messages)
        response = {
            "systemMessage": message,
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": message,
            },
        }
        if decision.action == "block":
            response["decision"] = "block"
            response["reason"] = message
        print(json.dumps(response))
        return 0
    except Exception as exc:  # pragma: no cover - defensive fail-open hook path
        print(json.dumps({"systemMessage": f"Codex post-tool policy failed open: {exc}"}))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
