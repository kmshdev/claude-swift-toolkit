# Sidebar-Liquid-Glass-Clone - Shapes And Clipping

**Pages:** 3

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
timestamp: 2026-02-13T01:04:47.728Z
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
timestamp: 2026-02-13T01:04:51.273Z
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
timestamp: 2026-02-13T01:04:49.736Z
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
