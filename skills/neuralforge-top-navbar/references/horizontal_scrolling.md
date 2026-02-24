# Neuralforge-Top-Navbar - Horizontal Scrolling

**Pages:** 5

---

## LazyHStack

**URL:** https://sosumi.ai/documentation/swiftui/lazyhstack?.md

**Contents:**
- Overview
- Conforms To
- Creating a lazy-loading horizontal stack
- Dynamically arranging views in one dimension

---
title: LazyHStack
description: A view that arranges its children in a line that grows horizontally, creating items only as needed.
source: https://developer.apple.com/documentation/swiftui/lazyhstack
timestamp: 2026-02-13T03:56:03.690Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A view that arranges its children in a line that grows horizontally, creating items only as needed.

The stack is “lazy,” in that the stack view doesn’t create items until it needs to render them onscreen.

In the following example, a [Scroll View](/documentation/swiftui/scrollview) contains a `LazyHStack` that consists of a horizontal row of text views. The stack aligns to the top of the scroll view and uses 10-point spacing between each text view.

- [View](/documentation/swiftui/view)

- [init(alignment:spacing:pinnedViews:content:)](/documentation/swiftui/lazyhstack/init(alignment:spacing:pinnedviews:content:)) Creates a lazy horizontal stack view with the given spacing, vertical alignment, pinning behavior, and content.

- [Grouping data with lazy stack views](/documentation/swiftui/grouping-data-with-lazy-stack-views)
- [Creating performant scrollable stacks](/documentation/swiftui/creating-performant-scrollable-stacks)
- [LazyVStack](/documentation/swiftui/lazyvstack)
- [PinnedScrollableViews](/documentation/swiftui/pinnedscrollableviews)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct LazyHStack<Content> where Content : View
```

Example 2 (swift):
```swift
ScrollView(.horizontal) {
    LazyHStack(alignment: .top, spacing: 10) {
        ForEach(1...100, id: \.self) {
            Text("Column \($0)")
        }
    }
}
```

---

## HStack

**URL:** https://sosumi.ai/documentation/swiftui/hstack?.md

**Contents:**
- Overview
- Conforms To
- Creating a stack
- Statically arranging views in one dimension

---
title: HStack
description: A view that arranges its subviews in a horizontal line.
source: https://developer.apple.com/documentation/swiftui/hstack
timestamp: 2026-02-13T03:56:01.426Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A view that arranges its subviews in a horizontal line.

Unlike [Lazy HStack](/documentation/swiftui/lazyhstack), which only renders the views when your app needs to display them onscreen, an `HStack` renders the views all at once, regardless of whether they are on- or offscreen. Use the regular `HStack` when you have a small number of subviews or don’t want the delayed rendering behavior of the “lazy” version.

The following example shows a simple horizontal stack of five text views:

> [!NOTE]
> If you need a horizontal stack that conforms to the [Layout](/documentation/swiftui/layout) protocol, like when you want to create a conditional layout using [Any Layout](/documentation/swiftui/anylayout), use [HStack Layout](/documentation/swiftui/hstacklayout) instead.

- [View](/documentation/swiftui/view)

- [init(alignment:spacing:content:)](/documentation/swiftui/hstack/init(alignment:spacing:content:)) Creates a horizontal stack with the given spacing and vertical alignment.

- [Building layouts with stack views](/documentation/swiftui/building-layouts-with-stack-views)
- [VStack](/documentation/swiftui/vstack)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct HStack<Content> where Content : View
```

Example 2 (swift):
```swift
var body: some View {
    HStack(
        alignment: .top,
        spacing: 10
    ) {
        ForEach(
            1...5,
            id: \.self
        ) {
            Text("Item \($0)")
        }
    }
}
```

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
timestamp: 2026-02-13T03:55:54.228Z
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

## ScrollViewReader

**URL:** https://sosumi.ai/documentation/swiftui/scrollviewreader?.md

**Contents:**
- Overview
- Conforms To
- Creating a scroll view reader
- Configuring a scroll view reader
- Creating a scroll view

---
title: ScrollViewReader
description: A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.
source: https://developer.apple.com/documentation/swiftui/scrollviewreader
timestamp: 2026-02-13T03:55:56.204Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.

The scroll view reader’s content view builder receives a [Scroll View Proxy](/documentation/swiftui/scrollviewproxy) instance; you use the proxy’s [scrollTo(_:anchor:)](/documentation/swiftui/scrollviewproxy/scrollto(_:anchor:)) to perform scrolling.

The following example creates a [Scroll View](/documentation/swiftui/scrollview) containing 100 views that together display a color gradient. It also contains two buttons, one each at the top and bottom. The top button tells the [Scroll View Proxy](/documentation/swiftui/scrollviewproxy) to scroll to the bottom button, and vice versa.

> [!IMPORTANT]
> You may not use the [Scroll View Proxy](/documentation/swiftui/scrollviewproxy) during execution of the `content` view builder; doing so results in a runtime error. Instead, only actions created within `content` can call the proxy, such as gesture handlers or a view’s `onChange(of:perform:)` method.

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/scrollviewreader/init(content:)) Creates an instance that can perform programmatic scrolling of its child scroll views.

- [content](/documentation/swiftui/scrollviewreader/content) The view builder that creates the reader’s content.

- [ScrollView](/documentation/swiftui/scrollview)
- [ScrollViewProxy](/documentation/swiftui/scrollviewproxy)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct ScrollViewReader<Content> where Content : View
```

Example 2 (swift):
```swift
@Namespace var topID
@Namespace var bottomID

var body: some View {
    ScrollViewReader { proxy in
        ScrollView {
            Button("Scroll to Bottom") {
                withAnimation {
                    proxy.scrollTo(bottomID)
                }
            }
            .id(topID)

            VStack(spacing: 0) {
                ForEach(0..<100) { i in
                    color(fraction: Double(i) / 100)
                        .frame(height: 32)
                }
            }

            Button("Top") {
                withAnimation {
                    proxy.scrollTo(topID)
                }
            }
            .id(bottomID)
        }
    }
}

func color(fraction: Double) -> Color {
    Color(red: fraction, green: 1 - fraction, blue: 0.5)
}
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
timestamp: 2026-02-13T03:55:58.513Z
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
