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
5. **Scaffold the project:**
   - If XcodeBuildMCP available: use `scaffold_macos_project` or `scaffold_ios_project` tool
   - If CLI: use `xcodebuildmcp-cli` skill scaffolding patterns
   - If Swift Package: create `Package.swift` with appropriate platform target
   - Load `swift-app-lifecycle` for scene structure (`WindowGroup`, `Settings`, `MenuBarExtra`, `DocumentGroup`)

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

## Phase 5 — Review (iterative)

**When:** Build is green, code needs quality review and refactoring.

**Exit criterion:** No CRITICAL or MAJOR findings remain. Grade A- or better (0 FAIL sections in code-analyzer output, 0 CRITICAL findings from swift-reviewer).

**Load:** `code-analyzer`, `swiftui-expert-skill` (review checklist), `swiftui-view-refactor`, `swift-concurrency` (review checklist)
**Optional deep-dive:** `audit-context-building` for security audit or architectural review
**Agents:** `swift-reviewer`, `code-reviewer` (dispatched via `/review` command)

**Steps:**
1. **Run review swarm:** `/review` dispatches `swift-reviewer` + `code-reviewer` in parallel
2. **Triage findings:** Classify each as CRITICAL (fix now), MAJOR (fix now), MINOR (fix later), SUGGESTION (backlog)
3. **Fix CRITICAL and MAJOR findings** — apply fixes one category at a time (security → concurrency → API → accessibility)
4. **Rebuild:** `/build` to verify fixes compile
5. **Re-run review swarm** — repeat steps 1-4 until exit criterion met
6. **Apply optional polish:** `/refactor-view` for view structure, `/swift-style` for conventions
7. **Grade check:** 0 FAIL + 0 CRITICAL = A- (proceed). Otherwise loop back to step 2.

**Grading scale:**
| Grade | Criteria | Action |
|-------|----------|--------|
| A- or better | 0 FAIL, 0 CRITICAL | Proceed to Phase 6 |
| B | 0 FAIL, 1-2 CRITICAL | Fix CRITICALs, re-review |
| C or below | 1+ FAIL | Fix all FAILs and CRITICALs, re-review |

**Next phase →** When review grade is A- or better, proceed to Phase 6. Load `ios-testing`.

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
