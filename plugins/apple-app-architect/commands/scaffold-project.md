---
description: Create a new Xcode project with Swift 6.2, iOS 26/macOS 26, strict concurrency, and proper app bundle structure
argument-hint: "[app name]"
allowed-tools: Read, Write, Bash(xcodegen *), Bash(which *), Bash(mkdir *), Bash(chmod *), Bash(open *), Bash(ls *), mcp__xcodebuildmcp__*
---

# /scaffold-project

Create a new Xcode project configured for iOS 26+ / macOS 26+ with Swift 6.2 and strict concurrency.

## Prerequisites

Load `apple-app-architect:swift-project-scaffold` skill using the Skill tool.

## Step 1 — Gather Requirements

Ask the user these questions (use defaults if `$ARGUMENTS` provides app name):

1. **App name** — default: `$ARGUMENTS` or current directory name
2. **Bundle ID prefix** — default: `com.developer`
3. **Platform** — `[1] macOS  [2] iOS  [3] Multiplatform` — default: 1 (macOS)
4. **Deployment target** — default: macOS 26.0 / iOS 26.0
5. **Archetype** — `[1] Standard (WindowGroup)  [2] Document-based  [3] Menu bar extra  [4] Utility` — default: 1
6. **Include test target?** — default: yes
7. **Include SwiftData?** — default: no

## Step 2 — Detect Tooling

```bash
which xcodegen
```

- If found → **XcodeGen path** (primary)
- If not found → **XcodeBuildMCP fallback**

## Step 3 — Create Project

### XcodeGen Path

1. Create directories: `Sources/<AppName>/`, `Tests/<AppName>Tests/`
2. Read template from `swift-project-scaffold` skill: select `macos.project.yml` or `ios.project.yml`
3. Replace template variables (`__APP_NAME__`, `__BUNDLE_PREFIX__`, `__BUNDLE_ID__`, `__MACOS_TARGET__` or `__IOS_TARGET__`)
4. Write `project.yml` at project root
5. Read and write `AppEntry.swift` to `Sources/<AppName>/` — replace archetype code block based on user's selection
6. Read and write `ContentView.swift` to `Sources/<AppName>/`
7. Write `.gitignore` from template
8. If SwiftData selected: add `import SwiftData` and `modelContainer(for:)` to AppEntry.swift
9. If test target excluded: remove the test target section from `project.yml`
10. Run: `xcodegen generate`

### XcodeBuildMCP Fallback

1. Call `scaffold_macos_project` or `scaffold_ios_project` MCP tool with the app name
2. Apply build setting patches (per `swift-project-scaffold` skill fallback section)
3. Replace generated AppEntry.swift with archetype-specific version
4. If SwiftData selected: add SwiftData imports and model container

## Step 4 — Verify

1. Run `BuildProject` to confirm clean build
2. Report result to user
3. Suggest: `open <AppName>.xcodeproj` to open in Xcode

## Step 5 — Report

Output summary:
```
Project scaffolded successfully:
- Name: <AppName>
- Platform: <platform>
- Archetype: <archetype>
- Swift: 6.2 (strict concurrency)
- Target: <deployment target>
- Test target: <yes/no>
- SwiftData: <yes/no>
- Method: <XcodeGen/XcodeBuildMCP>
```
