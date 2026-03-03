---
name: xcodebuildmcp
description: This skill should be used when the user asks to "build the Xcode project", "run tests", "debug the app", "capture logs", "automate UI", or needs Xcode build tooling via MCP for iOS/macOS/watchOS/tvOS/visionOS development. Prefer XcodeBuildMCP tools over raw xcodebuild commands.
---

# XcodeBuildMCP

## Lifecycle Position

Phase 4 (Build). Build, test, run, and debug via MCP tools. XcodeBuildMCP tools are the PRIMARY interface for file operations, builds, and tests when the MCP server is available.

## Setup Protocol

1. Call `XcodeListWindows` first to get valid tab identifiers
2. Cache tab mappings for the session
3. Call `session_show_defaults` to check current configuration
4. If macOS workflow tools are needed: `manage_workflows` to enable them (only simulator is enabled by default)

## File Operations (Primary Interface)

When XcodeBuildMCP is available, use these instead of standard tools:

| Action | Use This | NOT This |
|--------|----------|----------|
| Read files | `XcodeRead` | `Read` tool or `cat` |
| Write new files | `XcodeWrite` | `Write` tool |
| Update files | `XcodeUpdate` | `Edit` tool |
| Find files | `XcodeGlob` | `Glob` tool or `find` |
| Search code | `XcodeGrep` | `Grep` tool or `rg` |
| List directory | `XcodeLS` | `ls` |
| Create directory | `XcodeMakeDir` | `mkdir` |
| Delete files | `XcodeRM` | Confirm with user first |
| Move/rename | `XcodeMV` | `mv` |

Fall back to standard tools only in headless sessions (`claude -p` without MCP).

## BuildFix Loop (max 5 iterations)

```text
1. BuildProject
2. IF errors:
   a. XcodeListNavigatorIssues (preferred — structured)
   b. GetBuildLog (fallback — raw text)
3. Fix errors via XcodeUpdate
4. XcodeRefreshCodeIssuesInFile on changed files
5. GOTO 1 (max 5 iterations, then escalate to user)
```

After 5 consecutive build failures: stop and present the errors to the user. Do not keep cycling.

## TestFix Loop

```text
1. RunAllTests (or RunSomeTests for targeted iteration)
2. Parse result:

   ALL PASSED → done

   SOME FAILED (with failure messages):
   → Read failure details
   → Fix the failing code
   → RunSomeTests on ONLY the failures (fast iteration)
   → Once failures fixed, RunAllTests to verify full suite

   "notRun" OR "canceled" TESTS → TEST PROCESS CRASHED
   → Do NOT retry RunAllTests
   → Immediately run: swift test 2>&1 | head -80
   → Read the fatal error / crash log
   → Diagnose root cause from the crash message
   → Fix → BuildProject → re-run tests

   PROGRESS FROZEN >120 seconds → TEST RUNNER HUNG
   → pkill -f "xctest"
   → Wait 10 seconds
   → Run swift test via CLI as fallback
   → If CLI also hangs: escalate to user
```

CRITICAL RULES:
- NEVER retry RunAllTests immediately after an anomalous result
- ALWAYS get the crash log BEFORE hypothesizing about the cause
- "notRun" means the test process CRASHED — it does NOT mean "still running"
- "canceled" means a prior crash poisoned the suite

## Error Triage Decision Tree

| Signal | Meaning | Action |
|--------|---------|--------|
| All passed | Tests green | Done |
| Some failed + messages | Normal failures | Fix → RunSomeTests on failures |
| `notRun` status | Process crashed mid-suite | `swift test 2>&1` for crash log |
| `canceled` status | Prior crash poisoned suite | Kill test process, get crash log |
| AbortError -32001 | Xcode locked from prior crash | `pkill -f "xctest"`, wait 10s, retry |
| Progress stuck >120s | Test runner hung | Kill process, CLI fallback |
| `isError: true` | Build/test error | Read error details first |

## PreviewVerify

After any visual/UI change:
1. `RenderPreview` to capture the view
2. Read the screenshot to verify layout, colors, content
3. Compare before/after for glass/layout work

## Diagnostics

- `XcodeListNavigatorIssues` — structured issue list (preferred over parsing build logs)
- `XcodeRefreshCodeIssuesInFile` — refresh diagnostics after editing a file
- `DocumentationSearch` — search Apple docs and WWDC sessions
- `ExecuteSnippet` — test Swift code in isolation

## Tools Reference

### Session defaults
- `session_set_defaults` — set project/scheme/simulator/device defaults
- `session_show_defaults` — show current defaults
- `session_clear_defaults` — clear defaults

### Project discovery
- `discover_projs` — find .xcodeproj/.xcworkspace files
- `list_schemes` — list Xcode schemes
- `show_build_settings` — show build settings
- `get_app_bundle_id` / `get_mac_bundle_id` — extract bundle ID

### Build & Test
- `build_macos` / `build_sim` / `build_device` — compile
- `build_run_macos` / `build_run_sim` — compile and launch
- `test_macos` / `test_sim` / `test_device` — run tests
- `RunAllTests` / `RunSomeTests` / `GetTestList` — test management
- `BuildProject` / `GetBuildLog` — build with log access

### App lifecycle
- `launch_mac_app` / `launch_app_sim` / `launch_app_device` — launch
- `stop_mac_app` / `stop_app_sim` / `stop_app_device` — stop

### Logging
- `start_sim_log_cap` / `stop_sim_log_cap` — simulator log capture
- `start_device_log_cap` / `stop_device_log_cap` — device log capture

### Debugging
- `debug_attach_sim` — attach LLDB
- `debug_breakpoint_add` / `debug_breakpoint_remove` — breakpoints
- `debug_continue` / `debug_detach` — session control
- `debug_lldb_command` — arbitrary LLDB command
- `debug_stack` / `debug_variables` — inspection

### UI automation
- `snapshot_ui` — view hierarchy with coordinates
- `screenshot` — capture screenshot
- `tap` / `swipe` / `long_press` / `touch` — interactions
- `type_text` / `key_press` / `key_sequence` — input
- `gesture` / `button` — simulator controls

### SwiftPM
- `swift_package_build` / `swift_package_test` — build/test SPM targets
- `swift_package_run` / `swift_package_stop` / `swift_package_list` — process management
- `swift_package_clean` — clean

### Scaffolding & utilities
- `scaffold_ios_project` / `scaffold_macos_project` — project templates
- `clean` — clean build products
- `doctor` — MCP environment info
- `manage_workflows` — enable/disable tool groups
