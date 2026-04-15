# Claude Swift Toolkit — Lifecycle Map

End-to-end Apple app development toolkit split across 5 plugins. Every component maps to a phase below.

| Plugin | Path | Phase Coverage |
|--------|------|----------------|
| `apple-app-architect` | `plugins/apple-app-architect` | Scaffold + Architecture (0–1) |
| `apple-design-system` | `plugins/apple-design-system` | Design + API Ref (2–3) |
| `apple-app-builder` | `plugins/apple-app-builder` | Implement + Build (3–4) |
| `apple-app-quality` | `plugins/apple-app-quality` | Review + Test (5–6) |
| `hookify` | `plugins/hookify` | Utility — hook management |

## Development Lifecycle

```
Phase 0: Scaffold  →  Phase 1: Architecture  →  Phase 2: Design  →  Phase 3: Implement  →  Phase 4: Build  →  Phase 5: Review  →  Phase 6: Test
```

### Phase 0 — Scaffold
Plan the app, define scope, write implementation plan.
- **Plugin:** `apple-app-architect`
- **Skills:** `macos-development` (app-planner module), `app-development-workflow`, `swift-app-lifecycle`, `swift-project-scaffold`
- **Invoke:** `/write-plan`, `/brainstorm`, `/feature-dev`, `/scaffold-project`

### Phase 1 — Architecture
System design, navigation patterns, state management, data modeling.
- **Plugin:** `apple-app-architect`
- **Skills:** `macos-development` (architecture-patterns module), `swift-app-lifecycle`, `swift-actor-persistence`
- **Agents:** `macos-architect`, `code-architect`, `code-explorer`
- **Invoke:** `/execute-plan`, `/revise-claude-md`

### Phase 2 — UI Design
macOS HIG compliance, Liquid Glass adoption, app archetype selection.
- **Plugin:** `apple-design-system`
- **Skills:** `macos-app-design`, `apple-liquid-glass-design`
- **Invoke:** `/design-ui`

### Phase 3 — Implement
Write SwiftUI views, apply API references, build components, add networking and localization.
- **Plugins:** `apple-design-system` (UI components + API refs), `apple-app-builder` (Swift core + tooling)
- **Skills (design-system):** `swiftui-components`, `swiftui-ui-patterns`, `swiftui-colors-api`, `swiftui-effects-api`, `swiftui-iconography-api`, `swiftui-input-api`, `swiftui-material-api`, `swiftui-presentation-api`, `swiftui-typography-api`, `swiftui-26-api`
- **Skills (app-builder):** `swift-networking`, `swift-concurrency`, `swift-localization`
- **Agents:** `ui-developer`, `ios-developer`
- **Invoke:** `/implement-component`

### Phase 4 — Build
Compile, verify, iterate on build errors.
- **Plugin:** `apple-app-builder`
- **Skills:** `xcodebuildmcp`, `xcodebuildmcp-cli`, `autonomous-ui-workflow` (phases 5-8)
- **Invoke:** `/build-project`, `/fix-build`, `/run-app`

### Phase 5 — Review (iterative)
Run review swarm, fix findings, re-review until grade A- (0 FAIL, 0 CRITICAL).
- **Plugin:** `apple-app-quality`
- **Skills:** `swiftui-view-refactor`, `code-analyzer`, `audit-context-building`
- **Agents:** `swift-reviewer`, `code-reviewer` (dispatched via `/review`)
- **Invoke:** `/review`, `/review-ui`, `/refactor-view`, `/swift-style`

### Phase 6 — Test
Unit tests, UI tests, coverage analysis.
- **Plugin:** `apple-app-quality`
- **Skills:** `ios-testing`
- **Invoke:** `/test`

## Quick Start

**New macOS app:** Load `apple-app-architect` → `app-development-workflow` → follow phases 0-6, activating each plugin as you enter its phase.

**New feature in existing app:** `apple-app-architect` `/feature-dev` → `apple-app-builder` `autonomous-ui-workflow` → `apple-app-quality` `/test`

**Code review:** Load `apple-app-quality` → `code-analyzer` → `swiftui-view-refactor`

## Skill Taxonomy

49 skills, 10 agents, 10 hooks across 5 plugins. All invocable items are skills (no deprecated `commands/` format).

| Category | Plugin | Skills |
|----------|--------|--------|
| **Workflow** | `apple-app-architect` | `app-development-workflow`, `macos-development` |
| **Lifecycle** | `apple-app-architect` | `swift-app-lifecycle`, `swift-actor-persistence`, `swift-project-scaffold` (XcodeGen templates + build settings) |
| **Planning (invocable)** | `apple-app-architect` | `brainstorm`, `write-plan`, `execute-plan`, `feature-dev`, `revise-claude-md`, `scaffold-project` (invokes swift-project-scaffold) |
| **Design** | `apple-design-system` | `macos-app-design`, `apple-liquid-glass-design`, `design-ui` |
| **UI Components** | `apple-design-system` | `swiftui-components`, `swiftui-ui-patterns` |
| **API Reference** | `apple-design-system` | `swiftui-material-api`, `swiftui-iconography-api`, `swiftui-colors-api`, `swiftui-typography-api`, `swiftui-input-api`, `swiftui-effects-api`, `swiftui-presentation-api`, `swiftui-26-api` |
| **Build + Tooling** | `apple-app-builder` | `autonomous-ui-workflow`, `xcodebuildmcp`, `xcodebuildmcp-cli` |
| **Build (invocable)** | `apple-app-builder` | `build-project`, `fix-build`, `implement-component`, `run-app` |
| **Swift Core** | `apple-app-builder` | `swift-networking`, `swift-concurrency`, `swift-localization` |
| **Review** | `apple-app-quality` | `swiftui-view-refactor`, `code-analyzer`, `audit-context-building` |
| **Review (invocable)** | `apple-app-quality` | `review`, `review-ui`, `refactor-view`, `swift-style` |
| **Testing** | `apple-app-quality` | `ios-testing`, `test` |
| **Hook Management** | `hookify` | `hookify`, `configure`, `list`, `help`, `prompts`, `skills` |

## Hookify — Utility Plugin

The `hookify` plugin provides a generic hook rule engine separate from the development lifecycle.

**Skills:** `/hookify`, `/list`, `/configure`, `/help`, `/prompts`, `/skills`
**Agents:** `conversation-analyzer`, `skill-manager`, `prompt-manager`

**Design note — universal matchers:** Hookify hooks fire on ALL tool events (no matchers in `hooks.json`). This is intentional — the Python rule engine dynamically evaluates user-defined `.local.md` rules at runtime, so it must receive every event to apply rules correctly. Static matchers would break the dynamic architecture.

# Skill Creation Guide
Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. When asked to create a new skill or improve a skill, refer to the following guides:

- [View the specification](/specification) to understand the full format.
- [See example skills](https://github.com/anthropics/skills) on GitHub.
- [Use the reference library](https://github.com/agentskills/agentskills/tree/main/skills-ref) to validate skills and generate prompt XML.

Using the guides and follwing them by using the skill `writing skills` in the correct format ensures they can be easily integrated into agents and workflows, and that they function as intended when invoked.
