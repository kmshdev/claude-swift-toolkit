# Workflow Hardening: Iterative Loops, Review Gates, Xcode MCP Enforcement

**Date:** 2026-03-03
**Context:** Ciphyr session `12c125ee` — SwiftData migration produced a fatal test crash that hung the MCP tool chain for 40+ minutes. Systematic debugging of the agent's decision-making revealed three architectural gaps in the toolkit.

## Problem Statement

The agent performed a SwiftData migration (Batch 6 of a code simplification pass) that introduced a `ModelContainer` ARC lifetime bug, causing all 17 tests to crash with `SwiftData/BackingData.swift:835: Fatal error: This model instance was destroyed by calling ModelContext.reset`. The crash triggered a cascade:

1. `RunAllTests` returned 4 passed / 13 `notRun` — agent misread as "still running" and retried
2. Second `RunAllTests` while Xcode locked → AbortError
3. Xcode held process locks for 40 minutes, blocking all MCP operations
4. Agent hypothesized "Keychain blocking" for 40 minutes without reading the crash log
5. When it finally ran `swift test` CLI, it diagnosed the real issue in 30 seconds

**Root causes (from decision-chain analysis):**

- **No iterative error handling in xcodebuildmcp skill.** Agent had no guidance on what `notRun` means, when to escalate to CLI, or how to recover from hung MCP tools.
- **No review gate between implementation and testing.** The Plan subagent designed a flawed architecture (ModelContext without ModelContainer retention) and no review step caught it before tests ran.
- **Xcode MCP tools not enforced as primary interface.** The toolkit suggests MCP tools but doesn't mandate them across workflow skills.

## Design

### Change 1: `xcodebuildmcp` Skill — Iterative Loops + Error Triage

**Reference:** Axiom's `axiom-xcode-mcp-tools` (33 installs, defines BuildFix/TestFix/PreviewVerify loops)

Replace the current tool catalog with workflow-driven decision trees:

#### Setup Protocol
- ALWAYS call `XcodeListWindows` first to get tab identifiers
- Cache tab mappings for the session
- Verify macOS workflow is enabled via `manage_workflows`

#### BuildFix Loop (max 5 iterations)
1. `BuildProject`
2. IF errors → `XcodeListNavigatorIssues` (structured) > `GetBuildLog` (fallback)
3. Fix via `XcodeUpdate` (not `Edit`)
4. `XcodeRefreshCodeIssuesInFile` on changed files
5. GOTO 1 (max 5, then escalate to user)

#### TestFix Loop
1. `RunAllTests` (or `RunSomeTests` for targeted iteration)
2. Parse result:
   - All passed → done
   - Some failed → read failure messages → fix → `RunSomeTests` on failures only
   - **`notRun` or `canceled`** → TEST CRASHED. Do NOT retry `RunAllTests`.
     → Immediately: `swift test 2>&1 | head -80`
     → Read the fatal error / crash log
     → Diagnose root cause → fix → rebuild → retest
   - **Progress frozen >120s** → `pkill -f "xctest"` → `swift test` CLI fallback

#### Error Triage Decision Tree
| Signal | Meaning | Action |
|--------|---------|--------|
| `notRun` | Process crash mid-suite | Get crash log via CLI immediately |
| `canceled` | Prior crash poisoned suite | Kill test process, get crash log |
| AbortError -32001 | Xcode locked from prior crash | `pkill -f "xctest"`, wait 10s, retry |
| Progress stuck >120s | Test runner hung | Kill process, use CLI |
| `isError: true` + failures | Normal test failures | Read messages, fix, RunSomeTests |

**Rule:** NEVER retry `RunAllTests` immediately after anomalous result. ALWAYS get crash log first.

#### File Operations (Xcode MCP is primary)
- `XcodeRead` (not `Read`), `XcodeUpdate` (not `Edit`), `XcodeWrite` (not `Write`)
- `XcodeGrep`/`XcodeGlob` for search, `XcodeLS` for listing
- Standard tools only in headless sessions (`claude -p` without MCP)

### Change 2: `autonomous-ui-workflow` — Mandatory Review Gate

Current flow has no review between implementation and testing:
```
Implement → Build → Test → Visual Validate
```

New flow inserts a code review checkpoint:
```
Implement → Build → REVIEW GATE → Test → Visual Validate
```

#### Review Gate Protocol
After build passes, before tests:
1. Load `code-analyzer` skill
2. Review changed files for:
   - ARC lifetime hazards (local containers, unretained references)
   - Actor isolation correctness (`@MainActor`, `Sendable`)
   - SwiftData patterns (`ModelContainer` ownership, `@Model` conformance)
   - API usage against loaded skill guidance
3. If issues found → fix → rebuild → re-review
4. If clean → proceed to TestFix Loop

**This is not optional.** The gate fires after every build pass, before any test invocation.

### Change 3: Xcode MCP Enforcement Across Workflow Skills

Skills that touch files or builds reference Xcode MCP tool names as primary:

| Skill | Change |
|-------|--------|
| `xcodebuildmcp` | Full rewrite (Change 1 above) |
| `autonomous-ui-workflow` | All file ops → XcodeUpdate/XcodeRead; build → BuildProject; test → TestFix Loop |
| `app-development-workflow` | Phase 4 (Build) references Xcode MCP as the interface |
| `swiftui-components` | Implementation examples use XcodeUpdate for modifications |
| `ios-testing` | Test execution uses TestFix Loop pattern |

**Not changed:** API reference skills, design skills, and pure reference material.

### Skill Content Enrichment (Targeted)

Two specific skill gaps surfaced by the session:

#### `ios-testing` — Add SwiftData parallel testing note
```
Swift Testing runs @Suite tests in parallel by default. If your suite creates
ModelContainer instances, either:
- Add .serialized to the @Suite: @Suite("Name", .serialized)
- Create a fresh container inside each @Test function body

ModelContainer must outlive any ModelContext derived from it — if a container
is a local variable in a helper, the context becomes invalid when the helper returns.
```

#### `swift-concurrency` — Add SwiftData thread safety note
```
@Model classes are non-Sendable by design. ModelContext is @MainActor-bound.
Do not pass @Model instances across actor boundaries. Use PersistentIdentifier
for cross-actor references, then re-fetch in the target context.
```

## Verification

1. Load the rewritten `xcodebuildmcp` skill and verify TestFix Loop coverage
2. In a Ciphyr session: trigger a deliberate test crash → verify the agent follows the Error Triage Decision Tree instead of retrying RunAllTests
3. In `autonomous-ui-workflow`: verify the review gate fires between build and test
4. Check that all workflow skills reference Xcode MCP tool names as primary

## Files to Modify

| File | Change |
|------|--------|
| `skills/xcodebuildmcp/SKILL.md` | Full rewrite with iterative loops + error triage |
| `skills/autonomous-ui-workflow/SKILL.md` | Add review gate, update file ops to XcodeUpdate |
| `skills/app-development-workflow/SKILL.md` | Phase 4 references Xcode MCP |
| `skills/ios-testing/SKILL.md` | Add SwiftData parallel testing section |
| `skills/swift-concurrency/SKILL.md` | Add SwiftData thread safety section |

## Memory Updates

Update toolkit MEMORY.md with:
- Xcode MCP tools are the primary interface for all Ciphyr-like projects
- Axiom's `axiom-xcode-mcp-tools` is the reference for iterative loop patterns
- `notRun` in Swift Testing = crash (not "still running")
- `ModelContainer` must be retained by the object that uses its `ModelContext`
