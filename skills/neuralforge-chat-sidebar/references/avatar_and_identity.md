# Neuralforge-Chat-Sidebar - Avatar And Identity

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
timestamp: 2026-02-13T01:41:30.275Z
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

## AsyncImage

**URL:** https://sosumi.ai/documentation/swiftui/asyncimage?.md

**Contents:**
- Overview
- Conforms To
- Loading an image
- Loading an image in phases
- Loading images asynchronously

---
title: AsyncImage
description: A view that asynchronously loads and displays an image.
source: https://developer.apple.com/documentation/swiftui/asyncimage
timestamp: 2026-02-13T01:41:25.959Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> A view that asynchronously loads and displays an image.

This view uses the shared [URLSession](/documentation/Foundation/URLSession) instance to load an image from the specified URL, and then display it. For example, you can display an icon that’s stored on a server:

Until the image loads, the view displays a standard placeholder that fills the available space. After the load completes successfully, the view updates to display the image. In the example above, the icon is smaller than the frame, and so appears smaller than the placeholder.

You can specify a custom placeholder using [init(url:scale:content:placeholder:)](/documentation/swiftui/asyncimage/init(url:scale:content:placeholder:)). With this initializer, you can also use the `content` parameter to manipulate the loaded image. For example, you can add a modifier to make the loaded image resizable:

For this example, SwiftUI shows a [Progress View](/documentation/swiftui/progressview) first, and then the image scaled to fit in the specified frame:

> [!IMPORTANT]
> You can’t apply image-specific modifiers, like [resizable(capInsets:resizingMode:)](/documentation/swiftui/image/resizable(capinsets:resizingmode:)), directly to an `AsyncImage`. Instead, apply them to the [Image](/documentation/swiftui/image) instance that your `content` closure gets when defining the view’s appearance.

To gain more control over the loading process, use the [init(url:scale:transaction:content:)](/documentation/swiftui/asyncimage/init(url:scale:transaction:content:)) initializer, which takes a `content` closure that receives an [Async Image Phase](/documentation/swiftui/asyncimagephase) to indicate the state of the loading operation. Return a view that’s appropriate for the current phase:

- [View](/documentation/swiftui/view)

- [init(url:scale:)](/documentation/swiftui/asyncimage/init(url:scale:)) Loads and displays an image from the specified URL.
- [init(url:scale:content:placeholder:)](/documentation/swiftui/asyncimage/init(url:scale:content:placeholder:)) Loads and displays a modifiable image from the specified URL using a custom placeholder until the image loads.

- [init(url:scale:transaction:content:)](/documentation/swiftui/asyncimage/init(url:scale:transaction:content:)) Loads and displays a modifiable image from the specified URL in phases.

- [AsyncImagePhase](/documentation/swiftui/asyncimagephase)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct AsyncImage<Content> where Content : View
```

Example 2 (swift):
```swift
AsyncImage(url: URL(string: "https://example.com/icon.png"))
    .frame(width: 200, height: 200)
```

Example 3 (swift):
```swift
AsyncImage(url: URL(string: "https://example.com/icon.png")) { image in
    image.resizable()
} placeholder: {
    ProgressView()
}
.frame(width: 50, height: 50)
```

Example 4 (swift):
```swift
AsyncImage(url: URL(string: "https://example.com/icon.png")) { phase in
    if let image = phase.image {
        image // Displays the loaded image.
    } else if phase.error != nil {
        Color.red // Indicates an error.
    } else {
        Color.blue // Acts as a placeholder.
    }
}
```

---

## Image

**URL:** https://sosumi.ai/documentation/swiftui/image?.md

**Contents:**
- Overview
  - Making images accessible
- Conforms To
- Creating an image
- Creating an image for use as a control
- Creating an image for decorative use
- Creating a system symbol image
- Creating an image from another image
- Creating an image from drawing instructions
- Resizing images

---
title: Image
description: A view that displays an image.
source: https://developer.apple.com/documentation/swiftui/image
timestamp: 2026-02-13T01:41:23.916Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A view that displays an image.

Use an `Image` instance when you want to add images to your SwiftUI app. You can create images from many sources:

- Image files in your app’s asset library or bundle. Supported types include PNG, JPEG, HEIC, and more.
- Instances of platform-specific image types, like [UIImage](/documentation/UIKit/UIImage) and [NSImage](/documentation/AppKit/NSImage).
- A bitmap stored in a Core Graphics [CGImage](/documentation/CoreGraphics/CGImage) instance.
- System graphics from the SF Symbols set.

The following example shows how to load an image from the app’s asset library or bundle and scale it to fit within its container:

You can use methods on the `Image` type as well as standard view modifiers to adjust the size of the image to fit your app’s interface. Here, the `Image` type’s [resizable(capInsets:resizingMode:)](/documentation/swiftui/image/resizable(capinsets:resizingmode:)) method scales the image to fit the current view. Then, the [aspectRatio(_:contentMode:)](/documentation/swiftui/view/aspectratio(_:contentmode:)) view modifier adjusts this resizing behavior to maintain the image’s original aspect ratio, rather than scaling the x- and y-axes independently to fill all four sides of the view. The article [Fitting-Images-into-Available](/documentation/swiftui/fitting-images-into-available-space) shows how to apply scaling, clipping, and tiling to `Image` instances of different sizes.

An `Image` is a late-binding token; the system resolves its actual value only when it’s about to use the image in an environment.

To use an image as a control, use one of the initializers that takes a `label` parameter. This allows the system’s accessibility frameworks to use the label as the name of the control for users who use features like VoiceOver. For images that are only present for aesthetic reasons, use an initializer with the `decorative` parameter; the accessibility systems ignore these images.

- [Copyable](/documentation/Swift/Copyable)
- [Equatable](/documentation/Swift/Equatable)
- [JournalingSuggestionAsset](/documentation/JournalingSuggestions/JournalingSuggestionAsset)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Transferable](/documentation/CoreTransferable/Transferable)
- [View](/documentation/swiftui/view)

- [init(_:bundle:)](/documentation/swiftui/image/init(_:bundle:)) Creates a labeled image that you can use as content for controls.
- [init(_:variableValue:bundle:)](/documentation/swiftui/image/init(_:variablevalue:bundle:)) Creates a labeled image that you can use as content for controls, with a variable value.
- [init(_:)](/documentation/swiftui/image/init(_:)) Initialize an  with an image resource.

- [init(_:bundle:label:)](/documentation/swiftui/image/init(_:bundle:label:)) Creates a labeled image that you can use as content for controls, with the specified label.
- [init(_:variableValue:bundle:label:)](/documentation/swiftui/image/init(_:variablevalue:bundle:label:)) Creates a labeled image that you can use as content for controls, with the specified label and variable value.
- [init(_:scale:orientation:label:)](/documentation/swiftui/image/init(_:scale:orientation:label:)) Creates a labeled image based on a Core Graphics image instance, usable as content for controls.

- [init(decorative:bundle:)](/documentation/swiftui/image/init(decorative:bundle:)) Creates an unlabeled, decorative image.
- [init(decorative:variableValue:bundle:)](/documentation/swiftui/image/init(decorative:variablevalue:bundle:)) Creates an unlabeled, decorative image, with a variable value.
- [init(decorative:scale:orientation:)](/documentation/swiftui/image/init(decorative:scale:orientation:)) Creates an unlabeled, decorative image based on a Core Graphics image instance.

- [init(systemName:)](/documentation/swiftui/image/init(systemname:)) Creates a system symbol image.
- [init(systemName:variableValue:)](/documentation/swiftui/image/init(systemname:variablevalue:)) Creates a system symbol image with a variable value.

- [init(uiImage:)](/documentation/swiftui/image/init(uiimage:)) Creates a SwiftUI image from a UIKit image instance.
- [init(nsImage:)](/documentation/swiftui/image/init(nsimage:)) Creates a SwiftUI image from an AppKit image instance.

- [init(size:label:opaque:colorMode:renderer:)](/documentation/swiftui/image/init(size:label:opaque:colormode:renderer:)) Initializes an image of the given size, with contents provided by a custom rendering closure.

- [resizable(capInsets:resizingMode:)](/documentation/swiftui/image/resizable(capinsets:resizingmode:)) Sets the mode by which SwiftUI resizes an image to fit its space.

- [antialiased(_:)](/documentation/swiftui/image/antialiased(_:)) Specifies whether SwiftUI applies antialiasing when rendering the image.
- [symbolRenderingMode(_:)](/documentation/swiftui/image/symbolrenderingmode(_:)) Sets the rendering mode for symbol images within this view.
- [renderingMode(_:)](/documentation/swiftui/image/renderingmode(_:)) Indicates whether SwiftUI renders an image as-is, or by using a different mode.
- [interpolation(_:)](/documentation/swiftui/image/interpolation(_:)) Specifies the current level of quality for rendering an image that requires interpolation.
- [Image.TemplateRenderingMode](/documentation/swiftui/image/templaterenderingmode) A type that indicates how SwiftUI renders images.
- [Image.Interpolation](/documentation/swiftui/image/interpolation) The level of quality for rendering an image that requires interpolation, such as a scaled image.

- [allowedDynamicRange(_:)](/documentation/swiftui/image/alloweddynamicrange(_:)) Returns a new image configured with the specified allowed dynamic range.
- [allowedDynamicRange](/documentation/swiftui/environmentvalues/alloweddynamicrange) The allowed dynamic range for the view, or nil.
- [Image.DynamicRange](/documentation/swiftui/image/dynamicrange)

- [symbolColorRenderingMode(_:)](/documentation/swiftui/image/symbolcolorrenderingmode(_:)) Sets the color rendering mode of the image.
- [symbolVariableValueMode(_:)](/documentation/swiftui/image/symbolvariablevaluemode(_:)) Sets the variable value mode mode for symbol images within this view.
- [widgetAccentedRenderingMode(_:)](/documentation/swiftui/image/widgetaccentedrenderingmode(_:)) Specifies the how to render an  when using the  mode.

- [Image.Orientation](/documentation/swiftui/image/orientation) The orientation of an image.
- [Image.ResizingMode](/documentation/swiftui/image/resizingmode) The modes that SwiftUI uses to resize an image to fit within its containing view.
- [Image.Scale](/documentation/swiftui/image/scale) A scale to apply to vector images relative to text.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Image
```

Example 2 (swift):
```swift
Image("Landscape_4")
    .resizable()
    .aspectRatio(contentMode: .fit)
Text("Water wheel")
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
timestamp: 2026-02-13T01:41:40.736Z
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
