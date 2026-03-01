---
name: swift-actor-persistence
description: Thread-safe data persistence in Swift using actors — in-memory cache with file-backed storage. Use when building local storage layers, offline-first patterns, or any shared mutable state that needs both concurrency safety and disk persistence.
---

# Swift Actors for Thread-Safe Persistence

## Lifecycle Position

Phase 3 (Implement). Load when building local data storage, offline-first patterns, or caching layers. Related: `swift-concurrency` for general actor patterns, `swift-networking` for server sync.

## When to Use

- Building a local data persistence layer
- Need thread-safe access to shared mutable state with disk backing
- Want compile-time data race elimination (no manual locks or queues)
- Building offline-first apps with local storage
- Replacing legacy `DispatchQueue`-based file managers

## Core Pattern: Actor-Based Repository

The actor model guarantees serialized access — no data races, enforced by the compiler.

```swift
public actor LocalRepository<T: Codable & Identifiable> where T.ID: Hashable & Codable {
    private var cache: [T.ID: T] = [:]
    private let fileURL: URL

    public init(directory: URL = .documentsDirectory, filename: String = "data.json") {
        self.fileURL = directory.appendingPathComponent(filename)
        self.cache = Self.loadSynchronously(from: fileURL)
    }

    // MARK: - Public API

    public func save(_ item: T) throws {
        cache[item.id] = item
        try persistToFile()
    }

    public func delete(_ id: T.ID) throws {
        cache[id] = nil
        try persistToFile()
    }

    public func find(by id: T.ID) -> T? {
        cache[id]
    }

    public func loadAll() -> [T] {
        Array(cache.values)
    }

    // MARK: - Private

    private func persistToFile() throws {
        let data = try JSONEncoder().encode(Array(cache.values))
        try data.write(to: fileURL, options: .atomic)
    }

    private static func loadSynchronously(from url: URL) -> [T.ID: T] {
        guard let data = try? Data(contentsOf: url),
              let items = try? JSONDecoder().decode([T].self, from: data) else {
            return [:]
        }
        return Dictionary(uniqueKeysWithValues: items.map { ($0.id, $0) })
    }
}
```

All calls are automatically async due to actor isolation:

```swift
let repo = LocalRepository<Question>(filename: "questions.json")

let question = await repo.find(by: questionID)   // O(1) cache lookup
let all = await repo.loadAll()
try await repo.save(newQuestion)                  // updates cache + persists
try await repo.delete(questionID)
```

## Combining with @Observable ViewModel

```swift
@Observable @MainActor
final class QuestionListViewModel {
    private(set) var questions: [Question] = []
    private let repository: LocalRepository<Question>

    init(repository: LocalRepository<Question> = LocalRepository()) {
        self.repository = repository
    }

    func load() async {
        questions = await repository.loadAll()
    }

    func add(_ question: Question) async throws {
        try await repository.save(question)
        questions = await repository.loadAll()
    }

    func remove(_ id: Question.ID) async throws {
        try await repository.delete(id)
        questions = await repository.loadAll()
    }
}
```

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| Actor (not class + lock) | Compiler-enforced thread safety, zero manual synchronization |
| In-memory cache + file persistence | Fast reads from cache, durable writes to disk |
| Synchronous init loading | Avoids async initialization complexity; actor isolation not yet active during `init` |
| Dictionary keyed by ID | O(1) lookups by identifier |
| Generic over `Codable & Identifiable` | Reusable across any model type |
| Atomic file writes (`.atomic`) | Prevents partial writes on crash |

## Swift 6.2+ Considerations

### What Works Well

- **Actor isolation is fully enforced at compile time** — Swift 6 strict concurrency mode catches all data race violations. This pattern is the recommended replacement for `DispatchQueue`-based synchronization.
- **Synchronous init is safe** — Actor designated initializers can access stored properties synchronously because no other code can reference `self` until init completes. The `loadSynchronously` static method pattern is valid.
- **Generic actors** are fully supported.

### Adaptations Made (vs. Original)

1. **`@Observable @MainActor` on ViewModels** — The original used `@Observable final class` without `@MainActor`. In Swift 6 strict concurrency, ViewModels accessed from SwiftUI views must be `@MainActor`-isolated to avoid actor-boundary crossing errors.

2. **`T.ID: Hashable & Codable`** instead of `T.ID == String` — The original constrained ID to `String`. Relaxing to `Hashable & Codable` supports `UUID`, `Int`, and custom ID types used in real-world Swift apps.

### Known Trade-offs

**Synchronous file I/O inside actors:** `Data.write(to:)` and `Data(contentsOf:)` perform blocking disk I/O on the cooperative thread pool. For small files (< 1 MB) this is acceptable. For large datasets, consider:

```swift
// Option 1: Offload to a non-cooperative thread
private func persistToFile() async throws {
    let data = try JSONEncoder().encode(Array(cache.values))
    let url = fileURL
    try await Task.detached {
        try data.write(to: url, options: .atomic)
    }.value
}

// Option 2: Use SwiftData or Core Data for large datasets
// This pattern is best suited for lightweight local storage
```

**No migration support:** This is raw JSON file storage. If your model evolves, consider adding a version field:

```swift
private struct VersionedStore<T: Codable>: Codable {
    let version: Int
    let items: [T]
}
```

## Anti-Patterns

| Don't | Do Instead |
|-------|-----------|
| `DispatchQueue` or `NSLock` for thread safety | Use actors — compiler-enforced, zero runtime overhead |
| Expose the internal cache dictionary | Only expose domain operations (`save`, `find`, `loadAll`) |
| `nonisolated` to bypass actor isolation | Defeats the purpose — rethink the design |
| Call actor methods in a tight loop | Batch operations into a single actor method |
| Use for datasets > 10 MB | Switch to SwiftData, Core Data, or SQLite |

## Cross-References

- `swift-concurrency` — General actor patterns, reentrancy, `@MainActor`, GCD migration
- `swift-networking` — Async network calls that feed data into actor-based repositories
- `swift-app-lifecycle` — Scene phase changes for triggering persistence saves
