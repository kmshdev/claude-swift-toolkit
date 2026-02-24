---
description: Implement a SwiftUI component from a spec — creates files, builds, validates
argument-hint: <spec or description>
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Implement Component: $ARGUMENTS

## Workflow

1. **Read the spec** — understand what to build (from /design-ui output or direct description)
2. **Read existing patterns** — check similar views in `Kulpt/Views/` for consistency
3. **Implement:**
   - Create/modify Swift files in appropriate `Kulpt/Views/` subdirectory
   - Use `@Environment(AppState.self)` + `@Bindable var appState = appState`
   - Include `#Preview` block
   - Follow Kulpt coding standards (Swift 6, @Observable, guard for early exits)
4. **Build:**
   ```bash
   xcodebuild -project Kulpt.xcodeproj -scheme Kulpt -destination 'platform=macOS' build
   ```
5. **Validate:** Check build output for success. If errors, fix and rebuild.
6. **Report:** List created/modified files and build status.

## Rules

- NO glass on form elements (HIG violation)
- NO lagoonReveal on always-visible content
- ONE view at a time for multi-view changes
- Build MUST succeed before claiming completion
- Include `#Preview` in every new view file
