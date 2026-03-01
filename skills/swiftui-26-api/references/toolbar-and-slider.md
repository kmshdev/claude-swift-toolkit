# Toolbar and Slider APIs
ToolbarSpacer for toolbar layout spacing and Slider with tick mark support.

## Table of Contents
- [ToolbarSpacer](#toolbarspacer)
- [Slider](#slider)

## ToolbarSpacer

**URL:** https://sosumi.ai/documentation/SwiftUI/ToolbarSpacer?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Populating a toolbar

**Navigation:** [SwiftUI](/documentation/SwiftUI)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+

A space item creates visual breaks in the toolbar between items. Spacers can have a standard fixed size or be flexible and push items apart.

Spacers can also be used in customizable toolbars:

Space items are customizable and can be added, removed, and rearranged by users. If a customizable toolbar supports a spacer of a given type, users can also add in multiple copies of that spacer from the customization panel.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ToolbarSpacer
```

Example 2 (swift):
```swift
ContentView()
    .toolbar(id: "main-toolbar") {
        ToolbarItem(id: "tag") {
           TagButton()
        }
        ToolbarItem(id: "share") {
           ShareButton()
        }
        ToolbarSpacer(.fixed)
        ToolbarItem(id: "more") {
           MoreButton()
        }
    }
```

---

## Slider

**URL:** https://sosumi.ai/documentation/SwiftUI/Slider?.md

**Contents:**
- Overview
- Conforms To
- Creating a slider
- Creating a slider with labels
- Adding ticks to a slider
- Deprecated initializers
- Initializers
- Getting numeric inputs

**Navigation:** [SwiftUI](/documentation/SwiftUI)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 6.0+

A slider consists of a "thumb" image that the user moves between two extremes of a linear "track". The ends of the track represent the minimum and maximum possible values. As the user moves the thumb, the slider updates its bound value.

The following example shows a slider bound to the value `speed`. As the slider updates this value, a bound [Text](/documentation/swiftui/text) view shows the value updating. The `onEditingChanged` closure passed to the slider receives callbacks when the user drags the slider. The example uses this to change the color of the value text.

![An unlabeled slider, with its thumb about one third of the way from the](https://docs-assets.developer.apple.com/published/9a41fa64a088c04aef5d52935a5b4308/SwiftUI-Slider-simple%402x.png)

You can also use a `step` parameter to provide incremental steps along the path of the slider. For example, if you have a slider with a range of `0` to `100`, and you set the `step` value to `5`, the slider's increments would be `0`, `5`, `10`, and so on. The following example shows this approach, and also adds optional minimum and maximum value labels.

![A slider with labels show minimum and maximum values of 0 and 100,](https://docs-assets.developer.apple.com/published/391df10be6d7d1c252c6d81c8ca0b440/SwiftUI-Slider-withStepAndLabels%402x.png)

The slider also uses the `step` to increase or decrease the value when a VoiceOver user adjusts the slider with voice commands.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Slider<Label, ValueLabel> where Label : View, ValueLabel : View
```

Example 2 (swift):
```swift
@State private var speed = 50.0
@State private var isEditing = false

var body: some View {
    VStack {
        Slider(
            value: $speed,
            in: 0...100,
            onEditingChanged: { editing in
                isEditing = editing
            }
        )
        Text("\(speed)")
            .foregroundColor(isEditing ? .red : .blue)
    }
}
```

Example 3 (swift):
```swift
@State private var speed = 50.0
@State private var isEditing = false

var body: some View {
    Slider(
        value: $speed,
        in: 0...100,
        step: 5
    ) {
        Text("Speed")
    } minimumValueLabel: {
        Text("0")
    } maximumValueLabel: {
        Text("100")
    } onEditingChanged: { editing in
        isEditing = editing
    }
    Text("\(speed)")
        .foregroundColor(isEditing ? .red : .blue)
}
```

## Reading Paths

**Path A — Liquid Glass Adoption:** For glass design patterns and performance guidance, load `apple-liquid-glass-design` skill.

**Path E — macOS Features (this file is step 2):**
← From `macos-drag-and-windows.md` → this file
