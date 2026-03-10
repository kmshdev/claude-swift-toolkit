# Apple-Liquid-Glass-Design - Background Extension

**Pages:** 4

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
timestamp: 2026-02-13T00:18:26.300Z
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

## backgroundExtensionEffect()

**URL:** https://sosumi.ai/documentation/swiftui/view/backgroundextensioneffect()?.md

**Contents:**
- Discussion

---
title: backgroundExtensionEffect()
description: Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
source: https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect()
timestamp: 2026-02-13T00:18:59.853Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+

> Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.

Use this modifier when you want to extend the view beyond its bounds so the copies can function as backgrounds for other elements on top. The most common use case is to apply this to a view in the detail column of a navigation split view so it can extend under the sidebar or inspector region to provide seamless immersive visuals.

Apply this modifier with discretion. This should often be used with only a single instance of background content with consideration of visual clarity and performance.

> [!NOTE]
> This modifier will clip the view to prevent copies from overlapping with each other.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency func backgroundExtensionEffect() -> some View
```

Example 2 (swift):
```swift
NavigationSplitView {
    // sidebar content
} detail: {
    ZStack {
        BannerView()
            .backgroundExtensionEffect()
    }
}
.inspector(isPresented: $showInspector) {
    // inspector content
}
```

---

## UIBackgroundExtensionView

**URL:** https://sosumi.ai/documentation/UIKit/UIBackgroundExtensionView?.md

**Contents:**
- Overview
- Inherits From
- Conforms To
- Instance Properties
- Interacting with adjacent views

---
title: UIBackgroundExtensionView
description: A view that extends content to fill its own bounds.
source: https://developer.apple.com/documentation/UIKit/UIBackgroundExtensionView
timestamp: 2026-02-13T00:19:33.529Z
---

**Navigation:** [UIKit](/documentation/UIKit)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+

> A view that extends content to fill its own bounds.

A background extension view can be laid out to extend outside the safe area, such as under a sidebar or an inspector. By default, the view lays out its content to stay within the safe area, and uses modifications of the content along the edges to fill the container view.

- [UIView](/documentation/uikit/uiview)

- [CALayerDelegate](/documentation/QuartzCore/CALayerDelegate)
- [CVarArg](/documentation/Swift/CVarArg)
- [CustomDebugStringConvertible](/documentation/Swift/CustomDebugStringConvertible)
- [CustomStringConvertible](/documentation/Swift/CustomStringConvertible)
- [Equatable](/documentation/Swift/Equatable)
- [Hashable](/documentation/Swift/Hashable)
- [NSCoding](/documentation/Foundation/NSCoding)
- [NSObjectProtocol](/documentation/ObjectiveC/NSObjectProtocol)
- [NSTouchBarProvider](/documentation/AppKit/NSTouchBarProvider)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [UIAccessibilityIdentification](/documentation/uikit/uiaccessibilityidentification)
- [UIActivityItemsConfigurationProviding](/documentation/uikit/uiactivityitemsconfigurationproviding)
- [UIAppearance](/documentation/uikit/uiappearance)
- [UIAppearanceContainer](/documentation/uikit/uiappearancecontainer)
- [UICoordinateSpace](/documentation/uikit/uicoordinatespace)
- [UIDynamicItem](/documentation/uikit/uidynamicitem)
- [UIFocusEnvironment](/documentation/uikit/uifocusenvironment)
- [UIFocusItem](/documentation/uikit/uifocusitem)
- [UIFocusItemContainer](/documentation/uikit/uifocusitemcontainer)
- [UILargeContentViewerItem](/documentation/uikit/uilargecontentvieweritem)
- [UIPasteConfigurationSupporting](/documentation/uikit/uipasteconfigurationsupporting)
- [UIPopoverPresentationControllerSourceItem](/documentation/uikit/uipopoverpresentationcontrollersourceitem)
- [UIResponderStandardEditActions](/documentation/uikit/uiresponderstandardeditactions)
- [UITraitChangeObservable](/documentation/uikit/uitraitchangeobservable-67e94)
- [UITraitEnvironment](/documentation/uikit/uitraitenvironment)
- [UIUserActivityRestoring](/documentation/uikit/uiuseractivityrestoring)

- [automaticallyPlacesContentView](/documentation/uikit/uibackgroundextensionview/automaticallyplacescontentview) Controls the automatic safe area placement of the  within the container.
- [contentView](/documentation/uikit/uibackgroundextensionview/contentview) The content view to extend to fill the .

- [UIScrollEdgeElementContainerInteraction](/documentation/uikit/uiscrolledgeelementcontainerinteraction)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor class UIBackgroundExtensionView
```

---

## NSBackgroundExtensionView

**URL:** https://sosumi.ai/documentation/AppKit/NSBackgroundExtensionView?.md

**Contents:**
- Overview
- Inherits From
- Conforms To
- Instance Properties

---
title: NSBackgroundExtensionView
description: A view that extends content to fill its own bounds.
source: https://developer.apple.com/documentation/AppKit/NSBackgroundExtensionView
timestamp: 2026-02-13T00:19:35.672Z
---

**Navigation:** [AppKit](/documentation/AppKit)

**Available on:** macOS 26.0+

> A view that extends content to fill its own bounds.

A background extension view can be laid out to extend outside the safe area, such as under the titlebar, sidebar, or inspector. By default it lays out its content to stay within the safe area, and uses modifications of the content along the edges to fill the container view.

- [NSView](/documentation/appkit/nsview)

- [CVarArg](/documentation/Swift/CVarArg)
- [CustomDebugStringConvertible](/documentation/Swift/CustomDebugStringConvertible)
- [CustomStringConvertible](/documentation/Swift/CustomStringConvertible)
- [Equatable](/documentation/Swift/Equatable)
- [Hashable](/documentation/Swift/Hashable)
- [NSAccessibilityElementProtocol](/documentation/appkit/nsaccessibilityelementprotocol)
- [NSAccessibilityProtocol](/documentation/appkit/nsaccessibilityprotocol)
- [NSAnimatablePropertyContainer](/documentation/appkit/nsanimatablepropertycontainer)
- [NSAppearanceCustomization](/documentation/appkit/nsappearancecustomization)
- [NSCoding](/documentation/Foundation/NSCoding)
- [NSDraggingDestination](/documentation/appkit/nsdraggingdestination)
- [NSObjectProtocol](/documentation/ObjectiveC/NSObjectProtocol)
- [NSStandardKeyBindingResponding](/documentation/appkit/nsstandardkeybindingresponding)
- [NSTouchBarProvider](/documentation/appkit/nstouchbarprovider)
- [NSUserActivityRestoring](/documentation/appkit/nsuseractivityrestoring)
- [NSUserInterfaceItemIdentification](/documentation/appkit/nsuserinterfaceitemidentification)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [automaticallyPlacesContentView](/documentation/appkit/nsbackgroundextensionview/automaticallyplacescontentview) Controls the automatic safe area placement of the  within the container.
- [contentView](/documentation/appkit/nsbackgroundextensionview/contentview) The content view to extend to fill the .

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor class NSBackgroundExtensionView
```

---
