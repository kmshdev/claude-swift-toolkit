---
description: Implement a SwiftUI component from a spec — creates files, builds, validates
argument-hint: <spec or description>
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Implement Component: $ARGUMENTS

## Platform Detection

Before implementing, determine the target platform:
1. Check `.xcodeproj` or `Package.swift` for deployment target (macOS vs iOS)
2. Check existing imports: `AppKit`/`NSApplication` = macOS, `UIKit`/`UIApplication` = iOS
3. Dispatch the appropriate agent:
   - **macOS target:** `ui-developer` agent (loads swiftui-expert-skill, swiftui-components, macos-app-design)
   - **iOS target:** `ios-developer` agent (loads ios-testing, swiftui-expert-skill, swiftui-presentation-api)
   - **Universal:** Both agents in parallel, each handling their platform layer
   - **Unknown:** Ask the user which platform to target

## Workflow

1. **Read the spec** — understand what to build (from /design-ui output or direct description)
2. **Read existing patterns** — check similar views in the project's Views directory for consistency
3. **Implement:**
   - Create/modify Swift files in appropriate Views subdirectory
   - Use the project's state management pattern (check existing files)
   - If the component reads/writes persistent local data, load `swift-actor-persistence`
   - Include `#Preview` block
   - Follow project coding standards (check CLAUDE.md for conventions)
4. **Build** (mandatory — no exceptions):
   - If `mcp__xcodebuildmcp__*` tools available → use them
   - If not → use CLI: `xcodebuild -project *.xcodeproj -scheme <SchemeName> -destination 'platform=macOS' build`
   - If no Xcode project exists → use `swift build` for Swift packages
   - If none of the above work → **create a minimal Swift file and compile it**: `swiftc -typecheck <file>.swift` to verify syntax
   - "Build pending" or "mentally verified" is NOT acceptable — find a way to verify
5. **Validate:** Check build output for success. If errors, fix and rebuild. Maximum 3 rebuild cycles.
6. **Report:** List created/modified files and build result (success + method used).

## Rules

- NO glass on form elements (HIG violation)
- NO lagoonReveal on always-visible content
- ONE view at a time for multi-view changes
- Build MUST succeed before claiming completion — "build pending" is not completion
- Include `#Preview` in every new view file
- If build tooling is genuinely unavailable, say so explicitly and do NOT mark the task as complete
