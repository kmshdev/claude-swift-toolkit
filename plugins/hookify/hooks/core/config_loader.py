#!/usr/bin/env python3
"""Configuration loader for hookify plugin.

Loads and parses `.claude/hookify.*.local.md` files while delegating parsing
and rule normalization to the shared stdlib-only hook-policy module.
"""

from __future__ import annotations

import glob
import sys
from pathlib import Path
from typing import Optional


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.hook_policy.loader import (  # noqa: E402
    RuleParseError,
    extract_frontmatter,
    load_rule_file as shared_load_rule_file,
)
from scripts.hook_policy.models import Condition, Rule  # noqa: E402

__all__ = [
    "Condition",
    "Rule",
    "RuleParseError",
    "extract_frontmatter",
    "load_rule_file",
    "load_rules",
]


def load_rules(event: str | None = None) -> list[Rule]:
    """Load enabled hookify rules from the local `.claude` directory."""
    rules: list[Rule] = []
    for file_path in sorted(glob.glob(str(Path(".claude") / "hookify.*.local.md"))):
        rule = load_rule_file(file_path)
        if rule is None:
            continue
        if event and rule.event not in {"all", event}:
            continue
        if rule.enabled:
            rules.append(rule)
    return rules


def load_rule_file(file_path: str | Path) -> Optional[Rule]:
    """Load one hookify rule file, logging stable errors to stderr."""
    try:
        return shared_load_rule_file(file_path)
    except (OSError, UnicodeDecodeError) as exc:
        print(f"Error: Cannot read {file_path}: {exc}", file=sys.stderr)
        return None
    except RuleParseError as exc:
        print(f"Error: Malformed rule file {file_path}: {exc}", file=sys.stderr)
        return None
    except Exception as exc:  # pragma: no cover - defensive wrapper parity
        print(
            f"Error: Unexpected error parsing {file_path} ({type(exc).__name__}): {exc}",
            file=sys.stderr,
        )
        return None
