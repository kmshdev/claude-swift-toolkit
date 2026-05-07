"""Strict shared loader for hook-policy markdown rule files."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from scripts.hook_policy.models import Condition, Rule


EVENT_FIELD_MAP = {
    "bash": "command",
    "file": "new_text",
    "prompt": "user_prompt",
}


class RuleParseError(ValueError):
    """Raised when a rule file cannot be parsed."""


def parse_yaml_scalar(value: str, *, path: Path, line_number: int) -> object:
    """Parse the small YAML scalar subset used by hook policy files."""
    if value.startswith(("'", '"')):
        quote = value[0]
        if len(value) < 2 or not value.endswith(quote):
            raise RuleParseError(f"{path}:{line_number}: unterminated quoted scalar")
        return value[1:-1]
    if value == "null":
        return None
    if value == "true":
        return True
    if value == "false":
        return False
    return value


def _split_inline_pairs(item_text: str) -> list[str]:
    """Split inline mapping pairs while respecting quoted commas."""
    parts: list[str] = []
    current: list[str] = []
    quote: str | None = None

    for char in item_text:
        if quote:
            current.append(char)
            if char == quote:
                quote = None
            continue
        if char in {"'", '"'}:
            quote = char
            current.append(char)
            continue
        if char == ",":
            parts.append("".join(current).strip())
            current = []
            continue
        current.append(char)

    if current:
        parts.append("".join(current).strip())
    return [part for part in parts if part]


def _tokenize_yaml(text: str, *, path: Path, start_line: int) -> list[tuple[int, str, int]]:
    """Convert YAML text into indentation-aware entries."""
    entries: list[tuple[int, str, int]] = []
    for line_number, raw_line in enumerate(text.splitlines(), start=start_line):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        leading = raw_line[: len(raw_line) - len(raw_line.lstrip(" \t"))]
        if "\t" in leading:
            raise RuleParseError(f"{path}:{line_number}: tabs are not allowed for indentation")
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        if indent % 2 != 0:
            raise RuleParseError(
                f"{path}:{line_number}: indentation must use multiples of 2 spaces"
            )
        entries.append((indent, stripped, line_number))
    return entries


def _parse_yaml_text(text: str, *, path: Path, start_line: int) -> object:
    """Parse the narrow YAML subset used by hook policy frontmatter."""
    entries = _tokenize_yaml(text, path=path, start_line=start_line)
    if not entries:
        return {}

    def parse_block(index: int, indent: int) -> tuple[object, int]:
        if entries[index][1].startswith("- "):
            return parse_list(index, indent)
        return parse_mapping(index, indent)

    def parse_mapping(index: int, indent: int) -> tuple[dict[str, object], int]:
        mapping: dict[str, object] = {}
        while index < len(entries):
            current_indent, stripped, line_number = entries[index]
            if current_indent < indent:
                break
            if current_indent != indent:
                raise RuleParseError(f"{path}:{line_number}: unexpected indentation")
            if stripped.startswith("- "):
                raise RuleParseError(f"{path}:{line_number}: mixed YAML collection types")
            key, separator, raw_value = stripped.partition(":")
            if separator != ":" or not key.strip():
                raise RuleParseError(f"{path}:{line_number}: invalid mapping entry")
            key = key.strip()
            if key in mapping:
                raise RuleParseError(f"{path}:{line_number}: duplicate key '{key}'")
            index += 1
            raw_value = raw_value.lstrip()
            if raw_value:
                mapping[key] = parse_yaml_scalar(raw_value, path=path, line_number=line_number)
                continue
            if index < len(entries) and entries[index][0] > indent:
                child_indent = entries[index][0]
                if child_indent != indent + 2:
                    raise RuleParseError(
                        f"{path}:{entries[index][2]}: invalid nested indentation"
                    )
                mapping[key], index = parse_block(index, child_indent)
                continue
            mapping[key] = None
        return mapping, index

    def parse_list(index: int, indent: int) -> tuple[list[object], int]:
        items: list[object] = []
        while index < len(entries):
            current_indent, stripped, line_number = entries[index]
            if current_indent < indent:
                break
            if current_indent != indent:
                raise RuleParseError(f"{path}:{line_number}: unexpected indentation")
            if not stripped.startswith("- "):
                raise RuleParseError(f"{path}:{line_number}: mixed YAML collection types")
            item_text = stripped[2:].strip()
            index += 1

            if not item_text:
                if index < len(entries) and entries[index][0] > indent:
                    child_indent = entries[index][0]
                    if child_indent != indent + 2:
                        raise RuleParseError(
                            f"{path}:{entries[index][2]}: invalid nested indentation"
                        )
                    item_value, index = parse_block(index, child_indent)
                    items.append(item_value)
                    continue
                items.append(None)
                continue

            if ":" in item_text:
                item_mapping: dict[str, object] = {}
                for pair in _split_inline_pairs(item_text):
                    key, separator, raw_value = pair.partition(":")
                    if separator != ":" or not key.strip():
                        raise RuleParseError(f"{path}:{line_number}: invalid list mapping entry")
                    normalized_key = key.strip()
                    if normalized_key in item_mapping:
                        raise RuleParseError(
                            f"{path}:{line_number}: duplicate key '{normalized_key}'"
                        )
                    item_mapping[normalized_key] = parse_yaml_scalar(
                        raw_value.lstrip(), path=path, line_number=line_number
                    )
                if index < len(entries) and entries[index][0] > indent:
                    child_indent = entries[index][0]
                    if child_indent != indent + 2:
                        raise RuleParseError(
                            f"{path}:{entries[index][2]}: invalid nested indentation"
                        )
                    nested_value, index = parse_block(index, child_indent)
                    if not isinstance(nested_value, dict):
                        raise RuleParseError(
                            f"{path}:{line_number}: list item continuation must be a mapping"
                        )
                    for nested_key, nested_item in nested_value.items():
                        if nested_key in item_mapping:
                            raise RuleParseError(
                                f"{path}:{line_number}: duplicate key '{nested_key}'"
                            )
                        item_mapping[nested_key] = nested_item
                items.append(item_mapping)
                continue

            if index < len(entries) and entries[index][0] > indent:
                raise RuleParseError(
                    f"{path}:{entries[index][2]}: scalar list item cannot have nested values"
                )
            items.append(parse_yaml_scalar(item_text, path=path, line_number=line_number))
        return items, index

    parsed, final_index = parse_block(0, entries[0][0])
    if final_index != len(entries):
        line_number = entries[final_index][2]
        raise RuleParseError(f"{path}:{line_number}: trailing unparsed content")
    return parsed


def extract_frontmatter(
    content: str, *, path: str | Path = "<memory>"
) -> tuple[dict[str, object], str]:
    """Extract parsed frontmatter and the markdown body."""
    resolved_path = Path(path)
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, content

    closing_index: int | None = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break
    if closing_index is None:
        raise RuleParseError(f"{resolved_path}: missing closing frontmatter delimiter")

    frontmatter_text = "\n".join(lines[1:closing_index])
    body = "\n".join(lines[closing_index + 1 :]).strip()
    parsed = _parse_yaml_text(frontmatter_text, path=resolved_path, start_line=2)
    if not isinstance(parsed, dict):
        raise RuleParseError(f"{resolved_path}: frontmatter must be a mapping")
    return parsed, body


def _coerce_bool(value: object, *, default: bool = True) -> bool:
    """Coerce a parsed bool-like value."""
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, str) and value in {"true", "false"}:
        return value == "true"
    return default


def _infer_conditions(frontmatter: dict[str, object]) -> tuple[Condition, ...]:
    """Normalize legacy and explicit condition formats into condition objects."""
    raw_conditions = frontmatter.get("conditions")
    if raw_conditions is not None:
        if not isinstance(raw_conditions, list):
            raise RuleParseError("conditions must be a list")
        conditions: list[Condition] = []
        for item in raw_conditions:
            if not isinstance(item, dict):
                raise RuleParseError("each condition must be a mapping")
            conditions.append(Condition.from_mapping(item))
        return tuple(conditions)

    simple_pattern = frontmatter.get("pattern")
    if not isinstance(simple_pattern, str) or not simple_pattern:
        return ()
    event = str(frontmatter.get("event", "all"))
    field = EVENT_FIELD_MAP.get(event, "content")
    return (
        Condition.from_mapping(
            {
                "field": field,
                "operator": "regex_match",
                "pattern": simple_pattern,
            }
        ),
    )


def load_rule_file(file_path: str | Path) -> Rule:
    """Load one rule file from disk."""
    path = Path(file_path)
    content = path.read_text()
    frontmatter, message = extract_frontmatter(content, path=path)
    if not frontmatter:
        raise RuleParseError(f"{path}: missing YAML frontmatter")

    simple_pattern = frontmatter.get("pattern")
    if simple_pattern is not None and not isinstance(simple_pattern, str):
        simple_pattern = str(simple_pattern)

    tool_matcher = frontmatter.get("tool_matcher")
    if tool_matcher is not None and not isinstance(tool_matcher, str):
        tool_matcher = str(tool_matcher)

    action = frontmatter.get("action", "warn")
    if not isinstance(action, str):
        action = str(action)

    return Rule(
        name=str(frontmatter.get("name", "unnamed")),
        enabled=_coerce_bool(frontmatter.get("enabled"), default=True),
        event=str(frontmatter.get("event", "all")),
        pattern=simple_pattern,
        conditions=_infer_conditions(frontmatter),
        action=action,
        tool_matcher=tool_matcher,
        message=message,
    )


def load_rule_files(paths: Iterable[str | Path], *, event: str | None = None) -> list[Rule]:
    """Load enabled rules from an explicit file path list."""
    rules: list[Rule] = []
    for file_path in paths:
        rule = load_rule_file(file_path)
        if not rule.enabled:
            continue
        if event and rule.event not in {"all", event}:
            continue
        rules.append(rule)
    return rules
