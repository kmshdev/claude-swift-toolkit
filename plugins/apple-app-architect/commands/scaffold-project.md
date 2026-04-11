---
description: Create a new Xcode project with Swift 6.2, iOS 26/macOS 26, strict concurrency, and proper app bundle structure
argument-hint: "[app name]"
allowed-tools: Read, Write, Bash(xcodegen *), Bash(which *), Bash(mkdir *), Bash(chmod *), Bash(open *), Bash(ls *), mcp__xcode__*
---

# /scaffold-project

Create a new Xcode project configured for iOS 26+ / macOS 26+ with Swift 6.2 and strict concurrency.

## Prerequisites

Load `apple-app-architect:swift-project-scaffold` using the Skill tool.

## Step 1 — Gather Requirements

Ask the user these questions (use defaults if `$ARGUMENTS` provides the app name):

1. **App name** — default: `$ARGUMENTS` or current directory name
2. **Bundle ID prefix** — default: `com.developer`
3. **Platform** — `[1] macOS  [2] iOS` — default: 1
4. **Deployment target** — default: macOS 26.0 / iOS 26.0
5. **Archetype** — `[1] Standard  [2] Document-based  [3] Menu bar extra  [4] Utility` — default: 1
6. **Include test target?** — default: yes
7. **Include SwiftData?** — default: no

## Step 2 — Detect Tooling

```bash
which xcodegen
```

- If found → **XcodeGen path**
- If not found → stop and ask the user to either install XcodeGen or create the starter project in Xcode manually

## Step 3 — Create Project

### XcodeGen Path

1. Create directories: `Sources/<AppName>/`, `Tests/<AppName>Tests/`
2. Select the correct template from `swift-project-scaffold`
3. Replace template variables (`__APP_NAME__`, `__BUNDLE_PREFIX__`, `__BUNDLE_ID__`, deployment target variables)
4. Write `project.yml`, `AppEntry.swift`, `ContentView.swift`, and `.gitignore`
5. Apply the selected archetype and optional SwiftData configuration
6. Run `xcodegen generate`
7. Open the project in Xcode if needed

### Manual Xcode Path

- There is no bundled official Xcode MCP scaffolding command in this toolkit.
- If the user already created a starter project in Xcode, write the generated
  source files into that project and continue with verification.
- Otherwise stop after explaining the two supported options: install XcodeGen or
  create the starter project manually in Xcode.

## Step 4 — Verify

1. If the project is open in Xcode and the bridge is available, run `BuildProject`
2. Otherwise run `xcodebuild` for a clean build check
3. Report the result to the user

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
- Method: <XcodeGen/Manual Xcode>
```
