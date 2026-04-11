---
name: autonomous-ui-workflow
description: Implement SwiftUI changes in an existing Xcode project and validate them with previews, diagnostics, builds, and focused test handoff through the official Xcode MCP bridge.
---

# Autonomous UI Workflow

## Overview

Use this skill as the build-oriented wrapper around the toolkit's SwiftUI
reference skills. It keeps code editing in normal Codex file tools and uses the
official Xcode MCP bridge from this plugin's `.mcp.json` for project
inspection, diagnostics, preview rendering, builds, and targeted tests.

## Prerequisites

- This plugin bundles the official Xcode MCP bridge through `./.mcp.json` by
  running `xcrun mcpbridge`.
- Xcode must be installed and running on the host machine before the bridge can
  attach.
- If the bridge cannot connect, say so plainly and keep the task scoped to
  repo-local edits plus build and test guidance that the user can run from
  Xcode.

## Workflow

### 1) Spec
- Confirm the target screen, feature, and user interaction model.
- Identify the minimum OS and platform assumptions before editing code.
- Find the nearest existing SwiftUI implementation in the repo and preserve the
  local architecture and naming patterns.

### 2) Research
- Load the narrowest supporting skills that match the work:
  - `swiftui-ui-patterns` for structure and state flow, if the
    `apple-design-system` plugin is installed
  - `swiftui-components` for reusable view shapes and patterns, if the
    `apple-design-system` plugin is installed
  - `swiftui-material-api`, `swiftui-presentation-api`, `swiftui-typography-api`,
    `swiftui-effects-api`, or related Apple design-system references as needed
    when those design-system skills are available
  - `swift-networking`, `swift-concurrency`, or `swift-localization` when the UI
    change crosses into transport, async orchestration, or user-facing copy

### 3) Orient in Xcode
- Start with `xcode-mcp`.
- Use `XcodeListWindows` to find the active workspace tab.
- Use `XcodeGlob`, `XcodeGrep`, and `XcodeRead` to locate relevant files before
  editing.
- Use `DocumentationSearch` when you need current Apple API guidance.

### 4) Implement
- Edit Swift files with normal Codex file tools or `XcodeUpdate` when a precise
  in-project replacement is the cleanest option.
- Keep the view small, state ownership explicit, and behavior aligned with the
  repo's existing patterns.
- If the screen grows, extract dedicated subviews before adding new abstraction.

### 5) Validate in Xcode
- Use `XcodeRefreshCodeIssuesInFile` on touched files to catch immediate
  diagnostics.
- Use `RenderPreview` for UI-focused changes when the file exposes a relevant
  `#Preview`.
- Use `BuildProject` when you need project-level compile evidence.
- If the build fails, inspect `GetBuildLog`, fix the smallest cause, and retry.
  Stop after a small number of failed loops and report the blocking errors
  clearly.

### 6) Review and test handoff
- After build or preview evidence is green, hand off to the
  `apple-app-quality` plugin if it is installed:
  - `code-analyzer` for a structured review pass
  - `swiftui-view-refactor` if the view needs structural cleanup
  - `ios-testing` to discover tests with `GetTestList` and run the smallest
    relevant slice with `RunSomeTests` before broadening to `RunAllTests`
- If the quality plugin is not installed, tell the user the review and testing
  follow-up lives there instead of assuming those skills are present.

## Guardrails

- Do not claim runtime simulator or device behavior unless it was verified
  outside this plugin surface.
- Do not claim the feature works unless you have build evidence and, for UI
  changes, preview or test evidence.
- Keep the workflow outcome-focused. Do not refer users to Claude-only slash
  commands or named subagents.
- Prefer the bundled Xcode MCP bridge over direct `xcodebuild` shell commands
  for project inspection, diagnostics, and validation.
- If a task only needs reference guidance and not Xcode tooling, skip the MCP
  path and stay in the reference skills.
