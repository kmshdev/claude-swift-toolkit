from __future__ import annotations

import importlib.util
import io
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
PRE_TOOL_PATH = ROOT / ".codex" / "hooks" / "pre_tool_use_policy.py"
POST_TOOL_PATH = ROOT / ".codex" / "hooks" / "post_tool_use_policy.py"
HOOKS_PATH = ROOT / ".codex" / "hooks.json"


def load_module(name: str, path: Path):
    """Load a hook module from a concrete file path."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover - importlib guardrail
        raise RuntimeError(f"Unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CodexHookPolicyTests(unittest.TestCase):
    def test_pre_tool_blocks_destructive_bash_command(self) -> None:
        module = load_module("pre_tool_use_policy_block", PRE_TOOL_PATH)
        payload = {
            "tool_name": "Bash",
            "tool_input": {"command": 'rm -fr "$TMPDIR/demo"'},
        }
        stdout = io.StringIO()
        with mock.patch("sys.stdin", io.StringIO(json.dumps(payload))), mock.patch(
            "sys.stdout", stdout
        ):
            result = module.main()

        self.assertEqual(result, 0)
        response = json.loads(stdout.getvalue())
        self.assertEqual(
            response["hookSpecificOutput"]["permissionDecision"],
            "deny",
        )
        self.assertIn("destructive shell commands", response["systemMessage"])

    def test_pre_tool_allows_non_destructive_bash_command(self) -> None:
        module = load_module("pre_tool_use_policy_allow", PRE_TOOL_PATH)
        payload = {
            "tool_name": "Bash",
            "tool_input": {"command": "python3 scripts/validate-codex-support.py"},
        }
        stdout = io.StringIO()
        with mock.patch("sys.stdin", io.StringIO(json.dumps(payload))), mock.patch(
            "sys.stdout", stdout
        ):
            result = module.main()

        self.assertEqual(result, 0)
        self.assertEqual(json.loads(stdout.getvalue()), {})

    def test_pre_tool_fails_open_when_policy_file_is_malformed(self) -> None:
        module = load_module("pre_tool_use_policy_fail_open", PRE_TOOL_PATH)
        with TemporaryDirectory() as temp_dir:
            bad_policy = Path(temp_dir) / "bash-safety.md"
            bad_policy.write_text("---\nname: bad\npattern: \"unterminated\n---\nblocked\n")
            payload = {
                "tool_name": "Bash",
                "tool_input": {"command": "rm -rf /tmp/demo"},
            }
            stdout = io.StringIO()
            with mock.patch.object(module, "POLICY_FILES", (bad_policy,)), mock.patch(
                "sys.stdin", io.StringIO(json.dumps(payload))
            ), mock.patch("sys.stdout", stdout):
                result = module.main()

        self.assertEqual(result, 0)
        response = json.loads(stdout.getvalue())
        self.assertIn("Skipped bash-safety.md", response["systemMessage"])

    def test_post_tool_adds_follow_up_context_for_failed_runtime_command(self) -> None:
        module = load_module("post_tool_use_policy_warn", POST_TOOL_PATH)
        payload = {
            "tool_name": "Bash",
            "tool_input": {"command": "python3 scripts/validate-codex-support.py"},
            "tool_response": json.dumps(
                {
                    "returncode": 1,
                    "stderr": "Codex support validation failed: stale or invalid parity contract",
                }
            ),
        }
        stdout = io.StringIO()
        with mock.patch("sys.stdin", io.StringIO(json.dumps(payload))), mock.patch(
            "sys.stdout", stdout
        ):
            result = module.main()

        self.assertEqual(result, 0)
        response = json.loads(stdout.getvalue())
        self.assertIn("runtime or Xcode bridge is not ready", response["systemMessage"])
        self.assertEqual(response["hookSpecificOutput"]["hookEventName"], "PostToolUse")

    def test_hooks_json_uses_one_supported_handler_per_event(self) -> None:
        payload = json.loads(HOOKS_PATH.read_text())
        hooks = payload["hooks"]

        self.assertEqual(len(hooks["PreToolUse"]), 1)
        self.assertEqual(len(hooks["PostToolUse"]), 1)
        self.assertEqual(hooks["PreToolUse"][0]["matcher"], "Bash")
        self.assertEqual(hooks["PostToolUse"][0]["matcher"], "Bash")
        self.assertNotIn("matcher", hooks["Stop"][0])


if __name__ == "__main__":
    unittest.main()
