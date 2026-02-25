---
description: Run unit and integration tests
allowed-tools: mcp__xcodebuildmcp__*, Bash(swift *), Bash(xcodebuild *), Read, Grep
---

# Run Tests

## Steps

### 1. Discover Test Targets
- Check for test targets in the Xcode project: `mcp__xcodebuildmcp__list_schemes` or `xcodebuild -list`
- Look for schemes ending in `Tests` or `UITests`
- For Swift packages: check `Package.swift` for `.testTarget` entries
- If no test targets → suggest creating tests using the `ios-testing` skill

### 2. Select Framework
Identify which test framework the project uses:
- **Swift Testing** (`@Test`, `#expect`, `@Suite`) — preferred for new code
- **XCTest** (`XCTestCase`, `XCTAssert*`) — legacy but widely used
- Both can coexist in the same target
- Load `ios-testing` skill for framework patterns and best practices

### 3. Run Tests
- **Xcode project (MCP):** `mcp__xcodebuildmcp__test_sim_name_proj` with scheme and simulator
- **Xcode project (CLI):** `xcodebuild test -scheme <Scheme> -destination 'platform=iOS Simulator,name=iPhone 16'`
- **Swift package:** `swift test` (or `swift test --filter <TestName>` for specific tests)
- For focused testing: run only the test file or suite relevant to recent changes

### 4. Parse Results
Categorize failures:

| Category | Indicators | Action |
|----------|-----------|--------|
| **Assertion** | `#expect` failed, `XCTAssertEqual` mismatch | Check expected vs actual values; fix logic or update expectations |
| **Timeout** | "test timed out", "exceeded time limit" | Check for missing async fulfillment, deadlocks, or slow setup |
| **Crash** | `EXC_BAD_ACCESS`, `fatalError`, force-unwrap | Fix nil handling, check thread safety |
| **Setup** | "failed to load", "missing fixture" | Verify test data, mock configuration, `ModelContainer(for:configurations:inMemory: true)` |

### 5. Report
- Show pass/fail counts per target
- For failures: include test name, file:line reference, assertion message
- Suggest fixes based on failure category
- If all pass → confirm with target names and test count
