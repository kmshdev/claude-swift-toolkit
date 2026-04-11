# Codex Plugin Migration Knowledge Base

Status: Complete

- Total modules analyzed: 5
- Depth level used: focused
- Completion percentage: 100%
- Last updated: 2026-04-11

## Scope

This directory captures the research and implementation rationale for making
`claude-swift-toolkit` installable as a Codex/OpenAI plugin source without
breaking the existing Claude Code plugin layout.

## Outcome

The repository now follows a dual-host pattern supported by the official
Codex plugin docs and reinforced by current community practice:

- Keep existing Claude manifests in `.claude-plugin/`
- Add Codex manifests in `.codex-plugin/` where the repo has a plausible Codex
  surface
- Publish a repo-scoped Codex marketplace at
  `.agents/plugins/marketplace.json`
- Package Codex-facing wrapper skill trees only where host behavior diverges
- Bundle plugin-local `.mcp.json` files for the builder and quality plugins through Xcode's official MCP bridge (`xcrun mcpbridge`)
- Leave unsupported Claude-only surfaces explicit instead of guessing at a Codex
  equivalent

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
