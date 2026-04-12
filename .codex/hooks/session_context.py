#!/usr/bin/env python3
"""Inject the canonical Codex operating-layer context at session start."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = ROOT / ".codex" / "contracts" / "parity-contract.json"



def main() -> int:
    """Emit additional session context from the generated parity contract."""
    if not CONTRACT_PATH.is_file():
        return 0

    contract = json.loads(CONTRACT_PATH.read_text())
    canonical = contract.get("canonical", {})
    primary_skill = canonical.get("primarySkill", "codex-operating-layer")
    custom_agents = contract.get("runtime", {}).get("customAgents", [])
    agent_names = [item.get("name") for item in custom_agents if item.get("name")]

    additional_context = (
        "Canonical Codex source of truth lives at "
        f"{canonical.get('manifest')}, {canonical.get('config')}, {canonical.get('hooks')}, "
        f"{canonical.get('paritySource')}, and {canonical.get('mcp')}. "
        f"Primary entrypoint skill: {primary_skill}. "
        f"Available custom agents: {', '.join(agent_names)}. "
        "When those files change, regenerate the parity contract and rerun the validator before finishing."
    )
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": additional_context,
                }
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
