---
name: codex-operating-layer
description: Use as the primary autonomous entrypoint for this repo's Codex-first runtime. It maps the task to the canonical parity contract, loads the narrowest Apple lifecycle skills, delegates to the right specialist agents, and validates Codex-surface changes before finishing.
---

# Codex Operating Layer

## Purpose

This is the repo's canonical Codex workflow entrypoint.

Use it when the task should be routed through the repo's Codex-first operating
model rather than treated as an isolated skill lookup.

The operating layer is defined by:
- `.codex-plugin/plugin.json`
- `.codex/config.toml`
- `.codex/hooks.json`
- `.codex/agents/*.toml`
- `.codex/parity-source.toml`
- `.codex/contracts/parity-contract.json`
- `.mcp.json`

## Primary Workflow

### 1) Classify the outcome
- Start from `.codex/contracts/parity-contract.json`.
- Map the request to the narrowest supported outcome and reuse its listed skills
  and specialist agents.
- If the request spans multiple outcomes, choose one primary lane and sequence
  the rest behind it.

### 2) Load the narrowest skills
- For planning and architecture, start with:
  - `app-development-workflow`
  - `macos-development`
  - `swift-app-lifecycle`
  - `swift-project-scaffold`
- For design-system and HIG work, start with:
  - `macos-app-design`
  - `apple-liquid-glass-design`
  - `swiftui-ui-patterns`
  - `swiftui-components`
- For implementation and build work, start with:
  - `autonomous-ui-workflow`
  - `swift-networking`
  - `swift-concurrency`
  - `swift-localization`
  - `swift-actor-persistence`
  - `xcode-mcp`
- For review and test work, start with:
  - `code-analyzer`
  - `audit-context-building`
  - `swiftui-view-refactor`
  - `ios-testing`
- For runtime readiness and diagnosis, start with:
  - `codex-runtime-doctor`
  - Treat `codex-runtime-doctor` as diagnosis-only; it reports readiness and
    remediation, but it does not install, repair, build, or test
- For Codex/plugin/runtime work, include:
  - `codex-runtime-doctor` before deeper runtime or Xcode troubleshooting when
    hook behavior, contract truth, or root bridge wiring may be degraded
  - `plugin-creator` for backing-bundle scaffolding or external marketplace
    files only

### 3) Delegate deliberately
- Use `swift_architect` for lifecycle framing, architecture boundaries, and
  system decomposition.
- Use `swift_designer` for Apple HIG, component selection, and Liquid Glass or
  design-system guidance.
- Use `swift_builder` for code changes, build workflows, Xcode MCP tasks, and
  canonical Codex layer implementation.
- Use `swift_quality` for review, validation, test planning, and contract truth
  checks.
- Parallelize only non-overlapping work. Keep the blocking step local when the
  next action depends on it immediately.

### 4) Maintain Codex truth
- If the task touches `.codex/`, `.codex-plugin/`, `.mcp.json`,
  `.agents/plugins/marketplace.json`, `.agents/skills/plugin-creator/`,
  `README.md`, `AGENTS.md`, or the Codex validation/generation scripts,
  regenerate the parity contract and rerun the validator before you finish.
- Treat the repo-root Codex layer as canonical. The older plugin-local manifests
  under `plugins/*/.codex-plugin/` are backing bundles, not the primary runtime
  contract.
- The repo-root marketplace must stay a single canonical `./` install surface.
  Do not use `plugin-creator` to append backing-bundle entries there.

### 5) Finish with evidence
- For Codex-surface changes, run:
  - `python3 scripts/generate_codex_parity_contract.py`
  - `python3 scripts/generate_codex_parity_contract.py --check`
  - `python3 scripts/validate-codex-support.py`
- For app implementation work, also gather the smallest relevant build, preview,
  or test evidence through `xcode-mcp` or `ios-testing`.

## Guardrails

- Do not route users into Claude-only command manifests or named Claude agents.
- Do not invent parity claims beyond what the generated contract says.
- Do not treat hooks as a general interception framework. In this repo they are
  experimental, Bash-only for `PreToolUse` / `PostToolUse`, and still anchored
  by the authoritative `Stop` validation gate.
- Route runtime readiness questions through `codex-runtime-doctor` before
  escalating into broader Xcode or environment debugging.
- Keep the orchestration outcome-focused. Load the narrowest skill set that can
  do the job.
