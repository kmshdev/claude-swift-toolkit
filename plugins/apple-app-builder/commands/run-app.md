---
description: Build the app and launch what the current official tool surface can support
allowed-tools: mcp__xcode__*, Bash(swift *), Bash(xcodebuild *), Bash(open *), Bash(find *)
---

# Build and Run

## Steps

### 1. Build First
- Run the `/build` workflow to compile the project.
- If the build fails, stop and suggest `/fix-build`.

### 2. Detect the Platform
- macOS targets can be opened directly once built.
- iOS and iPadOS targets can be built here, but this toolkit no longer bundles
  simulator launch automation.

### 3. Launch What Is Supported
- **macOS:** locate the built `.app` bundle in DerivedData and open it.
- **iOS / iPadOS:** report a successful build and tell the user to run the
  active scheme from Xcode. Do not claim simulator launch support.
- **Swift package executables:** run the built executable if the package defines
  one and the user asked for it explicitly.

### 4. Report
- On macOS, report the app path you launched.
- On iOS or iPadOS, report that the build succeeded and the next step is to run
  from Xcode.
