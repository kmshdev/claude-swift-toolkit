# Neuralforge-Main-Content - Grid And Layout

**Pages:** 13

---

## fixedSize(horizontal:vertical:)

**URL:** https://sosumi.ai/documentation/swiftui/view/fixedsize(horizontal:vertical:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Influencing a view’s size

---
title: fixedSize(horizontal:vertical:)
description: Fixes this view at its ideal size in the specified dimensions.
source: https://developer.apple.com/documentation/swiftui/view/fixedsize(horizontal:vertical:)
timestamp: 2026-02-13T03:44:09.491Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Fixes this view at its ideal size in the specified dimensions.

A Boolean value that indicates whether to fix the width of the view.

A Boolean value that indicates whether to fix the height of the view.

A view that fixes this view at its ideal size in the dimensions specified by `horizontal` and `vertical`.

This function behaves like [fixedSize()](/documentation/swiftui/view/fixedsize()), except with `fixedSize(horizontal:vertical:)` the fixing of the axes can be optionally specified in one or both dimensions. For example, if you horizontally fix a text view before wrapping it in the frame view, you’re telling the text view to maintain its ideal *width*. The view calculates this to be the space needed to represent the entire string.

This can result in the view exceeding the parent’s bounds, which may or may not be the effect you want.

- [frame(width:height:alignment:)](/documentation/swiftui/view/frame(width:height:alignment:))
- [frame(depth:alignment:)](/documentation/swiftui/view/frame(depth:alignment:))
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:))
- [frame(minDepth:idealDepth:maxDepth:alignment:)](/documentation/swiftui/view/frame(mindepth:idealdepth:maxdepth:alignment:))
- [containerRelativeFrame(_:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:))
- [containerRelativeFrame(_:alignment:_:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:_:))
- [containerRelativeFrame(_:count:span:spacing:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:count:span:spacing:alignment:))
- [fixedSize()](/documentation/swiftui/view/fixedsize())
- [layoutPriority(_:)](/documentation/swiftui/view/layoutpriority(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func fixedSize(horizontal: Bool, vertical: Bool) -> some View
```

Example 2 (swift):
```swift
Text("A single line of text, too long to fit in a box.")
    .fixedSize(horizontal: true, vertical: false)
    .frame(width: 200, height: 200)
    .border(Color.gray)
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
timestamp: 2026-02-13T03:42:45.614Z
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
timestamp: 2026-02-13T03:42:29.111Z
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

## Grid

**URL:** https://sosumi.ai/documentation/swiftui/grid?.md

**Contents:**
- Overview
  - Multicolumn cells
  - Column count
  - Cell spacing and alignment
  - Performance considerations
- Conforms To
- Creating a grid
- Statically arranging views in two dimensions

---
title: Grid
description: A container view that arranges other views in a two dimensional layout.
source: https://developer.apple.com/documentation/swiftui/grid
timestamp: 2026-02-13T03:42:33.416Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> A container view that arranges other views in a two dimensional layout.

Create a two dimensional layout by initializing a `Grid` with a collection of [Grid Row](/documentation/swiftui/gridrow) structures. The first view in each grid row appears in the grid’s first column, the second view in the second column, and so on. The following example creates a grid with two rows and two columns:

A grid and its rows behave something like a collection of [HStack](/documentation/swiftui/hstack) instances wrapped in a [VStack](/documentation/swiftui/vstack). However, the grid handles row and column creation as a single operation, which applies alignment and spacing to cells, rather than first to rows and then to a column of unrelated rows. The grid produced by the example above demonstrates this:

> [!NOTE]
> If you need a grid that conforms to the [Layout](/documentation/swiftui/layout) protocol, like when you want to create a conditional layout using [Any Layout](/documentation/swiftui/anylayout), use [Grid Layout](/documentation/swiftui/gridlayout) instead.

If you provide a view rather than a [Grid Row](/documentation/swiftui/gridrow) as an element in the grid’s content, the grid uses the view to create a row that spans all of the grid’s columns. For example, you can add a [Divider](/documentation/swiftui/divider) between the rows of the previous example:

Because a divider takes as much horizontal space as its parent offers, the entire grid widens to fill the width offered by its parent view.

To prevent a flexible view from taking more space on a given axis than the other cells in a row or column require, add the [gridCellUnsizedAxes(_:)](/documentation/swiftui/view/gridcellunsizedaxes(_:)) view modifier to the view:

This restores the grid to the width that the text and images require:

To make a cell span a specific number of columns rather than the whole grid, use the [gridCellColumns(_:)](/documentation/swiftui/view/gridcellcolumns(_:)) modifier on a view that’s contained inside a [Grid Row](/documentation/swiftui/gridrow).

The grid’s column count grows to handle the row with the largest number of columns. If you create rows with different numbers of columns, the grid adds empty cells to the trailing edge of rows that have fewer columns. The example below creates three rows with different column counts:

The resulting grid has as many columns as the widest row, adding empty cells to rows that don’t specify enough views:

The grid sets the width of all the cells in a column to match the needs of column’s widest cell. In the example above, the width of the first column depends on the width of the widest [Text](/documentation/swiftui/text) view that the column contains. The other columns, which contain flexible [Color](/documentation/swiftui/color) views, share the remaining horizontal space offered by the grid’s parent view equally.

Similarly, the tallest cell in a row sets the height of the entire row. The cells in the first column of the grid above need only the height required for each string, but the [Color](/documentation/swiftui/color) cells expand to equally share the total height available to the grid. As a result, the color cells determine the row heights.

You can control the spacing between cells in both the horizontal and vertical dimensions and set a default alignment for the content in all the grid cells when you initialize the grid using the [init(alignment:horizontalSpacing:verticalSpacing:content:)](/documentation/swiftui/grid/init(alignment:horizontalspacing:verticalspacing:content:)) initializer. Consider a modified version of the previous example:

This configuration causes all of the cells to use [bottom](/documentation/swiftui/alignment/bottom) alignment — which only affects the text cells because the colors fill their cells completely — and it reduces the spacing between cells:

You can override the alignment of specific cells or groups of cells. For example, you can change the horizontal alignment of the cells in a column by adding the [gridColumnAlignment(_:)](/documentation/swiftui/view/gridcolumnalignment(_:)) modifier, or the vertical alignment of the cells in a row by configuring the row’s [init(alignment:content:)](/documentation/swiftui/gridrow/init(alignment:content:)) initializer. You can also align a single cell with the [gridCellAnchor(_:)](/documentation/swiftui/view/gridcellanchor(_:)) modifier.

A grid can size its rows and columns correctly because it renders all of its child views immediately. If your app exhibits poor performance when it first displays a large grid that appears inside a [Scroll View](/documentation/swiftui/scrollview), consider switching to a [Lazy VGrid](/documentation/swiftui/lazyvgrid) or [Lazy HGrid](/documentation/swiftui/lazyhgrid) instead.

Lazy grids render their cells when SwiftUI needs to display them, rather than all at once. This reduces the initial cost of displaying a large scrollable grid that’s never fully visible, but also reduces the grid’s ability to optimally lay out cells. Switch to a lazy grid only if profiling your code shows a worthwhile performance improvement.

- [Copyable](/documentation/Swift/Copyable)
- [View](/documentation/swiftui/view)

- [init(alignment:horizontalSpacing:verticalSpacing:content:)](/documentation/swiftui/grid/init(alignment:horizontalspacing:verticalspacing:content:)) Creates a grid with the specified spacing, alignment, and child views.

- [GridRow](/documentation/swiftui/gridrow)
- [gridCellColumns(_:)](/documentation/swiftui/view/gridcellcolumns(_:))
- [gridCellAnchor(_:)](/documentation/swiftui/view/gridcellanchor(_:))
- [gridCellUnsizedAxes(_:)](/documentation/swiftui/view/gridcellunsizedaxes(_:))
- [gridColumnAlignment(_:)](/documentation/swiftui/view/gridcolumnalignment(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Grid<Content> where Content : View
```

Example 2 (swift):
```swift
Grid {
    GridRow {
        Text("Hello")
        Image(systemName: "globe")
    }
    GridRow {
        Image(systemName: "hand.wave")
        Text("World")
    }
}
```

Example 3 (swift):
```swift
Grid {
    GridRow {
        Text("Hello")
        Image(systemName: "globe")
    }
    Divider()
    GridRow {
        Image(systemName: "hand.wave")
        Text("World")
    }
}
```

Example 4 (swift):
```swift
Divider()
    .gridCellUnsizedAxes(.horizontal)
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
timestamp: 2026-02-13T03:42:43.658Z
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
timestamp: 2026-02-13T03:42:39.895Z
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
timestamp: 2026-02-13T03:42:41.611Z
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

## containerRelativeFrame(_:alignment:)

**URL:** https://sosumi.ai/documentation/swiftui/view/containerrelativeframe(_:alignment:)?.md

**Contents:**
- Discussion
- Influencing a view’s size

---
title: containerRelativeFrame(_:alignment:)
description: Positions this view within an invisible frame with a size relative to the nearest container.
source: https://developer.apple.com/documentation/swiftui/view/containerrelativeframe(_:alignment:)
timestamp: 2026-02-13T03:44:07.311Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

> Positions this view within an invisible frame with a size relative to the nearest container.

Use this modifier to specify a size for a view’s width, height, or both that is dependent on the size of the nearest container. Different things can represent a “container” including:

- The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.
- A column of a NavigationSplitView
- A NavigationStack
- A tab of a TabView
- A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones listed above subtracting any safe area insets that might be applied to that container.

The following example will have each purple rectangle occupy the full size of the screen on iOS:

Use the [containerRelativeFrame(_:count:span:spacing:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:count:span:spacing:alignment:)) modifier to size a view such that multiple views will be visible in the container. When using this modifier, the count refers to the total number of rows or columns that the length of the container size in a particular axis should be divided into. The span refers to the number of rows or columns that the modified view should actually occupy. Thus the size of the element can be described like so:

The following example only uses the nearest container size in the horizontal axis, allowing the vertical axis to be determined using the [aspectRatio(_:contentMode:)](/documentation/swiftui/view/aspectratio(_:contentmode:)) modifier.

Use the [containerRelativeFrame(_:alignment:_:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:_:)) modifier to apply your own custom logic to adjust the size of the nearest container for your view. The following example will result in the container frame’s width being divided by 3 and using that value as the width of the purple rectangle.

- [frame(width:height:alignment:)](/documentation/swiftui/view/frame(width:height:alignment:))
- [frame(depth:alignment:)](/documentation/swiftui/view/frame(depth:alignment:))
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:))
- [frame(minDepth:idealDepth:maxDepth:alignment:)](/documentation/swiftui/view/frame(mindepth:idealdepth:maxdepth:alignment:))
- [containerRelativeFrame(_:alignment:_:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:_:))
- [containerRelativeFrame(_:count:span:spacing:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:count:span:spacing:alignment:))
- [fixedSize()](/documentation/swiftui/view/fixedsize())
- [fixedSize(horizontal:vertical:)](/documentation/swiftui/view/fixedsize(horizontal:vertical:))
- [layoutPriority(_:)](/documentation/swiftui/view/layoutpriority(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func containerRelativeFrame(_ axes: Axis.Set, alignment: Alignment = .center) -> some View
```

Example 2 (swift):
```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 0.0) {
        ForEach(items) { item in
            Rectangle()
                .fill(.purple)
                .containerRelativeFrame([.horizontal, .vertical])
        }
    }
}
```

Example 3 (swift):
```swift
let availableWidth = (containerWidth - (spacing * (count - 1)))
let columnWidth = (availableWidth / count)
let itemWidth = (columnWidth * span) + ((span - 1) * spacing)
```

Example 4 (swift):
```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 10.0) {
        ForEach(items) { item in
            Rectangle()
                .fill(.purple)
                .aspectRatio(3.0 / 2.0, contentMode: .fit)
                .containerRelativeFrame(
                    .horizontal, count: 4, span: 3, spacing: 10.0)
        }
    }
}
.safeAreaPadding(.horizontal, 20.0)
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
timestamp: 2026-02-13T03:42:27.014Z
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
timestamp: 2026-02-13T03:42:31.023Z
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
timestamp: 2026-02-13T03:42:37.605Z
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
timestamp: 2026-02-13T03:42:47.585Z
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

## layoutPriority(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/layoutpriority(_:)?.md

**Contents:**
- Parameters
- Discussion
- Influencing a view’s size

---
title: layoutPriority(_:)
description: Sets the priority by which a parent layout should apportion space to this child.
source: https://developer.apple.com/documentation/swiftui/view/layoutpriority(_:)
timestamp: 2026-02-13T03:44:11.597Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the priority by which a parent layout should apportion space to this child.

The priority by which a parent layout apportions space to the child.

Views typically have a default priority of `0` which causes space to be apportioned evenly to all sibling views. Raising a view’s layout priority encourages the higher priority view to shrink later when the group is shrunk and stretch sooner when the group is stretched.

In the example above, the first [Text](/documentation/swiftui/text) element has the default priority `0` which causes its view to shrink dramatically due to the higher priority of the second [Text](/documentation/swiftui/text) element, even though all of their other attributes (font, font size and character count) are the same.

A parent layout offers the child views with the highest layout priority all the space offered to the parent minus the minimum space required for all its lower-priority children.

- [frame(width:height:alignment:)](/documentation/swiftui/view/frame(width:height:alignment:))
- [frame(depth:alignment:)](/documentation/swiftui/view/frame(depth:alignment:))
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:))
- [frame(minDepth:idealDepth:maxDepth:alignment:)](/documentation/swiftui/view/frame(mindepth:idealdepth:maxdepth:alignment:))
- [containerRelativeFrame(_:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:))
- [containerRelativeFrame(_:alignment:_:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:_:))
- [containerRelativeFrame(_:count:span:spacing:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:count:span:spacing:alignment:))
- [fixedSize()](/documentation/swiftui/view/fixedsize())
- [fixedSize(horizontal:vertical:)](/documentation/swiftui/view/fixedsize(horizontal:vertical:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func layoutPriority(_ value: Double) -> some View
```

Example 2 (swift):
```swift
HStack {
    Text("This is a moderately long string.")
        .font(.largeTitle)
        .border(Color.gray)

    Spacer()

    Text("This is a higher priority string.")
        .font(.largeTitle)
        .layoutPriority(1)
        .border(Color.gray)
}
```

---
