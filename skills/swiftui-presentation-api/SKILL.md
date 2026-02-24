---
name: swiftui-presentation-api
description: Use when presenting sheets, popovers, full screen covers, alerts, confirmation dialogs, or inspectors in SwiftUI - covers presentation detents, drag indicators, background interaction, compact adaptation, and macOS window behaviors
---

# Presentation Modifiers API Reference

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
