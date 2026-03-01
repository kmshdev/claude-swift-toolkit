---
name: code-analyzer
description: This skill should be used when the user asks to "review code", "analyze architecture", "assess code quality", "audit the codebase", "review PR", or needs read-only code analysis. Provides structured review checklist for organization, error handling, performance, security, and test coverage.
allowed-tools: Read, Grep, Glob
---

# Code Analyzer (Read-Only)

Structured Swift/macOS code analysis protocol. Read-only — no file modifications.

## Lifecycle Position

Phase 5 (Review). Load before `swiftui-view-refactor` for architectural overview. For deep line-by-line analysis, use `audit-context-building`.

## Analysis Protocol

### Step 1 — Map the Entry Point

1. Find the `@main` App struct or entry point
2. Identify window scenes (`WindowGroup`, `Settings`, `MenuBarExtra`)
3. Trace the root navigation structure (`NavigationSplitView`, `TabView`)

### Step 2 — Trace the Module Graph

1. List all Swift source files grouped by directory/feature
2. Identify dependencies between modules (imports, protocol conformances)
3. Map state ownership: which types own `@Observable` models, which receive them
4. Identify services/repositories and their injection pattern

### Step 3 — Identify Architecture Pattern

Classify the codebase:
- **MV (Model-View):** Views consume models directly via `@State`, `@Environment`, `@Query`
- **MVVM:** Separate ViewModel classes mediate between Model and View
- **TCA:** Reducers, Store, Actions, State
- **Hybrid:** Mix of patterns across features

Note consistency — are all features using the same pattern?

## Review Checklist

### 1. Code Organization — PASS / WARN / FAIL

| Check | What to Look For |
|-------|------------------|
| File structure | Features grouped by domain, not by type (Views/, Models/, etc.) |
| File size | Swift files under 300 lines; views under 100 lines |
| Naming | Types are nouns, methods are verbs, booleans read as questions |
| Access control | `private` by default, `internal` where needed, `public` only for API surface |
| Extensions | Used to group protocol conformances and `// MARK:` sections |

### 2. State Management — PASS / WARN / FAIL

| Check | What to Look For |
|-------|------------------|
| `@Observable` vs `ObservableObject` | New code uses `@Observable`; legacy `ObservableObject` flagged |
| `@State` visibility | All `@State` and `@StateObject` are `private` |
| Ownership | Views don't create models they should receive via injection |
| `@MainActor` | Observable classes and view models are `@MainActor` |
| Binding direction | `@Binding` only where child modifies parent state |
| Nested observables | No nested `ObservableObject` (pass directly or use `@Observable`) |

### 3. Error Handling — PASS / WARN / FAIL

| Check | What to Look For |
|-------|------------------|
| `try` without `catch` | Unhandled throws that could crash |
| Force unwrap (`!`) | Every `!` must have justification comment or precondition |
| `Result` vs throws | Consistent error propagation strategy |
| User-facing errors | Errors surfaced to UI with actionable messages |
| Network errors | Retry logic, timeout handling, offline state |

### 4. Performance — PASS / WARN / FAIL

| Check | What to Look For |
|-------|------------------|
| View body complexity | No object creation, heavy computation, or side effects in `body` |
| Lazy containers | `LazyVStack`/`LazyHStack` for lists with >20 items |
| ForEach identity | Stable `id` (never `.indices` for dynamic content) |
| `GeometryReader` | Guarded with `> 0` and `.isFinite`; prefer `containerRelativeFrame()` |
| Image loading | `AsyncImage` or downsampled thumbnails, not raw `UIImage(data:)` |
| Glass effects | Multiple glass views wrapped in `GlassEffectContainer` |

### 5. Concurrency — PASS / WARN / FAIL

| Check | What to Look For |
|-------|------------------|
| `@MainActor` | UI-bound classes and properties are main actor isolated |
| `Sendable` | Types crossing isolation boundaries conform to `Sendable` |
| `.task` modifier | Async work uses `.task {}` (auto-cancels on disappear) |
| Actor isolation | Mutable shared state protected by actors |
| Data races | No unprotected mutable state accessed from multiple contexts |

### 6. Security — PASS / WARN / FAIL

| Check | What to Look For |
|-------|------------------|
| Hardcoded secrets | No API keys, tokens, or passwords in source |
| Keychain usage | Sensitive data stored in Keychain, not UserDefaults |
| Sandbox entitlements | Minimal entitlements; no unnecessary capabilities |
| Input validation | User input validated before use |
| URL handling | External URLs validated before opening |

### 7. Test Coverage — PASS / WARN / FAIL

| Check | What to Look For |
|-------|------------------|
| Test file existence | Every feature has corresponding test file |
| Model tests | Business logic and data transformations tested |
| Edge cases | Empty states, nil values, boundary conditions covered |
| Async tests | `async` test methods with proper expectations |
| SwiftData tests | In-memory `ModelContainer` for persistence tests |

## Output Format

For each section, provide:

```
### [Section Name] — [PASS/WARN/FAIL]

**Summary:** One-line assessment.

**Findings:**
- [file_path:line] Description of issue
- [file_path:line] Description of issue

**Recommendation:** What to fix and in what order.
```

## Cross-References

- For SwiftUI-specific review, use the `swiftui-ui-patterns` review checklist
- For view structure refactoring, load `swiftui-view-refactor`
- For deep line-by-line analysis, load `audit-context-building`
