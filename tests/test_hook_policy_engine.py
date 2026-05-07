from __future__ import annotations

import textwrap
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from plugins.hookify.hooks.core.config_loader import load_rule_file as load_hookify_rule_file
from plugins.hookify.hooks.core.rule_engine import RuleEngine
from scripts.hook_policy.engine import choose_outcome, evaluate_rules
from scripts.hook_policy.loader import load_rule_file


class HookPolicyEngineTests(unittest.TestCase):
    def test_blocking_rules_take_priority_in_normalized_decision(self) -> None:
        with TemporaryDirectory() as temp_dir:
            block_path = Path(temp_dir) / "hookify.block-rm.local.md"
            block_path.write_text(
                textwrap.dedent(
                    """
                    ---
                    name: block-dangerous-rm
                    enabled: true
                    event: bash
                    pattern: rm\\s+-rf
                    action: block
                    tool_matcher: Bash
                    ---

                    Block dangerous rm.
                    """
                ).strip()
            )
            warn_path = Path(temp_dir) / "hookify.warn-rm.local.md"
            warn_path.write_text(
                textwrap.dedent(
                    """
                    ---
                    name: warn-dangerous-rm
                    enabled: true
                    event: bash
                    pattern: rm\\s+-rf
                    action: warn
                    tool_matcher: Bash
                    ---

                    Warn about dangerous rm.
                    """
                ).strip()
            )

            rules = [load_rule_file(block_path), load_rule_file(warn_path)]

        match_set = evaluate_rules(
            rules,
            {
                "tool_name": "Bash",
                "command": "rm -rf /tmp/demo",
            },
        )
        decision = choose_outcome(match_set)

        self.assertEqual(decision.action, "block")
        self.assertEqual([rule.name for rule in decision.matched_rules], ["block-dangerous-rm"])
        self.assertIn("Block dangerous rm.", decision.message)

    def test_missing_fields_and_unknown_operators_do_not_match(self) -> None:
        with TemporaryDirectory() as temp_dir:
            missing_field_path = Path(temp_dir) / "hookify.missing-field.local.md"
            missing_field_path.write_text(
                textwrap.dedent(
                    """
                    ---
                    name: missing-field
                    enabled: true
                    event: stop
                    conditions:
                      - field: transcript
                        operator: contains
                        pattern: TODO
                    ---

                    Transcript contains TODO.
                    """
                ).strip()
            )
            bad_operator_path = Path(temp_dir) / "hookify.bad-operator.local.md"
            bad_operator_path.write_text(
                textwrap.dedent(
                    """
                    ---
                    name: bad-operator
                    enabled: true
                    event: bash
                    conditions:
                      - field: command
                        operator: unsupported
                        pattern: rm
                    ---

                    Bad operator.
                    """
                ).strip()
            )

            rules = [load_rule_file(missing_field_path), load_rule_file(bad_operator_path)]

        match_set = evaluate_rules(rules, {"tool_name": "Bash", "command": "rm -rf /tmp/demo"})
        decision = choose_outcome(match_set)

        self.assertEqual(match_set.all_matches, ())
        self.assertEqual(decision.action, "allow")
        self.assertEqual(decision.message, "")

    def test_hookify_wrapper_still_evaluates_bash_rule(self) -> None:
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "hookify.block-rm.local.md"
            path.write_text(
                textwrap.dedent(
                    """
                    ---
                    name: block-dangerous-rm
                    enabled: true
                    event: bash
                    pattern: rm\\s+-rf
                    action: block
                    tool_matcher: Bash
                    ---

                    Block dangerous rm.
                    """
                ).strip()
            )

            rule = load_hookify_rule_file(path)

        engine = RuleEngine()
        result = engine.evaluate_rules(
            [rule],
            {
                "hook_event_name": "PreToolUse",
                "tool_name": "Bash",
                "tool_input": {"command": "rm -rf /tmp/demo"},
            },
        )

        self.assertEqual(result["hookSpecificOutput"]["permissionDecision"], "deny")
        self.assertIn("block-dangerous-rm", result["systemMessage"])

    def test_hookify_wrapper_still_evaluates_stop_rule(self) -> None:
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "hookify.require-tests.local.md"
            path.write_text(
                textwrap.dedent(
                    """
                    ---
                    name: require-tests-before-stop
                    enabled: true
                    event: stop
                    conditions:
                      - field: reason
                        operator: contains
                        pattern: tests pending
                    ---

                    Tests are still pending.
                    """
                ).strip()
            )

            rule = load_hookify_rule_file(path)

        engine = RuleEngine()
        result = engine.evaluate_rules(
            [rule],
            {
                "hook_event_name": "Stop",
                "reason": "tests pending before completion",
            },
        )

        self.assertEqual(
            result["systemMessage"],
            "**[require-tests-before-stop]**\nTests are still pending.",
        )

    def test_hookify_wrapper_combines_multiedit_content(self) -> None:
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "hookify.console-log.local.md"
            path.write_text(
                textwrap.dedent(
                    """
                    ---
                    name: warn-console-log
                    enabled: true
                    event: file
                    conditions:
                      - field: content
                        operator: contains
                        pattern: console.log(
                    ---

                    Console log detected.
                    """
                ).strip()
            )

            rule = load_hookify_rule_file(path)

        engine = RuleEngine()
        result = engine.evaluate_rules(
            [rule],
            {
                "hook_event_name": "PostToolUse",
                "tool_name": "MultiEdit",
                "tool_input": {
                    "file_path": "src/app.ts",
                    "edits": [
                        {"new_string": "console.log('one')"},
                        {"new_string": "console.log('two')"},
                    ],
                },
            },
        )

        self.assertEqual(result["systemMessage"], "**[warn-console-log]**\nConsole log detected.")
