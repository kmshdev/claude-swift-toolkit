---
name: app-development-workflow
description: Use when starting a new Apple app, planning a major feature, or orienting to the Codex-ready lifecycle subset of this toolkit. Maps the planning, design, implementation, build, review, and test phases to the packaged Codex skills.
---

# App Development Workflow

Use this as the entry point for the Codex-ready subset of the toolkit.

This repository's current Codex marketplace includes all four lifecycle
plugins:
- planning and architecture via `apple-app-architect`
- design and SwiftUI reference guidance via `apple-design-system`
- implementation and build loops via `apple-app-builder`
- review and test workflows via `apple-app-quality`

The implementation, build, review, and test phases depend on Xcode being
installed and running so the official Xcode MCP bridge (`xcrun mcpbridge`) can
attach.

## Lifecycle Overview

```
Phase 0: Scaffold -> Phase 1: Architecture -> Phase 2: Design -> Phase 3: Implement -> Phase 4: Build -> Phase 5: Review -> Phase 6: Test
```

## Phase 0 — Scaffold

**When:** Starting a new app or major feature from scratch.

**Load:** `apple-app-architect:macos-development` and read the `app-planner/`
module.

**Steps:**
1. Define the app's purpose, target users, and core features.
2. Identify the app archetype: document-based, library plus editor, utility,
   menu bar, or pro tool.
3. Capture constraints that will shape the architecture: offline support, sync,
   data model complexity, platform targets, and accessibility expectations.
4. Turn the result into an implementation plan before writing code.

**Next phase ->** Continue with `apple-app-architect:macos-development`
`architecture-patterns/` for Phase 1.

## Phase 1 — Architecture

**When:** Designing system structure, navigation, state management, and the data
model.

**Load:** `apple-app-architect:macos-development` and read the
`architecture-patterns/` module.

**Steps:**
1. Choose navigation pattern (`NavigationSplitView`, `TabView`, and related
   shell decisions).
2. Design state management (`@Observable`, SwiftData, actor isolation).
3. Plan module boundaries and package seams.
4. Define persistence strategy and external integration boundaries.
5. Map commands, menus, keyboard shortcuts, and app-specific affordances.

**Next phase ->** Load `apple-design-system:macos-app-design` for Phase 2.

## Phase 2 — Design

**When:** Designing the UI layer, HIG alignment, and Liquid Glass adoption.

**Load:** `apple-design-system:macos-app-design` and
`apple-design-system:apple-liquid-glass-design`.

**Steps:**
1. Review the relevant HIG and platform conventions.
2. Decide which surfaces should use Liquid Glass and which should stay more
   restrained.
3. Plan information architecture, sidebar structure, toolbar groupings, and
   accessibility expectations.
4. Produce the design handoff artifacts you need for implementation.

**Next phase ->** Load `apple-app-builder:autonomous-ui-workflow` for the
implementation loop.

## Phase 3 — Implement

**Load:** `apple-app-builder:autonomous-ui-workflow` plus the narrowest
implementation or design reference skills the feature needs.

**Focus:** Edit the smallest set of files, keep the local architecture intact,
and use Xcode previews or diagnostics early instead of waiting for a full build
loop.

## Phase 4 — Build

**Load:** `apple-app-builder:xcode-mcp` when you need direct Xcode project
inspection, build logs, preview rendering, or targeted build evidence.

**Focus:** Use the smallest proof that answers the question: file diagnostics,
preview render, targeted build, then broader project build.

## Phase 5 — Review

**Load:** `apple-app-quality:code-analyzer` and
`apple-app-quality:swiftui-view-refactor`.

**Focus:** Review the change for architecture, clarity, test adequacy, and
SwiftUI structure before broadening the validation scope.

## Phase 6 — Test

**Load:** `apple-app-quality:ios-testing`.

**Focus:** Discover tests with `GetTestList`, run the smallest relevant slice
with `RunSomeTests`, then broaden to `RunAllTests` only when justified.

## Choosing Your Entry Point

| Situation | Start At |
|-----------|----------|
| Brand new app | Phase 0 |
| New feature in existing app | Phase 1 or 2 |
| UI design and API selection | Phase 2 with `apple-design-system` |
| Implementation handoff | Phase 3 after planning and design are complete |

## Related Skills

- `apple-app-architect:macos-development` — planning and architecture modules
  for Phase 0 and Phase 1.
- `apple-design-system:macos-app-design` — design-system and HIG guidance for
  Phase 2.
- `apple-design-system:apple-liquid-glass-design` — Liquid Glass reference for
  the design phase.
- `apple-app-builder:autonomous-ui-workflow` — implementation loop for Phase 3.
- `apple-app-builder:xcode-mcp` — direct Xcode MCP guidance for Phase 4.
- `apple-app-quality:ios-testing` — test strategy and execution guidance for
  Phase 6.
