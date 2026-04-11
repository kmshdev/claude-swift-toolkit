---
description: Diagnose and fix build errors systematically
allowed-tools: mcp__xcode__*, Read, Write, Edit, Bash(swift *), Bash(xcodebuild *), Grep
---

# Fix Build Errors

## Steps

### 1. Get Fresh Errors
- Run a fresh build rather than trusting stale diagnostics.
- Prefer `BuildProject` plus `GetBuildLog` when the official Xcode MCP bridge is
  available.
- Otherwise use `xcodebuild build` with the same project, workspace, scheme,
  and destination as `/build`.

### 2. Categorize Errors
Read each error and classify it before editing:

**Package Resolution**
- Missing or incompatible dependencies
- Fix package issues before touching application code

**Swift Compiler**
- Type mismatches, missing imports, unavailable APIs, macro or preview errors
- Fix the smallest upstream type or availability issue first

**Linker**
- Undefined symbols, missing frameworks, missing target membership
- Check target linkage and build settings

**Code Signing**
- Missing team, provisioning profile, or entitlement mismatch
- Verify signing configuration before retrying

### 3. Fix Errors
- Prefer `XcodeUpdate` or `XcodeWrite` when working through the MCP bridge.
- Otherwise edit files directly and keep changes minimal.
- Re-run `XcodeRefreshCodeIssuesInFile` on touched files when that tool is
  available.

### 4. Verify
- Rebuild after each focused fix.
- Stop after 3 fix/rebuild cycles and report the remaining blockers if the
  build is still red.
