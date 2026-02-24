---
name: ios-testing
description: This skill should be used when the user asks to "write tests", "add unit tests", "implement UI tests", "analyze test coverage", "use XCTest", "test SwiftUI views", or needs iOS/macOS testing guidance. Provides testing strategies, TDD patterns, and XCTest/Swift Testing framework usage.
allowed-tools: Read, Grep, Glob, mcp__xcodebuildmcp__test_*
---

# iOS Testing Expert

## Instructions
1. Analyze test coverage by examining existing test files and coverage reports
2. Identify untested code paths through static analysis
3. Generate comprehensive test cases covering edge cases and error paths
4. Use XCTest and Swift Testing frameworks for implementation

## Best Practices
- Focus tests on behavior, not implementation details
- Use dependency injection to enable testability
- Mock external dependencies to isolate units under test
- Target 80%+ code coverage for critical paths