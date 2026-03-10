# GCD to Swift Concurrency Migration Guide

## Step-by-Step Migration

### Phase 1: Enable Warnings
Add to build settings: `SWIFT_STRICT_CONCURRENCY = targeted` (or `complete` for Swift 6 preview)

### Phase 2: Convert Completion Handlers
```swift
// Before
func fetchUser(id: String, completion: @escaping (User?, Error?) -> Void) {
    URLSession.shared.dataTask(with: url) { data, _, error in
        // ...
    }.resume()
}

// After
func fetchUser(id: String) async throws -> User {
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}
```

### Phase 3: Replace GCD Queues with Actors
```swift
// Before
class Cache {
    private let queue = DispatchQueue(label: "cache", attributes: .concurrent)
    private var storage: [String: Data] = [:]

    func get(_ key: String) -> Data? {
        queue.sync { storage[key] }
    }
    func set(_ key: String, value: Data) {
        queue.async(flags: .barrier) { self.storage[key] = value }
    }
}

// After
actor Cache {
    private var storage: [String: Data] = [:]

    func get(_ key: String) -> Data? { storage[key] }
    func set(_ key: String, value: Data) { storage[key] = value }
}
```

### Phase 4: Annotate UI Code
- Add `@MainActor` to view models and UI state
- Add `@MainActor` to delegate methods that update UI
- Use `nonisolated` for methods that don't need MainActor

### Phase 5: Enable Swift 6
- Set `.swiftLanguageMode(.v6)` per target
- Fix remaining warnings (usually Sendable conformances)
- Use `@preconcurrency import` for third-party libraries not yet updated
