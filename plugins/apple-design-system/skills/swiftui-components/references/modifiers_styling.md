# Swiftui-Components - Modifiers Styling

**Pages:** 2

---

## Material

**URL:** https://sosumi.ai/documentation/swiftui/material?.md

**Contents:**
- Overview
- Conforms To
- Getting material types
- Instance Methods
- Supporting types

---
title: Material
description: A background material type.
source: https://developer.apple.com/documentation/swiftui/material
timestamp: 2026-02-13T19:34:25.841Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> A background material type.

You can apply a blur effect to a view that appears behind another view by adding a material with the [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:)) modifier:

In the example above, the [ZStack](/documentation/swiftui/zstack) layers a [Label](/documentation/swiftui/label) on top of the color [teal](/documentation/swiftui/shapestyle/teal). The background modifier inserts the regular material below the label, blurring the part of the background that the label — including its padding — covers:

A material isn’t a view, but adding a material is like inserting a translucent layer between the modified view and its background:

The blurring effect provided by the material isn’t simple opacity. Instead, it uses a platform-specific blending that produces an effect that resembles heavily frosted glass. You can see this more easily with a complex background, like an image:

For physical materials, the degree to which the background colors pass through depends on the thickness. The effect also varies with light and dark appearance:

If you need a material to have a particular shape, you can use the [background(_:in:fillStyle:)](/documentation/swiftui/view/background(_:in:fillstyle:)) modifier. For example, you can create a material with rounded corners:

When you add a material, foreground elements exhibit vibrancy, a context-specific blend of the foreground and background colors that improves contrast. However using [foregroundStyle(_:)](/documentation/swiftui/view/foregroundstyle(_:)) to set a custom foreground style — excluding the hierarchical styles, like [secondary-swift.type.property](/documentation/swiftui/shapestyle/secondary-swift.type.property) — disables vibrancy.

> [!NOTE]
> A material blurs a background that’s part of your app, but not what appears behind your app on the screen. For example, the content on the Home Screen doesn’t affect the appearance of a widget.

- [Copyable](/documentation/Swift/Copyable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [ShapeStyle](/documentation/swiftui/shapestyle)

- [ultraThin](/documentation/swiftui/material/ultrathin) A mostly translucent material.
- [thin](/documentation/swiftui/material/thin) A material that’s more translucent than opaque.
- [regular](/documentation/swiftui/material/regular) A material that’s somewhat translucent.
- [thick](/documentation/swiftui/material/thick) A material that’s more opaque than translucent.
- [ultraThick](/documentation/swiftui/material/ultrathick) A mostly opaque material.
- [bar](/documentation/swiftui/material/bar) A material matching the style of system toolbars.

- [materialActiveAppearance(_:)](/documentation/swiftui/material/materialactiveappearance(_:)) Sets an explicit active appearance for this material.

- [AngularGradient](/documentation/swiftui/angulargradient)
- [EllipticalGradient](/documentation/swiftui/ellipticalgradient)
- [LinearGradient](/documentation/swiftui/lineargradient)
- [RadialGradient](/documentation/swiftui/radialgradient)
- [ImagePaint](/documentation/swiftui/imagepaint)
- [HierarchicalShapeStyle](/documentation/swiftui/hierarchicalshapestyle)
- [HierarchicalShapeStyleModifier](/documentation/swiftui/hierarchicalshapestylemodifier)
- [ForegroundStyle](/documentation/swiftui/foregroundstyle)
- [BackgroundStyle](/documentation/swiftui/backgroundstyle)
- [SelectionShapeStyle](/documentation/swiftui/selectionshapestyle)
- [SeparatorShapeStyle](/documentation/swiftui/separatorshapestyle)
- [TintShapeStyle](/documentation/swiftui/tintshapestyle)
- [FillShapeStyle](/documentation/swiftui/fillshapestyle)
- [LinkShapeStyle](/documentation/swiftui/linkshapestyle)
- [PlaceholderTextShapeStyle](/documentation/swiftui/placeholdertextshapestyle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Material
```

Example 2 (swift):
```swift
ZStack {
    Color.teal
    Label("Flag", systemImage: "flag.fill")
        .padding()
        .background(.regularMaterial)
}
```

Example 3 (swift):
```swift
ZStack {
    Image("chili_peppers")
        .resizable()
        .aspectRatio(contentMode: .fit)
    Label("Flag", systemImage: "flag.fill")
        .padding()
        .background(.regularMaterial)
}
```

Example 4 (swift):
```swift
ZStack {
    Color.teal
    Label("Flag", systemImage: "flag.fill")
        .padding()
        .background(.regularMaterial, in: RoundedRectangle(cornerRadius: 8))
}
```

---

## Landmarks: Applying a background extension effect

**URL:** https://sosumi.ai/documentation/swiftui/landmarks-applying-a-background-extension-effect?.md

**Contents:**
- Overview
  - Align the view to the leading and trailing edges
  - Apply the background extension effect to the image
  - Configure only the image
- App features

---
title: Landmarks: Applying a background extension effect
description: Configure an image to blur and extend under a sidebar or inspector panel.
source: https://developer.apple.com/documentation/swiftui/landmarks-applying-a-background-extension-effect
timestamp: 2026-02-13T19:36:52.500Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, macOS 26.0+, Xcode 26.0+

> Configure an image to blur and extend under a sidebar or inspector panel.

The Landmarks app lets people explore interesting sites around the world. Whether it’s a national park near their home or a far-flung location on a different continent, the app provides a way for people to organize and mark their adventures and receive custom activity badges along the way.

This sample demonstrates how to apply a background extension effect. In the top Landmarks view, the sample applies a background extension effect to the featured image in `LandmarksView`, and to the main image in `LandmarkDetailView`. The background extension effect blurs and extends the image under the sidebar or inspector panel when open. The following images show the main image in `LandmarkDetailView` both with and without the background extension effect.

To apply the background extension effect, the sample:

1. Aligns the view to the leading and trailing edges of the containing view.
2. Applies the [backgroundExtensionEffect()](/documentation/swiftui/view/backgroundextensioneffect()) modifier to the view.
3. Configures only the image in the background extension, and avoids applying the effect to the title and button in the overlay.

To apply the [backgroundExtensionEffect()](/documentation/swiftui/view/backgroundextensioneffect()) to a view, align the leading edge of the view next to the sidebar, and align the trailing edge of the view to the trailing edge of the containing view.

In `LandmarksView`, the `LandmarkFeaturedItemView` and the containing [Lazy VStack](/documentation/swiftui/lazyvstack) and [Scroll View](/documentation/swiftui/scrollview) don’t have padding. This allows the `LandmarkFeaturedItemView` to align with the leading edge of the view next to the sidebar.

In `LandmarkDetailView`, the [Scroll View](/documentation/swiftui/scrollview) and [VStack](/documentation/swiftui/vstack) that contain the main image also don’t have any padding. This allows the main image to align against the leading edge of the containing view.

In `LandmarkDetailView`, the sample applies the background extension effect to the main image by adding the [backgroundExtensionEffect()](/documentation/swiftui/view/backgroundextensioneffect()) modifier:

When the sidebar is open, the system extends the image in the leading direction as follows:

- The system takes a section of the leading end of the image that matches the width of the sidebar.
- The system flips that portion of the image horizontally toward the leading edge and applies a blur to the flipped section.
- The system places the modified section of the image under the sidebar, immediately before the leading edge of the image.

When the inspector is open, the system extends the image in the trailing direction as follows:

- The system takes a section of the trailing end of the image that matches the width of the sidebar.
- The system flips that portion of the image horizontally toward the trailing edge and applies a blur to the flipped section.
- The system places the modified section of the image under the inspector, immediately after the trailing edge of the image.

In `LandmarksView`, the `LandmarkFeaturedItemView` has an image from the featured landmark, and includes a title for the landmark and a button you can click or tap to learn more about that location.

To avoid having the landmark’s title and button appear under the sidebar in macOS, the sample applies the [backgroundExtensionEffect()](/documentation/swiftui/view/backgroundextensioneffect()) modifier to the image before adding the overlay that includes the title and button:

- [Landmarks: Extending horizontal scrolling under a sidebar or inspector](/documentation/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector)
- [Landmarks: Refining the system provided Liquid Glass effect in toolbars](/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars)
- [Landmarks: Displaying custom activity badges](/documentation/swiftui/landmarks-displaying-custom-activity-badges)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
ScrollView(showsIndicators: false) {
    LazyVStack(alignment: .leading, spacing: Constants.standardPadding) {
        LandmarkFeaturedItemView(landmark: modelData.featuredLandmark!)
            .flexibleHeaderContent()
        //...
    }
}
```

Example 2 (swift):
```swift
Image(landmark.backgroundImageName)
    //...
    .backgroundExtensionEffect()
```

Example 3 (swift):
```swift
Image(decorative: landmark.backgroundImageName)
    //...
    .backgroundExtensionEffect()
    .overlay(alignment: .bottom) {
        VStack {
            Text("Featured Landmark", comment: "Big headline in the main image of featured landmarks.")
                //...
            Text(landmark.name)
                //...
            Button("Learn More") {
                modelData.path.append(landmark)
            }
            //...
        }
        .padding([.bottom], Constants.learnMoreBottomPadding)
    }
```

---
