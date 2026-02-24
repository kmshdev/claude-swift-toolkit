# Claude Swift Toolkit

**Swift/macOS development toolkit for Claude Code** — SwiftUI API references, Liquid Glass design, autonomous UI workflows, and specialized agents for native macOS development.

## Overview

This plugin provides specialized tools for Swift/macOS projects in Claude Code, with focused support for:

- **SwiftUI & Liquid Glass Design**: 8 comprehensive API reference skills covering glass effects, materials, typography, colors, iconography, and more
- **Autonomous UI Development**: Complete workflow automation from spec to validated implementation
- **Specialized Agents**: Domain-specific agents for architecture review, UI development, and code analysis
- **macOS Native Patterns**: HIG-compliant design, Liquid Glass components, and macOS-first development

## Installation

### Via GitHub (Recommended)

```bash
# Clone the plugin
git clone https://github.com/kmshdev/claude-swift-toolkit.git

# Use with Claude Code
claude --plugin ./claude-swift-toolkit
```

### Via Project Settings

Add to your project's `.claude/settings.json`:

```json
{
  "plugins": [
    "../claude-swift-toolkit"
  ]
}
```

### Via npx (if published to skills.sh)

```bash
npx skills add kmshdev/claude-swift-toolkit
```

## Dependencies

This toolkit works best alongside these recommended plugins:

### Required

- **[obra/superpowers](https://github.com/obra/superpowers)** — Core workflow skills (29K+ installs)
  - Includes: brainstorming, TDD, systematic debugging, planning, code review, subagent orchestration, verification workflows
  ```bash
  npx skills add obra/superpowers -g -y
  ```

### Recommended

- **[dimillian/skills@swiftui-view-refactor](https://skills.sh/dimillian/skills/swiftui-view-refactor)** — SwiftUI view refactoring (605 installs)
  ```bash
  npx skills add dimillian/skills@swiftui-view-refactor -g -y
  ```

## Component Inventory

| Component Type | Count | Description |
|---------------|-------|-------------|
| **Skills** | 20 | SwiftUI API references, UI workflows, and domain-specific skills |
| **Agents** | 11 | Task-specific AI agents (architect, reviewer, iOS/macOS developers) |
| **Commands** | 22 | Quick-access shortcuts for common workflows |
| **Hooks** | 5 | Event-driven automation (Python scripts) |

## Key Skills

### SwiftUI API References (8 skills)

Complete documentation coverage for macOS 26 SwiftUI development:

- **swiftui-liquid-glass-api** — `.glassEffect()`, `GlassEffectContainer`, morph transitions, tinting
- **swiftui-material-api** — Material backgrounds, shapes, blur effects
- **swiftui-iconography-api** — SF Symbols, custom icon patterns, asset catalogs
- **swiftui-colors-api** — Semantic colors, gradients, tint hierarchies
- **swiftui-typography-api** — Font choices, text styling, dynamic type
- **swiftui-input-api** — Form fields, pickers, toggles, text editing
- **swiftui-effects-api** — Blur, shadow, opacity, animations
- **swiftui-presentation-api** — Sheets, popovers, alerts, navigation

### Development Workflows (4 skills)

- **autonomous-ui-workflow** — Full loop: Spec → Research → Design → Implement → Build → Preview → Validate
- **code-analyzer** — Deep codebase analysis for patterns, dependencies, and architecture
- **senior-architect** — High-level system design and technical decision-making
- **audit-context-building** — Learn and document new patterns discovered during development

### Apple Design System (8 skills)

- **apple-liquid-glass-design** — Apple's Liquid Glass design language for macOS
- **macos-app-design** — macOS HIG compliance, native patterns
- **macos-development** — macOS-specific development patterns
- **ios-testing** — iOS/macOS testing strategies
- **swiftui-components** — Reusable component library patterns
- **swiftui-view-refactor** — View refactoring patterns
- **xcodebuildmcp** / **xcodebuildmcp-cli** — Xcode build integration

## Key Commands

### Development

- `/build` — Build the Xcode project and report errors
- `/test` — Run unit and integration tests
- `/run-app` — Build and launch the macOS app
- `/fix-build` — Diagnose and fix build errors autonomously

### UI Development

- `/design-ui` — Launch autonomous UI workflow with spec gathering
- `/implement-component` — Create or modify a SwiftUI view
- `/review-ui` — Visual validation of implemented UI
- `/create-view` — Scaffold a new SwiftUI view with boilerplate

### Planning & Architecture

- `/write-plan` — Create a detailed implementation plan
- `/execute-plan` — Execute an existing markdown plan
- `/brainstorm` — Ideate solutions for a feature or problem
- `/feature-dev` — Full feature development workflow (plan → implement → test)

### Code Quality

- `/swift-style` — Apply Swift style guide and format code
- `/refactor-view` — Refactor a view for clarity and maintainability

### Project Management

- `/help` — Show all available commands
- `/list` — List available skills and agents
- `/skills` — Search and describe skills
- `/prompts` — Manage prompt templates
- `/configure` — Configure project settings

### Utilities

- `/hookify` — Create a new hook for custom automation
- `/revise-claude-md` — Update CLAUDE.md with new patterns

## Agents

Specialized AI agents for focused tasks:

| Agent | Type | Use Case |
|-------|------|----------|
| **ui-developer** | General-purpose | Autonomous UI development with all SwiftUI API skills loaded |
| **macos-architect** | Read-only | Architecture review and system design |
| **swift-expert** | General-purpose | Swift language expertise and best practices |
| **code-reviewer** | Read-only | Code review and quality assessment |
| **ios-developer** | General-purpose | iOS/iPadOS-specific development |
| **swift-reviewer** | Read-only | Swift code style and convention review |
| **code-architect** | General-purpose | Technical architecture and design decisions |
| **code-explorer** | Read-only | Codebase exploration and analysis |
| **skill-manager** | General-purpose | Skill creation and management |
| **prompt-manager** | General-purpose | Prompt template management |
| **conversation-analyzer** | Read-only | Conversation pattern analysis |

## Hooks

Event-driven automation via Python scripts:

- **userpromptsubmit.py** — Pre-process user input before Claude sees it
- **pretooluse.py** — Intercept and augment tool calls
- **posttooluse.py** — Process tool results and add context
- **stop.py** — Run cleanup tasks when conversation ends

Configure hooks in `hooks/hooks.json`:

```json
{
  "userpromptsubmit": ["hooks/userpromptsubmit.py"],
  "pretooluse": ["hooks/pretooluse.py"],
  "posttooluse": ["hooks/posttooluse.py"],
  "stop": ["hooks/stop.py"]
}
```

## Configuration

The plugin is designed to work standalone or alongside project-specific `.claude/` configurations.

### Plugin Priority

- Project `.claude/` settings override plugin settings
- Plugin provides defaults and shared workflows
- No conflicts — additive enhancement model

### Customization

Fork this repository and modify:

- `skills/` — Add new workflows or API references
- `agents/` — Create specialized agents for your domain
- `commands/` — Add shortcuts for repetitive tasks
- `hooks/` — Automate with Python event handlers

## Usage Examples

### Autonomous UI Development

```bash
# Launch full UI workflow
/design-ui

# Implement a specific component
/implement-component SidebarView

# Review and validate UI visually
/review-ui
```

### Building & Testing

```bash
# Run tests first
/test

# Build project
/build

# Fix failing builds
/fix-build
```

### Code Quality

```bash
# Review Swift style
/swift-style

# Refactor a view
/refactor-view Views/ContentView.swift

# Analyze codebase
# Trigger via: "Use code-analyzer skill to map the architecture"
```

**Note**: For TDD, planning, debugging, and git workflows, use [obra/superpowers](https://github.com/obra/superpowers) skills:
- `/brainstorm` — Ideation (requires obra/superpowers)
- `test-driven-development` skill — TDD discipline (requires obra/superpowers)
- `systematic-debugging` skill — Structured debugging (requires obra/superpowers)
- `writing-plans` / `executing-plans` skills — Planning workflows (requires obra/superpowers)

## Integration with Kulpt

This plugin was extracted from the [Kulpt](https://github.com/kmshdev/kulpt) project — a native macOS resume builder with Liquid Glass design. Kulpt's `.claude/` directory maintains project-specific configurations while this plugin provides the shared toolkit.

## Requirements

- Claude Code CLI
- macOS 14.0+ (for SwiftUI/Liquid Glass features)
- Xcode 16.0+ (for SwiftUI API references to match)
- Python 3.8+ (for hooks)

## Contributing

This is a personal toolkit extracted from production use. Feel free to fork and adapt for your Swift/macOS projects. Pull requests welcome for:

- New SwiftUI API skills (keep them focused and comprehensive)
- Improved agent prompts (optimize for task specificity)
- Useful command shortcuts (must solve real pain points)
- Hook automation (share event-driven patterns)

## License

MIT License — use freely, attribute if you share publicly.

## Author

**kmshdev** — Extracted from the Kulpt project's AI-powered development workflow.

---

**Status**: Production-ready. 20 skills, 11 agents, 22 commands, 5 hooks — battle-tested in real SwiftUI/macOS development. Works best with [obra/superpowers](https://github.com/obra/superpowers) for complete workflow coverage.
