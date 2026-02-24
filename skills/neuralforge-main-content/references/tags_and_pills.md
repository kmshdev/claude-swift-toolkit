# Neuralforge-Main-Content - Tags And Pills

**Pages:** 6

---

## badge(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/badge(_:)?.md

**Contents:**
- Parameters
- Discussion
- Displaying a badge on a list item

---
title: badge(_:)
description: Generates a badge for the view from an integer value.
source: https://developer.apple.com/documentation/swiftui/view/badge(_:)
timestamp: 2026-02-13T03:43:14.515Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+

> Generates a badge for the view from an integer value.

An integer value to display in the badge. Set the value to zero to hide the badge.

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

The following example shows a [List](/documentation/swiftui/list) with the value of `recentItems.count` represented by a badge on one of the rows:

- [badgeProminence(_:)](/documentation/swiftui/view/badgeprominence(_:))
- [badgeProminence](/documentation/swiftui/environmentvalues/badgeprominence)
- [BadgeProminence](/documentation/swiftui/badgeprominence)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func badge(_ count: Int) -> some View
```

Example 2 (swift):
```swift
List {
    Text("Recents")
        .badge(recentItems.count)
    Text("Favorites")
}
```

---

## background(_:in:fillStyle:)

**URL:** https://sosumi.ai/documentation/swiftui/view/background(_:in:fillstyle:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Layering views

---
title: background(_:in:fillStyle:)
description: Sets the view’s background to an insettable shape filled with a style.
source: https://developer.apple.com/documentation/swiftui/view/background(_:in:fillstyle:)
timestamp: 2026-02-13T03:43:18.594Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Sets the view’s background to an insettable shape filled with a style.

A [Shape Style](/documentation/swiftui/shapestyle) that SwiftUI uses to the fill the shape that you specify.

An instance of a type that conforms to [Insettable Shape](/documentation/swiftui/insettableshape) that SwiftUI draws behind the view.

The [Fill Style](/documentation/swiftui/fillstyle) to use when drawing the shape. The default style uses the nonzero winding number rule and antialiasing.

A view with the specified insettable shape drawn behind it.

Use this modifier to layer a type that conforms to the [Insettable Shape](/documentation/swiftui/insettableshape) protocol — like a [Rectangle](/documentation/swiftui/rectangle), [Circle](/documentation/swiftui/circle), or [Capsule](/documentation/swiftui/capsule) — behind a view. Specify the [Shape Style](/documentation/swiftui/shapestyle) that’s used to fill the shape. For example, you can place a [Rounded Rectangle](/documentation/swiftui/roundedrectangle) behind a [Label](/documentation/swiftui/label):

The [teal](/documentation/swiftui/shapestyle/teal) color fills the shape:

This modifier is a convenience method for placing a single shape behind a view. To create a background with other [View](/documentation/swiftui/view) types — or with a stack of views — use [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:)) instead. To add a [Shape Style](/documentation/swiftui/shapestyle) as a background, use [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:)).

- [Adding a background to your view](/documentation/swiftui/adding-a-background-to-your-view)
- [ZStack](/documentation/swiftui/zstack)
- [zIndex(_:)](/documentation/swiftui/view/zindex(_:))
- [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:))
- [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:))
- [background(ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(ignoressafeareaedges:))
- [background(in:fillStyle:)](/documentation/swiftui/view/background(in:fillstyle:))
- [overlay(alignment:content:)](/documentation/swiftui/view/overlay(alignment:content:))
- [overlay(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/overlay(_:ignoressafeareaedges:))
- [overlay(_:in:fillStyle:)](/documentation/swiftui/view/overlay(_:in:fillstyle:))
- [backgroundMaterial](/documentation/swiftui/environmentvalues/backgroundmaterial)
- [containerBackground(_:for:)](/documentation/swiftui/view/containerbackground(_:for:))
- [containerBackground(for:alignment:content:)](/documentation/swiftui/view/containerbackground(for:alignment:content:))
- [ContainerBackgroundPlacement](/documentation/swiftui/containerbackgroundplacement)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func background<S, T>(_ style: S, in shape: T, fillStyle: FillStyle = FillStyle()) -> some View where S : ShapeStyle, T : InsettableShape
```

Example 2 (swift):
```swift
Label("Flag", systemImage: "flag.fill")
    .padding()
    .background(.teal, in: RoundedRectangle(cornerRadius: 8))
```

---

## clipShape(_:style:)

**URL:** https://sosumi.ai/documentation/swiftui/view/clipshape(_:style:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Masking and clipping

---
title: clipShape(_:style:)
description: Sets a clipping shape for this view.
source: https://developer.apple.com/documentation/swiftui/view/clipshape(_:style:)
timestamp: 2026-02-13T03:43:22.839Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets a clipping shape for this view.

The clipping shape to use for this view. The `shape` fills the view’s frame, while maintaining its aspect ratio.

The fill style to use when rasterizing `shape`.

A view that clips this view to `shape`, using `style` to define the shape’s rasterization.

Use `clipShape(_:style:)` to clip the view to the provided shape. By applying a clipping shape to a view, you preserve the parts of the view covered by the shape, while eliminating other parts of the view. The clipping shape itself isn’t visible.

For example, this code applies a circular clipping shape to a `Text` view:

The resulting view shows only the portion of the text that lies within the bounds of the circle.

- [mask(alignment:_:)](/documentation/swiftui/view/mask(alignment:_:))
- [clipped(antialiased:)](/documentation/swiftui/view/clipped(antialiased:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func clipShape<S>(_ shape: S, style: FillStyle = FillStyle()) -> some View where S : Shape
```

Example 2 (swift):
```swift
Text("Clipped text in a circle")
    .frame(width: 175, height: 100)
    .foregroundColor(Color.white)
    .background(Color.black)
    .clipShape(Circle())
```

---

## Capsule

**URL:** https://sosumi.ai/documentation/swiftui/capsule?.md

**Contents:**
- Overview
- Conforms To
- Creating a capsule
- Getting the shape’s characteristics
- Creating circular shapes

---
title: Capsule
description: A capsule shape aligned inside the frame of the view containing it.
source: https://developer.apple.com/documentation/swiftui/capsule
timestamp: 2026-02-13T03:43:24.955Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A capsule shape aligned inside the frame of the view containing it.

A capsule shape is equivalent to a rounded rectangle where the corner radius is chosen as half the length of the rectangle’s smallest edge.

- [Animatable](/documentation/swiftui/animatable)
- [Copyable](/documentation/Swift/Copyable)
- [InsettableShape](/documentation/swiftui/insettableshape)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init(style:)](/documentation/swiftui/capsule/init(style:)) Creates a new capsule shape.

- [style](/documentation/swiftui/capsule/style)

- [Circle](/documentation/swiftui/circle)
- [Ellipse](/documentation/swiftui/ellipse)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Capsule
```

---

## padding(_:_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/padding(_:_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Adding padding around a view

---
title: padding(_:_:)
description: Adds an equal padding amount to specific edges of this view.
source: https://developer.apple.com/documentation/swiftui/view/padding(_:_:)
timestamp: 2026-02-13T03:43:16.507Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds an equal padding amount to specific edges of this view.

The set of edges to pad for this view. The default is [all](/documentation/swiftui/edge/set/all).

An amount, given in points, to pad this view on the specified edges. If you set the value to `nil`, SwiftUI uses a platform-specific default amount. The default value of this parameter is `nil`.

A view that’s padded by the specified amount on the specified edges.

Use this modifier to add a specified amount of padding to one or more edges of the view. Indicate the edges to pad by naming either a single value from [Set](/documentation/swiftui/edge/set), or by specifying an [Option Set](/documentation/Swift/OptionSet) that contains edge values:

The order in which you apply modifiers matters. The example above applies the padding before applying the border to ensure that the border encompasses the padded region:

You can omit either or both of the parameters. If you omit the `length`, SwiftUI uses a default amount of padding. If you omit the `edges`, SwiftUI applies the padding to all edges. Omit both to add a default padding all the way around a view. SwiftUI chooses a default amount of padding that’s appropriate for the platform and the presentation context.

The example above looks like this in iOS under typical conditions:

To control the amount of padding independently for each edge, use [padding(_:)](/documentation/swiftui/view/padding(_:)-6pgqq). To pad all outside edges of a view by a specified amount, use [padding(_:)](/documentation/swiftui/view/padding(_:)-68shk).

- [padding(_:)](/documentation/swiftui/view/padding(_:))
- [padding3D(_:)](/documentation/swiftui/view/padding3d(_:))
- [padding3D(_:_:)](/documentation/swiftui/view/padding3d(_:_:))
- [scenePadding(_:)](/documentation/swiftui/view/scenepadding(_:))
- [scenePadding(_:edges:)](/documentation/swiftui/view/scenepadding(_:edges:))
- [ScenePadding](/documentation/swiftui/scenepadding)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func padding(_ edges: Edge.Set = .all, _ length: CGFloat? = nil) -> some View
```

Example 2 (swift):
```swift
VStack {
    Text("Text padded by 20 points on the bottom and trailing edges.")
        .padding([.bottom, .trailing], 20)
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
```

Example 3 (swift):
```swift
VStack {
    Text("Text with default padding.")
        .padding()
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
```

---

## RoundedRectangle

**URL:** https://sosumi.ai/documentation/swiftui/roundedrectangle?.md

**Contents:**
- Conforms To
- Creating a rounded rectangle
- Getting the shape’s characteristics
- Supporting types
- Creating rectangular shapes

---
title: RoundedRectangle
description: A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
source: https://developer.apple.com/documentation/swiftui/roundedrectangle
timestamp: 2026-02-13T03:43:27.078Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A rectangular shape with rounded corners, aligned inside the frame of the view containing it.

- [Animatable](/documentation/swiftui/animatable)
- [Copyable](/documentation/Swift/Copyable)
- [InsettableShape](/documentation/swiftui/insettableshape)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init(cornerRadius:style:)](/documentation/swiftui/roundedrectangle/init(cornerradius:style:)) Creates a new rounded rectangle shape.
- [init(cornerSize:style:)](/documentation/swiftui/roundedrectangle/init(cornersize:style:)) Creates a new rounded rectangle shape.

- [cornerSize](/documentation/swiftui/roundedrectangle/cornersize) The width and height of the rounded rectangle’s corners.
- [style](/documentation/swiftui/roundedrectangle/style) The style of corners drawn by the rounded rectangle.

- [animatableData](/documentation/swiftui/roundedrectangle/animatabledata) The data to animate.

- [Rectangle](/documentation/swiftui/rectangle)
- [RoundedCornerStyle](/documentation/swiftui/roundedcornerstyle)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [RoundedRectangularShapeCorners](/documentation/swiftui/roundedrectangularshapecorners)
- [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle)
- [RectangleCornerRadii](/documentation/swiftui/rectanglecornerradii)
- [RectangleCornerInsets](/documentation/swiftui/rectanglecornerinsets)
- [ConcentricRectangle](/documentation/swiftui/concentricrectangle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct RoundedRectangle
```

---
