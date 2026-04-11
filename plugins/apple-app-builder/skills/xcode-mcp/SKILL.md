---
name: xcode-mcp
description: Use when the user needs Xcode project inspection, Apple API docs, compiler diagnostics, build logs, preview rendering, snippet execution, or targeted test runs through the official Xcode MCP bridge.
---

# Xcode MCP

## Lifecycle Position

Phase 4 (Build). Build, inspect, preview, and test through Xcode's official MCP
bridge.

## Setup Protocol

1. Call `XcodeListWindows` first to get valid workspace tab identifiers.
2. Select the active Xcode workspace or project tab before building.
3. Use `DocumentationSearch` when Apple API behavior or availability needs
   confirmation.
4. If the user has not opened the project in Xcode, say so plainly and fall
   back to `xcodebuild` or `swift` CLI commands where appropriate.

## File Operations

When the Xcode bridge is available, prefer these tools over raw shell access for
project files:

| Action | Use This | Not This |
|--------|----------|----------|
| Read files | `XcodeRead` | `cat` |
| Write new files | `XcodeWrite` | ad-hoc shell redirection |
| Update files | `XcodeUpdate` | broad text edits in shell |
| Find files | `XcodeGlob` | `find` |
| Search code | `XcodeGrep` | `grep` |
| List directory | `XcodeLS` | `ls` |
| Create directory | `XcodeMakeDir` | `mkdir` |
| Delete files | `XcodeRM` | destructive shell deletes |
| Move or rename | `XcodeMV` | `mv` |

## BuildFix Loop

```text
1. BuildProject
2. If errors:
   a. XcodeListNavigatorIssues (preferred)
   b. GetBuildLog (fallback)
3. Fix the smallest issue via XcodeUpdate/XcodeWrite
4. XcodeRefreshCodeIssuesInFile on changed files
5. Repeat (max 5 iterations, then escalate)
```

After 5 consecutive build failures: stop and present the blocking errors to the
user. Do not keep cycling.

## TestFix Loop

```text
1. GetTestList
2. RunSomeTests for the narrowest relevant slice
3. If those pass and broader confidence is needed, RunAllTests
4. If the run fails at the build level, read GetBuildLog before editing
5. Fix the issue and repeat the smallest relevant test slice
```

## PreviewVerify

After any visual UI change:
1. `RenderPreview` to capture the relevant view.
2. Inspect the rendered output for layout, content, and styling issues.
3. Rebuild or rerender after each meaningful fix.

## Diagnostics

- `XcodeListNavigatorIssues` — structured issue list
- `XcodeRefreshCodeIssuesInFile` — fresh diagnostics after editing a file
- `DocumentationSearch` — Apple docs and API references
- `ExecuteSnippet` — minimal local experiments inside a file's build context

## Guardrails

- This official Xcode bridge is IDE-centric. It does not provide simulator UI
  automation, log capture, or LLDB session control in this toolkit.
- It also does not scaffold new Xcode projects.
- Prefer the narrowest proof available: file diagnostics, preview render,
  targeted build, then targeted tests.
- If the bridge is unavailable, fall back to native Apple CLI tooling such as
  `xcodebuild`, `swift test`, or `open`, and say that clearly.
