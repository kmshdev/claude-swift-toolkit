---
description: Build the Xcode project or Swift package
allowed-tools: mcp__xcode__*, Bash(swift *), Bash(xcodebuild *)
---

# Build Project

## Steps

### 1. Discover Project
- Prefer the active Xcode window when the official Xcode MCP bridge is
  available: start with `XcodeListWindows` and build the selected tab.
- If the project is not open in Xcode, search for `.xcworkspace` first, then
  `.xcodeproj`, then `Package.swift`.
- If nothing is found, stop and ask the user for the project path.

### 2. Choose the Build Path
- **Official Xcode MCP available:** load `xcode-mcp` and use `BuildProject`.
- **Swift package:** use `swift build` directly.
- **No Xcode MCP bridge:** use `xcodebuild` CLI against the discovered project
  or workspace.

### 3. Identify Scheme and Destination
- For Xcode MCP builds, rely on the active scheme from the selected Xcode tab.
- For CLI builds, list schemes with `xcodebuild -list` and prefer the main app
  scheme over test or extension schemes.
- Default to Debug configuration unless the user explicitly asks for Release.

### 4. Build
- Use `BuildProject` for the MCP path.
- For CLI fallback, use `xcodebuild build` with the discovered project or
  workspace and chosen scheme.
- For Swift packages, use `swift build`.

### 5. Parse Results
- For the MCP path, inspect `XcodeListNavigatorIssues` first and `GetBuildLog`
  second.
- For CLI fallback, categorize failures from the shell output.
- Typical categories: package resolution, compiler errors, linker failures,
  code-signing issues, and API availability.

### 6. Report
- On success, report the build method, target, and configuration.
- On failure, show the smallest useful error set with file references and
  suggest `/fix-build`.
