"""Shared stdlib-only hook policy primitives."""

from scripts.hook_policy.engine import (
    choose_outcome,
    compile_regex,
    evaluate_rules,
    matches_tool,
    rule_matches,
)
from scripts.hook_policy.loader import (
    RuleParseError,
    extract_frontmatter,
    load_rule_file,
    load_rule_files,
)
from scripts.hook_policy.models import (
    Condition,
    Match,
    MatchSet,
    NormalizedDecision,
    Rule,
)

__all__ = [
    "Condition",
    "Match",
    "MatchSet",
    "NormalizedDecision",
    "Rule",
    "RuleParseError",
    "choose_outcome",
    "compile_regex",
    "evaluate_rules",
    "extract_frontmatter",
    "load_rule_file",
    "load_rule_files",
    "matches_tool",
    "rule_matches",
]
