#!/usr/bin/env python3
"""Rule evaluation engine for hookify plugin."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.hook_policy.engine import choose_outcome, evaluate_rules  # noqa: E402
from scripts.hook_policy.models import Rule  # noqa: E402


class RuleEngine:
    """Evaluate legacy hookify input against the shared policy engine."""

    def evaluate_rules(self, rules: list[Rule], input_data: dict[str, Any]) -> dict[str, Any]:
        """Evaluate hookify rules and return the legacy hook response format."""
        normalized_fields = self._normalize_fields(input_data)
        decision = choose_outcome(evaluate_rules(rules, normalized_fields))
        if decision.action == "allow":
            return {}

        hook_event = input_data.get("hook_event_name", "")
        if decision.action == "block":
            if hook_event == "Stop":
                return {
                    "decision": "block",
                    "reason": decision.message,
                    "systemMessage": decision.message,
                }
            if hook_event in {"PreToolUse", "PostToolUse"}:
                return {
                    "hookSpecificOutput": {
                        "hookEventName": hook_event,
                        "permissionDecision": "deny",
                    },
                    "systemMessage": decision.message,
                }
        return {"systemMessage": decision.message}

    def _normalize_fields(self, input_data: dict[str, Any]) -> dict[str, str]:
        """Convert hookify input payloads into the shared string field map."""
        normalized: dict[str, str] = {
            "hook_event_name": self._stringify(input_data.get("hook_event_name")),
            "tool_name": self._stringify(input_data.get("tool_name")),
            "reason": self._stringify(input_data.get("reason")),
            "user_prompt": self._stringify(input_data.get("user_prompt")),
        }

        tool_input = input_data.get("tool_input")
        if isinstance(tool_input, dict):
            for key, value in tool_input.items():
                if isinstance(value, list):
                    continue
                normalized[key] = self._stringify(value)

        tool_name = normalized.get("tool_name", "")
        if tool_name == "Bash":
            normalized.setdefault(
                "command",
                self._stringify((tool_input or {}).get("command")),
            )
        elif tool_name in {"Write", "Edit"}:
            normalized.setdefault(
                "content",
                self._stringify(
                    (tool_input or {}).get("content")
                    or (tool_input or {}).get("new_string")
                ),
            )
            normalized.setdefault(
                "new_text",
                self._stringify((tool_input or {}).get("new_string")),
            )
            normalized.setdefault(
                "new_string",
                self._stringify((tool_input or {}).get("new_string")),
            )
            normalized.setdefault(
                "old_text",
                self._stringify((tool_input or {}).get("old_string")),
            )
            normalized.setdefault(
                "old_string",
                self._stringify((tool_input or {}).get("old_string")),
            )
            normalized.setdefault(
                "file_path",
                self._stringify((tool_input or {}).get("file_path")),
            )
        elif tool_name == "MultiEdit":
            edits = (tool_input or {}).get("edits", [])
            combined = " ".join(
                self._stringify(edit.get("new_string"))
                for edit in edits
                if isinstance(edit, dict)
            )
            normalized.setdefault("content", combined)
            normalized.setdefault("new_text", combined)
            normalized.setdefault(
                "file_path",
                self._stringify((tool_input or {}).get("file_path")),
            )

        transcript = self._load_transcript(input_data.get("transcript_path"))
        if transcript is not None:
            normalized["transcript"] = transcript
        return normalized

    def _load_transcript(self, transcript_path: Any) -> str | None:
        """Read transcript content for stop-rule evaluation when available."""
        if transcript_path in {None, ""}:
            return None
        try:
            return Path(str(transcript_path)).read_text()
        except FileNotFoundError:
            print(f"Warning: Transcript file not found: {transcript_path}", file=sys.stderr)
        except PermissionError:
            print(
                f"Warning: Permission denied reading transcript: {transcript_path}",
                file=sys.stderr,
            )
        except OSError as exc:
            print(
                f"Warning: Error reading transcript {transcript_path}: {exc}",
                file=sys.stderr,
            )
        except UnicodeDecodeError as exc:
            print(
                f"Warning: Encoding error in transcript {transcript_path}: {exc}",
                file=sys.stderr,
            )
        return ""

    @staticmethod
    def _stringify(value: Any) -> str:
        """Convert hook payload values to strings for the shared engine."""
        if value is None:
            return ""
        if isinstance(value, str):
            return value
        if isinstance(value, bool):
            return "true" if value else "false"
        return str(value)
