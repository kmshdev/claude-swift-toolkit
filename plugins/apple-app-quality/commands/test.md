---
description: Run unit and integration tests
allowed-tools: mcp__xcode__*, Bash(swift *), Bash(xcodebuild *), Read, Grep
---

# Run Tests

## Steps

### 1. Discover Test Targets
- If the project is open in Xcode and the official bridge is available, use
  `GetTestList` for the active scheme.
- Otherwise inspect the project with `xcodebuild -list` or look for `.testTarget`
  entries in `Package.swift`.
- If no test targets exist, suggest creating tests with the
  `apple-app-quality:ios-testing` skill.

### 2. Select the Framework
Identify which test framework the project uses:
- **Swift Testing** (`@Test`, `#expect`, `@Suite`) — preferred for new code
- **XCTest** (`XCTestCase`, `XCTAssert*`) — legacy and UI/performance coverage
- Both can coexist in the same target

### 3. Run Tests
- **Official Xcode MCP:** `RunSomeTests` for the narrowest useful slice, then
  `RunAllTests` only when broader coverage is warranted
- **Xcode CLI fallback:** `xcodebuild test -scheme <Scheme> -destination <Destination>`
- **Swift package:** `swift test` or `swift test --filter <TestName>`

### 4. Parse Results
Categorize failures:

| Category | Indicators | Action |
|----------|-----------|--------|
| Assertion | `#expect` or `XCTAssert*` failure | Check expected vs actual values |
| Timeout | test timed out | Check async fulfillment, deadlocks, or slow setup |
| Crash | `EXC_BAD_ACCESS`, `fatalError`, force-unwrap | Fix nil handling or thread-safety issues |
| Setup | missing fixture, container, or scheme issue | Verify data, mocks, and active scheme |

### 5. Report
- Show pass/fail counts per target or scheme
- For failures, include the test name, file reference, and key assertion or log message
- If all pass, confirm the targets or suites covered
