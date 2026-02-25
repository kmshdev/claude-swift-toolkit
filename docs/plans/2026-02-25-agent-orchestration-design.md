# Agent Orchestration Design: Phase-Based Swarms

**Date:** 2026-02-25
**Scope:** Consolidate agents (11 → 8), wire phase-based swarms, add /review command
**Target:** 8 lifecycle agents + 3 utility agents, every lifecycle agent has a dispatch path

## Problem

The toolkit has 11 agents but only 3 are dispatched by commands (`code-explorer`, `code-architect`, `code-reviewer` via `/feature-dev`). Five agents are orphaned (no dispatch path), one overlaps heavily with another, and two are utility agents outside the lifecycle. Users must know agent names and invoke them manually.

## Agent Consolidation (11 → 8 lifecycle + 3 utility)

### Merge: `swift-expert` → `macos-architect`

**Rationale:** Both cover Swift 6/SwiftUI architecture with near-identical domain. `swift-expert` (250 lines) adds concurrency, `@MainActor` patterns, and modern API guidance. `macos-architect` (125 lines) adds macOS Tahoe patterns, navigation, and system design. Merge unique content from `swift-expert` into `macos-architect`.

**Action:**
- Absorb Swift 6 concurrency section into `macos-architect`
- Absorb `@MainActor` ViewModel pattern and `Sendable` guidance
- Remove dead "Integration with other agents" section (references non-existent agents)
- Delete `agents/swift-expert.md`

### Move to Utility: `prompt-manager`, `skill-manager`

These serve the external prompts.chat MCP service, not the app development lifecycle. Keep the files but remove from lifecycle documentation.

### Clean: `conversation-analyzer`

Keep as utility agent for `/hookify`. Fix `/hookify` command to dispatch it properly instead of inlining its logic.

### Result: 8 Lifecycle Agents

| Agent | Phase | Role | Dispatch Path |
|-------|-------|------|---------------|
| `code-explorer` | 0-1 | Read-only codebase exploration | `/feature-dev` Phase 2 |
| `code-architect` | 1 | Feature architecture blueprints | `/feature-dev` Phase 4 |
| `macos-architect` | 1 | Architecture validation, macOS patterns, concurrency | `/feature-dev` Phase 4 (validation gate) |
| `ui-developer` | 3 | macOS SwiftUI implementation with build verification | `/implement-component` (macOS target) |
| `ios-developer` | 3 | iOS/iPadOS implementation with UIKit bridging | `/implement-component` (iOS target) |
| `swift-reviewer` | 5 | Swift-specific code review with severity classification | `/review` (parallel) |
| `code-reviewer` | 5 | General quality, plan adherence review | `/review` (parallel) |
| `conversation-analyzer` | Utility | Hookify conversation analysis | `/hookify` |

### 3 Utility Agents (outside lifecycle)

| Agent | Purpose |
|-------|---------|
| `prompt-manager` | prompts.chat prompt management |
| `skill-manager` | prompts.chat skill management |
| `conversation-analyzer` | Hookify rule generation |

---

## Phase Swarm Definitions

### Phase 0-1: Discovery & Architecture Swarm

**Trigger:** `/feature-dev`

```
Step 1: code-explorer (×2-3, parallel)
  → Gather codebase context from different angles
  → Merge findings into unified exploration report

Step 2: code-architect (×2-3, parallel)
  → Propose 2-3 architecture approaches
  → User selects preferred approach

Step 3: macos-architect (×1, sequential) [NEW]
  → Validate selected approach against macOS patterns
  → Check: navigation pattern, state management, concurrency safety, Liquid Glass fit
  → Output: validated architecture OR flagged concerns for user
```

**What changes:** Step 3 is new. Currently `/feature-dev` skips architecture validation — the user selects an approach and implementation begins immediately. Adding `macos-architect` as a validation gate catches architectural issues before implementation starts.

### Phase 3: Implementation Swarm

**Trigger:** `/implement-component` (updated)

```
Step 1: Platform detection
  → Check deployment target in .xcodeproj or Package.swift
  → Check existing code patterns (UIKit imports = iOS, AppKit = macOS)

Step 2: Dispatch
  macOS target → ui-developer (×1)
  iOS target → ios-developer (×1)
  Universal → ui-developer + ios-developer (parallel, split by platform layer)
```

**What changes:** `/implement-component` currently runs as a skill-only command with no agent dispatch. The update adds platform detection and dispatches the appropriate implementation agent. Each agent has the right skills pre-loaded (swiftui-expert-skill, API refs, platform-specific patterns).

### Phase 5: Review Swarm

**Trigger:** `/review` (new command)

```
Step 1: Identify changed files
  → git diff against main branch
  → Or user-specified file paths

Step 2: Dispatch reviewers (parallel)
  → swift-reviewer: Swift 6 concurrency, Liquid Glass, deprecated APIs, accessibility
  → code-reviewer: plan adherence, organization, error handling, test coverage

Step 3: Merge findings
  → Deduplicate overlapping issues
  → Unify severity classification (CRITICAL → MAJOR → MINOR)
  → Present single report with file:line references
```

**What changes:** No command currently dispatches either reviewer. `/swift-style` checks linting, `/refactor-view` restructures views, but neither runs a full code review. `/review` fills this gap.

### Phase 4 (Build) & Phase 6 (Test): No Swarms

These phases are command + skill driven. `/build`, `/fix-build`, `/run-app`, `/test` work well as tool commands. No agent dispatch needed.

---

## File Changes

| File | Action |
|------|--------|
| `agents/swift-expert.md` | **Delete** — merged into macos-architect |
| `agents/macos-architect.md` | Add Swift 6 concurrency section, remove dead agent refs |
| `commands/review.md` | **Create** — Phase 5 review swarm dispatcher |
| `commands/feature-dev.md` | Add macos-architect validation gate (Phase 4), replace code-reviewer with /review swarm (Phase 6) |
| `commands/implement-component.md` | Add platform detection + agent dispatch |
| `commands/hookify.md` | Fix to dispatch conversation-analyzer agent properly |
| `CLAUDE.md` | Remove swift-expert, add /review to Phase 5, move utility agents to Utility section |
| `README.md` | Same updates as CLAUDE.md, update agent table (10 agents total) |
| `plugin.json` | Version bump to 1.5.0 |

## Verification

1. `ls agents/swift-expert.md` → not found (deleted)
2. `grep -r "swift-expert" CLAUDE.md README.md agents/` → zero hits
3. `commands/review.md` exists and dispatches both `swift-reviewer` and `code-reviewer`
4. `commands/feature-dev.md` includes macos-architect validation step
5. `commands/implement-component.md` has platform detection logic
6. Every lifecycle agent in CLAUDE.md has at least one command dispatch path
7. `grep "prompt-manager\|skill-manager" CLAUDE.md` → only in Utility section
8. Agent count: 8 lifecycle + 3 utility = 11 files in agents/ (same count, different classification)
