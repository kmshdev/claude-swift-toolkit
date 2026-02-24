# Sidebar-Liquid-Glass-Clone - Interaction And Feedback

**Pages:** 1

---

## sensoryFeedback(_:trigger:)

**URL:** https://sosumi.ai/documentation/swiftui/view/sensoryFeedback(_:trigger:)?.md

**Contents:**
- Parameters
- Discussion
- Providing haptic feedback

---
title: sensoryFeedback(_:trigger:)
description: Plays the specified  when the provided  value changes.
source: https://developer.apple.com/documentation/swiftui/view/sensoryFeedback(_:trigger:)
timestamp: 2026-02-13T01:05:57.611Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+

> Plays the specified  when the provided  value changes.

Which type of feedback to play.

A value to monitor for changes to determine when to play.

For example, you could play feedback when a state value changes:

- [sensoryFeedback(trigger:_:)](/documentation/swiftui/view/sensoryfeedback(trigger:_:))
- [sensoryFeedback(_:trigger:condition:)](/documentation/swiftui/view/sensoryfeedback(_:trigger:condition:))
- [SensoryFeedback](/documentation/swiftui/sensoryfeedback)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func sensoryFeedback<T>(_ feedback: SensoryFeedback, trigger: T) -> some View where T : Equatable
```

Example 2 (swift):
```swift
struct MyView: View {
    @State private var showAccessory = false

    var body: some View {
        ContentView()
            .sensoryFeedback(.selection, trigger: showAccessory)
            .onLongPressGesture {
                showAccessory.toggle()
            }

        if showAccessory {
            AccessoryView()
        }
    }
}
```

---
