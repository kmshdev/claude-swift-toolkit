# Codex Swift Toolkit

This repo packages Codex plugin skills for Apple app lifecycle work. For Codex users,
`.codex-plugin/plugin.json` is the source of truth for what is actually shipped.

## Codex Scope

- Packaged Codex skills live in:
  - `plugins/apple-app-architect/codex-skills`
  - `plugins/apple-design-system/skills`
  - `plugins/apple-app-builder/codex-skills`
  - `plugins/apple-app-quality/codex-skills`
- Do not treat `commands/`, `agents/`, `hooks/`, or `plugins/hookify` as active Codex
  surfaces unless a future `.codex-plugin/plugin.json` explicitly packages them.

## Lifecycle Map

| Plugin | Packaged Skill Root | Phase Coverage |
|--------|---------------------|----------------|
| `apple-app-architect` | `plugins/apple-app-architect/codex-skills` | Phases 0-1 |
| `apple-design-system` | `plugins/apple-design-system/skills` | Phases 2-3 |
| `apple-app-builder` | `plugins/apple-app-builder/codex-skills` | Phases 3-4 |
| `apple-app-quality` | `plugins/apple-app-quality/codex-skills` | Phases 5-6 |

## Development Lifecycle

```text
Phase 0: Scaffold -> Phase 1: Architecture -> Phase 2: Design
Phase 3: Implement -> Phase 4: Build -> Phase 5: Review -> Phase 6: Test
```

### Phase 0-1 — Plan and Architect
- Plugin: `apple-app-architect`
- Codex skills: `app-development-workflow`, `macos-development`

### Phase 2 — Design
- Plugin: `apple-design-system`
- Codex skills: `macos-app-design`, `apple-liquid-glass-design`

### Phase 3 — UI Components and API Reference
- Plugin: `apple-design-system`
- Codex skills: `swiftui-components`, `swiftui-ui-patterns`, `swiftui-colors-api`,
  `swiftui-effects-api`, `swiftui-iconography-api`, `swiftui-input-api`,
  `swiftui-material-api`, `swiftui-presentation-api`, `swiftui-typography-api`,
  `swiftui-26-api`

### Phase 3-4 — Core Implementation and Build
- Plugin: `apple-app-builder`
- Codex skills: `autonomous-ui-workflow`, `swift-networking`, `swift-concurrency`,
  `swift-localization`, `xcode-mcp`

### Phase 5-6 — Review and Test
- Plugin: `apple-app-quality`
- Codex skills: `audit-context-building`, `code-analyzer`,
  `swiftui-view-refactor`, `ios-testing`

## Quick Start

- New app: start with `app-development-workflow`, then `macos-development`, then move
  through the design, build, review, and test skills by lifecycle phase.
- New feature: use the phase 2-4 skills that match the work, then finish with
  `code-analyzer` and `ios-testing`.
- Review pass: start with `code-analyzer`; use `swiftui-view-refactor` when the work is
  view-heavy.
