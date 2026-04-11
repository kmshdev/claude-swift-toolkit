---
description: Implement a SwiftUI component from a spec — creates files, builds, validates
argument-hint: <spec or description>
allowed-tools: Read, Write, Edit, Bash(xcodebuild *), Bash(swift *), Bash(swiftc *), Glob, Grep, mcp__xcode__*
---

# Implement Component: $ARGUMENTS

## Platform Detection

Before implementing, determine the target platform:
1. Check `.xcodeproj` or `Package.swift` for deployment target.
2. Check existing imports: `AppKit`/`NSApplication` = macOS, `UIKit`/`UIApplication` = iOS.
3. Dispatch the appropriate agent:
   - **macOS target:** `ui-developer`
   - **iOS target:** `ios-developer`
   - **Unknown:** ask the user which platform to target

## Workflow

1. **Read the spec** — understand what to build.
2. **Read existing patterns** — inspect similar views for consistency.
3. **Implement**
   - Create or modify Swift files in the appropriate feature area.
   - Use the project's existing state-management pattern.
   - Add a `#Preview` block.
4. **Build**
   - If the official Xcode MCP bridge is available, use `BuildProject`.
   - Use `XcodeRefreshCodeIssuesInFile` on touched files when possible.
   - Use `RenderPreview` for UI-focused verification.
   - If the project is not open in Xcode, fall back to `xcodebuild`.
   - For Swift packages, use `swift build`.
   - If none of the above works, use `swiftc -typecheck` as a syntax-only last resort.
5. **Validate** — fix build or preview failures and retry. Maximum 3 rebuild cycles.
6. **Report** — list created or modified files and the verification method used.

## Rules

- No glass on form elements.
- No lagoonReveal on always-visible content.
- One view at a time for multi-view changes.
- Include `#Preview` in every new view file.
- Do not mark the task complete without build or preview evidence.
