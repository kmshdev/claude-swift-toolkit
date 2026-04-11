# Codex Plugin Migration Knowledge Base

Archive status: Historical research snapshot

- Snapshot captured: 2026-04-11
- Total modules analyzed: 5
- Depth level used: focused
- Completion percentage at capture: 100%

This directory is an archive of the research and migration notes used to add a
Codex-compatible package surface to this repository. It is not the live source
of truth for the current Codex install surface.

## Live Source Of Truth

Use these files for the current package contract:

- `README.md` for the active lifecycle and host-compatibility overview
- `AGENTS.md` and `CLAUDE.md` for contributor-facing workflow guidance
- `.agents/plugins/marketplace.json` for the repo-scoped Codex marketplace
- `plugins/*/.codex-plugin/plugin.json` for the published plugin manifests
- `plugins/apple-app-builder/.mcp.json` and
  `plugins/apple-app-quality/.mcp.json` for the official Xcode MCP bridge
  wiring

## Scope

This directory captures the research and migration-time rationale for making
`claude-swift-toolkit` installable as a Codex/OpenAI plugin source without
breaking the existing Claude Code plugin layout.

## What This Archive Records

At the time of the migration snapshot, the repository had adopted a dual-host
pattern supported by the official Codex plugin docs and reinforced by current
community practice:

- Keep existing Claude manifests in `.claude-plugin/`
- Add Codex manifests in `.codex-plugin/` where the repo has a plausible Codex
  surface
- Publish a repo-scoped Codex marketplace at
  `.agents/plugins/marketplace.json`
- Package Codex-facing wrapper skill trees only where host behavior diverges
- Bundle plugin-local `.mcp.json` files for the builder and quality plugins through Xcode's official MCP bridge (`xcrun mcpbridge`)
- Leave unsupported Claude-only surfaces explicit instead of guessing at a
  Codex equivalent

Those statements describe the migration snapshot, not an evergreen contract.
Check the live source-of-truth files above before treating any archived note as
current guidance.

## Modules

- `official-build-surface` — official Codex plugin packaging and marketplace rules
- `community-validation-and-distribution` — validation, CI, and repo-marketplace practices
- `dual-manifest-compatibility` — dual Claude/Codex manifest pattern for discoverability
- `thin-wrapper-patterns` — example wrapper patterns around skills and MCP
- `repo-application-plan` — direct mapping of those findings onto this repository

## File Guide

- `*_entry.json` — analyzed module entries
- `database.json` — merged module database
- `by_category.json` — module index by category
- `by_trait.json` — module index by trait
- `dependencies.json` — dependency graph across modules
- `ANALYSIS_COMPLETE.md` — final synthesis summary
