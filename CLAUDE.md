# Claude Swift Toolkit — Lifecycle Map

End-to-end Apple app development toolkit. Every skill, agent, and command maps to a phase below.

## Development Lifecycle

```
Phase 0: Scaffold  →  Phase 1: Architecture  →  Phase 2: Design  →  Phase 3: Implement  →  Phase 4: Build  →  Phase 5: Review  →  Phase 6: Test
```

### Phase 0 — Scaffold
Plan the app, define scope, write implementation plan.
- **Skills:** `macos-development` (app-planner module), `app-development-workflow`
- **Commands:** `/write-plan`, `/brainstorm`, `/feature-dev`

### Phase 1 — Architecture
System design, navigation patterns, state management, data modeling.
- **Skills:** `macos-development` (architecture-patterns module)
- **Agent:** `macos-architect`

### Phase 2 — UI Design
macOS HIG compliance, Liquid Glass adoption, app archetype selection.
- **Skills:** `macos-app-design`, `apple-liquid-glass-design`
- **Commands:** `/design-ui`

### Phase 3 — Implement
Write SwiftUI views, apply API references, build components.
- **Skills:** `swiftui-components`, `swiftui-expert-skill`, 7 API reference skills
- **Agent:** `ui-developer`
- **Commands:** `/implement-component`, `/create-view`
- **API References:** `swiftui-material-api`, `swiftui-iconography-api`, `swiftui-colors-api`, `swiftui-typography-api`, `swiftui-input-api`, `swiftui-effects-api`, `swiftui-presentation-api`

### Phase 4 — Build
Compile, verify, iterate on build errors.
- **Skills:** `xcodebuildmcp`, `xcodebuildmcp-cli`, `autonomous-ui-workflow` (phases 5-8)
- **Commands:** `/build`, `/fix-build`, `/run-app`

### Phase 5 — Review
Refactor views, review code quality, audit architecture.
- **Skills:** `swiftui-view-refactor`, `swiftui-expert-skill` (review checklist), `code-analyzer`, `audit-context-building`
- **Agents:** `swift-reviewer`, `code-reviewer`
- **Commands:** `/refactor-view`, `/swift-style`

### Phase 6 — Test
Unit tests, UI tests, coverage analysis.
- **Skills:** `ios-testing`
- **Commands:** `/test`

## Quick Start

**New macOS app:** Load `app-development-workflow` → follow phases 0-6 sequentially.

**New feature in existing app:** `/feature-dev` → `autonomous-ui-workflow` → `/test`

**Code review:** Load `code-analyzer` → `swiftui-expert-skill` (review checklist) → `swiftui-view-refactor`

## Skill Taxonomy

| Category | Skills |
|----------|--------|
| **Workflow** | `app-development-workflow`, `autonomous-ui-workflow`, `macos-development` |
| **Design** | `macos-app-design`, `apple-liquid-glass-design` |
| **Implementation** | `swiftui-components`, `swiftui-expert-skill` |
| **API Reference** | `swiftui-material-api`, `swiftui-iconography-api`, `swiftui-colors-api`, `swiftui-typography-api`, `swiftui-input-api`, `swiftui-effects-api`, `swiftui-presentation-api` |
| **Tooling** | `xcodebuildmcp`, `xcodebuildmcp-cli` |
| **Review** | `swiftui-view-refactor`, `code-analyzer`, `audit-context-building` |
| **Testing** | `ios-testing` |
