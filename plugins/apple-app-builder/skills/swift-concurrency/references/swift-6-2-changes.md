# Swift 6.2 Approachable Concurrency

Swift 6.2 changes the concurrency philosophy: **stay single-threaded by default until you choose to introduce parallelism.** Async functions no longer hop to the global concurrent executor — they stay on the calling actor.

## The Key Behavioral Change

**Before (Swift 6.0/6.1):** Calling an async function from `@MainActor` code could offload the call to a background thread, causing data race errors for non-Sendable types.

```swift
// Swift 6.0/6.1 — ERROR: Sending 'self.photoProcessor' risks causing data races
@MainActor
final class StickerModel {
    let photoProcessor = PhotoProcessor()

    func extractSticker(_ item: PhotosPickerItem) async throws -> Sticker? {
        let data = try await item.loadTransferable(type: Data.self)
        return await photoProcessor.extractSticker(data: data!) // ❌ Error
    }
}
```

**After (Swift 6.2):** The async function stays on the caller's actor. No data race, no error.

```swift
// Swift 6.2 — No error. extractSticker stays on MainActor.
@MainActor
final class StickerModel {
    let photoProcessor = PhotoProcessor()

    func extractSticker(_ item: PhotosPickerItem) async throws -> Sticker? {
        let data = try await item.loadTransferable(type: Data.self)
        return await photoProcessor.extractSticker(data: data!) // ✅ OK
    }
}
```

## Isolated Conformances

Protocol conformances can now be actor-isolated. This eliminates the common workaround of marking everything `nonisolated` to satisfy conformances.

```swift
protocol Exportable {
    func export()
}

// Swift 6.2: Isolated conformance — safe because compiler ensures
// this conformance is only used on the main actor
extension StickerModel: @MainActor Exportable {
    func export() {
        photoProcessor.exportAsPNG() // ✅ Can access MainActor state
    }
}
```

The compiler enforces safety — using the conformance from a nonisolated context produces an error:

```swift
nonisolated struct ImageExporter {
    var items: [any Exportable]

    mutating func add(_ item: StickerModel) {
        items.append(item) // ❌ Error: Main actor-isolated conformance cannot be used in nonisolated context
    }
}
```

## Main-Actor-by-Default Module Mode

An opt-in build setting that makes all types in a target implicitly `@MainActor`:

```swift
// With main-actor-by-default enabled, no @MainActor annotations needed:
final class StickerLibrary {
    static let shared: StickerLibrary = .init()  // Implicitly @MainActor
}

final class StickerModel {
    let photoProcessor: PhotoProcessor  // Implicitly @MainActor
    var selection: [PhotosPickerItem]
}
```

**Enable in Xcode:** Swift Compiler → Concurrency → Default Actor Isolation
**Enable in SwiftPM:** `swiftSettings: [.defaultIsolation(MainActor.self)]`

**Recommended for:** Apps, scripts, and executable targets.
**Not recommended for:** Libraries (would force `@MainActor` on consumers).

## `@concurrent` — Explicit Background Work

When you need to offload work to the concurrent thread pool, use `@concurrent` instead of `Task.detached`:

```swift
nonisolated struct PhotoProcessor {
    @concurrent
    func process(data: Data) async -> ProcessedPhoto? {
        // Runs on concurrent pool, not the calling actor
    }
}

// Caller
processedPhotos[item.id] = await PhotoProcessor().process(data: data)
```

**Pattern:** `nonisolated` type + `@concurrent` async function = explicit background work.

| Approach | When to Use |
|----------|------------|
| `@concurrent` function | Preferred. Explicit, typed, composable |
| `Task.detached { }` | Legacy. Breaks actor inheritance, harder to reason about |
| `Task { }` | Default. Inherits calling actor (stays on MainActor in 6.2) |

## Detecting Approachable Concurrency Mode

Before diagnosing concurrency errors, check the project's settings:

1. **Xcode:** Build Settings → Swift Compiler → Concurrency
   - Swift Language Version (must be 6.2+)
   - Default Actor Isolation / Main Actor by Default
   - Strict Concurrency Checking level
2. **SwiftPM:** Inspect `Package.swift` for `swiftSettings`
3. **Migration tooling:** swift.org/migration

## Keywords Reference

| Keyword | What It Does |
|---------|-------------|
| `async` | Function can pause |
| `await` | Pause here until done |
| `Task { }` | Start async work, inherits actor context |
| `Task.detached { }` | Start async work, no inherited context |
| `@MainActor` | Runs on main thread |
| `actor` | Type with isolated mutable state |
| `nonisolated` | Opts out of actor isolation |
| `Sendable` | Safe to pass between isolation domains |
| `@concurrent` | Always run on background (Swift 6.2+) |
| `async let` | Start parallel work |
| `TaskGroup` | Dynamic parallel work |
