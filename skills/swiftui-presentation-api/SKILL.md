---
name: swiftui-presentation-api
description: This skill should be used when the user asks to "present sheet", "show popover", "create alert", "add confirmation dialog", "configure presentation", or needs SwiftUI presentation API reference. Provides sheet, popover, fullScreenCover, alert, confirmation dialog, inspector modifiers, and macOS window behaviors.
---

# Presentation Modifiers API Reference

## Lifecycle Position

Phase 3 API Reference — load during implementation when presenting sheets, alerts, popovers, or inspectors. Dispatched from `autonomous-ui-workflow` Phase 2 research table.

## Sheet / Cover / Popover

```swift
.sheet(isPresented: $show) { Content() }
.sheet(item: $item) { item in Detail(item: item) }
.fullScreenCover(isPresented: $show) { Content() }
.popover(isPresented: $show, arrowEdge: .top) { Content() }
```

## Sheet Configuration

| Modifier | Purpose |
|----------|---------|
| `.presentationDetents([.medium, .large])` | Available heights |
| `.presentationDetents(_:selection:)` | Programmatic height control |
| `.presentationDragIndicator(_:)` | Show/hide drag handle |
| `.presentationBackground(_:)` | Custom background style |
| `.presentationCornerRadius(_:)` | Corner radius |
| `.presentationSizing(_:)` | Size control |
| `.interactiveDismissDisabled()` | Prevent swipe dismiss |
| `.presentationBackgroundInteraction(_:)` | Interact behind sheet |
| `.presentationCompactAdaptation(_:)` | Adapt for compact: `.sheet`, `.popover`, `.fullScreenCover` |

## Alerts

```swift
.alert("Title", isPresented: $show) {
    Button("OK") { }
} message: {
    Text("Description")
}

.alert("Save Failed", isPresented: $didError, presenting: details) { d in
    Button(role: .destructive) { } label: { Text("Delete \(d.name)") }
    Button("Retry") { }
} message: { d in Text(d.error) }
```

Rules: All actions dismiss. System may reorder by role. No actions = "OK" added.

## Confirmation Dialog

```swift
.confirmationDialog("Delete?", isPresented: $show) {
    Button("Delete", role: .destructive) { delete() }
    Button("Cancel", role: .cancel) { }
}
```

## Inspector

```swift
.inspector(isPresented: $showInspector) { InspectorContent() }
```

## macOS Window Behaviors

```swift
.windowFullScreenBehavior(.disabled)
.windowMinimizeBehavior(.disabled)
.windowDismissBehavior(.disabled)
.windowToolbarFullScreenVisibility(.visible)
```

## When to Use Which

| Need | Use |
|------|-----|
| Detail view with dismiss | `.sheet(item:) { item in DetailView(item) }` |
| Confirmation before destructive action | `.confirmationDialog("Delete?", isPresented:)` |
| Simple alert with message | `.alert("Title", isPresented:) { } message: { }` |
| Contextual popover | `.popover(isPresented:) { }` |
| Side panel on iPad/Mac | `.inspector(isPresented:)` |
| Bottom sheet with drag | `.sheet` + `.presentationDetents([.medium, .large])` |
| Full screen takeover | `.fullScreenCover(item:)` |

## Sheet Best Practices

```swift
// PREFER: model-based presentation (no stale data)
.sheet(item: $selectedItem) { item in
    DetailView(item: item)
}

// AVOID: boolean presentation (can show stale data)
.sheet(isPresented: $showDetail) {
    DetailView(item: selectedItem) // selectedItem might be stale
}

// Sheets own their dismissal
struct DetailView: View {
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            content
                .toolbar {
                    ToolbarItem(placement: .cancellationAction) {
                        Button("Cancel") { dismiss() }
                    }
                }
        }
    }
}

// Programmatic detent control
@State private var detent: PresentationDetent = .medium
.sheet(isPresented: $show) {
    SheetContent()
        .presentationDetents([.medium, .large], selection: $detent)
}
```

## macOS Window Presentation

```swift
// New window (macOS)
@Environment(\.openWindow) private var openWindow
Button("Open") { openWindow(id: "detail") }

// Inspector panel (macOS/iPadOS)
.inspector(isPresented: $showInspector) {
    InspectorView()
        .inspectorColumnWidth(min: 200, ideal: 300, max: 400)
}
```

## Common Mistakes

1. `.sheet(isPresented:)` with stale captured data — use `.sheet(item:)` for model-based presentation
2. Missing `@Environment(\.dismiss)` — sheets should dismiss themselves, not rely on parent state
3. Nested sheets (sheet presenting another sheet) — breaks on some OS versions. Use NavigationStack inside the sheet instead
4. Missing `NavigationStack` inside sheets — no toolbar placement support without it
5. `.popover` without `.presentationCompactAdaptation(.sheet)` — on iPhone, popovers become sheets by default but may need explicit control

## Checklist

- [ ] Using `.sheet(item:)` over `.sheet(isPresented:)` for data-driven presentation
- [ ] Sheets contain their own `NavigationStack` for toolbar support
- [ ] Sheets use `@Environment(\.dismiss)` for self-dismissal
- [ ] Confirmation dialogs used for destructive actions (not alerts)
- [ ] `.presentationDetents` specified when bottom sheet behavior is needed
- [ ] macOS inspectors use `.inspectorColumnWidth()` for sizing

## Cross-References

- `swiftui-input-api` — forms presented inside sheets
- `swiftui-ui-patterns` — sheet/navigation patterns in review checklist
- `swiftui-material-api` — material backgrounds in presented content
