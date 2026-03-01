---
name: macos-development
description: This skill should be used when the user asks about "macOS development", "Swift 6 patterns", "SwiftData best practices", "AppKit bridging", "macOS 26 APIs", "Tahoe features", or needs comprehensive macOS development guidance. Covers coding practices, architecture, SwiftData, sandboxing, and Tahoe APIs with detailed reference modules.
allowed-tools: [Read, Glob, Grep, WebFetch]
---

# macOS Development Expert

## Lifecycle Position

Phases 0-1 (Scaffold → Architecture). Start here for new apps (`app-planner/` module) and system design (`architecture-patterns/` module). Next: load `macos-app-design` for UI design.

Comprehensive guidance for macOS app development. This skill aggregates specialized modules for different aspects of macOS development.

## When This Skill Activates

Use this skill when the user:
- Asks about macOS development best practices
- Wants code review for macOS/Swift projects
- Needs help with SwiftUI, SwiftData, or AppKit
- Is implementing macOS 26 (Tahoe) features
- Wants UI/UX review against HIG
- Needs architecture guidance for macOS apps

## Available Modules

Read relevant module files based on the user's needs:

### coding-best-practices/
Swift 6+ code quality and modern idioms.
- **`coding-best-practices/swift-language.md`** - Modern Swift patterns
- **`coding-best-practices/modern-concurrency.md`** - async/await, actors, Sendable
- **`coding-best-practices/data-persistence.md`** - SwiftData, UserDefaults, Keychain, actor-based JSON persistence (`swift-actor-persistence`)
- **`coding-best-practices/code-organization.md`** - Project structure and modularity
- **`coding-best-practices/architecture-principles.md`** - Clean architecture patterns

### architecture-patterns/
Software design and architecture.
- **`architecture-patterns/solid-detailed.md`** - SOLID principles with Swift examples
- **`architecture-patterns/design-patterns.md`** - Common design patterns
- **`architecture-patterns/modular-design.md`** - Modular architecture approaches

### swiftdata-architecture/
SwiftData deep dive.
- **`swiftdata-architecture/schema-design.md`** - Model design and relationships
- **`swiftdata-architecture/query-patterns.md`** - Efficient queries and predicates
- **`swiftdata-architecture/performance.md`** - Optimization techniques

### macos-tahoe-apis/
macOS 26 specific features.
- **`macos-tahoe-apis/tahoe-features.md`** - New macOS 26 capabilities
- **`macos-tahoe-apis/apple-intelligence.md`** - AI/ML integration
- **`macos-tahoe-apis/mlx-framework.md`** - On-device ML with MLX
- **`macos-tahoe-apis/continuity.md`** - Cross-device features
- **`macos-tahoe-apis/xcode16.md`** - Xcode 16 tools and features

### macos-capabilities/
Platform integration.
- **`macos-capabilities/sandboxing.md`** - App Sandbox and entitlements
- System integration features

### appkit-swiftui-bridge/
Hybrid development.
- **`appkit-swiftui-bridge/nsviewrepresentable.md`** - Wrapping AppKit views
- State management between frameworks

### ui-review-tahoe/
UI/UX review for macOS 26.
- Liquid Glass design system
- HIG compliance checking
- Accessibility review

### app-planner/
Project planning and analysis.
- New app architecture planning
- Existing app audits

## How to Use

1. Identify user's need from their question
2. Read relevant module files from subdirectories
3. Apply the guidance to their specific context
4. Reference Apple documentation when needed

## Example Workflow

**User asks about SwiftData performance:**
1. Read **`swiftdata-architecture/performance.md`**
2. Read **`swiftdata-architecture/query-patterns.md`** if relevant
3. Apply recommendations to their code
