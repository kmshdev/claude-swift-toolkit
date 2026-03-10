# Apple-Liquid-Glass-Design - Navigation And Layout

**Pages:** 2

---

## tabBarMinimizeBehavior(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/tabbarminimizebehavior(_:)?.md

**Contents:**
- Parameters
- Discussion

---
title: tabBarMinimizeBehavior(_:)
description: Sets the behavior for tab bar minimization.
source: https://developer.apple.com/documentation/swiftui/view/tabbarminimizebehavior(_:)
timestamp: 2026-02-13T00:19:27.062Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+

> Sets the behavior for tab bar minimization.

The minimize behavior.

The following TabView minimizes its tab bar when scrolling in the ‘Numbers’ or ‘Alerts’ tabs on iPhone.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func tabBarMinimizeBehavior(_ behavior: TabBarMinimizeBehavior) -> some View
```

Example 2 (swift):
```swift
struct ContentView: View {
    var body: some View {
         TabView {
             Tab("Numbers", systemImage: "number") {
                 ScrollView {
                    ForEach(0 ..< 50) { index in
                        Text("\(index)")
                            .padding()
                    }
                 }
             }
             Tab("Alerts", systemImage: "bell") {
                 AlertsView()
             }
         }
         .tabBarMinimizeBehavior(.onScrollDown)
    }
}
```

---

## scrollEdgeEffectStyle(_:for:)

**URL:** https://sosumi.ai/documentation/swiftui/view/scrolledgeeffectstyle(_:for:)?.md

**Contents:**
- Discussion
- Configuring scroll edge effects

---
title: scrollEdgeEffectStyle(_:for:)
description: Configures the scroll edge effect style for scroll views within this hierarchy.
source: https://developer.apple.com/documentation/swiftui/view/scrolledgeeffectstyle(_:for:)
timestamp: 2026-02-13T00:19:24.886Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> Configures the scroll edge effect style for scroll views within this hierarchy.

By default, a scroll view renders an automatic edge effect. Use this modifier to change the scroll edge effect style.

- [scrollEdgeEffectHidden(_:for:)](/documentation/swiftui/view/scrolledgeeffecthidden(_:for:))
- [ScrollEdgeEffectStyle](/documentation/swiftui/scrolledgeeffectstyle)
- [safeAreaBar(edge:alignment:spacing:content:)](/documentation/swiftui/view/safeareabar(edge:alignment:spacing:content:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func scrollEdgeEffectStyle(_ style: ScrollEdgeEffectStyle?, for edges: Edge.Set) -> some View
```

Example 2 (swift):
```swift
ScrollView {
    LazyVStack {
        ForEach(data) { item in
            RowView(item)
        }
    }
}
.scrollEdgeEffectStyle(.hard, for: .all)
```

---
