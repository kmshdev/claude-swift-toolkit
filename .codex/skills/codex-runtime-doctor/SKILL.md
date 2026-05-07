---
name: codex-runtime-doctor
description: Use when Codex hook behavior, canonical runtime truth, or Xcode MCP readiness might be degraded. It diagnoses the repo-scoped Codex surface, reports hook and overlay constraints, and classifies root Xcode bridge readiness without mutating the environment.
---

# Codex Runtime Doctor

## Purpose

Use this skill before relying on hook-backed guardrails or Xcode-backed Apple
workflows in this repository.

It is diagnosis-only. It checks the repo-owned Codex runtime surface and reports
what is ready, degraded, or unavailable.

## What It Checks

- canonical repo-local Codex files parse and remain internally consistent
- repo-local hook readiness, including platform and feature-flag constraints
- whether a user-level `~/.codex/hooks.json` overlay exists outside the repo
- root `.mcp.json` wiring and low-cost `xcrun` / `mcpbridge` discoverability

## What It Must Not Do

- mutate config or rewrite files
- install tools or start background MCP sessions
- open Xcode, build projects, run previews, or run tests
- diagnose unrelated Apple toolchain issues beyond the root Xcode bridge

## Workflow

1. Run:
   `python3 .codex/skills/codex-runtime-doctor/scripts/check_runtime.py`
2. Summarize the worst failing sections first.
3. Keep remediation scoped to the reported degradation.
4. If the canonical surface is degraded, route runtime work back through
   `codex-operating-layer` only after the reported issue is fixed.

## Output Contract

Expect four sections:

- `canonical_surface`
- `repo_hooks`
- `external_hook_overlay`
- `xcode_bridge`

Each section returns status, evidence, and remediation.
