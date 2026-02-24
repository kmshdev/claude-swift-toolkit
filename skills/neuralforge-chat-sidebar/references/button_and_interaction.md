# Neuralforge-Chat-Sidebar - Button And Interaction

**Pages:** 3

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
timestamp: 2026-02-13T01:42:59.616Z
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

## onHover(perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/onhover(perform:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Responding to hover events

---
title: onHover(perform:)
description: Adds an action to perform when the user moves the pointer over or away from the view’s frame.
source: https://developer.apple.com/documentation/swiftui/view/onhover(perform:)
timestamp: 2026-02-13T01:41:53.109Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+

> Adds an action to perform when the user moves the pointer over or away from the view’s frame.

The action to perform whenever the pointer enters or exits this view’s frame. If the pointer is in the view’s frame, the `action` closure passes `true` as a parameter; otherwise, `false`.

A view that triggers `action` when the pointer enters or exits this view’s frame.

Calling this method defines a region for detecting pointer movement with the size and position of this view.

- [onContinuousHover(coordinateSpace:perform:)](/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:))
- [hoverEffect(_:isEnabled:)](/documentation/swiftui/view/hovereffect(_:isenabled:))
- [hoverEffectDisabled(_:)](/documentation/swiftui/view/hovereffectdisabled(_:))
- [defaultHoverEffect(_:)](/documentation/swiftui/view/defaulthovereffect(_:))
- [isHoverEffectEnabled](/documentation/swiftui/environmentvalues/ishovereffectenabled)
- [HoverPhase](/documentation/swiftui/hoverphase)
- [HoverEffectPhaseOverride](/documentation/swiftui/hovereffectphaseoverride)
- [OrnamentHoverContentEffect](/documentation/swiftui/ornamenthovercontenteffect)
- [OrnamentHoverEffect](/documentation/swiftui/ornamenthovereffect)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onHover(perform action: @escaping (Bool) -> Void) -> some View
```

---

## disabled(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/disabled(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Managing view interaction

---
title: disabled(_:)
description: Adds a condition that controls whether users can interact with this view.
source: https://developer.apple.com/documentation/swiftui/view/disabled(_:)
timestamp: 2026-02-13T01:41:51.117Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds a condition that controls whether users can interact with this view.

A Boolean value that determines whether users can interact with this view.

A view that controls whether users can interact with this view.

The higher views in a view hierarchy can override the value you set on this view. In the following example, the button isn’t interactive because the outer `disabled(_:)` modifier overrides the inner one:

- [isEnabled](/documentation/swiftui/environmentvalues/isenabled)
- [interactionActivityTrackingTag(_:)](/documentation/swiftui/view/interactionactivitytrackingtag(_:))
- [invalidatableContent(_:)](/documentation/swiftui/view/invalidatablecontent(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func disabled(_ disabled: Bool) -> some View
```

Example 2 (swift):
```swift
HStack {
    Button(Text("Press")) {}
    .disabled(false)
}
.disabled(true)
```

---
