---
description: Build and launch the app on simulator or Mac
allowed-tools: mcp__xcodebuildmcp__*, Bash(swift *), Bash(xcodebuild *), Bash(xcrun *), Bash(open *)
---

# Build and Run

## Steps

### 1. Build First
- Run the `/build` workflow to compile the project
- If build fails → stop and suggest `/fix-build`

### 2. Select Run Target
Determine the appropriate destination:

| App Type | Default Target | How to Detect |
|----------|---------------|---------------|
| **macOS** | "My Mac" | Deployment target is macOS, or `@main` uses `WindowGroup`/`MenuBarExtra` |
| **iOS** | iPhone 16 Simulator | Deployment target is iOS |
| **iPadOS** | iPad Pro Simulator | User requests iPad or app uses `NavigationSplitView` patterns |
| **Multi-platform** | Ask user | Both iOS and macOS destinations available |

- List available simulators: `xcrun simctl list devices available` or `mcp__xcodebuildmcp__list_available_simulators`
- If user specifies a device name → use that
- If simulator is not booted → boot it: `xcrun simctl boot <device-id>`

### 3. Launch
- **macOS apps:** Build and open the `.app` from derived data, or use `mcp__xcodebuildmcp__run_app`
- **iOS Simulator:** Install and launch via `xcrun simctl install` + `xcrun simctl launch`
- Pass any launch arguments the user specifies (e.g., `-com.apple.CoreData.SQLDebug 1`)
- Pass environment variables if specified (e.g., `SQLITE_ENABLE_THREAD_ASSERTIONS=1`)

### 4. Monitor
- Watch console output for runtime errors, crashes, or constraint warnings
- Auto Layout warnings: report the conflicting constraints
- Fatal errors / crashes: report the crash log with stack trace
- If the app launches successfully → report success with the run target
