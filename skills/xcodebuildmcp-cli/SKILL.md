---
name: xcodebuildmcp-cli
description: This skill should be used when the user asks to "build via CLI", "run tests from terminal", "debug from command line", or needs xcodebuildmcp CLI as alternative to MCP tool calls for iOS/macOS/watchOS/tvOS/visionOS development. Provides CLI command reference for build, test, run, debug, log, and UI automation workflows.
---

# XcodeBuildMCP CLI

## Lifecycle Position

Phase 4 (Build). CLI alternative to MCP tool calls for build, test, and automation.

This skill positions the XcodeBuildMCP CLI as a low-overhead alternative to MCP tool calls: agents can run shell commands directly, and the CLI exposes the same tool surface without schema-exchange cost. Prefer the CLI over raw `xcodebuild`, `xcrun`, or `simctl` commands.

## When To Use This CLI (Capabilities And Workflows)

Use this CLI when:
- Build/test/run/debugging/logging/UI automation capabilities are needed
- Simulator/device management capabilities are needed
- AI-optimized tools and tool responses are required
- Project discovery capabilities are needed (schemes, bundle IDs, app paths)

## Command Discovery

Discover workflows, tools, and arguments with `--help`:

```bash
xcodebuildmcp --help
xcodebuildmcp tools --help
xcodebuildmcp tools --json
xcodebuildmcp <workflow> --help
xcodebuildmcp <workflow> <tool> --help
```

Notes:
- Use `--json '{...}'` for complex arguments and `--output json` if you need machine-readable results (not recommended).

## Common Workflows

### Build And Run On Simulator

1. List simulators and pick a device name or UDID.
2. Build and run.

When project details are unknown, discover them:
```bash
xcodebuildmcp simulator discover-projs --workspace-root .
xcodebuildmcp simulator list-schemes --project-path ./MyApp.xcodeproj
xcodebuildmcp simulator list-sims
```

To build, install and launch the app in one command:
```bash
xcodebuildmcp simulator build-run-sim --scheme MyApp --project-path ./MyApp.xcodeproj --simulator-name "iPhone 17 Pro"
```

### Build only

When you only need to check that there are no build errors, you can build without running the app.

```bash
xcodebuildmcp simulator build-sim --scheme MyApp --project-path ./MyApp.xcodeproj --simulator-name "iPhone 17 Pro"
```

### Run Tests

When you need to run tests, you can do so with the `test-sim` tool.

```bash
xcodebuildmcp simulator test-sim --scheme MyAppTests --project-path ./MyApp.xcodeproj --simulator-name "iPhone 17 Pro"
```

### Install And Launch On Physical Device

```bash
xcodebuildmcp device list-devices
xcodebuildmcp device build-device --scheme MyApp --project-path ./MyApp.xcodeproj
xcodebuildmcp device get-device-app-path --scheme MyApp --project-path ./MyApp.xcodeproj
xcodebuildmcp device get-app-bundle-id --app-path /path/to/MyApp.app
xcodebuildmcp device install-app-device --device-id DEVICE_UDID --app-path /path/to/MyApp.app
xcodebuildmcp device launch-app-device --device-id DEVICE_UDID --bundle-id io.sentry.MyApp --app-path /path/to/MyApp.app
```

### Capture Logs On Simulator

```bash
xcodebuildmcp logging start-sim-log-cap --simulator-id SIMULATOR_UDID --bundle-id io.sentry.MyApp
xcodebuildmcp logging stop-sim-log-cap --log-session-id LOG_SESSION_ID
```

### Debug A Running App (Simulator)

1. Launch the app.
2. Attach the debugger after the app is fully launched.

Launch if not already running:
```bash
xcodebuildmcp simulator launch-app-sim --bundle-id io.sentry.MyApp --simulator-id SIMULATOR_UDID
```

Attach the debugger:

It's generally a good idea to wait for 1-2s for the app to fully launch before attaching the debugger.

```bash
xcodebuildmcp debugging debug-attach-sim --bundle-id io.sentry.MyApp --simulator-id SIMULATOR_UDID
```

To add/remove breakpoints, inspect stack/variables, and issue arbitrary LLDB commands, view debugging help:
```bash
xcodebuildmcp debugging --help
```


### Inspect UI And Automate Input

Snapshot UI accessibility tree, tap/swipe/type, and capture screenshots:

```bash
xcodebuildmcp ui-automation snapshot-ui --simulator-id SIMULATOR_UDID
xcodebuildmcp ui-automation tap --simulator-id SIMULATOR_UDID --x 200 --y 400
xcodebuildmcp ui-automation type-text --simulator-id SIMULATOR_UDID --text "hello"
xcodebuildmcp ui-automation screenshot --simulator-id SIMULATOR_UDID --return-format path
```

To see all UI automation tools, view UI automation help:
```bash
xcodebuildmcp ui-automation --help
```

### macOS App Build/Run

```bash
xcodebuildmcp macos build-macos --scheme MyMacApp --project-path ./MyMacApp.xcodeproj
xcodebuildmcp macos build-run-macos --scheme MyMacApp --project-path ./MyMacApp.xcodeproj
```

To see all macOS tools, view macOS help:
```bash
xcodebuildmcp macos --help
```

### SwiftPM Package Workflows

```bash
xcodebuildmcp swift-package list --package-path ./MyPackage
xcodebuildmcp swift-package build --package-path ./MyPackage
xcodebuildmcp swift-package test --package-path ./MyPackage
```

To see all SwiftPM tools, view SwiftPM help:
```bash
xcodebuildmcp swift-package --help
```

### Project Discovery

```bash
xcodebuildmcp project-discovery discover-projs --workspace-root .
xcodebuildmcp project-discovery list-schemes --project-path ./MyApp.xcodeproj
xcodebuildmcp project-discovery get-app-bundle-id --app-path ./Build/MyApp.app
```

To see all project discovery tools, view project discovery help:
```bash
xcodebuildmcp project-discovery --help
```

### Scaffolding new projects

It's worth viewing the --help for the scaffolding tools to see the available options.
Here are some minimal examples:

```bash
xcodebuildmcp project-scaffolding scaffold-ios-project --project-name MyApp --output-path ./Projects
xcodebuildmcp project-scaffolding scaffold-macos-project --project-name MyMacApp --output-path ./Projects
```

To see all project scaffolding tools, view project scaffolding help:
```bash
xcodebuildmcp project-scaffolding --help
```

## Daemon Notes (Stateful Tools)

Stateful tools (logs, debug, video recording, background run) go through a per-workspace daemon that auto-starts, if you find you are getting errors with the stateful tools, you can manage the daemon process manually.

```bash
xcodebuildmcp daemon status
xcodebuildmcp daemon restart
```

To see all daemon commands, view daemon help:
```bash
xcodebuildmcp daemon --help
```