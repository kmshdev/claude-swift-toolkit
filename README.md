# Codex Swift Toolkit

Codex-first Apple app development toolkit for this repository.

The canonical system is no longer "a marketplace of four lifecycle plugins." It
is one repo-scoped Codex operating layer that combines:

- one root Codex plugin manifest
- one repo-local Codex runtime in `.codex/`
- one root Xcode MCP bridge config
- one primary orchestration entrypoint skill
- one generated parity contract that documents the supported surface

## Canonical Source Of Truth

Treat these files as the live Codex contract for this repo:

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
- `AGENTS.md`

Everything else is secondary. In particular, the older plugin-local manifests in
`plugins/*/.codex-plugin/` are now backing bundles for lifecycle skills, not the
canonical Codex operating contract.

## What This Repo Provides

### 1. Root install surface

The repo now exposes one canonical local plugin:

- name: `codex-swift-toolkit`
- manifest: `.codex-plugin/plugin.json`
- marketplace wrapper: `.agents/plugins/marketplace.json`
- Xcode MCP bridge: `.mcp.json`

### 2. Repo-local runtime layer

The runtime lives in `.codex/` and adds:

- repo-scoped hooks
- custom specialist agents
- curated skill activation through `skills.config`
- generated parity-contract metadata

### 3. One primary workflow entrypoint

Start with:

- `codex-operating-layer`

That skill is the top-level orchestrator for the repo. It maps the task to the
right outcome lane, loads the narrowest skills, delegates to the right
specialist agents, and reruns Codex-surface validation when the canonical layer
changes.

### 4. Backing lifecycle knowledge

The operating layer reuses the existing Apple lifecycle skill library from the
repo's backing bundles. Those skills are activated through `.codex/config.toml`
rather than treated as four separate primary install units.

## Quick Start

### Codex / OpenAI

1. Clone the repo.
2. Open the repo in Codex.
3. Install the local plugin from `.agents/plugins/marketplace.json`.
4. Restart Codex after changing `.codex-plugin/plugin.json`, `.codex/config.toml`,
   `.codex/hooks.json`, or `.agents/plugins/marketplace.json`.
5. Start with `$codex-operating-layer`.
6. In the Codex app, enabled skills also appear in the slash-command list.

### Xcode requirement

The build and test lanes depend on Xcode's official MCP bridge via `xcrun mcpbridge`.
Xcode must be installed and running before the bridge can attach.

## Runtime Layout

| Path | Role |
|------|------|
| `.codex-plugin/plugin.json` | Canonical root plugin manifest |
| `.agents/plugins/marketplace.json` | Local install wrapper pointing at repo root |
| `.mcp.json` | Root Xcode MCP bridge configuration |
| `.codex/config.toml` | Repo-local Codex runtime config and curated skill activation |
| `.codex/hooks.json` | Repo-local experimental hooks |
| `.codex/hooks/` | Hook scripts for session context and stop-time validation |
| `.codex/agents/` | Specialist custom-agent definitions |
| `.codex/skills/codex-operating-layer/` | Primary orchestration entrypoint |
| `.codex/parity-source.toml` | Human-authored outcome and validation source |
| `.codex/contracts/parity-contract.json` | Generated machine-readable Codex surface contract |
| `.agents/skills/plugin-creator/` | Integrated runtime-tooling skill for backing-bundle scaffolding |
| `scripts/generate_codex_parity_contract.py` | Contract generator |
| `scripts/validate-codex-support.py` | Canonical Codex surface validator |

## Specialist Agents

The operating layer uses these repo-local custom agents:

- `swift_architect` — planning, lifecycle boundaries, module seams
- `swift_designer` — HIG alignment, Liquid Glass, component-system guidance
- `swift_builder` — implementation, Xcode MCP workflows, runtime changes
- `swift_quality` — review, refactor, testing, contract truth checks

## Outcome Lanes

The parity contract currently defines five high-value lanes:

- `plan-architecture` — app planning, architecture, lifecycle setup
- `design-system` — Apple HIG, Liquid Glass, SwiftUI reference work
- `implementation-build` — implementation, concurrency, networking, localization, Xcode-backed verification
- `review-test` — read-heavy review, audit context, refactor, tests
- `plugin-runtime` — Codex runtime, hooks, manifests, packaging, parity-contract work

The exact skill-to-lane mapping lives in `.codex/contracts/parity-contract.json`.

## Backing Skill Inventory

The runtime currently activates the following backing skill families through
`.codex/config.toml`:

- Core orchestration: `codex-operating-layer`
- Runtime tooling: `plugin-creator` for backing-bundle scaffolding and external
  marketplace files; the repo-root marketplace remains the single canonical
  `./` install surface
- Architecture: `app-development-workflow`, `macos-development`,
  `swift-app-lifecycle`, `swift-project-scaffold`
- Design system: `macos-app-design`, `apple-liquid-glass-design`,
  `swiftui-components`, `swiftui-ui-patterns`, and the focused SwiftUI API
  reference skills
- Implementation and build: `autonomous-ui-workflow`, `swift-networking`,
  `swift-concurrency`, `swift-localization`, `swift-actor-persistence`,
  `xcode-mcp`
- Quality: `code-analyzer`, `audit-context-building`, `swiftui-view-refactor`,
  `ios-testing`

## Hooks

Hooks are repo-scoped and experimental.

This repo uses them narrowly:

- `SessionStart` injects canonical Codex operating-layer context from the
  generated parity contract.
- `Stop` regenerates and validates the Codex surface when canonical files have
  changed.

Do not treat these hooks as a general Claude-style hook surface. They exist to
keep the root Codex runtime truthful and self-checking.

## Validation

When editing the canonical Codex layer, run:

```bash
python3 scripts/generate_codex_parity_contract.py
python3 scripts/generate_codex_parity_contract.py --check
python3 scripts/validate-codex-support.py
```

Also rerun that stack when editing the integrated runtime-tooling skill at
`.agents/skills/plugin-creator/`, because it is part of the canonical
`plugin-runtime` lane.

## Legacy Note

Claude-specific commands, hook workflows, and older plugin-local install shapes
still exist in the repo, but they are not the canonical Codex story anymore.
If you are intentionally working on Claude compatibility, use `CLAUDE.md` and
those legacy surfaces directly. Otherwise, stay on the root Codex layer.
