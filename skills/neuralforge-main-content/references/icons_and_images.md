# Neuralforge-Main-Content - Icons And Images

**Pages:** 3

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
timestamp: 2026-02-13T03:43:04.682Z
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

## symbolRenderingMode(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/symbolrenderingmode(_:)?.md

**Contents:**
- Parameters
- Return Value
- Setting symbol rendering modes

---
title: symbolRenderingMode(_:)
description: Sets the rendering mode for symbol images within this view.
source: https://developer.apple.com/documentation/swiftui/view/symbolrenderingmode(_:)
timestamp: 2026-02-13T03:43:06.757Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Sets the rendering mode for symbol images within this view.

The symbol rendering mode to use.

A view that uses the rendering mode you supply.

- [symbolRenderingMode](/documentation/swiftui/environmentvalues/symbolrenderingmode)
- [SymbolRenderingMode](/documentation/swiftui/symbolrenderingmode)
- [SymbolColorRenderingMode](/documentation/swiftui/symbolcolorrenderingmode)
- [SymbolVariableValueMode](/documentation/swiftui/symbolvariablevaluemode)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func symbolRenderingMode(_ mode: SymbolRenderingMode?) -> some View
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
timestamp: 2026-02-13T03:43:02.395Z
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
