"""Shared host-agnostic hook-policy evaluation engine."""

from __future__ import annotations

import re
from functools import lru_cache
from typing import Mapping

from scripts.hook_policy.models import Match, MatchSet, NormalizedDecision, Rule


@lru_cache(maxsize=128)
def compile_regex(pattern: str) -> re.Pattern[str]:
    """Compile regex patterns with caching."""
    return re.compile(pattern, re.IGNORECASE)


def matches_tool(matcher: str, tool_name: str) -> bool:
    """Return whether the normalized tool name matches the matcher."""
    if matcher == "*":
        return True
    return tool_name in matcher.split("|")


def _match_condition(operator: str, pattern: str, field_value: str) -> bool:
    """Evaluate one operator against a normalized field value."""
    if operator == "regex_match":
        try:
            return bool(compile_regex(pattern).search(field_value))
        except re.error:
            return False
    if operator == "contains":
        return pattern in field_value
    if operator == "equals":
        return pattern == field_value
    if operator == "not_contains":
        return pattern not in field_value
    if operator == "starts_with":
        return field_value.startswith(pattern)
    if operator == "ends_with":
        return field_value.endswith(pattern)
    return False


def rule_matches(rule: Rule, normalized_fields: Mapping[str, str]) -> bool:
    """Return whether a rule matches the normalized string field map."""
    tool_name = normalized_fields.get("tool_name", "")
    if rule.tool_matcher and not matches_tool(rule.tool_matcher, tool_name):
        return False
    if not rule.conditions:
        return False
    for condition in rule.conditions:
        field_name = condition.field
        if not field_name:
            return False
        field_value = normalized_fields.get(field_name)
        if field_value is None:
            return False
        if not _match_condition(condition.operator, condition.pattern, field_value):
            return False
    return True


def evaluate_rules(rules: list[Rule], normalized_fields: Mapping[str, str]) -> MatchSet:
    """Evaluate rules against a normalized field map."""
    blocking: list[Match] = []
    warnings: list[Match] = []
    for rule in rules:
        if not rule_matches(rule, normalized_fields):
            continue
        match = Match(rule=rule)
        if rule.action == "block":
            blocking.append(match)
        else:
            warnings.append(match)
    return MatchSet(blocking=tuple(blocking), warnings=tuple(warnings))


def choose_outcome(match_set: MatchSet) -> NormalizedDecision:
    """Choose the highest-priority normalized decision from matched rules."""
    if match_set.blocking:
        matched_rules = tuple(match.rule for match in match_set.blocking)
        return NormalizedDecision(
            action="block",
            matched_rules=matched_rules,
            message=_combine_messages(matched_rules),
        )
    if match_set.warnings:
        matched_rules = tuple(match.rule for match in match_set.warnings)
        return NormalizedDecision(
            action="warn",
            matched_rules=matched_rules,
            message=_combine_messages(matched_rules),
        )
    return NormalizedDecision(action="allow")


def _combine_messages(rules: tuple[Rule, ...]) -> str:
    """Join rule messages in stable evaluation order."""
    return "\n\n".join(f"**[{rule.name}]**\n{rule.message}" for rule in rules)
