# Swiftui-Components - Layout System

**Pages:** 14

---

## ConcentricRectangle

**URL:** https://sosumi.ai/documentation/swiftui/concentricrectangle?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Creating rectangular shapes

---
title: ConcentricRectangle
description: A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.
source: https://developer.apple.com/documentation/swiftui/concentricrectangle
timestamp: 2026-02-13T19:32:19.113Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+

> A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.

To use [Concentric Rectangle](/documentation/swiftui/concentricrectangle), first make sure the ancestor view hierarchy provides the container shape. Some container shapes are provided by platform kits, but you could provide your own by writing the [containerShape(_:)](/documentation/swiftui/view/containershape(_:)-3br47) modifier with a shape. Then, either call one of the initializers of [Concentric Rectangle](/documentation/swiftui/concentricrectangle) or use the static [Shape](/documentation/swiftui/shape) convenience to create the concentric shape.

The above example will generate a shape that is inset by `padding` on all sides. It will stay concentric to its container shape which has a 24 pts corner radius, so the shape will have a smaller radius with more padding. However, since here we provided a minimum value, the radius will be at least 12 pts, ensuring the shape to never have a square corner.

[Concentric Rectangle](/documentation/swiftui/concentricrectangle) also provides per-corner control with the initializers that take different styles for each corner.

The above example will have the top leading corner as square, the top trailing corner as constant 28 pts radius, the bottom leading as concentric to container shape, and bottom trailing as concentric with a minimum radius.

If you wish [Concentric Rectangle](/documentation/swiftui/concentricrectangle) to be symmetric on two corners, create the shape with initializers that takes an uniform corner style for any two corners on the rectangle. [Concentric Rectangle](/documentation/swiftui/concentricrectangle) will still resolves corner radius individually, but use the maximum value out of the corners as the final, shared corner radius of the uniform corners.

When the container shape provided is not a [Rounded Rectangular Shape](/documentation/swiftui/roundedrectangularshape) compatible shape, [Concentric Rectangle](/documentation/swiftui/concentricrectangle) will not be able to resolve corner radius based on concentricity. In those cases, it will fallback to be a [Container Relative Shape](/documentation/swiftui/containerrelativeshape), which is an inset version of the container shape.

> [!NOTE]
> [Container Relative Shape](/documentation/swiftui/containerrelativeshape).

> [!NOTE]
> `Shape/rect(corners:isUniform:))`, [rect(uniformTopCorners:uniformBottomCorners:)](/documentation/swiftui/shape/rect(uniformtopcorners:uniformbottomcorners:)), [rect(uniformLeadingCorners:uniformTrailingCorners:)](/documentation/swiftui/shape/rect(uniformleadingcorners:uniformtrailingcorners:)), [rect(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)](/documentation/swiftui/shape/rect(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:)), [rect(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)](/documentation/swiftui/shape/rect(uniformbottomcorners:topleadingcorner:toptrailingcorner:)), [rect(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)](/documentation/swiftui/shape/rect(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:)), [rect(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)](/documentation/swiftui/shape/rect(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:)).

- [Animatable](/documentation/swiftui/animatable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init()](/documentation/swiftui/concentricrectangle/init()) Create a concentric rectangle with each corner being concentric individually to the container shape.
- [init(corners:isUniform:)](/documentation/swiftui/concentricrectangle/init(corners:isuniform:)) Create a rectangle with the same corner style set on four corners.
- [init(topLeadingCorner:topTrailingCorner:bottomLeadingCorner:bottomTrailingCorner:)](/documentation/swiftui/concentricrectangle/init(topleadingcorner:toptrailingcorner:bottomleadingcorner:bottomtrailingcorner:)) Create a rectangle with individual styles of four corners.
- [init(uniformBottomCorners:topLeadingCorner:topTrailingCorner:)](/documentation/swiftui/concentricrectangle/init(uniformbottomcorners:topleadingcorner:toptrailingcorner:)) Create a rectangle with a corner style set on the top two corners uniformly, and two other styles for the bottom two corners respectively.
- [init(uniformLeadingCorners:topTrailingCorner:bottomTrailingCorner:)](/documentation/swiftui/concentricrectangle/init(uniformleadingcorners:toptrailingcorner:bottomtrailingcorner:)) Create a rectangle with a corner style set on the leading two corners uniformly, and two other styles for the trailing two corners respectively.
- [init(uniformLeadingCorners:uniformTrailingCorners:)](/documentation/swiftui/concentricrectangle/init(uniformleadingcorners:uniformtrailingcorners:)) Create a rectangle with a corner style set on the leading two corners uniformly, and another style set on the trailing two corners uniformly.
- [init(uniformTopCorners:bottomLeadingCorner:bottomTrailingCorner:)](/documentation/swiftui/concentricrectangle/init(uniformtopcorners:bottomleadingcorner:bottomtrailingcorner:)) Create a rectangle with a corner style set on the top two corners uniformly, and two other styles for the bottom two corners respectively.
- [init(uniformTopCorners:uniformBottomCorners:)](/documentation/swiftui/concentricrectangle/init(uniformtopcorners:uniformbottomcorners:)) Create a rectangle with a corner style set on the top two corners uniformly, and another style set on the bottom two corners uniformly.
- [init(uniformTrailingCorners:topLeadingCorner:bottomLeadingCorner:)](/documentation/swiftui/concentricrectangle/init(uniformtrailingcorners:topleadingcorner:bottomleadingcorner:)) Create a rectangle with a corner style set on the trailing two corners uniformly, and two other styles for the leading two corners respectively.

- [Rectangle](/documentation/swiftui/rectangle)
- [RoundedRectangle](/documentation/swiftui/roundedrectangle)
- [RoundedCornerStyle](/documentation/swiftui/roundedcornerstyle)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [RoundedRectangularShapeCorners](/documentation/swiftui/roundedrectangularshapecorners)
- [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle)
- [RectangleCornerRadii](/documentation/swiftui/rectanglecornerradii)
- [RectangleCornerInsets](/documentation/swiftui/rectanglecornerinsets)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ConcentricRectangle
```

Example 2 (swift):
```swift
ZStack {
        Color.cyan
            .fill(.rect(corners: .concentric(minimum: 12), isUniform: false))
            .padding(.all, padding)
    }
    .containerShape(.rect(cornerRadius: 24))
```

Example 3 (swift):
```swift
ConcentricRectangle(
    topLeadingCorner: 0,
    topTrailingCorner: 28,
    bottomLeadingCorner: .concentric,
    bottomTrailingCorner: .concentric(minimum: 12)
)
```

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
timestamp: 2026-02-13T19:31:44.812Z
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

## Spacer

**URL:** https://sosumi.ai/documentation/swiftui/spacer?.md

**Contents:**
- Overview
- Conforms To
- Creating a spacer
- Separators

---
title: Spacer
description: A flexible space that expands along the major axis of its containing stack layout, or on both axes if not contained in a stack.
source: https://developer.apple.com/documentation/swiftui/spacer
timestamp: 2026-02-13T19:31:57.164Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A flexible space that expands along the major axis of its containing stack layout, or on both axes if not contained in a stack.

A spacer creates an adaptive view with no content that expands as much as it can. For example, when placed within an [HStack](/documentation/swiftui/hstack), a spacer expands horizontally as much as the stack allows, moving sibling views out of the way, within the limits of the stack’s size. SwiftUI sizes a stack that doesn’t contain a spacer up to the combined ideal widths of the content of the stack’s child views.

The following example provides a simple checklist row to illustrate how you can use a spacer:

Adding a spacer before the image creates an adaptive view with no content that expands to push the image and text to the right side of the stack. The stack also now expands to take as much space as the parent view allows, shown by the blue border that indicates the boundary of the stack:

Moving the spacer between the image and the name pushes those elements to the left and right sides of the [HStack](/documentation/swiftui/hstack), respectively. Because the stack contains the spacer, it expands to take as much horizontal space as the parent view allows; the blue border indicates its size:

Adding two spacer views on the outside of the stack leaves the image and text together, while the stack expands to take as much horizontal space as the parent view allows:

- [BitwiseCopyable](/documentation/Swift/BitwiseCopyable)
- [Copyable](/documentation/Swift/Copyable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [View](/documentation/swiftui/view)

- [init(minLength:)](/documentation/swiftui/spacer/init(minlength:))
- [minLength](/documentation/swiftui/spacer/minlength) The minimum length this spacer can be shrunk to, along the axis or axes of expansion.

- [Divider](/documentation/swiftui/divider)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Spacer
```

Example 2 (swift):
```swift
struct ChecklistRow: View {
    let name: String

    var body: some View {
        HStack {
            Image(systemName: "checkmark")
            Text(name)
        }
        .border(Color.blue)
    }
}
```

Example 3 (swift):
```swift
struct ChecklistRow: View {
    let name: String

    var body: some View {
        HStack {
            Spacer()
            Image(systemName: "checkmark")
            Text(name)
        }
        .border(Color.blue)
    }
}
```

Example 4 (swift):
```swift
struct ChecklistRow: View {
    let name: String

    var body: some View {
        HStack {
            Image(systemName: "checkmark")
            Spacer()
            Text(name)
        }
        .border(Color.blue)
    }
}
```

---

## LazyHGrid

**URL:** https://sosumi.ai/documentation/swiftui/lazyhgrid?.md

**Contents:**
- Overview
- Conforms To
- Creating a horizontal grid
- Dynamically arranging views in two dimensions

---
title: LazyHGrid
description: A container view that arranges its child views in a grid that grows horizontally, creating items only as needed.
source: https://developer.apple.com/documentation/swiftui/lazyhgrid
timestamp: 2026-02-13T19:31:49.018Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A container view that arranges its child views in a grid that grows horizontally, creating items only as needed.

Use a lazy horizontal grid when you want to display a large, horizontally scrollable collection of views arranged in a two dimensional layout. The first view that you provide to the grid’s `content` closure appears in the top row of the column that’s on the grid’s leading edge. Additional views occupy successive cells in the grid, filling the first column from top to bottom, then the second column, and so on. The number of columns can grow unbounded, but you specify the number of rows by providing a corresponding number of [Grid Item](/documentation/swiftui/griditem) instances to the grid’s initializer.

The grid in the following example defines two rows and uses a [For Each](/documentation/swiftui/foreach) structure to repeatedly generate a pair of [Text](/documentation/swiftui/text) views for the rows in each column:

For each column in the grid, the top row shows a Unicode code point from the “Smileys” group, and the bottom shows its corresponding emoji:

You can achieve a similar layout using a [Grid](/documentation/swiftui/grid) container. Unlike a lazy grid, which creates child views only when SwiftUI needs to display them, a regular grid creates all of its child views right away. This enables the grid to provide better support for cell spacing and alignment. Only use a lazy grid if profiling your app shows that a [Grid](/documentation/swiftui/grid) view performs poorly because it tries to load too many views at once.

- [View](/documentation/swiftui/view)

- [init(rows:alignment:spacing:pinnedViews:content:)](/documentation/swiftui/lazyhgrid/init(rows:alignment:spacing:pinnedviews:content:)) Creates a grid that grows horizontally.

- [LazyVGrid](/documentation/swiftui/lazyvgrid)
- [GridItem](/documentation/swiftui/griditem)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct LazyHGrid<Content> where Content : View
```

Example 2 (swift):
```swift
struct HorizontalSmileys: View {
    let rows = [GridItem(.fixed(30)), GridItem(.fixed(30))]

    var body: some View {
        ScrollView(.horizontal) {
            LazyHGrid(rows: rows) {
                ForEach(0x1f600...0x1f679, id: \.self) { value in
                    Text(String(format: "%x", value))
                    Text(emoji(value))
                        .font(.largeTitle)
                }
            }
        }
    }

    private func emoji(_ value: Int) -> String {
        guard let scalar = UnicodeScalar(value) else { return "?" }
        return String(Character(scalar))
    }
}
```

---

## ZStack

**URL:** https://sosumi.ai/documentation/swiftui/zstack?.md

**Contents:**
- Overview
- Conforms To
- Creating a stack
- Supporting symbols
- Initializers
- Layering views

---
title: ZStack
description: A view that overlays its subviews, aligning them in both axes.
source: https://developer.apple.com/documentation/swiftui/zstack
timestamp: 2026-02-13T19:31:41.053Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A view that overlays its subviews, aligning them in both axes.

The `ZStack` assigns each successive subview a higher z-axis value than the one before it, meaning later subviews appear “on top” of earlier ones.

The following example creates a `ZStack` of 100 x 100 point [Rectangle](/documentation/swiftui/rectangle) views filled with one of six colors, offsetting each successive subview by 10 points so they don’t completely overlap:

The `ZStack` uses an [Alignment](/documentation/swiftui/alignment) to set the x- and y-axis coordinates of each subview, defaulting to a [center](/documentation/swiftui/alignment/center) alignment. In the following example, the `ZStack` uses a [bottom Leading](/documentation/swiftui/alignment/bottomleading) alignment to lay out two subviews, a red 100 x 50 point rectangle below, and a blue 50 x 100 point rectangle on top. Because of the alignment value, both rectangles share a bottom-left corner with the `ZStack` (in locales where left is the leading side).

> [!NOTE]
> If you need a version of this stack that conforms to the [Layout](/documentation/swiftui/layout) protocol, like when you want to create a conditional layout using [Any Layout](/documentation/swiftui/anylayout), use [ZStack Layout](/documentation/swiftui/zstacklayout) instead.

- [View](/documentation/swiftui/view)

- [init(alignment:content:)](/documentation/swiftui/zstack/init(alignment:content:)) Creates an instance with the given alignment.

- [ZStackContent3D](/documentation/swiftui/zstackcontent3d) A type that adds spacing to a .

- [init(alignment:spacing:content:)](/documentation/swiftui/zstack/init(alignment:spacing:content:)) Creates an instance with the given spacing and alignment.

- [Adding a background to your view](/documentation/swiftui/adding-a-background-to-your-view)
- [zIndex(_:)](/documentation/swiftui/view/zindex(_:))
- [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:))
- [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:))
- [background(ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(ignoressafeareaedges:))
- [background(_:in:fillStyle:)](/documentation/swiftui/view/background(_:in:fillstyle:))
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
@frozen struct ZStack<Content> where Content : View
```

Example 2 (swift):
```swift
let colors: [Color] =
    [.red, .orange, .yellow, .green, .blue, .purple]

var body: some View {
    ZStack {
        ForEach(0..<colors.count) {
            Rectangle()
                .fill(colors[$0])
                .frame(width: 100, height: 100)
                .offset(x: CGFloat($0) * 10.0,
                        y: CGFloat($0) * 10.0)
        }
    }
}
```

Example 3 (swift):
```swift
var body: some View {
    ZStack(alignment: .bottomLeading) {
        Rectangle()
            .fill(Color.red)
            .frame(width: 100, height: 50)
        Rectangle()
            .fill(Color.blue)
            .frame(width:50, height: 100)
    }
    .border(Color.green, width: 1)
}
```

---

## VStack

**URL:** https://sosumi.ai/documentation/swiftui/vstack?.md

**Contents:**
- Overview
- Conforms To
- Creating a stack
- Statically arranging views in one dimension

---
title: VStack
description: A view that arranges its subviews in a vertical line.
source: https://developer.apple.com/documentation/swiftui/vstack
timestamp: 2026-02-13T19:31:36.699Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A view that arranges its subviews in a vertical line.

Unlike [Lazy VStack](/documentation/swiftui/lazyvstack), which only renders the views when your app needs to display them, a `VStack` renders the views all at once, regardless of whether they are on- or offscreen. Use the regular `VStack` when you have a small number of subviews or don’t want the delayed rendering behavior of the “lazy” version.

The following example shows a simple vertical stack of 10 text views:

> [!NOTE]
> If you need a vertical stack that conforms to the [Layout](/documentation/swiftui/layout) protocol, like when you want to create a conditional layout using [Any Layout](/documentation/swiftui/anylayout), use [VStack Layout](/documentation/swiftui/vstacklayout) instead.

- [View](/documentation/swiftui/view)

- [init(alignment:spacing:content:)](/documentation/swiftui/vstack/init(alignment:spacing:content:)) Creates an instance with the given spacing and horizontal alignment.

- [Building layouts with stack views](/documentation/swiftui/building-layouts-with-stack-views)
- [HStack](/documentation/swiftui/hstack)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct VStack<Content> where Content : View
```

Example 2 (swift):
```swift
var body: some View {
    VStack(
        alignment: .leading,
        spacing: 10
    ) {
        ForEach(
            1...10,
            id: \.self
        ) {
            Text("Item \($0)")
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
timestamp: 2026-02-13T19:31:38.901Z
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

## ContentMarginPlacement

**URL:** https://sosumi.ai/documentation/swiftui/contentmarginplacement?.md

**Contents:**
- Overview
- Getting the placement
- Setting margins

---
title: ContentMarginPlacement
description: The placement of margins.
source: https://developer.apple.com/documentation/swiftui/contentmarginplacement
timestamp: 2026-02-13T19:32:21.217Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

> The placement of margins.

Different views can support customizating margins that appear in different parts of that view. Use values of this type to customize those margins of a particular placement.

For example, use a [scroll Indicators](/documentation/swiftui/contentmarginplacement/scrollindicators) placement to customize the margins of scrollable view’s scroll indicators separately from the margins of a scrollable view’s content.

Use this type with the [contentMargins(_:for:)](/documentation/swiftui/view/contentmargins(_:for:)) modifier.

- [automatic](/documentation/swiftui/contentmarginplacement/automatic) The automatic placement.
- [scrollContent](/documentation/swiftui/contentmarginplacement/scrollcontent) The scroll content placement.
- [scrollIndicators](/documentation/swiftui/contentmarginplacement/scrollindicators) The scroll indicators placement.

- [contentMargins(_:for:)](/documentation/swiftui/view/contentmargins(_:for:))
- [contentMargins(_:_:for:)](/documentation/swiftui/view/contentmargins(_:_:for:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ContentMarginPlacement
```

---

## GridRow

**URL:** https://sosumi.ai/documentation/swiftui/gridrow?.md

**Contents:**
- Overview
- Conforms To
- Creating a grid row
- Statically arranging views in two dimensions

---
title: GridRow
description: A horizontal row in a two dimensional grid container.
source: https://developer.apple.com/documentation/swiftui/gridrow
timestamp: 2026-02-13T19:31:55.158Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> A horizontal row in a two dimensional grid container.

Use one or more `GridRow` instances to define the rows of a [Grid](/documentation/swiftui/grid) container. The child views inside the row define successive grid cells. You can add rows to the grid explicitly, or use the [For Each](/documentation/swiftui/foreach) structure to generate multiple rows. Similarly, you can add cells to the row explicitly or you can use [For Each](/documentation/swiftui/foreach) to generate multiple cells inside the row. The following example mixes these strategies:

The grid in the example above has an explicit first row and three generated rows. Similarly, each row has an explicit first cell and three generated cells:

To create an empty cell, use something invisible, like the [clear](/documentation/swiftui/shapestyle/clear) color that appears in the first column of the first row in the example above. However, if you use a flexible view like a [Color](/documentation/swiftui/color) or a [Spacer](/documentation/swiftui/spacer), you might also need to add the [gridCellUnsizedAxes(_:)](/documentation/swiftui/view/gridcellunsizedaxes(_:)) modifier to prevent the view from taking up more space than the other cells in the row or column need.

> [!IMPORTANT]
> You can’t use [Empty View](/documentation/swiftui/emptyview) to create a blank cell because that resolves to the absence of a view and doesn’t generate a cell.

By default, the cells in the row use the [Alignment](/documentation/swiftui/alignment) that you define when you initialize the [Grid](/documentation/swiftui/grid). However, you can override the vertical alignment for the cells in a row by providing a [Vertical Alignment](/documentation/swiftui/verticalalignment) value to the row’s [init(alignment:content:)](/documentation/swiftui/gridrow/init(alignment:content:)) initializer.

If you apply a view modifier to a row, the row applies the modifier to all of the cells, similar to how a [Group](/documentation/swiftui/group) behaves. For example,  if you apply the [border(_:width:)](/documentation/swiftui/view/border(_:width:)) modifier to a row, SwiftUI draws a border on each cell in the row rather than around the row.

- [Copyable](/documentation/Swift/Copyable)
- [View](/documentation/swiftui/view)

- [init(alignment:content:)](/documentation/swiftui/gridrow/init(alignment:content:)) Creates a horizontal row of child views in a grid.

- [Grid](/documentation/swiftui/grid)
- [gridCellColumns(_:)](/documentation/swiftui/view/gridcellcolumns(_:))
- [gridCellAnchor(_:)](/documentation/swiftui/view/gridcellanchor(_:))
- [gridCellUnsizedAxes(_:)](/documentation/swiftui/view/gridcellunsizedaxes(_:))
- [gridColumnAlignment(_:)](/documentation/swiftui/view/gridcolumnalignment(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct GridRow<Content> where Content : View
```

Example 2 (swift):
```swift
Grid {
    GridRow {
        Color.clear
            .gridCellUnsizedAxes([.horizontal, .vertical])
        ForEach(1..<4) { column in
            Text("C\(column)")
        }
    }
    ForEach(1..<4) { row in
        GridRow {
            Text("R\(row)")
            ForEach(1..<4) { _ in
                Circle().foregroundStyle(.mint)
            }
        }
    }
}
```

---

## LazyVGrid

**URL:** https://sosumi.ai/documentation/swiftui/lazyvgrid?.md

**Contents:**
- Overview
- Conforms To
- Creating a vertical grid
- Dynamically arranging views in two dimensions

---
title: LazyVGrid
description: A container view that arranges its child views in a grid that grows vertically, creating items only as needed.
source: https://developer.apple.com/documentation/swiftui/lazyvgrid
timestamp: 2026-02-13T19:31:46.848Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A container view that arranges its child views in a grid that grows vertically, creating items only as needed.

Use a lazy vertical grid when you want to display a large, vertically scrollable collection of views arranged in a two dimensional layout. The first view that you provide to the grid’s `content` closure appears in the top row of the column that’s on the grid’s leading edge. Additional views occupy successive cells in the grid, filling the first row from leading to trailing edges, then the second row, and so on. The number of rows can grow unbounded, but you specify the number of columns by providing a corresponding number of [Grid Item](/documentation/swiftui/griditem) instances to the grid’s initializer.

The grid in the following example defines two columns and uses a [For Each](/documentation/swiftui/foreach) structure to repeatedly generate a pair of [Text](/documentation/swiftui/text) views for the columns in each row:

For each row in the grid, the first column shows a Unicode code point from the “Smileys” group, and the second shows its corresponding emoji:

You can achieve a similar layout using a [Grid](/documentation/swiftui/grid) container. Unlike a lazy grid, which creates child views only when SwiftUI needs to display them, a regular grid creates all of its child views right away. This enables the grid to provide better support for cell spacing and alignment. Only use a lazy grid if profiling your app shows that a [Grid](/documentation/swiftui/grid) view performs poorly because it tries to load too many views at once.

- [View](/documentation/swiftui/view)

- [init(columns:alignment:spacing:pinnedViews:content:)](/documentation/swiftui/lazyvgrid/init(columns:alignment:spacing:pinnedviews:content:)) Creates a grid that grows vertically.

- [LazyHGrid](/documentation/swiftui/lazyhgrid)
- [GridItem](/documentation/swiftui/griditem)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct LazyVGrid<Content> where Content : View
```

Example 2 (swift):
```swift
struct VerticalSmileys: View {
    let columns = [GridItem(.flexible()), GridItem(.flexible())]

    var body: some View {
         ScrollView {
             LazyVGrid(columns: columns) {
                 ForEach(0x1f600...0x1f679, id: \.self) { value in
                     Text(String(format: "%x", value))
                     Text(emoji(value))
                         .font(.largeTitle)
                 }
             }
         }
    }

    private func emoji(_ value: Int) -> String {
        guard let scalar = UnicodeScalar(value) else { return "?" }
        return String(Character(scalar))
    }
}
```

---

## GridItem

**URL:** https://sosumi.ai/documentation/swiftui/griditem?.md

**Contents:**
- Overview
- Conforms To
- Creating a grid item
- Inspecting grid item properties
- Dynamically arranging views in two dimensions

---
title: GridItem
description: A description of a row or a column in a lazy grid.
source: https://developer.apple.com/documentation/swiftui/griditem
timestamp: 2026-02-13T19:31:51.084Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A description of a row or a column in a lazy grid.

Use an array of `GridItem` instances to configure the layout of items in a lazy grid. Each grid item in the array specifies layout properties like size and spacing for the rows of a [Lazy HGrid](/documentation/swiftui/lazyhgrid) or the columns of a [Lazy VGrid](/documentation/swiftui/lazyvgrid). The following example defines four rows for a horizontal grid, each with different characteristics:

A lazy horizontal grid sets the width of each column based on the widest cell in the column. It can do this because it has access to all of the views in a given column at once. In the example above, the [Color](/documentation/swiftui/color) views always have the same fixed width, resulting in a uniform column width across the whole grid.

However, a lazy horizontal grid doesn’t generally have access to all the views in a row, because it generates new cells as people scroll through information in your app. Instead, it relies on a grid item for information about each row. The example above indicates a different fixed height for each row, and sets a different amount of spacing to appear after each row:

- [Copyable](/documentation/Swift/Copyable)
- [Equatable](/documentation/Swift/Equatable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [init(_:spacing:alignment:)](/documentation/swiftui/griditem/init(_:spacing:alignment:)) Creates a grid item with the specified size, spacing, and alignment.

- [alignment](/documentation/swiftui/griditem/alignment) The alignment to use when placing each view.
- [spacing](/documentation/swiftui/griditem/spacing) The spacing to the next item.
- [size](/documentation/swiftui/griditem/size-swift.property) The size of the item, which is the width of a column item or the height of a row item.
- [GridItem.Size](/documentation/swiftui/griditem/size-swift.enum) The size in the minor axis of one or more rows or columns in a grid layout.

- [LazyHGrid](/documentation/swiftui/lazyhgrid)
- [LazyVGrid](/documentation/swiftui/lazyvgrid)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct GridItem
```

Example 2 (swift):
```swift
struct GridItemDemo: View {
    let rows = [
        GridItem(.fixed(30), spacing: 1),
        GridItem(.fixed(60), spacing: 10),
        GridItem(.fixed(90), spacing: 20),
        GridItem(.fixed(10), spacing: 50)
    ]

    var body: some View {
        ScrollView(.horizontal) {
            LazyHGrid(rows: rows, spacing: 5) {
                ForEach(0...300, id: \.self) { _ in
                    Color.red.frame(width: 30)
                    Color.green.frame(width: 30)
                    Color.blue.frame(width: 30)
                    Color.yellow.frame(width: 30)
                }
            }
        }
    }
}
```

---

## GeometryReader

**URL:** https://sosumi.ai/documentation/swiftui/geometryreader?.md

**Contents:**
- Overview
- Conforms To
- Creating a geometry reader
- Measuring a view

---
title: GeometryReader
description: A container view that defines its content as a function of its own size and coordinate space.
source: https://developer.apple.com/documentation/swiftui/geometryreader
timestamp: 2026-02-13T19:32:07.253Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A container view that defines its content as a function of its own size and coordinate space.

This view returns a flexible preferred size to its parent layout.

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/geometryreader/init(content:))
- [content](/documentation/swiftui/geometryreader/content)

- [GeometryReader3D](/documentation/swiftui/geometryreader3d)
- [GeometryProxy](/documentation/swiftui/geometryproxy)
- [GeometryProxy3D](/documentation/swiftui/geometryproxy3d)
- [coordinateSpace(_:)](/documentation/swiftui/view/coordinatespace(_:))
- [CoordinateSpace](/documentation/swiftui/coordinatespace)
- [CoordinateSpaceProtocol](/documentation/swiftui/coordinatespaceprotocol)
- [PhysicalMetric](/documentation/swiftui/physicalmetric)
- [PhysicalMetricsConverter](/documentation/swiftui/physicalmetricsconverter)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct GeometryReader<Content> where Content : View
```

---

## LazyVStack

**URL:** https://sosumi.ai/documentation/swiftui/lazyvstack?.md

**Contents:**
- Overview
- Conforms To
- Creating a lazy-loading vertical stack
- Dynamically arranging views in one dimension

---
title: LazyVStack
description: A view that arranges its children in a line that grows vertically, creating items only as needed.
source: https://developer.apple.com/documentation/swiftui/lazyvstack
timestamp: 2026-02-13T19:31:43.084Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A view that arranges its children in a line that grows vertically, creating items only as needed.

The stack is “lazy,” in that the stack view doesn’t create items until it needs to render them onscreen.

In the following example, a [Scroll View](/documentation/swiftui/scrollview) contains a `LazyVStack` that consists of a vertical row of text views. The stack aligns to the leading edge of the scroll view, and uses default spacing between the text views.

- [View](/documentation/swiftui/view)

- [init(alignment:spacing:pinnedViews:content:)](/documentation/swiftui/lazyvstack/init(alignment:spacing:pinnedviews:content:)) Creates a lazy vertical stack view with the given spacing, vertical alignment, pinning behavior, and content.

- [Grouping data with lazy stack views](/documentation/swiftui/grouping-data-with-lazy-stack-views)
- [Creating performant scrollable stacks](/documentation/swiftui/creating-performant-scrollable-stacks)
- [LazyHStack](/documentation/swiftui/lazyhstack)
- [PinnedScrollableViews](/documentation/swiftui/pinnedscrollableviews)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct LazyVStack<Content> where Content : View
```

Example 2 (swift):
```swift
ScrollView {
    LazyVStack(alignment: .leading) {
        ForEach(1...100, id: \.self) {
            Text("Row \($0)")
        }
    }
}
```

---

## Divider

**URL:** https://sosumi.ai/documentation/swiftui/divider?.md

**Contents:**
- Overview
- Conforms To
- Creating a divider
- Separators

---
title: Divider
description: A visual element that can be used to separate other content.
source: https://developer.apple.com/documentation/swiftui/divider
timestamp: 2026-02-13T19:31:59.222Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A visual element that can be used to separate other content.

When contained in a stack, the divider extends across the minor axis of the stack, or horizontally when not in a stack.

- [View](/documentation/swiftui/view)

- [init()](/documentation/swiftui/divider/init())

- [Spacer](/documentation/swiftui/spacer)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Divider
```

---
