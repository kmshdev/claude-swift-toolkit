# Sidebar-Liquid-Glass-Clone - Layout And Spacing

**Pages:** 9

---

## frame(width:height:alignment:)

**URL:** https://sosumi.ai/documentation/swiftui/view/frame(width:height:alignment:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Influencing a view’s size

---
title: frame(width:height:alignment:)
description: Positions this view within an invisible frame with the specified size.
source: https://developer.apple.com/documentation/swiftui/view/frame(width:height:alignment:)
timestamp: 2026-02-13T01:05:26.958Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Positions this view within an invisible frame with the specified size.

A fixed width for the resulting view. If `width` is `nil`, the resulting view assumes this view’s sizing behavior.

A fixed height for the resulting view. If `height` is `nil`, the resulting view assumes this view’s sizing behavior.

The alignment of this view inside the resulting frame. Note that most alignment values have no apparent effect when the size of the frame happens to match that of this view.

A view with fixed dimensions of `width` and `height`, for the parameters that are non-`nil`.

Use this method to specify a fixed size for a view’s width, height, or both. If you only specify one of the dimensions, the resulting view assumes this view’s sizing behavior in the other dimension.

For example, the following code lays out an ellipse in a fixed 200 by 100 frame. Because a shape always occupies the space offered to it by the layout system, the first ellipse is 200x100 points. The second ellipse is laid out in a frame with only a fixed height, so it occupies that height, and whatever width the layout system offers to its parent.

`The alignment` parameter specifies this view’s alignment within the frame.

In the example above, the text is positioned at the top, leading corner of the frame. If the text is taller than the frame, its bounds may extend beyond the bottom of the frame’s bounds.

- [frame(depth:alignment:)](/documentation/swiftui/view/frame(depth:alignment:))
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:))
- [frame(minDepth:idealDepth:maxDepth:alignment:)](/documentation/swiftui/view/frame(mindepth:idealdepth:maxdepth:alignment:))
- [containerRelativeFrame(_:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:))
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
nonisolated func frame(width: CGFloat? = nil, height: CGFloat? = nil, alignment: Alignment = .center) -> some View
```

Example 2 (swift):
```swift
VStack {
    Ellipse()
        .fill(Color.purple)
        .frame(width: 200, height: 100)
    Ellipse()
        .fill(Color.blue)
        .frame(height: 100)
}
```

Example 3 (swift):
```swift
Text("Hello world!")
    .frame(width: 200, height: 30, alignment: .topLeading)
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
timestamp: 2026-02-13T01:05:35.133Z
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
timestamp: 2026-02-13T01:05:33.041Z
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
timestamp: 2026-02-13T01:05:28.650Z
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
timestamp: 2026-02-13T01:05:30.776Z
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
timestamp: 2026-02-13T01:05:37.224Z
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
timestamp: 2026-02-13T01:05:24.676Z
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

## ToolbarSpacer

**URL:** https://sosumi.ai/documentation/swiftui/toolbarspacer?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Populating a toolbar

---
title: ToolbarSpacer
description: A standard space item in toolbars.
source: https://developer.apple.com/documentation/swiftui/toolbarspacer
timestamp: 2026-02-13T01:05:55.667Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+

> A standard space item in toolbars.

A space item creates visual breaks in the toolbar between items. Spacers can have a standard fixed size or be flexible and push items apart.

Spacers can also be used in customizable toolbars:

Space items are customizable and can be added, removed, and rearranged by users. If a customizable toolbar supports a spacer of a given type, users can also add in multiple copies of that spacer from the customization panel.

- [CustomizableToolbarContent](/documentation/swiftui/customizabletoolbarcontent)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)

- [init(_:placement:)](/documentation/swiftui/toolbarspacer/init(_:placement:)) Creates a toolbar spacer item with the specified sizing behavior and placement.

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:))
- [ToolbarItem](/documentation/swiftui/toolbaritem)
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup)
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder)
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

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

## contentMargins(_:_:for:)

**URL:** https://sosumi.ai/documentation/swiftui/view/contentmargins(_:_:for:)?.md

**Contents:**
- Parameters
- Discussion
- Setting margins

---
title: contentMargins(_:_:for:)
description: Configures the content margin for a provided placement.
source: https://developer.apple.com/documentation/swiftui/view/contentmargins(_:_:for:)
timestamp: 2026-02-13T01:06:03.020Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

> Configures the content margin for a provided placement.

The edges to add the margins to.

The amount of margins to add.

Where the margins should be added.

Use this modifier to customize the content margins of different kinds of views. For example, you can use this modifier to customize the margins of scrollable views like [Scroll View](/documentation/swiftui/scrollview). In the following example, the scroll view will automatically inset its content by the safe area plus an additional 20 points on the leading and trailing edge.

You can provide a [Content Margin Placement](/documentation/swiftui/contentmarginplacement) to target specific parts of a view to customize. For example, provide a [scroll Content](/documentation/swiftui/contentmarginplacement/scrollcontent) placement to inset the content of a [Text Editor](/documentation/swiftui/texteditor) without affecting the insets of its scroll indicators.

Similarly, you can customize the insets of scroll indicators separately from scroll content. Consider doing this when applying a custom clip shape that may clip the indicators.

When applying multiple contentMargins modifiers, modifiers with the same placement will override modifiers higher up in the view hierarchy.

- [contentMargins(_:for:)](/documentation/swiftui/view/contentmargins(_:for:))
- [ContentMarginPlacement](/documentation/swiftui/contentmarginplacement)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func contentMargins(_ edges: Edge.Set = .all, _ insets: EdgeInsets, for placement: ContentMarginPlacement = .automatic) -> some View
```

Example 2 (swift):
```swift
ScrollView(.horizontal) {
    // ...
}
.contentMargins(.horizontal, 20.0)
```

Example 3 (swift):
```swift
TextEditor(text: $text)
    .contentMargins(.horizontal, 20.0, for: .scrollContent)
```

Example 4 (swift):
```swift
ScrollView {
    // ...
}
.clipShape(.rect(cornerRadius: 20.0))
.contentMargins(10.0, for: .scrollIndicators)
```

---
