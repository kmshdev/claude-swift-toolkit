# Workflow Hardening Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Harden the toolkit's workflow skills to prevent the Ciphyr session failure cascade — iterative build/test loops, mandatory review gates, Xcode MCP enforcement, and targeted SwiftData safety knowledge.

**Architecture:** Rewrite `xcodebuildmcp` skill with Axiom-style iterative loops and error triage. Insert a review gate into `autonomous-ui-workflow` between build and test. Add SwiftData concurrency/testing notes to `swift-concurrency` and `ios-testing`. Update `app-development-workflow` Phase 4 to reference Xcode MCP as primary interface.

**Tech Stack:** Skill markdown files (SKILL.md), no code changes.

---

### Task 1: Rewrite `xcodebuildmcp/SKILL.md` with Iterative Loops

**Files:**
- Modify: `skills/xcodebuildmcp/SKILL.md`

**Step 1: Read the current skill file**

Read `skills/xcodebuildmcp/SKILL.md` to confirm current state (199 lines, pure tool catalog).

**Step 2: Replace the entire SKILL.md content**

Keep the frontmatter unchanged. Replace the body with this structure:

```markdown
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

<collapsed: Full tool list — expand only when needed>

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

</collapsed>
```

**Step 3: Verify the file is valid markdown**

Read the file back and confirm frontmatter is intact, sections render correctly.

**Step 4: Commit**

```bash
git add skills/xcodebuildmcp/SKILL.md
git commit -m "feat(xcodebuildmcp): rewrite with iterative loops and error triage

Replace tool catalog with workflow-driven decision trees: BuildFix Loop,
TestFix Loop, Error Triage Decision Tree, Xcode MCP as primary file
interface. Modeled on Axiom's axiom-xcode-mcp-tools patterns."
```

---

### Task 2: Add Review Gate to `autonomous-ui-workflow/SKILL.md`

**Files:**
- Modify: `skills/autonomous-ui-workflow/SKILL.md`

**Step 1: Read the current file**

Read `skills/autonomous-ui-workflow/SKILL.md` to confirm current state.

**Step 2: Insert review gate between Phase 5 (Build) and Phase 6 (Preview)**

After the current "Phase 5: Build" section (line 79-87), insert a new section:

```markdown
## Phase 5b: Review Gate (Before Testing)

After build passes, BEFORE running any tests:

1. Load `code-analyzer` skill
2. Review all changed files for:
   - ARC lifetime hazards (local containers passed as references that outlive their scope)
   - Actor isolation correctness (`@MainActor`, `Sendable` conformance)
   - SwiftData patterns (`ModelContainer` must be retained by the owner of `ModelContext`)
   - Consistency with project patterns (check CLAUDE.md)
3. If issues found → fix → rebuild (BuildFix Loop) → re-review
4. If clean → proceed to Preview/Test

This gate is mandatory. It catches architectural bugs before they reach the test runner and cause MCP tool hangs.
```

**Step 3: Update Phase 5 Build section to reference BuildFix Loop**

Replace line 85-87:
```
Or via Xcode MCP: `BuildProject`

If build fails → read errors → fix → rebuild. Do NOT claim success without build evidence.
```

With:
```
Via Xcode MCP: follow the **BuildFix Loop** from the `xcodebuildmcp` skill.

If build fails → `XcodeListNavigatorIssues` → fix via `XcodeUpdate` → rebuild (max 5 iterations).
Do NOT claim success without build evidence.
```

**Step 4: Update The Loop diagram at line 33**

Replace:
```
Spec → Research → Design → Implement → Build → Preview → Validate → Iterate
```

With:
```
Spec → Research → Design → Implement → Build → Review Gate → Preview → Validate → Iterate
```

**Step 5: Update file operation references to Xcode MCP**

In Phase 4 (Implement, line 73-77), add after "Follow project conventions":
```
Use Xcode MCP tools as primary file interface when available: `XcodeUpdate` for edits, `XcodeRead` for reading, `XcodeWrite` for new files. See `xcodebuildmcp` skill for the full tool mapping.
```

**Step 6: Commit**

```bash
git add skills/autonomous-ui-workflow/SKILL.md
git commit -m "feat(autonomous-ui-workflow): add review gate before testing

Insert mandatory review checkpoint between build and test phases.
Reference BuildFix Loop from xcodebuildmcp skill. Update file ops
to use Xcode MCP as primary interface."
```

---

### Task 3: Add SwiftData Parallel Testing Safety to `ios-testing/SKILL.md`

**Files:**
- Modify: `skills/ios-testing/SKILL.md`

**Step 1: Read the current file**

Read `skills/ios-testing/SKILL.md` to confirm current state (260 lines).

**Step 2: Insert SwiftData testing safety section after "Testing SwiftData Models" (after line 191)**

After the cascading delete example, add:

```markdown
### SwiftData Testing Safety

Swift Testing runs `@Suite` tests **in parallel by default**. This causes crashes with SwiftData:

**The Problem:** Multiple tests creating separate in-memory `ModelContainer` instances simultaneously leads to Core Data coordinator conflicts → `Fatal error: This model instance was destroyed by calling ModelContext.reset`.

**Two Safe Patterns:**

**Option 1 — Serialize the suite (recommended when tests share setup patterns):**
```swift
@MainActor
@Suite("MyModel Tests", .serialized)  // Forces sequential execution
struct MyModelTests {
    private func makeContainer() throws -> ModelContainer {
        let config = ModelConfiguration(isStoredInMemoryOnly: true)
        return try ModelContainer(for: MyModel.self, configurations: config)
    }

    @Test("insert persists")
    func insert() throws {
        let container = try makeContainer()
        let context = container.mainContext
        // container stays alive for the duration of this test
        // ...
    }
}
```

**Option 2 — Fresh container per test (safe without `.serialized`):**
```swift
@Test("insert persists")
func insert() throws {
    let config = ModelConfiguration(isStoredInMemoryOnly: true)
    let container = try ModelContainer(for: MyModel.self, configurations: config)
    let context = container.mainContext
    // container is local to this test — no cross-test interference
    // ...
}
```

**Critical Rule:** `ModelContainer` must outlive any `ModelContext` or `@Model` objects derived from it. If a helper function creates a container and returns only a context or a model object, the container is ARC-deallocated when the helper returns — and all model instances become invalid.

```swift
// WRONG — container dies when helper returns
func makeContext() throws -> ModelContext {
    let container = try ModelContainer(...)  // local → deallocated on return
    return container.mainContext  // orphaned context
}

// RIGHT — return the container (or have the owner retain it)
func makeContainer() throws -> ModelContainer {
    return try ModelContainer(for: MyModel.self,
        configurations: ModelConfiguration(isStoredInMemoryOnly: true))
}
```
```

**Step 3: Update the checklist (around line 248)**

After the existing item `- [ ] SwiftData tests use isStoredInMemoryOnly: true`, add:
```
- [ ] SwiftData test suites use `.serialized` or create fresh containers per `@Test`
- [ ] `ModelContainer` is retained for the lifetime of any `ModelContext` using it
```

**Step 4: Commit**

```bash
git add skills/ios-testing/SKILL.md
git commit -m "feat(ios-testing): add SwiftData parallel testing safety patterns

Add .serialized trait guidance, ModelContainer lifetime rules, and
safe vs unsafe helper patterns. Prevents the fatal crash from
parallel test execution with in-memory SwiftData containers."
```

---

### Task 4: Add SwiftData Thread Safety to `swift-concurrency/SKILL.md`

**Files:**
- Modify: `skills/swift-concurrency/SKILL.md`

**Step 1: Read the full file**

Read `skills/swift-concurrency/SKILL.md` to find the best insertion point.

**Step 2: Add a SwiftData Concurrency section**

Insert after the Actor Isolation section (after the `@MainActor` patterns), before Sendable:

```markdown
## SwiftData Concurrency

`@Model` classes have specific concurrency constraints enforced by Swift 6:

- **`@Model` is non-Sendable** — do not pass model instances across actor boundaries
- **`ModelContext` is `@MainActor`-bound** — create and use on the main actor
- **`ModelContainer` is Sendable** — safe to pass between actors

### Cross-Actor Access Pattern

```swift
// WRONG — passing @Model across actors
let item = context.fetch(...)  // on MainActor
await backgroundActor.process(item)  // non-Sendable error

// RIGHT — pass the identifier, re-fetch on the other side
let itemID = item.persistentModelID
await backgroundActor.process(itemID, container: container)

// In the background actor:
let bgContext = ModelContext(container)
let item = bgContext.model(for: itemID) as? Item
```

### Testing Implications

When writing tests for `@Observable @MainActor` models that use SwiftData:
- Test suites must be `@MainActor` (matches the model's isolation)
- Use `.serialized` on `@Suite` to prevent parallel container conflicts
- See `ios-testing` skill for complete SwiftData testing patterns
```

**Step 3: Commit**

```bash
git add skills/swift-concurrency/SKILL.md
git commit -m "feat(swift-concurrency): add SwiftData thread safety patterns

Add @Model non-Sendable rules, ModelContext actor binding, cross-actor
access via PersistentIdentifier, and testing implications."
```

---

### Task 5: Update `app-development-workflow/SKILL.md` Phase 4

**Files:**
- Modify: `skills/app-development-workflow/SKILL.md`

**Step 1: Read the Phase 4 section of the file**

Find the Phase 4 (Build) section.

**Step 2: Add Xcode MCP as primary interface reference**

In Phase 4, add after the existing build instructions:

```markdown
**Xcode MCP (Primary Interface):**
When XcodeBuildMCP MCP server is available, it is the primary interface for ALL file operations, builds, and tests. Load the `xcodebuildmcp` skill for:
- File ops: `XcodeRead`/`XcodeUpdate`/`XcodeWrite` (not `Read`/`Edit`/`Write`)
- Build: **BuildFix Loop** (max 5 iterations with Issue Navigator diagnostics)
- Test: **TestFix Loop** (with crash detection and CLI fallback)
- Preview: `RenderPreview` for visual verification
```

**Step 3: Commit**

```bash
git add skills/app-development-workflow/SKILL.md
git commit -m "feat(app-development-workflow): reference Xcode MCP as primary in Phase 4

Direct agents to load xcodebuildmcp skill and use BuildFix/TestFix
loops as the standard build/test workflow."
```

---

### Task 6: Verify all changes

**Step 1: Count skill sizes**

Verify each modified skill has valid frontmatter and reasonable size.

**Step 2: Run a quick grep to confirm key terms appear**

```bash
grep -l "BuildFix Loop" skills/*/SKILL.md
# Expected: xcodebuildmcp, autonomous-ui-workflow, app-development-workflow

grep -l "\.serialized" skills/*/SKILL.md
# Expected: ios-testing, swift-concurrency

grep -l "Review Gate" skills/*/SKILL.md
# Expected: autonomous-ui-workflow

grep -l "XcodeUpdate" skills/*/SKILL.md
# Expected: xcodebuildmcp, autonomous-ui-workflow
```

**Step 3: Final commit with version bump if desired**

```bash
git log --oneline -6  # verify all 5 task commits are clean
```
