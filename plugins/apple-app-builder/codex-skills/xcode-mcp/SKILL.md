---
name: xcode-mcp
description: Use when the user needs Xcode project inspection, Apple API docs, compiler diagnostics, build logs, preview rendering, snippet execution, or targeted test runs through the official Xcode MCP bridge exposed by `xcrun mcpbridge`.
---

# Xcode MCP

## Overview

This plugin bundles the official Xcode MCP bridge through `./.mcp.json`:

```json
{
  "mcpServers": {
    "xcode": {
      "command": "xcrun",
      "args": ["mcpbridge"]
    }
  }
}
```

That keeps the Codex packaging story aligned with Xcode itself instead of a
third-party wrapper.

## Host requirements

- Xcode must be installed.
- Xcode must be running; `xcrun mcpbridge` attaches to a live Xcode process.
- If multiple Xcode instances are open, the bridge follows Xcode's own
  selection logic. If attachment fails, report that clearly before proceeding.

## Core workflows

### Project orientation
- `XcodeListWindows` to identify the active workspace tab.
- `XcodeLS`, `XcodeGlob`, `XcodeGrep`, and `XcodeRead` to inspect the project
  tree and open source files.
- `DocumentationSearch` when Apple API behavior or availability needs
  confirmation.

### Editing and diagnostics
- `XcodeUpdate` for targeted replacements.
- `XcodeWrite`, `XcodeMakeDir`, `XcodeMV`, and `XcodeRM` when project structure
  changes are required.
- `XcodeRefreshCodeIssuesInFile` to pull current compiler diagnostics for a
  touched file.

### Build and preview
- `BuildProject` for project-wide compile verification.
- `GetBuildLog` for actionable compiler and build task output.
- `RenderPreview` for SwiftUI visual confirmation when a `#Preview` exists.
- `ExecuteSnippet` for quick local experiments inside a file's build context
  when a minimal check is faster than editing production code first.

### Tests
- `GetTestList` to discover test identifiers.
- `RunSomeTests` for narrow test slices.
- `RunAllTests` only when the change or failure mode justifies the broader
  cost.

## Guardrails

- This Xcode MCP surface is IDE-centric. It does not provide simulator UI
  automation, screenshots, or LLDB session control in this plugin.
- Prefer the narrowest proof: file diagnostics, preview render, targeted build,
  then targeted tests.
- When a preview or targeted test is unavailable, say that plainly and fall
  back to the next smallest available proof.
