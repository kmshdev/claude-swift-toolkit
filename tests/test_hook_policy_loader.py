from __future__ import annotations

import textwrap
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.hook_policy.loader import RuleParseError, load_rule_file, load_rule_files


class HookPolicyLoaderTests(unittest.TestCase):
    def test_loads_valid_markdown_rule(self) -> None:
        content = textwrap.dedent(
            """
            ---
            name: warn-dangerous-rm
            enabled: true
            event: bash
            pattern: rm\\s+-rf
            action: warn
            tool_matcher: Bash
            ---

            Dangerous command detected.
            """
        ).strip()
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "hookify.warn-dangerous-rm.local.md"
            path.write_text(content)

            rule = load_rule_file(path)

        self.assertEqual(rule.name, "warn-dangerous-rm")
        self.assertTrue(rule.enabled)
        self.assertEqual(rule.event, "bash")
        self.assertEqual(rule.pattern, r"rm\s+-rf")
        self.assertEqual(rule.action, "warn")
        self.assertEqual(rule.tool_matcher, "Bash")
        self.assertEqual(len(rule.conditions), 1)
        self.assertEqual(rule.conditions[0].field, "command")
        self.assertEqual(rule.conditions[0].operator, "regex_match")
        self.assertEqual(rule.conditions[0].pattern, r"rm\s+-rf")
        self.assertEqual(rule.message, "Dangerous command detected.")

    def test_preserves_mixed_condition_metadata_order(self) -> None:
        content = textwrap.dedent(
            """
            ---
            name: mixed-conditions
            enabled: true
            event: file
            conditions:
              - field: file_path
                operator: regex_match
                pattern: \\.env$
              - field: new_text, operator: contains
                pattern: API_KEY
                note: preserve-order
            ---

            Sensitive file change.
            """
        ).strip()
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "hookify.mixed-conditions.local.md"
            path.write_text(content)

            rule = load_rule_file(path)

        first_condition = rule.conditions[0].as_dict()
        second_condition = rule.conditions[1].as_dict()
        self.assertEqual(list(first_condition), ["field", "operator", "pattern"])
        self.assertEqual(list(second_condition), ["field", "operator", "pattern", "note"])
        self.assertEqual(second_condition["note"], "preserve-order")

    def test_duplicate_keys_raise_stable_loader_error(self) -> None:
        content = textwrap.dedent(
            """
            ---
            name: duplicate-key
            event: bash
            pattern: rm
            pattern: cp
            ---

            Duplicate key.
            """
        ).strip()
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "hookify.duplicate-key.local.md"
            path.write_text(content)

            with self.assertRaisesRegex(RuleParseError, r"duplicate key 'pattern'"):
                load_rule_file(path)

    def test_invalid_indentation_raises_stable_loader_error(self) -> None:
        content = (
            "---\n"
            "name: bad-indent\n"
            "event: file\n"
            "conditions:\n"
            "   - field: file_path\n"
            "---\n"
            "msg\n"
        )
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "hookify.bad-indent.local.md"
            path.write_text(content)

            with self.assertRaisesRegex(
                RuleParseError,
                r"indentation must use multiples of 2 spaces",
            ):
                load_rule_file(path)

    def test_unterminated_quoted_scalar_raises_stable_loader_error(self) -> None:
        content = textwrap.dedent(
            """
            ---
            name: "unterminated
            event: bash
            pattern: rm
            ---

            Broken quotes.
            """
        ).strip()
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "hookify.unterminated.local.md"
            path.write_text(content)

            with self.assertRaisesRegex(RuleParseError, r"unterminated quoted scalar"):
                load_rule_file(path)

    def test_load_rule_files_filters_disabled_and_event_mismatch(self) -> None:
        with TemporaryDirectory() as temp_dir:
            bash_path = Path(temp_dir) / "hookify.warn.local.md"
            bash_path.write_text(
                textwrap.dedent(
                    """
                    ---
                    name: warn-dangerous-rm
                    enabled: true
                    event: bash
                    pattern: rm\\s+-rf
                    ---

                    Dangerous command detected.
                    """
                ).strip()
            )
            disabled_path = Path(temp_dir) / "hookify.disabled.local.md"
            disabled_path.write_text(
                textwrap.dedent(
                    """
                    ---
                    name: disabled-rule
                    enabled: false
                    event: bash
                    pattern: ls
                    ---

                    Disabled rule.
                    """
                ).strip()
            )
            stop_path = Path(temp_dir) / "hookify.stop.local.md"
            stop_path.write_text(
                textwrap.dedent(
                    """
                    ---
                    name: stop-rule
                    enabled: true
                    event: stop
                    conditions:
                      - field: reason
                        operator: equals
                        pattern: user-requested
                    ---

                    Stop rule.
                    """
                ).strip()
            )

            rules = load_rule_files([bash_path, disabled_path, stop_path], event="bash")

        self.assertEqual([rule.name for rule in rules], ["warn-dangerous-rm"])
