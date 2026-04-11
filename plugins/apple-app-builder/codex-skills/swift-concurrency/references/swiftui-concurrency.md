# SwiftUI Concurrency Patterns

SwiftUI-specific concurrency guidance. Covers where SwiftUI runs code off the main thread, Sendable closure requirements, and async work structuring.

## Main Actor Default in SwiftUI

- `View` is `@MainActor` isolated by default — `body` and members inherit isolation
- Swift 6.2 can infer `@MainActor` for all types in a module (main-actor-by-default mode)
- This aligns with UIKit/AppKit `@MainActor` APIs

## SwiftUI APIs That Run Off the Main Thread

SwiftUI may evaluate these on background threads for performance. Their closures require `Sendable`:

| API | Why Background |
|-----|---------------|
| `Shape` path generation | Geometry computation |
| `Layout` methods (`sizeThatFits`, `placeSubviews`) | Layout engine |
| `visualEffect` closures | Render-time effects |
| `onGeometryChange` closures | Geometry change callbacks |

### Unsafe Pattern

```swift
// ❌ Accessing @MainActor state from a Sendable closure
struct MyView: View {
    @State private var isExpanded = false

    var body: some View {
        Rectangle()
            .visualEffect { content, proxy in
                content.scaleEffect(isExpanded ? 1.5 : 1.0) // ❌ Data race
            }
    }
}
```

### Safe Pattern

```swift
// ✅ Capture value copy in closure capture list
struct MyView: View {
    @State private var isExpanded = false

    var body: some View {
        let expanded = isExpanded  // Value copy
        Rectangle()
            .visualEffect { content, proxy in
                content.scaleEffect(expanded ? 1.5 : 1.0) // ✅ Safe
            }
    }
}
```

**Rule:** Never send `self` or `@MainActor` state into a `Sendable` closure. Capture value copies instead.

## Structuring Async Work in SwiftUI

SwiftUI action callbacks (`Button`, `.onChange`, `.onTapGesture`) are **synchronous**. Bridge into async with `Task`:

```swift
Button("Load") {
    // This is synchronous — set loading state immediately
    isLoading = true
    Task {
        await viewModel.load()
        isLoading = false
    }
}
```

**Pattern:** Use state as the boundary. Async work updates model/state; UI reacts synchronously.

## Performance Guidance

- **Offload expensive work** from the main actor to avoid animation hitches
- **Keep synchronous:** Animations, gesture responses, layout changes
- **Offload to background:** Network calls, image processing, data parsing
- Use `@concurrent` (Swift 6.2+) or `Task.detached` for CPU-heavy work
- Separate UI code from long-running async work for responsiveness and testability
