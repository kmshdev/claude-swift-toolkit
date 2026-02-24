# Neuralforge-Main-Content - Card Component

**Pages:** 5

---

## shadow(color:radius:x:y:)

**URL:** https://sosumi.ai/documentation/swiftui/view/shadow(color:radius:x:y:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Applying blur and shadows

---
title: shadow(color:radius:x:y:)
description: Adds a shadow to this view.
source: https://developer.apple.com/documentation/swiftui/view/shadow(color:radius:x:y:)
timestamp: 2026-02-13T03:43:31.177Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds a shadow to this view.

A measure of how much to blur the shadow. Larger values result in more blur.

An amount to offset the shadow horizontally from the view.

An amount to offset the shadow vertically from the view.

A view that adds a shadow to this view.

Use this modifier to add a shadow of a specified color behind a view. You can offset the shadow from its view independently in the horizontal and vertical dimensions using the `x` and `y` parameters. You can also blur the edges of the shadow using the `radius` parameter. Use a radius of zero to create a sharp shadow. Larger radius values produce softer shadows.

The example below creates a grid of boxes with varying offsets and blur. Each box displays its radius and offset values for reference.

The example above uses [primary](/documentation/swiftui/color/primary) as the color to make the shadow easy to see for the purpose of illustration. In practice, you might prefer something more subtle, like [gray](/documentation/swiftui/color/gray). If you don’t specify a color, the method uses a semi-transparent black.

- [blur(radius:opaque:)](/documentation/swiftui/view/blur(radius:opaque:))
- [ColorMatrix](/documentation/swiftui/colormatrix)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func shadow(color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33), radius: CGFloat, x: CGFloat = 0, y: CGFloat = 0) -> some View
```

Example 2 (swift):
```swift
struct Shadow: View {
    let steps = [0, 5, 10]

    var body: some View {
        VStack(spacing: 50) {
            ForEach(steps, id: \.self) { offset in
                HStack(spacing: 50) {
                    ForEach(steps, id: \.self) { radius in
                        Color.blue
                            .shadow(
                                color: .primary,
                                radius: CGFloat(radius),
                                x: CGFloat(offset), y: CGFloat(offset))
                            .overlay {
                                VStack {
                                    Text("\(radius)")
                                    Text("(\(offset), \(offset))")
                                }
                            }
                    }
                }
            }
        }
    }
}
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
timestamp: 2026-02-13T03:43:20.699Z
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

## groupBoxStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/groupboxstyle(_:)?.md

**Contents:**
- Parameters
- Grouping views into a box

---
title: groupBoxStyle(_:)
description: Sets the style for group boxes within this view.
source: https://developer.apple.com/documentation/swiftui/view/groupboxstyle(_:)
timestamp: 2026-02-13T03:43:46.028Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+

> Sets the style for group boxes within this view.

The style to apply to boxes within this view.

- [GroupBox](/documentation/swiftui/groupbox)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func groupBoxStyle<S>(_ style: S) -> some View where S : GroupBoxStyle
```

---

## border(_:width:)

**URL:** https://sosumi.ai/documentation/swiftui/view/border(_:width:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Styling content

---
title: border(_:width:)
description: Adds a border to this view with the specified style and width.
source: https://developer.apple.com/documentation/swiftui/view/border(_:width:)
timestamp: 2026-02-13T03:43:33.315Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds a border to this view with the specified style and width.

A value that conforms to the [Shape Style](/documentation/swiftui/shapestyle) protocol, like a [Color](/documentation/swiftui/color) or [Hierarchical Shape Style](/documentation/swiftui/hierarchicalshapestyle), that SwiftUI uses to fill the border.

The thickness of the border. The default is 1 pixel.

A view that adds a border with the specified style and width to this view.

Use this modifier to draw a border of a specified width around the view’s frame. By default, the border appears inside the bounds of this view. For example, you can add a four-point wide border covers the text:

To place a border around the outside of this view, apply padding of the same width before adding the border:

- [foregroundStyle(_:)](/documentation/swiftui/view/foregroundstyle(_:))
- [foregroundStyle(_:_:)](/documentation/swiftui/view/foregroundstyle(_:_:))
- [foregroundStyle(_:_:_:)](/documentation/swiftui/view/foregroundstyle(_:_:_:))
- [backgroundStyle(_:)](/documentation/swiftui/view/backgroundstyle(_:))
- [backgroundStyle](/documentation/swiftui/environmentvalues/backgroundstyle)
- [ShapeStyle](/documentation/swiftui/shapestyle)
- [AnyShapeStyle](/documentation/swiftui/anyshapestyle)
- [Gradient](/documentation/swiftui/gradient)
- [MeshGradient](/documentation/swiftui/meshgradient)
- [AnyGradient](/documentation/swiftui/anygradient)
- [ShadowStyle](/documentation/swiftui/shadowstyle)
- [Glass](/documentation/swiftui/glass)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func border<S>(_ content: S, width: CGFloat = 1) -> some View where S : ShapeStyle
```

Example 2 (swift):
```swift
Text("Purple border inside the view bounds.")
    .border(Color.purple, width: 4)
```

Example 3 (swift):
```swift
Text("Purple border outside the view bounds.")
    .padding(4)
    .border(Color.purple, width: 4)
```

---

## GroupBox

**URL:** https://sosumi.ai/documentation/swiftui/groupbox?.md

**Contents:**
- Overview
- Conforms To
- Creating a group box
- Creating a group box from a configuration
- Deprecated initializers
- Grouping views into a box

---
title: GroupBox
description: A stylized view, with an optional label, that visually collects a logical grouping of content.
source: https://developer.apple.com/documentation/swiftui/groupbox
timestamp: 2026-02-13T03:43:43.781Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, visionOS 1.0+

> A stylized view, with an optional label, that visually collects a logical grouping of content.

Use a group box when you want to visually distinguish a portion of your user interface with an optional title for the boxed content.

The following example sets up a `GroupBox` with the label “End-User Agreement”, and a long `agreementText` string in a [Text](/documentation/swiftui/text) view wrapped by a [Scroll View](/documentation/swiftui/scrollview). The box also contains a [Toggle](/documentation/swiftui/toggle) for the user to interact with after reading the text.

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/groupbox/init(content:)) Creates an unlabeled group box with the provided view content.
- [init(content:label:)](/documentation/swiftui/groupbox/init(content:label:)) Creates a group box with the provided label and view content.
- [init(_:content:)](/documentation/swiftui/groupbox/init(_:content:)) Creates a group box with the provided view content and title.

- [init(_:)](/documentation/swiftui/groupbox/init(_:)) Creates a group box based on a style configuration.

- [init(label:content:)](/documentation/swiftui/groupbox/init(label:content:))

- [groupBoxStyle(_:)](/documentation/swiftui/view/groupboxstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct GroupBox<Label, Content> where Label : View, Content : View
```

Example 2 (swift):
```swift
var body: some View {
    GroupBox(label:
        Label("End-User Agreement", systemImage: "building.columns")
    ) {
        ScrollView(.vertical, showsIndicators: true) {
            Text(agreementText)
                .font(.footnote)
        }
        .frame(height: 100)
        Toggle(isOn: $userAgreed) {
            Text("I agree to the above terms")
        }
    }
}
```

---
