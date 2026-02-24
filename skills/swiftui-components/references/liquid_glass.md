# Swiftui-Components - Liquid Glass

**Pages:** 3

---

## Landmarks: Displaying custom activity badges

**URL:** https://sosumi.ai/documentation/swiftui/landmarks-displaying-custom-activity-badges?.md

**Contents:**
- Overview
- Add a modifier to show badges in other views
- Apply Liquid Glass to the toggle button
- Add Liquid Glass to the badges
- Animate the badges using the morph effect
- App features

---
title: Landmarks: Displaying custom activity badges
description: Provide people with a way to mark their adventures by displaying animated custom activity badges.
source: https://developer.apple.com/documentation/swiftui/landmarks-displaying-custom-activity-badges
timestamp: 2026-02-13T19:36:54.441Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, macOS 26.0+, Xcode 26.0+

> Provide people with a way to mark their adventures by displaying animated custom activity badges.

The Landmarks app lets people track their adventures as they explore sites around the world. Whether it’s a national park near their home or a far-flung location on a different continent, the app provides a way for people to mark their adventures and receive custom activity badges along the way.

This sample displays the badges in a vertical view that includes a toggle button for showing or hiding the badges. The Landmarks app includes a custom modifier that makes it easier for other views to adopt the badge view. By configuring the badges to use Liquid Glass, the badges gain the advantage of using the morphing animation when you show or hide the badges.

To make the badges available in other views, like `CollectionsView`, the sample uses a custom modifier, `ShowBadgesViewModifier`, as a [View Modifier](/documentation/swiftui/viewmodifier). The sample layers the badges over another view using a [ZStack](/documentation/swiftui/zstack), and positions the badge view in the lower trailing corner:

The sample extends [View](/documentation/swiftui/view) by adding the `showBadges` modifier:

To create the toggle button, the sample configures a [Button](/documentation/swiftui/button) using `ToggleBadgesLabel` which has different system images for the Show and Hide toggle states. To apply Liquid Glass, style the button with the [glass](/documentation/swiftui/primitivebuttonstyle/glass) modifier:

To add Liquid Glass to each badge, the sample uses the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) modifier. To make a custom glass view appearance, the sample specifies a rectangular option with a corner radius:

The morph effect is an animation for Liquid Glass views. During this animation, the toggle button and each badge start as a combined view. Then, the button and badges change shape like a liquid as they separate and move from one location to another. In reverse, the toggle button and badges change shape and combine back into one view.

To achieve the Liquid Glass morph effect, the app:

- organizes the badges and toggle button into a [Glass Effect Container](/documentation/swiftui/glasseffectcontainer)
- adds [glassEffectID(_:in:)](/documentation/swiftui/view/glasseffectid(_:in:)) to each badge
- adds [glassEffectID(_:in:)](/documentation/swiftui/view/glasseffectid(_:in:)) to the toggle button
- wraps the command that toggles the `isExpanded` property in [withAnimation(_:_:)](/documentation/swiftui/withanimation(_:_:))

- [Landmarks: Applying a background extension effect](/documentation/swiftui/landmarks-applying-a-background-extension-effect)
- [Landmarks: Extending horizontal scrolling under a sidebar or inspector](/documentation/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector)
- [Landmarks: Refining the system provided Liquid Glass effect in toolbars](/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
private struct ShowsBadgesViewModifier: ViewModifier {
    func body(content: Content) -> some View {
        ZStack {
            content
            HStack {
                Spacer()
                VStack {
                    Spacer()
                    BadgesView()
                        .padding()
                }
            }
        }
    }
}
```

Example 2 (swift):
```swift
extension View {
    func showsBadges() -> some View {
        modifier(ShowsBadgesViewModifier())
    }
}
```

Example 3 (swift):
```swift
Button {
    //...
} label: {
    //...
}
.buttonStyle(.glass)
```

Example 4 (swift):
```swift
BadgeLabel(badge: $0)
    .glassEffect(.regular, in: .rect(cornerRadius: Constants.badgeCornerRadius))
```

---

## Landmarks: Building an app with Liquid Glass

**URL:** https://sosumi.ai/documentation/swiftui/landmarks-building-an-app-with-liquid-glass?.md

**Contents:**
- Overview
- Apply a background extension effect
- Extend horizontal scrolling under the sidebar
- Refine the Liquid Glass in the toolbar
- Display badges with Liquid Glass
- Create the app icon with Icon Composer
- App features
- Essentials

---
title: Landmarks: Building an app with Liquid Glass
description: Enhance your app experience with system-provided and custom Liquid Glass.
source: https://developer.apple.com/documentation/swiftui/landmarks-building-an-app-with-liquid-glass
timestamp: 2026-02-13T19:36:50.560Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, macOS 26.0+, Xcode 26.0+

> Enhance your app experience with system-provided and custom Liquid Glass.

Landmarks is a SwifUI app that demonstrates how to use the new dynamic and expressive design feature, Liquid Glass. The Landmarks app lets people explore interesting sites around the world. Whether it’s a national park near their home or a far-flung location on a different continent, the app provides a way for people to organize and mark their adventures and receive custom activity badges along the way. Landmarks runs on iPad, iPhone, and Mac.

Landmarks uses a [Navigation Split View](/documentation/swiftui/navigationsplitview) to organize and navigate to content in the app, and demonstrates several key concepts to optimize the use of Liquid Glass:

- Stretching content behind the sidebar and inspector with the background extension effect.
- Extending horizontal scroll views under a sidebar or inspector.
- Leveraging the system-provided glass effect in toolbars.
- Applying Liquid Glass effects to custom interface elements and animations.
- Building a new app icon with Icon Composer.

The sample also demonstrates several techniques to use when changing window sizes, and for adding global search.

The sample applies a background extension effect to the featured landmark header in the top view, and the main image in the landmark detail view. This effect extends and blurs the image under the sidebar and inspector when they’re open, creating a full edge-to-edge experience.

To achieve this effect, the sample creates and configures an [Image](/documentation/swiftui/image) that extends to both the leading and trailing edges of the containing view, and applies the [backgroundExtensionEffect()](/documentation/swiftui/view/backgroundextensioneffect()) modifier to the image. For the featured image, the sample adds an overlay with a headline and button after the modifier, so that only the image extends under the sidebar and inspector.

> [!NOTE]
> The sample also extends the image beyond the top safe area, and adds logic to interactively extend the image when you scroll down beyond the view’s bounds. While this improves the experience of the image in the app, it isn’t required to implement the background extension effect.

For more information, see [Landmarks-Applying-a-background-extension](/documentation/swiftui/landmarks-applying-a-background-extension-effect).

Within each continent section in `LandmarksView`, an instance of `LandmarkHorizontalListView` shows a horizontally scrolling list of landmark views. When open, the landmark views can scroll underneath the sidebar or inspector.

To achieve this effect, the app aligns the scroll views next to the leading and trailing edges of the containing view.

For more information, see [Landmarks-Extending-horizontal-scrolling-under-a-sidebar-or](/documentation/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector).

In `LandmarkDetailView`, the sample adds toolbar items for:

- sharing a landmark
- adding or removing a landmark from a list of Favorites
- adding or removing a landmark from Collections
- showing or hiding the inspector

The system applies Liquid Glass to toolbar items automatically:

The sample also organizes the toolbar into related groups, instead of having all the buttons in one group. For more information, see [Landmarks-Refining-the-system-provided-glass-effect-in](/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars).

Badges provide people with a visual indicator of the activities they’ve recorded in the Landmarks app. When a person completes all four activities for a landmark, they earn that landmark’s badge. The sample uses custom Liquid Glass elements with badges, and shows how to coordinate animations with Liquid Glass.

To create a custom Liquid Glass badge, Landmarks uses a view with an `Image` to display a system symbol image for the badge. The badge has a background hexagon `Image` filled with a custom color. The badge view uses the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) modifier to apply Liquid Glass to the badge.

To demonstrate the morphing effect that the system provides with Liquid Glass animations, the sample organizes the badges and the toggle button into a [Glass Effect Container](/documentation/swiftui/glasseffectcontainer), and assigns each badge a unique [glassEffectID(_:in:)](/documentation/swiftui/view/glasseffectid(_:in:)).

For more information, see [Landmarks-Displaying-custom-activity](/documentation/swiftui/landmarks-displaying-custom-activity-badges). For information about building custom views with Liquid Glass, see [Applying-Liquid-Glass-to-custom](/documentation/swiftui/applying-liquid-glass-to-custom-views).

Landmarks includes a dynamic and expressive app icon composed in Icon Composer. You build app icons with four layers that the system uses to produce specular highlights when a person moves their device, so that the icon responds as if light was reflecting off the glass. The Settings app allows people to personalize the icon by selecting light, dark, clear, or tinted variants of your app icon as well.

For more information on creating a new app icon, see [creating-your-app-icon-using-icon](/documentation/Xcode/creating-your-app-icon-using-icon-composer).

For design guidance, see Human Interface Guidelines >  [app](/design/Human-Interface-Guidelines/app-icons).

- [Landmarks: Applying a background extension effect](/documentation/swiftui/landmarks-applying-a-background-extension-effect) Configure an image to blur and extend under a sidebar or inspector panel.
- [Landmarks: Extending horizontal scrolling under a sidebar or inspector](/documentation/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector) Improve your horizontal scrollbar’s appearance by extending it under a sidebar or inspector.
- [Landmarks: Refining the system provided Liquid Glass effect in toolbars](/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars) Organize toolbars into related groupings to improve their appearance and utility.
- [Landmarks: Displaying custom activity badges](/documentation/swiftui/landmarks-displaying-custom-activity-badges) Provide people with a way to mark their adventures by displaying animated custom activity badges.

- [Adopting Liquid Glass](/documentation/TechnologyOverviews/adopting-liquid-glass)
- [Learning SwiftUI](/tutorials/swiftui-concepts)
- [Exploring SwiftUI Sample Apps](/tutorials/Sample-Apps)
- [SwiftUI updates](/documentation/Updates/SwiftUI)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

---

## Glass

**URL:** https://sosumi.ai/documentation/swiftui/glass?.md

**Contents:**
- Overview
- Conforms To
- Instance Methods
- Type Properties
- Styling content

---
title: Glass
description: A structure that defines the configuration of the Liquid Glass material.
source: https://developer.apple.com/documentation/swiftui/glass
timestamp: 2026-02-13T19:37:00.525Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> A structure that defines the configuration of the Liquid Glass material.

You provide instances of a variant of Liquid Glass to the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) view modifier:

You can combine Liquid Glass effects using a [Glass Effect Container](/documentation/swiftui/glasseffectcontainer), which supports morphing views with this effect into each other based on the geometry of their associated views.

- [Equatable](/documentation/Swift/Equatable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [interactive(_:)](/documentation/swiftui/glass/interactive(_:)) Returns a copy of the structure configured to be interactive.
- [tint(_:)](/documentation/swiftui/glass/tint(_:)) Returns a copy of the structure with a configured tint color.

- [clear](/documentation/swiftui/glass/clear) The clear variant of glass.
- [identity](/documentation/swiftui/glass/identity) The identity variant of glass. When applied, your content remains unaffected as if no glass effect was applied.
- [regular](/documentation/swiftui/glass/regular) The regular variant of the Liquid Glass material.

- [border(_:width:)](/documentation/swiftui/view/border(_:width:))
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

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Glass
```

Example 2 (swift):
```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()
```

---
