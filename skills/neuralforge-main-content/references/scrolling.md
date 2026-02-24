# Neuralforge-Main-Content - Scrolling

**Pages:** 3

---

## ScrollView

**URL:** https://sosumi.ai/documentation/swiftui/scrollview?.md

**Contents:**
- Overview
  - Controlling Scroll Position
- Conforms To
- Creating a scroll view
- Configuring a scroll view
- Supporting types
- Creating a scroll view

---
title: ScrollView
description: A scrollable view.
source: https://developer.apple.com/documentation/swiftui/scrollview
timestamp: 2026-02-13T03:42:35.618Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

The scroll view displays its content within the scrollable content region. As the user performs platform-appropriate scroll gestures, the scroll view adjusts what portion of the underlying content is visible. `ScrollView` can scroll horizontally, vertically, or both, but does not provide zooming functionality.

In the following example, a `ScrollView` allows the user to scroll through a [VStack](/documentation/swiftui/vstack) containing 100 [Text](/documentation/swiftui/text) views. The image after the listing shows the scroll view’s temporarily visible scrollbar at the right; you can disable it with the `showsIndicators` parameter of the `ScrollView` initializer.

You can influence where a scroll view is initially scrolled by using the [defaultScrollAnchor(_:)](/documentation/swiftui/view/defaultscrollanchor(_:)) view modifier.

Provide a value of `UnitPoint/center`` to have the scroll view start in the center of its content when a scroll view is scrollable in both axes.

Or provide an alignment of `UnitPoint/bottom`` to have the scroll view start at the bottom of its content when a scroll view is scrollable in its vertical axes.

After the scroll view initially renders, the user may scroll the content of the scroll view.

To perform programmatic scrolling, wrap one or more scroll views with a [Scroll View Reader](/documentation/swiftui/scrollviewreader).

- [View](/documentation/swiftui/view)

- [init(_:showsIndicators:content:)](/documentation/swiftui/scrollview/init(_:showsindicators:content:)) Creates a new instance that’s scrollable in the direction of the given axis and can show indicators while scrolling.
- [init(_:content:)](/documentation/swiftui/scrollview/init(_:content:)) Creates a new instance that’s scrollable in the direction of the given axis and can show indicators while scrolling.

- [content](/documentation/swiftui/scrollview/content) The scroll view’s content.
- [axes](/documentation/swiftui/scrollview/axes) The scrollable axes of the scroll view.
- [showsIndicators](/documentation/swiftui/scrollview/showsindicators) A value that indicates whether the scroll view displays the scrollable component of the content offset, in a way that’s suitable for the platform.

- [body](/documentation/swiftui/scrollview/body) The content and behavior of the scroll view.

- [ScrollViewReader](/documentation/swiftui/scrollviewreader)
- [ScrollViewProxy](/documentation/swiftui/scrollviewproxy)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ScrollView<Content> where Content : View
```

Example 2 (swift):
```swift
var body: some View {
    ScrollView {
        VStack(alignment: .leading) {
            ForEach(0..<100) {
                Text("Row \($0)")
            }
        }
    }
}
```

Example 3 (swift):
```swift
ScrollView([.horizontal, .vertical]) {
    // initially centered content
}
.defaultScrollAnchor(.center)
```

Example 4 (swift):
```swift
ScrollView {
    // initially bottom aligned content
}
.defaultScrollAnchor(.bottom)
```

---

## scrollTargetBehavior(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/scrolltargetbehavior(_:)?.md

**Contents:**
- Discussion
  - Paging Behavior
  - View Aligned Behavior
- Defining scroll targets

---
title: scrollTargetBehavior(_:)
description: Sets the scroll behavior of views scrollable in the provided axes.
source: https://developer.apple.com/documentation/swiftui/view/scrolltargetbehavior(_:)
timestamp: 2026-02-13T03:43:56.393Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

> Sets the scroll behavior of views scrollable in the provided axes.

A scrollable view calculates where scroll gestures should end using its deceleration rate and the state of its scroll gesture by default. A scroll behavior allows for customizing this logic. You can provide your own [Scroll Target Behavior](/documentation/swiftui/scrolltargetbehavior) or use one of the built in behaviors provided by SwiftUI.

SwiftUI offers a [Paging Scroll Target Behavior](/documentation/swiftui/pagingscrolltargetbehavior) behavior which uses the geometry of the scroll view to decide where to allow scrolls to end.

In the following example, every view in the lazy stack is flexible in both directions and the scroll view will settle to container aligned boundaries.

SwiftUI offers a [View Aligned Scroll Target Behavior](/documentation/swiftui/viewalignedscrolltargetbehavior) scroll behavior that will always settle on the geometry of individual views.

You configure which views should be used for settling using the [scrollTargetLayout(isEnabled:)](/documentation/swiftui/view/scrolltargetlayout(isenabled:)) modifier. Apply this modifier to a layout container like [Lazy VStack](/documentation/swiftui/lazyvstack) or [HStack](/documentation/swiftui/hstack) and each individual view in that layout will be considered for alignment.

- [scrollTargetLayout(isEnabled:)](/documentation/swiftui/view/scrolltargetlayout(isenabled:))
- [ScrollTarget](/documentation/swiftui/scrolltarget)
- [ScrollTargetBehavior](/documentation/swiftui/scrolltargetbehavior)
- [ScrollTargetBehaviorContext](/documentation/swiftui/scrolltargetbehaviorcontext)
- [PagingScrollTargetBehavior](/documentation/swiftui/pagingscrolltargetbehavior)
- [ViewAlignedScrollTargetBehavior](/documentation/swiftui/viewalignedscrolltargetbehavior)
- [AnyScrollTargetBehavior](/documentation/swiftui/anyscrolltargetbehavior)
- [ScrollTargetBehaviorProperties](/documentation/swiftui/scrolltargetbehaviorproperties)
- [ScrollTargetBehaviorPropertiesContext](/documentation/swiftui/scrolltargetbehaviorpropertiescontext)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func scrollTargetBehavior(_ behavior: some ScrollTargetBehavior) -> some View
```

Example 2 (swift):
```swift
ScrollView {
    LazyVStack(spacing: 0.0) {
        ForEach(items) { item in
            FullScreenItem(item)
        }
    }
}
.scrollTargetBehavior(.paging)
```

Example 3 (swift):
```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 10.0) {
        ForEach(items) { item in
            ItemView(item)
        }
    }
    .scrollTargetLayout()
}
.scrollTargetBehavior(.viewAligned)
.safeAreaPadding(.horizontal, 20.0)
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
timestamp: 2026-02-13T03:43:54.331Z
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
