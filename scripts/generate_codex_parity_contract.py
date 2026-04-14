#!/usr/bin/env python3
"""Generate the canonical Codex parity contract for this repository."""

from __future__ import annotations

import argparse
import json
import sys
import tomllib
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.hook_policy.loader import extract_frontmatter as extract_markdown_frontmatter  # noqa: E402

CONFIG_PATH = ROOT / ".codex" / "config.toml"
HOOKS_PATH = ROOT / ".codex" / "hooks.json"
AGENTS_DIR = ROOT / ".codex" / "agents"
PARITY_SOURCE_PATH = ROOT / ".codex" / "parity-source.toml"
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE_PATH = ROOT / ".agents" / "plugins" / "marketplace.json"
MCP_PATH = ROOT / ".mcp.json"
OUTPUT_PATH = ROOT / ".codex" / "contracts" / "parity-contract.json"


@dataclass(frozen=True)
class SkillRecord:
    """Resolved skill metadata from a configured skill folder."""

    name: str
    description: str
    path: str
    source_group: str


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the committed parity contract is stale.",
    )
    parser.add_argument(
        "--output",
        default=str(OUTPUT_PATH),
        help="Write path for the generated contract.",
    )
    return parser.parse_args()


def load_json(path: Path) -> object:
    """Load a JSON file with a stable error message."""
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # pragma: no cover - surfaced to user
        raise ValueError(f"{path}: invalid JSON ({exc})") from exc



def load_toml(path: Path) -> dict[str, object]:
    """Load a TOML file with a stable error message."""
    try:
        return tomllib.loads(path.read_text())
    except Exception as exc:  # pragma: no cover - surfaced to user
        raise ValueError(f"{path}: invalid TOML ({exc})") from exc



def parse_frontmatter(skill_path: Path) -> tuple[dict[str, str], str]:
    """Read the limited SKILL frontmatter used by this repository."""
    payload, body = extract_markdown_frontmatter(skill_path.read_text(), path=skill_path)
    if not isinstance(payload, dict):
        raise ValueError(f"{skill_path}: frontmatter must be a top-level mapping")

    frontmatter: dict[str, str] = {}
    for key, value in payload.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{skill_path}: frontmatter '{key}' must be a non-empty string")
        frontmatter[str(key)] = value
    return frontmatter, body



def relative_to_root(path: Path) -> str:
    """Return a repo-relative POSIX path."""
    return path.resolve().relative_to(ROOT.resolve()).as_posix()



def classify_skill_source(path: Path) -> str:
    """Map a skill folder to a human-meaningful source group."""
    parts = path.resolve().relative_to(ROOT.resolve()).parts
    if parts[:2] == (".codex", "skills"):
        return "runtime"
    if parts[:2] == (".agents", "skills"):
        return "automation"
    if len(parts) >= 2 and parts[0] == "plugins":
        return parts[1]
    return parts[0]



def resolve_skill_records(config_path: Path) -> list[SkillRecord]:
    """Resolve enabled skills from `.codex/config.toml`."""
    payload = load_toml(config_path)
    skills_section = payload.get("skills", {})
    if not isinstance(skills_section, dict):
        raise ValueError(f"{config_path}: skills section must be a table")
    skill_entries = skills_section.get("config", [])
    if not isinstance(skill_entries, list):
        raise ValueError(f"{config_path}: skills.config must be an array")

    seen_names: set[str] = set()
    records: list[SkillRecord] = []
    for entry in skill_entries:
        if not isinstance(entry, dict):
            raise ValueError(f"{config_path}: each skills.config entry must be a table")
        if entry.get("enabled") is False:
            continue
        raw_path = entry.get("path")
        if not isinstance(raw_path, str) or not raw_path:
            raise ValueError(f"{config_path}: each enabled skills.config entry needs path")
        skill_dir = (config_path.parent / raw_path).resolve()
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.is_file():
            raise ValueError(f"{skill_dir}: missing SKILL.md")
        frontmatter, _ = parse_frontmatter(skill_path)
        name = frontmatter.get("name")
        description = frontmatter.get("description")
        if not name or not description:
            raise ValueError(f"{skill_path}: missing name or description")
        if name in seen_names:
            raise ValueError(f"duplicate configured skill name: {name}")
        seen_names.add(name)
        records.append(
            SkillRecord(
                name=name,
                description=description,
                path=relative_to_root(skill_dir),
                source_group=classify_skill_source(skill_dir),
            )
        )
    return records



def inventory_hooks(hooks_path: Path) -> list[dict[str, object]]:
    """Flatten hook metadata for the parity contract."""
    payload = load_json(hooks_path)
    if not isinstance(payload, dict):
        raise ValueError(f"{hooks_path}: expected top-level object")
    hooks = payload.get("hooks")
    if not isinstance(hooks, dict):
        raise ValueError(f"{hooks_path}: missing hooks object")

    items: list[dict[str, object]] = []
    for event_name, matcher_groups in hooks.items():
        if not isinstance(matcher_groups, list):
            raise ValueError(f"{hooks_path}: hooks.{event_name} must be a list")
        for group in matcher_groups:
            if not isinstance(group, dict):
                raise ValueError(f"{hooks_path}: matcher groups must be objects")
            group_matcher = group.get("matcher")
            group_hooks = group.get("hooks")
            if not isinstance(group_hooks, list):
                raise ValueError(f"{hooks_path}: hooks.{event_name} group missing hooks list")
            for hook in group_hooks:
                if not isinstance(hook, dict):
                    raise ValueError(f"{hooks_path}: hook entries must be objects")
                items.append(
                    {
                        "event": event_name,
                        "matcher": group_matcher,
                        "type": hook.get("type"),
                        "command": hook.get("command"),
                        "statusMessage": hook.get("statusMessage"),
                    }
                )
    return items



def build_hook_support(
    parity_source: dict[str, object], configured_events: set[str]
) -> list[dict[str, object]]:
    """Resolve support-level metadata for documented Codex hook events."""
    hook_support = parity_source.get("hook_support", [])
    if not isinstance(hook_support, list):
        raise ValueError(f"{PARITY_SOURCE_PATH}: hook_support must be an array")

    resolved: list[dict[str, object]] = []
    seen_events: set[str] = set()
    for item in hook_support:
        if not isinstance(item, dict):
            raise ValueError(f"{PARITY_SOURCE_PATH}: each hook_support entry must be a table")

        event = item.get("event")
        status = item.get("status")
        configured = item.get("configured")
        matcher_behavior = item.get("matcher_behavior")
        support_tags = item.get("support_tags", [])
        policy_files = item.get("policy_files", [])
        limitations = item.get("limitations", [])
        handler = item.get("handler")

        if not isinstance(event, str) or not event.strip():
            raise ValueError(f"{PARITY_SOURCE_PATH}: hook_support.event must be a non-empty string")
        if event in seen_events:
            raise ValueError(f"{PARITY_SOURCE_PATH}: duplicate hook_support event '{event}'")
        seen_events.add(event)
        if not isinstance(status, str) or not status.strip():
            raise ValueError(f"{PARITY_SOURCE_PATH}: hook_support.{event} missing status")
        if not isinstance(configured, bool):
            raise ValueError(f"{PARITY_SOURCE_PATH}: hook_support.{event} configured must be boolean")
        if not isinstance(matcher_behavior, str) or not matcher_behavior.strip():
            raise ValueError(
                f"{PARITY_SOURCE_PATH}: hook_support.{event} missing matcher_behavior"
            )
        if not isinstance(support_tags, list) or any(
            not isinstance(tag, str) or not tag for tag in support_tags
        ):
            raise ValueError(f"{PARITY_SOURCE_PATH}: hook_support.{event} support_tags invalid")
        if not isinstance(policy_files, list) or any(
            not isinstance(path, str) or not path for path in policy_files
        ):
            raise ValueError(f"{PARITY_SOURCE_PATH}: hook_support.{event} policy_files invalid")
        if not isinstance(limitations, list) or any(
            not isinstance(text, str) or not text for text in limitations
        ):
            raise ValueError(f"{PARITY_SOURCE_PATH}: hook_support.{event} limitations invalid")
        if handler is not None and (not isinstance(handler, str) or not handler.strip()):
            raise ValueError(f"{PARITY_SOURCE_PATH}: hook_support.{event} handler must be a string")
        if configured and event not in configured_events:
            raise ValueError(
                f"{PARITY_SOURCE_PATH}: hook_support.{event} is configured but missing from hooks.json"
            )
        if not configured and event in configured_events and event != "UserPromptSubmit":
            raise ValueError(
                f"{PARITY_SOURCE_PATH}: hook_support.{event} must mark configured=true"
            )
        if handler is not None and not (ROOT / handler).is_file():
            raise ValueError(
                f"{PARITY_SOURCE_PATH}: hook_support.{event} handler missing: {ROOT / handler}"
            )
        for policy_path in policy_files:
            if not (ROOT / policy_path).is_file():
                raise ValueError(
                    f"{PARITY_SOURCE_PATH}: hook_support.{event} policy missing: {ROOT / policy_path}"
                )

        resolved.append(
            {
                "event": event,
                "status": status,
                "configured": configured,
                "matcherBehavior": matcher_behavior,
                "handler": handler,
                "policyFiles": policy_files,
                "supportTags": support_tags,
                "limitations": limitations,
            }
        )
    return resolved


def inventory_agents(agents_dir: Path) -> list[dict[str, object]]:
    """Load custom-agent metadata from `.codex/agents/*.toml`."""
    if not agents_dir.is_dir():
        raise ValueError(f"{agents_dir}: missing agent directory")

    records: list[dict[str, object]] = []
    seen_names: set[str] = set()
    for agent_path in sorted(agents_dir.glob("*.toml")):
        payload = load_toml(agent_path)
        name = payload.get("name")
        description = payload.get("description")
        developer_instructions = payload.get("developer_instructions")
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"{agent_path}: missing name")
        if not isinstance(description, str) or not description.strip():
            raise ValueError(f"{agent_path}: missing description")
        if not isinstance(developer_instructions, str) or not developer_instructions.strip():
            raise ValueError(f"{agent_path}: missing developer_instructions")
        if name in seen_names:
            raise ValueError(f"duplicate custom agent name: {name}")
        seen_names.add(name)
        records.append(
            {
                "name": name,
                "description": description,
                "path": relative_to_root(agent_path),
                "model": payload.get("model"),
                "model_reasoning_effort": payload.get("model_reasoning_effort"),
                "sandbox_mode": payload.get("sandbox_mode"),
            }
        )
    return records



def build_outcomes(
    parity_source: dict[str, object],
    skill_lookup: dict[str, SkillRecord],
    agent_lookup: set[str],
) -> list[dict[str, object]]:
    """Resolve outcome mappings against current skill and agent inventories."""
    outcomes = parity_source.get("outcomes", [])
    if not isinstance(outcomes, list):
        raise ValueError(f"{PARITY_SOURCE_PATH}: outcomes must be an array")

    resolved: list[dict[str, object]] = []
    for outcome in outcomes:
        if not isinstance(outcome, dict):
            raise ValueError(f"{PARITY_SOURCE_PATH}: each outcome must be a table")
        outcome_skills = outcome.get("skills", [])
        outcome_agents = outcome.get("agents", [])
        if not isinstance(outcome_skills, list) or not isinstance(outcome_agents, list):
            raise ValueError(f"{PARITY_SOURCE_PATH}: outcome skills and agents must be arrays")

        missing_skills = [name for name in outcome_skills if name not in skill_lookup]
        missing_agents = [name for name in outcome_agents if name not in agent_lookup]
        if missing_skills:
            raise ValueError(
                f"{PARITY_SOURCE_PATH}: unknown outcome skills: {', '.join(missing_skills)}"
            )
        if missing_agents:
            raise ValueError(
                f"{PARITY_SOURCE_PATH}: unknown outcome agents: {', '.join(missing_agents)}"
            )

        resolved.append(
            {
                "id": outcome.get("id"),
                "label": outcome.get("label"),
                "description": outcome.get("description"),
                "skills": [
                    {
                        "name": name,
                        "path": skill_lookup[name].path,
                        "source_group": skill_lookup[name].source_group,
                    }
                    for name in outcome_skills
                ],
                "agents": list(outcome_agents),
            }
        )
    return resolved



def build_runtime_doctor(
    parity_source: dict[str, object], skill_lookup: dict[str, SkillRecord]
) -> dict[str, object] | None:
    """Resolve runtime doctor metadata from parity source."""
    runtime_doctor = parity_source.get("runtime_doctor")
    if runtime_doctor is None:
        return None
    if not isinstance(runtime_doctor, dict):
        raise ValueError(f"{PARITY_SOURCE_PATH}: runtime_doctor must be a table")

    skill_name = runtime_doctor.get("skill")
    role = runtime_doctor.get("role")
    checks = runtime_doctor.get("checks", [])
    limitations = runtime_doctor.get("limitations", [])
    if not isinstance(skill_name, str) or skill_name not in skill_lookup:
        raise ValueError(f"{PARITY_SOURCE_PATH}: runtime_doctor.skill must name a configured skill")
    if not isinstance(role, str) or not role.strip():
        raise ValueError(f"{PARITY_SOURCE_PATH}: runtime_doctor.role must be a string")
    if not isinstance(checks, list) or any(not isinstance(item, str) or not item for item in checks):
        raise ValueError(f"{PARITY_SOURCE_PATH}: runtime_doctor.checks must be a string array")
    if not isinstance(limitations, list) or any(
        not isinstance(item, str) or not item for item in limitations
    ):
        raise ValueError(
            f"{PARITY_SOURCE_PATH}: runtime_doctor.limitations must be a string array"
        )

    skill = skill_lookup[skill_name]
    return {
        "skill": {
            "name": skill.name,
            "path": skill.path,
            "source_group": skill.source_group,
        },
        "role": role,
        "checks": checks,
        "limitations": limitations,
    }


def build_bundles(skill_records: list[SkillRecord]) -> list[dict[str, object]]:
    """Group skills by source group for easier inspection."""
    bundles: defaultdict[str, list[SkillRecord]] = defaultdict(list)
    for record in skill_records:
        bundles[record.source_group].append(record)

    return [
        {
            "id": bundle_name,
            "skills": [
                {
                    "name": record.name,
                    "path": record.path,
                }
                for record in sorted(bundle_records, key=lambda item: item.name)
            ],
        }
        for bundle_name, bundle_records in sorted(bundles.items())
    ]



def build_contract() -> dict[str, object]:
    """Build the parity contract payload."""
    manifest = load_json(MANIFEST_PATH)
    marketplace = load_json(MARKETPLACE_PATH)
    config = load_toml(CONFIG_PATH)
    parity_source = load_toml(PARITY_SOURCE_PATH)
    skill_records = resolve_skill_records(CONFIG_PATH)
    skill_lookup = {record.name: record for record in skill_records}
    agent_records = inventory_agents(AGENTS_DIR)
    agent_lookup = {record["name"] for record in agent_records}
    hook_records = inventory_hooks(HOOKS_PATH)
    configured_events = {
        record["event"] for record in hook_records if isinstance(record.get("event"), str)
    }
    hook_support = build_hook_support(parity_source, configured_events)
    runtime_doctor = build_runtime_doctor(parity_source, skill_lookup)

    primary_skill = parity_source.get("primary_skill")
    if not isinstance(primary_skill, str) or primary_skill not in skill_lookup:
        raise ValueError(f"{PARITY_SOURCE_PATH}: primary_skill must name a configured skill")

    validation_targets = parity_source.get("validation_targets", [])
    if not isinstance(validation_targets, list) or any(
        not isinstance(target, str) or not target for target in validation_targets
    ):
        raise ValueError(f"{PARITY_SOURCE_PATH}: validation_targets must be a string array")

    if not isinstance(manifest, dict) or not isinstance(marketplace, dict):
        raise ValueError("manifest and marketplace must be JSON objects")

    outcomes = build_outcomes(parity_source, skill_lookup, agent_lookup)
    features = config.get("features", {})
    agents_config = config.get("agents", {})

    return {
        "version": parity_source.get("version", 1),
        "canonical": {
            "manifest": relative_to_root(MANIFEST_PATH),
            "marketplace": relative_to_root(MARKETPLACE_PATH),
            "config": relative_to_root(CONFIG_PATH),
            "hooks": relative_to_root(HOOKS_PATH),
            "agentsDir": relative_to_root(AGENTS_DIR),
            "paritySource": relative_to_root(PARITY_SOURCE_PATH),
            "mcp": relative_to_root(MCP_PATH),
            "primarySkill": primary_skill,
            "validationTargets": list(validation_targets),
        },
        "plugin": {
            "name": manifest.get("name"),
            "version": manifest.get("version"),
            "description": manifest.get("description"),
            "skillsPath": manifest.get("skills"),
            "mcpServersPath": manifest.get("mcpServers"),
            "interface": manifest.get("interface"),
        },
        "marketplace": {
            "name": marketplace.get("name"),
            "displayName": marketplace.get("interface", {}).get("displayName"),
            "plugins": marketplace.get("plugins"),
        },
        "runtime": {
            "features": features,
            "agents": agents_config,
            "skills": [record.__dict__ for record in skill_records],
            "skillBundles": build_bundles(skill_records),
            "customAgents": agent_records,
            "hooks": hook_records,
            "hookSupport": hook_support,
            "readiness": runtime_doctor,
        },
        "outcomes": outcomes,
    }



def render_contract(contract: dict[str, object]) -> str:
    """Serialize the contract deterministically."""
    return json.dumps(contract, indent=2) + "\n"



def main() -> int:
    """Generate or validate the parity contract."""
    args = parse_args()
    output_path = Path(args.output).expanduser().resolve()
    contract_text = render_contract(build_contract())

    if args.check:
        if not output_path.exists():
            print(f"Missing parity contract: {output_path}", file=sys.stderr)
            return 1
        existing_text = output_path.read_text()
        if existing_text != contract_text:
            print("Codex parity contract is stale.", file=sys.stderr)
            return 1
        print("Codex parity contract is current.")
        return 0

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(contract_text)
    print(f"Wrote parity contract: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
