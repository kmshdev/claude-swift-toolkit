"""Shared hook-policy data models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

ScalarValue = str | bool | None


@dataclass(frozen=True)
class Condition:
    """A normalized condition preserving metadata insertion order."""

    metadata: tuple[tuple[str, ScalarValue], ...]

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "Condition":
        """Build a condition from a parsed mapping."""
        entries: list[tuple[str, ScalarValue]] = []
        for key, value in data.items():
            if isinstance(value, bool) or value is None:
                normalized = value
            elif isinstance(value, str):
                normalized = value
            else:
                normalized = str(value)
            entries.append((str(key), normalized))
        return cls(metadata=tuple(entries))

    def as_dict(self) -> dict[str, ScalarValue]:
        """Return the condition metadata as an insertion-ordered dict."""
        return dict(self.metadata)

    def get(self, key: str, default: str = "") -> str:
        """Return a string condition value for engine matching."""
        value = dict(self.metadata).get(key)
        if value is None:
            return default
        if isinstance(value, bool):
            return "true" if value else "false"
        return value

    @property
    def field(self) -> str:
        """Return the normalized field name."""
        return self.get("field")

    @property
    def operator(self) -> str:
        """Return the normalized operator name."""
        return self.get("operator", "regex_match") or "regex_match"

    @property
    def pattern(self) -> str:
        """Return the normalized pattern string."""
        return self.get("pattern")


@dataclass(frozen=True)
class Rule:
    """A parsed hook-policy rule."""

    name: str
    enabled: bool
    event: str
    pattern: str | None = None
    conditions: tuple[Condition, ...] = ()
    action: str = "warn"
    tool_matcher: str | None = None
    message: str = ""


@dataclass(frozen=True)
class Match:
    """A single rule match."""

    rule: Rule


@dataclass(frozen=True)
class MatchSet:
    """Accumulated matches grouped by outcome priority."""

    blocking: tuple[Match, ...] = ()
    warnings: tuple[Match, ...] = ()

    @property
    def all_matches(self) -> tuple[Match, ...]:
        """Return all matches in priority order."""
        return self.blocking + self.warnings


@dataclass(frozen=True)
class NormalizedDecision:
    """Host-agnostic decision derived from matched rules."""

    action: str
    matched_rules: tuple[Rule, ...] = ()
    message: str = ""

    @property
    def matched(self) -> bool:
        """Return whether any rule matched."""
        return bool(self.matched_rules)
