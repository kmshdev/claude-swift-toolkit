---
description: Build the Xcode project or Swift package
allowed-tools: mcp__xcodebuildmcp__*, Bash(swift *), Bash(xcodebuild *)
---

# Build Project

## Steps

### 1. Discover Project
- Search for `.xcworkspace` first (takes priority over `.xcodeproj` when both exist)
- If no workspace, search for `.xcodeproj`
- If neither, check for `Package.swift` (Swift Package)
- If nothing found → stop and ask the user for the project path

### 2. Load Build Skill
- If `mcp__xcodebuildmcp__*` tools are available → use `xcodebuildmcp` skill patterns
- If not → use `xcodebuildmcp-cli` skill for direct `xcodebuild` CLI commands
- For Swift packages → use `swift build` directly

### 3. Identify Scheme and Destination
- List available schemes: `mcp__xcodebuildmcp__list_schemes` or `xcodebuild -list`
- Prefer the main app scheme (not test schemes or extension schemes)
- Default destination: macOS for macOS apps, iOS Simulator for iOS apps
- If multiple schemes match → ask the user which to build

### 4. Build
- Use Debug configuration for development builds (faster, includes debug symbols)
- Use Release configuration only when the user explicitly asks
- For workspaces: specify both `-workspace` and `-scheme`
- Capture full build output for error parsing

### 5. Parse Results
Categorize any build errors:

| Category | Indicators | Typical Fix |
|----------|-----------|-------------|
| **SPM Resolution** | "package resolution failed", "dependency not found" | Clean package caches, check minimum deployment target |
| **Swift Compiler** | type mismatches, missing imports, API availability | Fix types, add `import`, wrap in `#available` |
| **Linker** | "undefined symbol", "framework not found" | Check framework search paths, verify linking |
| **Signing** | "no provisioning profile", "code signing" | Verify team, bundle ID, entitlements |

### 6. Report
- On success → report build succeeded with scheme and destination
- On failure → show categorized errors with file:line references, suggest `/fix-build`
