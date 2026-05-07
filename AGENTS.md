# Codex Swift Toolkit

This repository now uses a canonical repo-scoped Codex operating layer.

## Canonical Codex Surface

Treat these files as the live Codex source of truth:

- `.codex-plugin/plugin.json`
- `.codex/config.toml`
- `.codex/hooks.json`
- `.codex/agents/*.toml`
- `.codex/skills/codex-operating-layer/`
- `.codex/parity-source.toml`
- `.codex/contracts/parity-contract.json`
- `.mcp.json`
- `.agents/plugins/marketplace.json`
- `.agents/skills/plugin-creator/`
- `README.md`

The older plugin-local manifests under `plugins/*/.codex-plugin/` are internal
backing bundles. They are no longer the primary Codex operating contract.

## Primary Entry Point

Start with `codex-operating-layer` for Codex work in this repo.

That skill is the top-level orchestrator. It maps the task to the right outcome
lane, loads the narrowest skills, delegates to the right custom agents, and
reruns Codex-surface validation when canonical files change.

## Specialist Agents

The repo-local custom-agent layer lives under `.codex/agents/`.

Use these roles when delegation helps:

- `swift_architect` for architecture, lifecycle boundaries, and planning
- `swift_designer` for HIG alignment, Liquid Glass, and design-system choices
- `swift_builder` for implementation, build workflows, and Codex runtime edits
- `swift_quality` for review, testing, and contract-truth verification

## Runtime Notes

- `.codex/config.toml` is the runtime control plane.
- `.codex/hooks.json` wires an experimental, Bash-only hook policy pack.
- `PreToolUse` and `PostToolUse` apply only to `Bash`, and `Stop` remains the
  authoritative completion gate.
- Use `codex-runtime-doctor` as the diagnosis-only readiness entrypoint before
  deeper hook or Xcode bridge troubleshooting.
- `.mcp.json` is the single Xcode MCP dependency story.
- `.codex/contracts/parity-contract.json` is generated. Do not hand-edit it.
- `.agents/skills/plugin-creator/` is part of the canonical `plugin-runtime`
  lane, but it must not rewrite the repo-root marketplace away from the single
  canonical `./` entry.

## Validation

If you touch `.codex/`, `.codex-plugin/`, `.mcp.json`,
`.agents/plugins/marketplace.json`, `.agents/skills/plugin-creator/`,
`README.md`, `AGENTS.md`, or the Codex validation/generation scripts, run:

```bash
python3 scripts/generate_codex_parity_contract.py
python3 scripts/generate_codex_parity_contract.py --check
python3 scripts/validate-codex-support.py
```

## Guardrails

- Do not route Codex users into Claude-only command manifests or named Claude
  agents.
- Do not claim parity beyond what `.codex/contracts/parity-contract.json`
  describes.
- Keep the Codex runtime repo-scoped and deterministic.
- Prefer the root Codex layer over the older child-plugin split when updating
  docs, validation, or workflow guidance.
- Use `plugin-creator` for backing-bundle scaffolding, not for adding extra
  entries to the repo-root canonical marketplace.
