# Claude Swift Toolkit v1.8.0

**End-to-end Apple app development toolkit for Claude Code, with a Codex-ready lifecycle plugin set** — systematic lifecycle workflow from scaffold to shipping, with 25 skills, 10 agents, and 21 commands covering Liquid Glass design, SwiftUI patterns, networking, concurrency, actor persistence, and localization. Claude keeps the full command, agent, and hook surface. Codex now gets the four lifecycle plugins through `.codex-plugin` manifests, a repo-scoped marketplace, and plugin-level `.mcp.json` wiring that uses Xcode's official MCP bridge.

## Development Lifecycle

The full lifecycle table below describes the complete toolkit. The Codex / OpenAI section below calls out the packaged Codex surface and the shared Xcode MCP dependency story.

```
Phase 0: Scaffold → Phase 1: Architecture → Phase 2: Design → Phase 3: Implement → Phase 4: Build → Phase 5: Review → Phase 6: Test
```

| Phase | Skills | Agent | Commands |
|-------|--------|-------|----------|
| **0 — Scaffold** | `macos-development`, `app-development-workflow`, `swift-app-lifecycle` | — | `/write-plan`, `/brainstorm` |
| **1 — Architecture** | `macos-development` (architecture-patterns), `swift-app-lifecycle` | `macos-architect` | — |
| **2 — Design** | `macos-app-design`, `apple-liquid-glass-design` | — | `/design-ui` |
| **3 — Implement** | `swiftui-components`, `swiftui-ui-patterns`, `swift-networking`, `swift-concurrency`, `swift-actor-persistence`, `swift-localization`, 8 API refs | `ui-developer` | `/implement-component` |
| **4 — Build** | `xcode-mcp`, `autonomous-ui-workflow` | — | `/build`, `/fix-build`, `/run-app` |
| **5 — Review** | `swiftui-view-refactor`, `code-analyzer`, `swift-concurrency` (checklist), `audit-context-building` | `swift-reviewer`, `code-reviewer` | `/review`, `/refactor-view`, `/swift-style` |
| **6 — Test** | `ios-testing` | — | `/test` |

## Quick Start

**New macOS app:** Load `app-development-workflow` skill, follow phases 0-6.

**New feature:** `/feature-dev` → `autonomous-ui-workflow` → `/test`

**Code review:** `code-analyzer` → `swiftui-ui-patterns` (checklist) → `swiftui-view-refactor`

## Installation

### Claude Code

```bash
git clone https://github.com/kmshdev/claude-swift-toolkit.git
claude --plugin ./claude-swift-toolkit
```

### Claude Project Settings

Add to your project's `.claude/settings.json`:

```json
{
  "plugins": [
    "../claude-swift-toolkit"
  ]
}
```

### Claude via npx (if published to skills.sh)

```bash
npx skills add kmshdev/claude-swift-toolkit
```

### Codex / OpenAI

This repo now includes a Codex marketplace at `.agents/plugins/marketplace.json`
and `.codex-plugin/plugin.json` manifests for the lifecycle plugins that are
currently packaged for Codex:

- `apple-app-architect`
- `apple-design-system`
- `apple-app-builder`
- `apple-app-quality`

Clone the repo, open the plugin directory in Codex, choose the repo marketplace
source from this checkout, and install whichever lifecycle plugins you need.
Restart Codex after changing the marketplace or any `.codex-plugin/plugin.json`
file so the local install picks up the new metadata.

`apple-app-builder` and `apple-app-quality` now bundle plugin-local
`.mcp.json` files that start Xcode's official MCP bridge through
`xcrun mcpbridge`, so their Codex build and test guidance no longer relies on
an undeclared host MCP setup. Xcode must be installed and running before the
bridge can attach. The lifecycle tables elsewhere in this README now use the same official Xcode MCP model.

When editing the Codex marketplace, manifests, `.mcp.json`, or Codex-exposed
skills, run:

```bash
python3 scripts/validate-codex-support.py
```

`hookify` remains Claude-only for now because its current surface is built around
Claude commands, agents, and hooks rather than Codex-packaged skills, apps, or
MCP config.

See `docs/codex-plugin-migration/README.md` for the archived migration
rationale and research snapshot. Use this README, `AGENTS.md`,
`.agents/plugins/marketplace.json`, and the plugin manifests as the live Codex
source of truth.

## Dependencies

### Required

- **[obra/superpowers](https://github.com/obra/superpowers)** — Core workflow skills (29K+ installs)
  ```bash
  npx skills add obra/superpowers -g -y
  ```

### Recommended

- **[dimillian/skills@swiftui-view-refactor](https://skills.sh/dimillian/skills/swiftui-view-refactor)** — SwiftUI view refactoring (605 installs)
  ```bash
  npx skills add dimillian/skills@swiftui-view-refactor -g -y
  ```

## Skills by Phase

### Workflow (Phases 0-4)

| Skill | Phase | Purpose |
|-------|-------|---------|
| `app-development-workflow` | 0-6 | Master lifecycle map — start here |
| `autonomous-ui-workflow` | 2-4 | Inner UI loop: Spec → Build → Validate |
| `macos-development` | 0-1 | macOS reference modules (architecture, SwiftData, Tahoe) |

### Design (Phases 1-2)

| Skill | Phase | Purpose |
|-------|-------|---------|
| `macos-app-design` | 1-2 | macOS HIG compliance, app archetypes |
| `apple-liquid-glass-design` | 2-3 | Liquid Glass API reference and adoption guide |

### Implementation (Phase 3)

| Skill | Phase | Purpose |
|-------|-------|---------|
| `swiftui-components` | 3 | Reusable view patterns, templates, component library |
| `swiftui-ui-patterns` | 3, 5 | Best practices + review checklist |

### Swift Core (Phases 0-3)

| Skill | Phase | Purpose |
|-------|-------|---------|
| `swift-networking` | 3 | URLSession async/await, API clients, error handling, retry |
| `swift-concurrency` | 3, 5 | Actors, Sendable, structured concurrency, Swift 6 migration |
| `swift-actor-persistence` | 3 | Thread-safe local storage with actor-based in-memory cache + file backing |
| `swift-app-lifecycle` | 0-1 | App entry point, scenes, deep links, notifications |
| `swift-localization` | 3 | String Catalogs, plurals, RTL layout, locale-aware formatting |

### API Reference (Phase 3)

| Skill | Covers |
|-------|--------|
| `swiftui-material-api` | Material backgrounds, shapes, stroke patterns |
| `swiftui-iconography-api` | SF Symbols, rendering modes, symbol effects |
| `swiftui-colors-api` | Semantic colors, gradients, tints, dark mode |
| `swiftui-typography-api` | Fonts, text styles, Dynamic Type, text layout |
| `swiftui-input-api` | Text fields, focus management, forms, pickers |
| `swiftui-effects-api` | Blur, shadow, opacity, Canvas, Metal shaders |
| `swiftui-presentation-api` | Sheets, popovers, alerts, detents, inspectors |
| `swiftui-26-api` | iOS 26 non-glass APIs: WebView, rich text, @Animatable, UIKit bridge |

### Tooling (Phase 4)

| Skill | Purpose |
|-------|---------|
| `xcode-mcp` | Official Xcode MCP bridge for build, diagnostics, previews, and tests |

### Review (Phase 5)

| Skill | Purpose |
|-------|---------|
| `code-analyzer` | Structured code quality review (read-only) |
| `swiftui-view-refactor` | View structure and ordering refactoring |
| `audit-context-building` | Ultra-granular deep analysis |

### Testing (Phase 6)

| Skill | Purpose |
|-------|---------|
| `ios-testing` | XCTest + Swift Testing patterns |

## Agents

| Agent | Tools | Use Case |
|-------|-------|----------|
| **ui-developer** | Read/Write/Edit/Bash | Autonomous UI development with build verification |
| **macos-architect** | Read/Grep/Glob/Edit/Bash | Architecture review and system design |
| **code-reviewer** | Read-only | Code review and quality assessment |
| **ios-developer** | Read/Write/Edit/Bash | iOS/iPadOS development with UIKit bridging |
| **swift-reviewer** | Read-only | Swift code style review |
| **code-architect** | General-purpose | Technical architecture decisions |
| **code-explorer** | Read-only | Codebase exploration and analysis |
| **skill-manager** | General-purpose | Skill creation and management |
| **prompt-manager** | General-purpose | Prompt template management |
| **conversation-analyzer** | Read-only | Conversation pattern analysis |

## Commands

### Development
- `/build` — Build the Xcode project with error categorization
- `/test` — Run unit and integration tests with failure analysis
- `/run-app` — Build and launch on simulator or Mac
- `/fix-build` — Diagnose and fix build errors systematically

### UI Development
- `/design-ui` — Launch autonomous UI workflow
- `/implement-component` — Create or modify a SwiftUI view
- `/review-ui` — Visual validation of implemented UI

### Planning & Architecture
- `/write-plan` — Create a detailed implementation plan
- `/execute-plan` — Execute an existing markdown plan
- `/brainstorm` — Ideate solutions for a feature or problem
- `/feature-dev` — Full feature development workflow

### Code Quality
- `/review` — Run parallel review swarm (swift-reviewer + code-reviewer) with unified grading
- `/swift-style` — Check Swift style, conventions, and modern API usage
- `/refactor-view` — Analyze and refactor a SwiftUI view

### Project Management
- `/skills`, `/prompts`, `/revise-claude-md`

### Utilities (Hook Management)
- `/hookify` — Create a new hook rule
- `/help` — Hookify documentation
- `/list` — List active hook rules
- `/configure` — Configure hookify settings

## Hooks

Event-driven automation via Python scripts:
- **userpromptsubmit.py** — Pre-process user input
- **pretooluse.py** — Intercept tool calls
- **posttooluse.py** — Process tool results
- **stop.py** — Cleanup on conversation end

## Usage Examples

### Full App Development Workflow

```bash
# Start with the lifecycle skill
# Load app-development-workflow, follow Phase 0 → Phase 6

# Or jump to a specific phase:
/design-ui          # Phase 2 — design UI
/build              # Phase 4 — build and verify
/test               # Phase 6 — run tests
```

### Autonomous UI Development

```bash
/design-ui                      # Full UI workflow
/implement-component SidebarView  # Specific component
/review-ui                      # Visual validation
```

### Code Quality

```bash
/swift-style                    # Style review
/refactor-view Views/ContentView.swift  # Refactor
# Load code-analyzer for architecture review
```

## Integration with Kulpt

This plugin was extracted from the [Kulpt](https://github.com/kmshdev/kulpt) project — a native macOS resume builder with Liquid Glass design.

## Requirements

- Claude Code CLI
- macOS 14.0+ (for SwiftUI/Liquid Glass features)
- Xcode 16.0+ (for SwiftUI API references to match)
- Python 3.8+ (for hooks)

## Contributing

Fork and adapt for your Swift/macOS projects. Pull requests welcome for new skills, improved agent prompts, useful commands, and hook automation.

## License

MIT License — use freely, attribute if you share publicly.

## Author

**kmshdev** — Extracted from the Kulpt project's AI-powered development workflow.
