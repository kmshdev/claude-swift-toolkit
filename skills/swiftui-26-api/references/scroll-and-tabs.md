# Scroll and Tab APIs
APIs for configuring scroll edge effects, tab bar minimize behavior, and tab roles.

## Table of Contents
- [scrollEdgeEffectStyle(_:for:)](#scrolledgeeffectstyle_for) — Configure the visual effect style applied at the scroll edges of a scroll view
- [tabBarMinimizeBehavior(_:)](#tabbarminimizebehavior_) — Control when the tab bar minimizes during scroll interactions
- [search](#search) — Designate a tab as the primary search tab in a tab view

## scrollEdgeEffectStyle(_:for:)

**URL:** https://sosumi.ai/documentation/SwiftUI/View/scrollEdgeEffectStyle(_:for:)?.md

**Contents:**
- Discussion
- Configuring scroll edge effects

**Navigation:** [SwiftUI](/documentation/SwiftUI) › [View](/documentation/SwiftUI/View)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

By default, a scroll view renders an automatic edge effect. Use this modifier to change the scroll edge effect style.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

### ScrollEdgeEffectStyle Values

| Value | Behavior |
|-------|----------|
| `.automatic` | System default edge effect |
| `.soft` | Gradual fade at scroll edges |
| `.hard` | Sharp clip at scroll edges |
| `nil` | Disable edge effect entirely |

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

## tabBarMinimizeBehavior(_:)

**URL:** https://sosumi.ai/documentation/SwiftUI/View/tabBarMinimizeBehavior(_:)?.md

**Contents:**
- Parameters
- Discussion

**Navigation:** [SwiftUI](/documentation/SwiftUI) › [View](/documentation/SwiftUI/View)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+

The minimize behavior.

The following TabView minimizes its tab bar when scrolling in the 'Numbers' or 'Alerts' tabs on iPhone.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

### TabBarMinimizeBehavior Values

| Value | Behavior |
|-------|----------|
| `.automatic` | System decides when to minimize |
| `.onScrollDown` | Minimize when user scrolls down |
| `.never` | Tab bar always visible |

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

## search

**URL:** https://sosumi.ai/documentation/SwiftUI/TabRole/search?.md

**Contents:**
- Discussion

**Navigation:** [SwiftUI](/documentation/SwiftUI) › [TabRole](/documentation/SwiftUI/TabRole)

**Available on:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

Searchable tab views will prefer to have the first tab with this role implement search. If no tabs are specified as the search tab, the tab view will apply search to all tabs, resetting search state as the selected tab changes.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
static var search: TabRole { get }
```

---

## Reading Paths

**Path A — Liquid Glass Adoption:** For glass design patterns, load `apple-liquid-glass-design` skill.

This file covers scroll edge effects and tab bar minimization — non-glass APIs that complement the glass design language.
