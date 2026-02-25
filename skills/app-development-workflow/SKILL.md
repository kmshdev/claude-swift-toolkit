---
name: app-development-workflow
description: Use when starting a new Apple app, planning a major feature, or orienting to the full development lifecycle. Maps 6 phases (Scaffold → Architecture → Design → Implement → Build → Review → Test) to specific skills, agents, and commands.
---

# App Development Workflow

End-to-end lifecycle for building Apple apps with this toolkit. Each phase tells you what to do, which skills to load, and where to go next.

## Lifecycle Overview

```
Phase 0: Scaffold → Phase 1: Architecture → Phase 2: Design → Phase 3: Implement → Phase 4: Build → Phase 5: Review → Phase 6: Test
```

## Phase 0 — Scaffold

**When:** Starting a new app or major feature from scratch.

**Load:** `macos-development` (read `app-planner/` module)

**Steps:**
1. Define the app's purpose, target users, and core features
2. Use `/brainstorm` to explore approaches and constraints
3. Use `/write-plan` to create a detailed implementation plan
4. Identify app archetype (document-based, library+editor, utility, menu-bar, pro tool)

**Next phase →** Load `macos-development` architecture-patterns module for Phase 1.

## Phase 1 — Architecture

**When:** Designing system structure, navigation, state management, data model.

**Load:** `macos-development` (read `architecture-patterns/` module)
**Agent:** `macos-architect` — consult for architecture decisions

**Steps:**
1. Choose navigation pattern (`NavigationSplitView`, `TabView`, etc.)
2. Design state management (`@Observable`, SwiftData, actor isolation)
3. Plan module boundaries (Swift Package Manager local packages)
4. Define data model and persistence strategy
5. Map command structure (menus, keyboard shortcuts)

**Next phase →** Load `macos-app-design` for UI design in Phase 2.

## Phase 2 — Design

**When:** Designing the UI layer — HIG compliance, Liquid Glass, layout decisions.

**Load:** `macos-app-design`, `apple-liquid-glass-design`

**Steps:**
1. Review Mac Citizen Checklist from `macos-app-design`
2. Identify which surfaces get Liquid Glass treatment
3. Plan information architecture (sidebar structure, toolbar groups)
4. Define accessibility plan (VoiceOver, keyboard nav, Reduce Motion)
5. Produce deliverables: app archetype, IA, command map, state model, a11y plan

**Next phase →** Load `swiftui-components` + `swiftui-expert-skill` for Phase 3. For autonomous UI loop, load `autonomous-ui-workflow`.

## Phase 3 — Implement

**When:** Writing SwiftUI views and business logic.

**Load:** `swiftui-components`, `swiftui-expert-skill`
**Agent:** `ui-developer` — autonomous implementation with build verification
**API References:** Load as needed from the research table:

| Need | Skill |
|------|-------|
| Glass effects, floating controls | `apple-liquid-glass-design` |
| Icons, SF Symbols | `swiftui-iconography-api` |
| Background materials, shapes | `swiftui-material-api` |
| Text fields, pickers, forms | `swiftui-input-api` |
| Font choices, text styling | `swiftui-typography-api` |
| Colors, gradients, tint | `swiftui-colors-api` |
| Blur, shadow, opacity | `swiftui-effects-api` |
| Sheets, popovers, alerts | `swiftui-presentation-api` |

**Steps:**
1. Read existing similar views for pattern consistency
2. Apply templates from `swiftui-components/templates/`
3. Follow `swiftui-expert-skill` core guidelines for state, APIs, composition
4. Use `#Preview` blocks for every view
5. Run `/implement-component` or `/create-view` for scaffolding

**Next phase →** Build and verify in Phase 4.

## Phase 4 — Build

**When:** Compiling, verifying builds, iterating on errors.

**Load:** `xcodebuildmcp` or `xcodebuildmcp-cli`
**Also:** `autonomous-ui-workflow` covers phases 5-8 (Build → Preview → Validate → Iterate)

**Steps:**
1. Build via XcodeBuildMCP tools or CLI (`/build`)
2. Fix build errors (`/fix-build`) — read full error, fix, rebuild
3. Preview with `RenderPreview` to verify visual correctness
4. Validate against project rules (see `autonomous-ui-workflow` Phase 7)
5. Iterate until build is green and preview matches intent

**Next phase →** When build is green, proceed to Phase 5. Load `swiftui-view-refactor`.

## Phase 5 — Review

**When:** Build is green, code needs quality review and refactoring.

**Load:** `code-analyzer`, `swiftui-expert-skill` (review checklist), `swiftui-view-refactor`
**Optional deep-dive:** `audit-context-building` for security audit or architectural review

**Steps:**
1. Run `code-analyzer` for architectural overview and quality assessment
2. Walk through `swiftui-expert-skill` review checklist (state, APIs, performance, animations)
3. Apply `swiftui-view-refactor` for consistent view structure and ordering
4. Use `/refactor-view` and `/swift-style` commands
5. For deep analysis, load `audit-context-building`

**Next phase →** Proceed to Phase 6 for testing.

## Phase 6 — Test

**When:** Code is reviewed, ready for test coverage.

**Load:** `ios-testing`

**Steps:**
1. Write unit tests with XCTest or Swift Testing framework
2. Test @Observable models with in-memory `ModelContainer`
3. Follow Arrange/Act/Assert pattern
4. Target 80%+ coverage for critical paths
5. Run tests via `/test` or XcodeBuildMCP `test_macos`/`test_sim`

## Choosing Your Entry Point

| Situation | Start At |
|-----------|----------|
| Brand new app | Phase 0 (Scaffold) |
| New feature in existing app | Phase 1 or 2 |
| Building a specific view | Phase 3 (load `autonomous-ui-workflow`) |
| Build is broken | Phase 4 |
| Code review | Phase 5 |
| Adding tests | Phase 6 |

## Related Skills

- **`autonomous-ui-workflow`** — The inner UI development loop (Spec → Build → Validate). Lives within Phases 2-4.
- **`macos-development`** — Comprehensive macOS reference modules. Spans Phases 0-1.
- **`macos-app-design`** — macOS HIG and design system. Phase 2.
- **`apple-liquid-glass-design`** — Liquid Glass API reference. Phases 2-3.
