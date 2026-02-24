# Sidebar-Liquid-Glass-Clone - Badges And Indicators

**Pages:** 4

---

## Circle

**URL:** https://sosumi.ai/documentation/swiftui/circle?.md

**Contents:**
- Overview
- Conforms To
- Creating a circle
- Creating circular shapes

---
title: Circle
description: A circle centered on the frame of the view containing it.
source: https://developer.apple.com/documentation/swiftui/circle
timestamp: 2026-02-13T01:05:43.164Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A circle centered on the frame of the view containing it.

The circle’s radius equals half the length of the frame rectangle’s smallest edge.

- [Animatable](/documentation/swiftui/animatable)
- [BitwiseCopyable](/documentation/Swift/BitwiseCopyable)
- [ChartSymbolShape](/documentation/Charts/ChartSymbolShape)
- [Copyable](/documentation/Swift/Copyable)
- [InsettableShape](/documentation/swiftui/insettableshape)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init()](/documentation/swiftui/circle/init()) Creates a new circle shape.

- [Ellipse](/documentation/swiftui/ellipse)
- [Capsule](/documentation/swiftui/capsule)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Circle
```

---

## Label

**URL:** https://sosumi.ai/documentation/swiftui/label?.md

**Contents:**
- Overview
- Conforms To
- Creating a label
- Displaying text

---
title: Label
description: A standard label for user interface items, consisting of an icon with a title.
source: https://developer.apple.com/documentation/swiftui/label
timestamp: 2026-02-13T01:04:24.535Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A standard label for user interface items, consisting of an icon with a title.

One of the most common and recognizable user interface components is the combination of an icon and a label. This idiom appears across many kinds of apps and shows up in collections, lists, menus of action items, and disclosable lists, just to name a few.

You create a label, in its simplest form, by providing a title and the name of an image, such as an icon from the [sf](/design/Human-Interface-Guidelines/sf-symbols) collection:

You can also apply styles to labels in several ways. In the case of dynamic changes to the view after device rotation or change to a window size you might want to show only the text portion of the label using the [title Only](/documentation/swiftui/labelstyle/titleonly) label style:

Conversely, there’s also an icon-only label style:

Some containers might apply a different default label style, such as only showing icons within toolbars on macOS and iOS. To opt in to showing both the title and the icon, you can apply the [title And Icon](/documentation/swiftui/labelstyle/titleandicon) label style:

You can also create a customized label style by modifying an existing style; this example adds a red border to the default label style:

For more extensive customization or to create a completely new label style, you’ll need to adopt the [Label Style](/documentation/swiftui/labelstyle) protocol and implement a [Label Style Configuration](/documentation/swiftui/labelstyleconfiguration) for the new style.

To apply a common label style to a group of labels, apply the style to the view hierarchy that contains the labels:

It’s also possible to make labels using views to compose the label’s icon programmatically, rather than using a pre-made image. In this example, the icon portion of the label uses a filled [Circle](/documentation/swiftui/circle) overlaid with the user’s initials:

- [View](/documentation/swiftui/view)

- [init(_:image:)](/documentation/swiftui/label/init(_:image:)) Creates a label with an icon image and a title generated from a localized string.
- [init(_:systemImage:)](/documentation/swiftui/label/init(_:systemimage:)) Creates a label with a system icon image and a title generated from a localized string.
- [init(title:icon:)](/documentation/swiftui/label/init(title:icon:)) Creates a label with a custom title and icon.
- [init(_:)](/documentation/swiftui/label/init(_:)) Creates a label representing a family activity application.
- [init(_:image:)](/documentation/swiftui/label/init(_:image:)) Creates a label with an icon image and a title generated from a localized string.

- [Text](/documentation/swiftui/text)
- [labelStyle(_:)](/documentation/swiftui/view/labelstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Label<Title, Icon> where Title : View, Icon : View
```

Example 2 (swift):
```swift
Label("Lightning", systemImage: "bolt.fill")
```

Example 3 (swift):
```swift
Label("Lightning", systemImage: "bolt.fill")
    .labelStyle(.titleOnly)
```

Example 4 (swift):
```swift
Label("Lightning", systemImage: "bolt.fill")
    .labelStyle(.iconOnly)
```

---

## overlay(alignment:content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/overlay(alignment:content:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Layering views

---
title: overlay(alignment:content:)
description: Layers the views that you specify in front of this view.
source: https://developer.apple.com/documentation/swiftui/view/overlay(alignment:content:)
timestamp: 2026-02-13T01:04:45.687Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Layers the views that you specify in front of this view.

The alignment that the modifier uses to position the implicit [ZStack](/documentation/swiftui/zstack) that groups the foreground views. The default is [center](/documentation/swiftui/alignment/center).

A [View Builder](/documentation/swiftui/viewbuilder) that you use to declare the views to draw in front of this view, stacked in the order that you list them. The last view that you list appears at the front of the stack.

A view that uses the specified content as a foreground.

Use this modifier to place one or more views in front of another view. For example, you can place a group of stars on a [Rounded Rectangle](/documentation/swiftui/roundedrectangle):

The example above assumes that you’ve defined a `Star` view with a parameterized color:

By setting different `alignment` values for each modifier, you make the stars appear in different places on the rectangle:

If you specify more than one view in the `content` closure, the modifier collects all of the views in the closure into an implicit [ZStack](/documentation/swiftui/zstack), taking them in order from back to front. For example, you can place a star and a [Circle](/documentation/swiftui/circle) on a field of [blue](/documentation/swiftui/shapestyle/blue):

Both the overlay modifier and the implicit [ZStack](/documentation/swiftui/zstack) composed from the overlay content — the circle and the star — use a default [center](/documentation/swiftui/alignment/center) alignment. The star appears centered on the circle, and both appear as a composite view centered in front of the square:

If you specify an alignment for the overlay, it applies to the implicit stack rather than to the individual views in the closure. You can see this if you add the [bottom](/documentation/swiftui/alignment/bottom) alignment:

The circle and the star move down as a unit to align the stack’s bottom edge with the bottom edge of the square, while the star remains centered on the circle:

To control the placement of individual items inside the `content` closure, either use a different overlay modifier for each item, as the earlier example of stars in the corners of a rectangle demonstrates, or add an explicit [ZStack](/documentation/swiftui/zstack) inside the content closure with its own alignment:

The stack alignment ensures that the star’s bottom edge aligns with the circle’s, while the overlay aligns the composite view with the square:

You can achieve layering without an overlay modifier by putting both the modified view and the overlay content into a [ZStack](/documentation/swiftui/zstack). This can produce a simpler view hierarchy, but changes the layout priority that SwiftUI applies to the views. Use the overlay modifier when you want the modified view to dominate the layout.

If you want to specify a [Shape Style](/documentation/swiftui/shapestyle) like a [Color](/documentation/swiftui/color) or a [Material](/documentation/swiftui/material) as the overlay, use [overlay(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/overlay(_:ignoressafeareaedges:)) instead. To specify a [Shape](/documentation/swiftui/shape), use [overlay(_:in:fillStyle:)](/documentation/swiftui/view/overlay(_:in:fillstyle:)).

- [Adding a background to your view](/documentation/swiftui/adding-a-background-to-your-view)
- [ZStack](/documentation/swiftui/zstack)
- [zIndex(_:)](/documentation/swiftui/view/zindex(_:))
- [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:))
- [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:))
- [background(ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(ignoressafeareaedges:))
- [background(_:in:fillStyle:)](/documentation/swiftui/view/background(_:in:fillstyle:))
- [background(in:fillStyle:)](/documentation/swiftui/view/background(in:fillstyle:))
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
nonisolated func overlay<V>(alignment: Alignment = .center, @ViewBuilder content: () -> V) -> some View where V : View
```

Example 2 (swift):
```swift
RoundedRectangle(cornerRadius: 8)
    .frame(width: 200, height: 100)
    .overlay(alignment: .topLeading) { Star(color: .red) }
    .overlay(alignment: .topTrailing) { Star(color: .yellow) }
    .overlay(alignment: .bottomLeading) { Star(color: .green) }
    .overlay(alignment: .bottomTrailing) { Star(color: .blue) }
```

Example 3 (swift):
```swift
struct Star: View {
    var color = Color.yellow

    var body: some View {
        Image(systemName: "star.fill")
            .foregroundStyle(color)
    }
}
```

Example 4 (swift):
```swift
Color.blue
    .frame(width: 200, height: 200)
    .overlay {
        Circle()
            .frame(width: 100, height: 100)
        Star()
    }
```

---

## badge(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/badge(_:)-6k2u9?.md

**Contents:**
- Parameters
- Discussion

---
title: badge(_:)
description: Generates a badge for the view from a text view.
source: https://developer.apple.com/documentation/swiftui/view/badge(_:)-6k2u9
timestamp: 2026-02-13T01:04:26.477Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+

> Generates a badge for the view from a text view.

An optional [Text](/documentation/swiftui/text) view to display as a badge. Set the value to `nil` to hide the badge.

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

Use this initializer when you want to style a [Text](/documentation/swiftui/text) view for use as a badge. The following example customizes the badge with the [monospacedDigit()](/documentation/swiftui/text/monospaceddigit()), [foregroundColor(_:)](/documentation/swiftui/text/foregroundcolor(_:)), and [bold()](/documentation/swiftui/text/bold()) modifiers.

Styling the text view has no effect when the badge appears in a [Tab View](/documentation/swiftui/tabview).

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func badge(_ label: Text?) -> some View
```

Example 2 (swift):
```swift
var body: some View {
    let badgeView = Text("\(recentItems.count)")
        .monospacedDigit()
        .foregroundColor(.red)
        .bold()

    List {
        Text("Recents")
            .badge(badgeView)
        Text("Favorites")
    }
}
```

---
