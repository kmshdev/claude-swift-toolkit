---
name: swift-concurrency
description: Write, review, or fix Swift concurrency code using actors, async/await, and structured concurrency. Use when implementing concurrent features, resolving data race warnings, migrating from GCD, or enabling Swift 6 strict concurrency mode.
---

# Swift Concurrency

## Lifecycle Position

Phase 3 (Implement) and Phase 5 (Review). Load for async patterns during implementation; use checklist during code review. Related: `swift-networking` for async network calls.

## Decision Tree: Where Should This Code Run?

```
Is it UI code (views, view models, UI state)?
  → Yes → @MainActor
Does it manage shared mutable state?
  → Yes → Custom actor
Is it pure computation with no shared state?
  → Yes → nonisolated (or Task.detached for CPU-heavy work)
Is it a one-off async operation from synchronous code?
  → Yes → Task { } (inherits actor context)
```

## Actor Isolation

### @MainActor
```swift
// On the entire class (recommended for ViewModels)
@Observable @MainActor
class UserViewModel {
    var users: [User] = []
    var isLoading = false

    func loadUsers() async {
        isLoading = true
        defer { isLoading = false }
        users = try? await api.fetchUsers() ?? []
    }
}

// On specific methods only
class DataProcessor {
    @MainActor func updateUI(with results: [Result]) {
        // Safe to touch UI state
    }

    nonisolated func processInBackground(_ data: Data) -> [Result] {
        // Runs on any thread, no actor isolation
    }
}
```

### Custom Actors
```swift
actor ImageCache {
    private var cache: [URL: Image] = [:]

    func image(for url: URL) -> Image? {
        cache[url]
    }

    func store(_ image: Image, for url: URL) {
        cache[url] = image
    }
}

// Usage — every call crosses an isolation boundary
let cache = ImageCache()
let image = await cache.image(for: url)  // await required
```

### Actor Reentrancy
```swift
actor BankAccount {
    var balance: Decimal

    func withdraw(_ amount: Decimal) async throws {
        // WARNING: balance might change between check and deduction
        // because another task could run during the await
        guard balance >= amount else { throw BankError.insufficientFunds }

        await recordTransaction(amount)  // suspension point — other tasks can interleave

        // Re-check invariant after suspension
        guard balance >= amount else { throw BankError.insufficientFunds }
        balance -= amount
    }
}
```

**Rule:** Always re-validate state after any `await` inside an actor.

## Sendability

### Sendable Protocol
```swift
// Value types are automatically Sendable
struct UserID: Sendable { let rawValue: UUID }

// Immutable classes can be Sendable
final class Configuration: Sendable {
    let apiURL: URL        // let = immutable = safe
    let timeout: TimeInterval
}

// Mutable shared state needs an actor, not @unchecked Sendable
// AVOID unless you truly manage synchronization yourself:
final class LegacyCache: @unchecked Sendable {
    private let lock = NSLock()
    private var storage: [String: Data] = [:]
    // Must manually synchronize ALL access
}
```

### The `sending` Keyword (Swift 6)
```swift
func process(_ data: sending Data) async {
    // Compiler guarantees caller won't access data after passing it
}
```

## Structured Concurrency

### async let (parallel independent work)
```swift
async let profile = api.fetchProfile(id)
async let posts = api.fetchPosts(userId: id)
async let followers = api.fetchFollowers(userId: id)

let (p, po, f) = try await (profile, posts, followers)  // all run in parallel
```

### TaskGroup (dynamic parallel work)
```swift
let images = try await withThrowingTaskGroup(of: (URL, Image).self) { group in
    for url in urls {
        group.addTask {
            let image = try await downloadImage(from: url)
            return (url, image)
        }
    }
    var results: [URL: Image] = [:]
    for try await (url, image) in group {
        results[url] = image
    }
    return results
}
```

### Cancellation
```swift
func processLargeDataset(_ items: [Item]) async throws {
    for item in items {
        try Task.checkCancellation()  // Throws if cancelled
        await process(item)
    }
}

// Or check without throwing
if Task.isCancelled { return }
```

## Unstructured Tasks

```swift
// Task { } — inherits current actor context
@MainActor class ViewModel {
    func start() {
        Task {
            // This runs on MainActor (inherited)
            await loadData()
        }
    }
}

// Task.detached { } — no actor inheritance, runs on global executor
Task.detached(priority: .background) {
    // This does NOT run on MainActor
    let result = heavyComputation(data)
    await MainActor.run { self.updateUI(result) }
}
```

**When to use each:**
- `Task { }` — 90% of cases. Starting async work from sync context.
- `Task.detached { }` — CPU-heavy work that must NOT run on MainActor.

## Migration from GCD

| GCD Pattern | Modern Equivalent |
|-------------|-------------------|
| `DispatchQueue.main.async { }` | `@MainActor` or `MainActor.run { }` |
| `DispatchQueue.global().async { }` | `Task.detached { }` or `nonisolated` method |
| `DispatchGroup` | `TaskGroup` or `async let` |
| `DispatchSemaphore` | Actor isolation (semaphores + async = deadlock risk) |
| `DispatchQueue` (serial, for sync) | Actor |
| Completion handler | `async throws ->` return value |

### Bridging Completion Handlers
```swift
func legacyFetch(completion: @escaping (Result<Data, Error>) -> Void) { /* ... */ }

// Wrap with continuation
func modernFetch() async throws -> Data {
    try await withCheckedThrowingContinuation { continuation in
        legacyFetch { result in
            continuation.resume(with: result)  // MUST be called exactly once
        }
    }
}
```

## Swift 6 Strict Concurrency

### Incremental Adoption
```swift
// Enable per-target in Package.swift
.target(name: "MyApp", swiftSettings: [.swiftLanguageMode(.v6)])

// Or per-file: suppress specific warnings during migration
@preconcurrency import SomeOldLibrary
```

### Common Warnings and Fixes

| Warning | Fix |
|---------|-----|
| "Sending 'value' risks data race" | Make type `Sendable` or use `sending` parameter |
| "Non-sendable type captured by @Sendable closure" | Move to actor-isolated method or make type Sendable |
| "Actor-isolated property cannot be mutated from nonisolated context" | Add `await` or annotate caller with same actor |
| "Global variable is not concurrency-safe" | Make it `let`, move to actor, or use `nonisolated(unsafe)` (last resort) |

## Common Patterns

### Actor-Isolated Repository
```swift
actor UserRepository {
    private let api: any APIClientProtocol
    private var cache: [UserID: User] = [:]

    func user(_ id: UserID) async throws -> User {
        if let cached = cache[id] { return cached }
        let user: User = try await api.request("/users/\(id.rawValue)")
        cache[id] = user
        return user
    }
}
```

### .task Modifier for View Lifecycle
```swift
struct UserView: View {
    @State private var viewModel = UserViewModel()

    var body: some View {
        content
            .task { await viewModel.load() }          // auto-cancels on disappear
            .task(id: selectedID) { await viewModel.load(selectedID) }  // re-runs when ID changes
    }
}
```

## Review Checklist

- [ ] No data races: mutable shared state in actors or protected by isolation
- [ ] Actor isolation boundaries clearly documented (which actor owns which state)
- [ ] Cancellation cooperative: long operations check `Task.checkCancellation()`
- [ ] `Task` references stored for cleanup if not using `.task` modifier
- [ ] `.task` modifier used for view lifecycle async work (not `onAppear { Task { } }`)
- [ ] `@MainActor` on view models and UI state classes
- [ ] No `DispatchSemaphore` mixed with async code (deadlock risk)
- [ ] `withCheckedContinuation` resumes exactly once (not zero, not twice)
- [ ] State re-validated after suspension points in actors (reentrancy)
- [ ] `@unchecked Sendable` justified in comment if used

## Cross-References

- `swift-networking` — async/await network patterns
- `swiftui-expert-skill` — `.task` modifier, `@MainActor` ViewModel pattern, `Sendable` checks
- `ios-testing` — testing async code with Swift Testing (`#expect` with `await`)
- `code-analyzer` — concurrency safety review section
