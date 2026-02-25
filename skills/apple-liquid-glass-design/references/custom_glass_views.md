# Apple-Liquid-Glass-Design - Custom Glass Views

**Pages:** 23

---

## interactive(_:)

**URL:** https://sosumi.ai/documentation/swiftui/glass/interactive(_:)?.md

**Contents:**
- Styling views with Liquid Glass

---
title: interactive(_:)
description: Returns a copy of the structure configured to be interactive.
source: https://developer.apple.com/documentation/swiftui/glass/interactive(_:)
timestamp: 2026-02-13T00:19:01.964Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [glass](/documentation/swiftui/glass)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> Returns a copy of the structure configured to be interactive.

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
func interactive(_ isEnabled: Bool = true) -> Glass
```

---

## materialize

**URL:** https://sosumi.ai/documentation/swiftui/glasseffecttransition/materialize?.md

---
title: materialize
description: The materialize glass effect transition which will fade in content and animate in or out the glass material but will not attempt to match the geometry of any other glass effects.
source: https://developer.apple.com/documentation/swiftui/glasseffecttransition/materialize
timestamp: 2026-02-13T00:19:14.528Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [glasseffecttransition](/documentation/swiftui/glasseffecttransition)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> The materialize glass effect transition which will fade in content and animate in or out the glass material but will not attempt to match the geometry of any other glass effects.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
static var materialize: GlassEffectTransition { get }
```

---

## GlassEffectTransition

**URL:** https://sosumi.ai/documentation/swiftui/glasseffecttransition?.md

**Contents:**
- Conforms To
- Type Properties
- Styling views with Liquid Glass

---
title: GlassEffectTransition
description: A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.
source: https://developer.apple.com/documentation/swiftui/glasseffecttransition
timestamp: 2026-02-13T00:18:39.746Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.

- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [identity](/documentation/swiftui/glasseffecttransition/identity) The identity transition specifying no changes.
- [matchedGeometry](/documentation/swiftui/glasseffecttransition/matchedgeometry) Returns the matched geometry glass effect transition.
- [materialize](/documentation/swiftui/glasseffecttransition/materialize) The materialize glass effect transition which will fade in content and animate in or out the glass material but will not attempt to match the geometry of any other glass effects.

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct GlassEffectTransition
```

---

## DefaultGlassEffectShape

**URL:** https://sosumi.ai/documentation/swiftui/defaultglasseffectshape?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Styling views with Liquid Glass

---
title: DefaultGlassEffectShape
description: The default shape applied by glass effects, a capsule.
source: https://developer.apple.com/documentation/swiftui/defaultglasseffectshape
timestamp: 2026-02-13T00:18:45.881Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> The default shape applied by glass effects, a capsule.

You do not use this type directly. Instead, SwiftUI creates this shape on your behalf as the default parameter of the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) modifier.

- [Animatable](/documentation/swiftui/animatable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init()](/documentation/swiftui/defaultglasseffectshape/init())

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct DefaultGlassEffectShape
```

---

## regular

**URL:** https://sosumi.ai/documentation/swiftui/glass/regular?.md

---
title: regular
description: The regular variant of the Liquid Glass material.
source: https://developer.apple.com/documentation/swiftui/glass/regular
timestamp: 2026-02-13T00:19:03.840Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [glass](/documentation/swiftui/glass)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> The regular variant of the Liquid Glass material.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
static var regular: Glass { get }
```

---

## FeatheredGlassBackgroundEffect

**URL:** https://sosumi.ai/documentation/swiftui/featheredglassbackgroundeffect?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Adding a glass background on views in visionOS

---
title: FeatheredGlassBackgroundEffect
description: The feathered glass background effect.
source: https://developer.apple.com/documentation/swiftui/featheredglassbackgroundeffect
timestamp: 2026-02-13T00:18:48.016Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** visionOS 2.4+

> The feathered glass background effect.

You can also use [feathered](/documentation/swiftui/glassbackgroundeffect/feathered) to construct this effect.

The layout size of a view with feathered glass background is based on the content size instead of the glass background size. When the glass background is clipped by an outer container, such as VStack or HStack, it can be resolved by incrasing content size, such as content padding, or reducing the feathered glass background size with its padding parameter.

- [GlassBackgroundEffect](/documentation/swiftui/glassbackgroundeffect)

- [init()](/documentation/swiftui/featheredglassbackgroundeffect/init()) Creates a feathered glassBackground effect.
- [init(padding:softEdgeRadius:)](/documentation/swiftui/featheredglassbackgroundeffect/init(padding:softedgeradius:)) Creates a feathered glassBackground effect.

- [glassBackgroundEffect(displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(displaymode:))
- [glassBackgroundEffect(in:displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(in:displaymode:))
- [GlassBackgroundDisplayMode](/documentation/swiftui/glassbackgrounddisplaymode)
- [GlassBackgroundEffect](/documentation/swiftui/glassbackgroundeffect)
- [AutomaticGlassBackgroundEffect](/documentation/swiftui/automaticglassbackgroundeffect)
- [GlassBackgroundEffectConfiguration](/documentation/swiftui/glassbackgroundeffectconfiguration)
- [PlateGlassBackgroundEffect](/documentation/swiftui/plateglassbackgroundeffect)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct FeatheredGlassBackgroundEffect
```

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
timestamp: 2026-02-13T00:18:35.750Z
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

## glassEffect(_:in:)

**URL:** https://sosumi.ai/documentation/swiftui/view/glasseffect(_:in:)?.md

**Contents:**
- Discussion
- Styling views with Liquid Glass

---
title: glassEffect(_:in:)
description: Applies the Liquid Glass effect to a view.
source: https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)
timestamp: 2026-02-13T00:18:51.932Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> Applies the Liquid Glass effect to a view.

When you use this effect, the system:

- Renders a shape anchored behind a view with the Liquid Glass material.
- Applies the foreground effects of Liquid Glass over a view.

For example, to add this effect to a [Text](/documentation/swiftui/text):

SwiftUI uses the [regular](/documentation/swiftui/glass/regular) variant by default along with a [Capsule](/documentation/swiftui/capsule) shape.

SwiftUI anchors the Liquid Glass to a view’s bounds. For the example above, the material fills the entirety of the `Text` frame, which includes the padding.

You typically use this modifier with a [Glass Effect Container](/documentation/swiftui/glasseffectcontainer) to combine multiple Liquid Glass shapes into a single shape that can morph into one another.

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func glassEffect(_ glass: Glass = .regular, in shape: some Shape = DefaultGlassEffectShape()) -> some View
```

Example 2 (swift):
```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()
```

---

## Landmarks: Refining the system provided Liquid Glass effect in toolbars

**URL:** https://sosumi.ai/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars?.md

**Contents:**
- Overview
- Organize the toolbar items into logical groupings
- App features

---
title: Landmarks: Refining the system provided Liquid Glass effect in toolbars
description: Organize toolbars into related groupings to improve their appearance and utility.
source: https://developer.apple.com/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars
timestamp: 2026-02-13T00:18:31.863Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, macOS 26.0+, Xcode 26.0+

> Organize toolbars into related groupings to improve their appearance and utility.

The Landmarks app lets people explore interesting sites around the world. Whether it’s a national park near their home or a far-flung location on a different continent, the app provides a way for people to organize and mark their adventures and receive custom activity badges along the way.

This sample demonstrates how to refine the system provided glass effect in toolbars. In `LandmarkDetailView`, the sample adds toolbar items for:

- sharing a landmark
- adding or removing a landmark from a list of Favorites
- adding or removing a landmark from Collections
- showing or hiding the inspector

The system applies Liquid Glass to the toolbar items automatically.

To organize the toolbar items into logical groupings, the sample adds [Toolbar Spacer](/documentation/swiftui/toolbarspacer) items and passes [fixed](/documentation/swiftui/spacersizing/fixed) as the `sizing` parameter to divide the toolbar into sections:

- [Landmarks: Applying a background extension effect](/documentation/swiftui/landmarks-applying-a-background-extension-effect)
- [Landmarks: Extending horizontal scrolling under a sidebar or inspector](/documentation/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector)
- [Landmarks: Displaying custom activity badges](/documentation/swiftui/landmarks-displaying-custom-activity-badges)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
.toolbar {
    ToolbarSpacer(.flexible)

    ToolbarItem {
        ShareLink(item: landmark, preview: landmark.sharePreview)
    }

    ToolbarSpacer(.fixed)
    
    ToolbarItemGroup {
        LandmarkFavoriteButton(landmark: landmark)
        LandmarkCollectionsMenu(landmark: landmark)
    }
    
    ToolbarSpacer(.fixed)

    ToolbarItem {
        Button("Info", systemImage: "info") {
            modelData.selectedLandmark = landmark
            modelData.isLandmarkInspectorPresented.toggle()
        }
    }
}
```

---

## glass

**URL:** https://sosumi.ai/documentation/swiftui/primitivebuttonstyle/glass?.md

**Contents:**
- Discussion
- Getting built-in button styles

---
title: glass
description: A button style that applies a Liquid Glass effect based on the button’s context.
source: https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/glass
timestamp: 2026-02-13T00:19:05.938Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [primitivebuttonstyle](/documentation/swiftui/primitivebuttonstyle)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> A button style that applies a Liquid Glass effect based on the button’s context.

In tvOS, this button style applies a Liquid Glass effect regardless of whether the button has focus.

To apply this style to a button, or to a view that contains buttons, use the [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:)-66fbx) modifier.

- [automatic](/documentation/swiftui/primitivebuttonstyle/automatic)
- [accessoryBar](/documentation/swiftui/primitivebuttonstyle/accessorybar)
- [accessoryBarAction](/documentation/swiftui/primitivebuttonstyle/accessorybaraction)
- [bordered](/documentation/swiftui/primitivebuttonstyle/bordered)
- [borderedProminent](/documentation/swiftui/primitivebuttonstyle/borderedprominent)
- [borderless](/documentation/swiftui/primitivebuttonstyle/borderless)
- [card](/documentation/swiftui/primitivebuttonstyle/card)
- [glassProminent](/documentation/swiftui/primitivebuttonstyle/glassprominent)
- [glass(_:)](/documentation/swiftui/primitivebuttonstyle/glass(_:))
- [link](/documentation/swiftui/primitivebuttonstyle/link)
- [plain](/documentation/swiftui/primitivebuttonstyle/plain)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency static var glass: GlassButtonStyle { get }
```

---

## glass(_:)

**URL:** https://sosumi.ai/documentation/swiftui/primitivebuttonstyle/glass(_:)?.md

**Contents:**
- Discussion
- Getting built-in button styles

---
title: glass(_:)
description: A button style that applies a configurable Liquid Glass effect based on the button’s context.
source: https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/glass(_:)
timestamp: 2026-02-13T00:19:08.084Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [primitivebuttonstyle](/documentation/swiftui/primitivebuttonstyle)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> A button style that applies a configurable Liquid Glass effect based on the button’s context.

This button style applies a Liquid Glass effect that you can customize by specifying a tint or variant. In the following example, the button renders using the clear variant of Liquid Glass:

In tvOS, this button style applies a Liquid Glass effect regardless of whether the button has focus. This style is similar to the [bordered](/documentation/swiftui/primitivebuttonstyle/bordered) style.

To apply this style to a button, or to a view that contains buttons, use the [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:)-66fbx) modifier.

- [automatic](/documentation/swiftui/primitivebuttonstyle/automatic)
- [accessoryBar](/documentation/swiftui/primitivebuttonstyle/accessorybar)
- [accessoryBarAction](/documentation/swiftui/primitivebuttonstyle/accessorybaraction)
- [bordered](/documentation/swiftui/primitivebuttonstyle/bordered)
- [borderedProminent](/documentation/swiftui/primitivebuttonstyle/borderedprominent)
- [borderless](/documentation/swiftui/primitivebuttonstyle/borderless)
- [card](/documentation/swiftui/primitivebuttonstyle/card)
- [glass](/documentation/swiftui/primitivebuttonstyle/glass)
- [glassProminent](/documentation/swiftui/primitivebuttonstyle/glassprominent)
- [link](/documentation/swiftui/primitivebuttonstyle/link)
- [plain](/documentation/swiftui/primitivebuttonstyle/plain)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency static func glass(_ glass: Glass) -> Self
```

Example 2 (swift):
```swift
Button("Button") {}
    .buttonStyle(.glass(.clear))
```

---

## GlassBackgroundDisplayMode

**URL:** https://sosumi.ai/documentation/swiftui/glassbackgrounddisplaymode?.md

**Contents:**
- Overview
- Conforms To
- Getting the mode
- Adding a glass background on views in visionOS

---
title: GlassBackgroundDisplayMode
description: The display mode of a glass background.
source: https://developer.apple.com/documentation/swiftui/glassbackgrounddisplaymode
timestamp: 2026-02-13T00:18:49.951Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** visionOS 1.0+

> The display mode of a glass background.

Use a value of this type to indicate when to display a glass background that you add to a view using a view modifier like [glassBackgroundEffect(displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(displaymode:)).

- [Copyable](/documentation/Swift/Copyable)
- [Equatable](/documentation/Swift/Equatable)
- [Hashable](/documentation/Swift/Hashable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [GlassBackgroundDisplayMode.always](/documentation/swiftui/glassbackgrounddisplaymode/always) Always display the glass material.
- [GlassBackgroundDisplayMode.implicit](/documentation/swiftui/glassbackgrounddisplaymode/implicit) Display the glass material only when the view isn’t already contained in glass.
- [GlassBackgroundDisplayMode.never](/documentation/swiftui/glassbackgrounddisplaymode/never) Never display the glass material.

- [glassBackgroundEffect(displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(displaymode:))
- [glassBackgroundEffect(in:displayMode:)](/documentation/swiftui/view/glassbackgroundeffect(in:displaymode:))
- [GlassBackgroundEffect](/documentation/swiftui/glassbackgroundeffect)
- [AutomaticGlassBackgroundEffect](/documentation/swiftui/automaticglassbackgroundeffect)
- [GlassBackgroundEffectConfiguration](/documentation/swiftui/glassbackgroundeffectconfiguration)
- [FeatheredGlassBackgroundEffect](/documentation/swiftui/featheredglassbackgroundeffect)
- [PlateGlassBackgroundEffect](/documentation/swiftui/plateglassbackgroundeffect)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
enum GlassBackgroundDisplayMode
```

---

## GlassProminentButtonStyle

**URL:** https://sosumi.ai/documentation/swiftui/glassprominentbuttonstyle?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Instance Methods
- Styling views with Liquid Glass

---
title: GlassProminentButtonStyle
description: A button style that applies prominent glass border artwork based on the button’s context.
source: https://developer.apple.com/documentation/swiftui/glassprominentbuttonstyle
timestamp: 2026-02-13T00:18:43.768Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> A button style that applies prominent glass border artwork based on the button’s context.

You can also use [glass Prominent](/documentation/swiftui/primitivebuttonstyle/glassprominent) to construct this style.

- [PrimitiveButtonStyle](/documentation/swiftui/primitivebuttonstyle)

- [init()](/documentation/swiftui/glassprominentbuttonstyle/init()) Creates a prominent glass button style.

- [makeBody(configuration:)](/documentation/swiftui/glassprominentbuttonstyle/makebody(configuration:)) Creates a view that represents the body of a button.

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct GlassProminentButtonStyle
```

---

## glassEffectID(_:in:)

**URL:** https://sosumi.ai/documentation/swiftui/view/glasseffectid(_:in:)?.md

**Contents:**
- Discussion

---
title: glassEffectID(_:in:)
description: Associates an identity value to Liquid Glass effects defined within this view.
source: https://developer.apple.com/documentation/swiftui/view/glasseffectid(_:in:)
timestamp: 2026-02-13T00:18:53.920Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> Associates an identity value to Liquid Glass effects defined within this view.

You use this modifier with the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) view modifier and a [Glass Effect Container](/documentation/swiftui/glasseffectcontainer) view. When used together, SwiftUI uses the identifier to animate shapes to and from each other during transitions.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func glassEffectID(_ id: (some Hashable & Sendable)?, in namespace: Namespace.ID) -> some View
```

---

## glassEffectTransition(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/glasseffecttransition(_:)?.md

**Contents:**
- Discussion

---
title: glassEffectTransition(_:)
description: Associates a glass effect transition with any glass effects defined within this view.
source: https://developer.apple.com/documentation/swiftui/view/glasseffecttransition(_:)
timestamp: 2026-02-13T00:18:55.870Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> Associates a glass effect transition with any glass effects defined within this view.

You use this modifier with the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) view modifier and [Glass Effect Container](/documentation/swiftui/glasseffectcontainer) view. When used together, SwiftUI will use the provided transition to apply changes to the glass effect when you add or remove views with these effects from the view hierarchy.

In the example below, the notepad image will transition into and out of the pencil image when the isExpanded variable changes.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency func glassEffectTransition(_ transition: GlassEffectTransition) -> some View
```

Example 2 (swift):
```swift
var isExpanded: Bool
@Namespace private var namespace

var body: some View {
    GlassEffectContainer(spacing: 10.0) {
        HStack(spacing: 10.0) {
            Image(systemName: "pencil")
                .frame(width: 20.0, height: 20.0)
                .glassEffect()
                .glassEffectID("pencil", in: namespace)

                if isExpanded {
                    Image(systemName: "note")
                        .frame(width: 20.0, height: 20.0)
                        .glassEffect()
                        .glassEffectID("note", in: namespace)
                        .glassEffectTransition(.matchedGeometry)
                }
            }
        }
    }
}
```

---

## GlassButtonStyle

**URL:** https://sosumi.ai/documentation/swiftui/glassbuttonstyle?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Instance Methods
- Styling views with Liquid Glass

---
title: GlassButtonStyle
description: A button style that applies glass border artwork based on the button’s context.
source: https://developer.apple.com/documentation/swiftui/glassbuttonstyle
timestamp: 2026-02-13T00:18:41.783Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> A button style that applies glass border artwork based on the button’s context.

You can also use [glass](/documentation/swiftui/primitivebuttonstyle/glass) to construct this style.

- [PrimitiveButtonStyle](/documentation/swiftui/primitivebuttonstyle)

- [init()](/documentation/swiftui/glassbuttonstyle/init()) Creates a glass button style.
- [init(_:)](/documentation/swiftui/glassbuttonstyle/init(_:))

- [makeBody(configuration:)](/documentation/swiftui/glassbuttonstyle/makebody(configuration:)) Creates a view that represents the body of a button.

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct GlassButtonStyle
```

---

## UIGlassEffect

**URL:** https://sosumi.ai/documentation/UIKit/UIGlassEffect?.md

**Contents:**
- Inherits From
- Conforms To
- Initializers
- Instance Properties
- Enumerations
- Liquid Glass effects

---
title: UIGlassEffect
description: A visual effect that renders a glass material.
source: https://developer.apple.com/documentation/UIKit/UIGlassEffect
timestamp: 2026-02-13T00:19:29.381Z
---

**Navigation:** [UIKit](/documentation/UIKit)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+

> A visual effect that renders a glass material.

- [UIVisualEffect](/documentation/uikit/uivisualeffect)

- [CVarArg](/documentation/Swift/CVarArg)
- [CustomDebugStringConvertible](/documentation/Swift/CustomDebugStringConvertible)
- [CustomStringConvertible](/documentation/Swift/CustomStringConvertible)
- [Equatable](/documentation/Swift/Equatable)
- [Hashable](/documentation/Swift/Hashable)
- [NSCoding](/documentation/Foundation/NSCoding)
- [NSCopying](/documentation/Foundation/NSCopying)
- [NSObjectProtocol](/documentation/ObjectiveC/NSObjectProtocol)
- [NSSecureCoding](/documentation/Foundation/NSSecureCoding)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [init(style:)](/documentation/uikit/uiglasseffect/init(style:)) Creates a glass effect with the specified style.

- [isInteractive](/documentation/uikit/uiglasseffect/isinteractive) Enables interactive behavior for the glass effect.
- [tintColor](/documentation/uikit/uiglasseffect/tintcolor) A tint color applied to the glass.

- [UIGlassEffect.Style](/documentation/uikit/uiglasseffect/style)

- [UIGlassContainerEffect](/documentation/uikit/uiglasscontainereffect)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor class UIGlassEffect
```

---

## Applying Liquid Glass to custom views

**URL:** https://sosumi.ai/documentation/swiftui/applying-liquid-glass-to-custom-views?.md

**Contents:**
- Overview
- Apply and configure Liquid Glass effects
- Combine multiple views with Liquid Glass containers
- Morph Liquid Glass effects during transitions
- Optimize performance when using Liquid Glass effects
- Styling views with Liquid Glass

---
title: Applying Liquid Glass to custom views
description: Configure, combine, and morph views using Liquid Glass effects.
source: https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views
timestamp: 2026-02-13T00:18:33.852Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

> Configure, combine, and morph views using Liquid Glass effects.

Interfaces across Apple platforms feature a new dynamic material called Liquid Glass, which combines the optical properties of glass with a sense of fluidity. Liquid Glass is a material that blurs content behind it, reflects color and light of surrounding content, and reacts to touch and pointer interactions in real time. Standard components in SwiftUI use Liquid Glass. Adopt Liquid Glass on custom components to move, combine, and morph them into one another with unique animations and transitions.

To learn about Liquid Glass and more, see [Landmarks-Building-an-app-with-Liquid](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass).

Use the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) modifier to add Liquid Glass effects to a view. By default, the modifier uses the [regular](/documentation/swiftui/glass/regular) variant of [Glass](/documentation/swiftui/glass) and applies the given effect within a [Capsule](/documentation/swiftui/capsule) shape behind the view’s content.

Configure the effect to customize your components in a variety of ways:

- Use different shapes to have a consistent look and feel across custom components in your app. For example, use a rounded rectangle if you’re applying the effect to larger components that would look odd as a `Capsule` or [Circle](/documentation/swiftui/circle).
- Assign a tint color to suggest prominence.
- Add [interactive(_:)](/documentation/swiftui/glass/interactive(_:)) to custom components to make them react to touch and pointer interactions. This applies the same responsive and fluid reactions that [glass](/documentation/swiftui/primitivebuttonstyle/glass) provides to standard buttons.

In the examples below, observe how to apply Liquid Glass effects to a view, use an alternate shape with a specific corner radius, and create a tinted view that responds to interactivity:

Use [Glass Effect Container](/documentation/swiftui/glasseffectcontainer) when applying Liquid Glass effects on multiple views to achieve the best rendering performance. A container also allows views with Liquid Glass effects to blend their shapes together and to morph in and out of each other during transitions. Inside a container, each view with the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) modifier renders with the effects behind it.

Customize the spacing on the container to control how the Liquid Glass effects behind views interact with one another. The larger the spacing value on the container, the sooner the Liquid Glass effects behind views blend together and merge the shapes during a transition. A spacing value on the container that’s larger than the spacing of an interior [HStack](/documentation/swiftui/hstack), [VStack](/documentation/swiftui/vstack), or other layout container causes Liquid Glass effects to blend together at rest because the views are too close to each other. Animating views in or out causes the shapes to morph apart or together as the space in the container changes.

The `glassEffect(_:in:)` modifier captures the content to send to the container to render. Apply the `glassEffect(_:in:)` modifier after other modifiers that affect the appearance of the view.

In the example below, two images are placed close to each other and the Liquid Glass effects begin to blend their shapes together. This creates a fluid animation as components move around each other within a container:

In some cases, you want the geometries of multiple views to contribute to a single Liquid Glass effect capsule, even when your content is at rest. Use the [glassEffectUnion(id:namespace:)](/documentation/swiftui/view/glasseffectunion(id:namespace:)) modifier to specify that a view contributes to a unified effect with a particular ID. This combines all effects with a similar shape, Liquid Glass effect, and ID into a single shape with the applied Liquid Glass material. This is especially useful when creating views dynamically, or with views that live outside of a layout container, like an `HStack` or `VStack`.

Morphing effects occur during transitions or animations between views with Liquid Glass effects. Coordinate transitions between views with effects in a container by using the [glassEffectID(_:in:)](/documentation/swiftui/view/glasseffectid(_:in:)) modifier. [Glass Effect Transition](/documentation/swiftui/glasseffecttransition) allows you to specify the type of transition to use when you want to add or remove effects within a container. For effects you want to add or remove that are positioned within the container’s assigned spacing, the default transition type is [matched Geometry](/documentation/swiftui/glasseffecttransition/matchedgeometry).

If you prefer to have a simpler transition or to create a custom transition, use the [materialize](/documentation/swiftui/glasseffecttransition/materialize) transition and [withAnimation(_:_:)](/documentation/swiftui/withanimation(_:_:)). Use the `materialize` transition for effects you want to add or remove that are farther from each other than the container’s assigned spacing. To provide people with a consistent experience, use `matchedGeometry` and `materialize` transitions across your apps. The system applies more than opacity changes with the available transition types.

Associate each Liquid Glass effect with a unique identifier within a namespace that the [Namespace](/documentation/swiftui/namespace) property wrapper provides. These IDs ensure SwiftUI animates the same shapes correctly when a shape appears or disappears due to view hierarchy changes. SwiftUI uses the spacing provided to the effect container along with the geometry of the shapes themselves to determine when and which appropriate shapes to morph into and out of.

The `glassEffectID(_:in:)` and `glassEffectTransition(_:)` modifiers only affect their content during view hierarchy transitions or animations.

In the example below, the eraser image transitions into and out of the pencil image when the `isExpanded` variable changes. The `GlassEffectContainer` has a spacing value of `40.0`, and the `HStack` within it has a spacing of `40.0`. This morphs the eraser image into the pencil image when the eraser’s nearest edge is less than or equal to the container’s spacing.

Creating too many Liquid Glass effect containers and applying too many effects to views outside of containers can degrade performance. Limit the use of Liquid Glass effects onscreen at the same time. Additionally, optimize how your app spends rendering time as people use it. To learn how to improve the performance of your UI, see [](https://developer.apple.com/videos/play/tech-talks/10855/) and [](https://developer.apple.com/videos/play/wwdc2025/306/).

- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectContainer](/documentation/swiftui/glasseffectcontainer)
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()

Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect(in: .rect(cornerRadius: 16.0))

Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect(.regular.tint(.orange).interactive())
```

Example 2 (swift):
```swift
GlassEffectContainer(spacing: 40.0) {
    HStack(spacing: 40.0) {
        Image(systemName: "scribble.variable")
            .frame(width: 80.0, height: 80.0)
            .font(.system(size: 36))
            .glassEffect()

        Image(systemName: "eraser.fill")
            .frame(width: 80.0, height: 80.0)
            .font(.system(size: 36))
            .glassEffect()

            // An `offset` shows how Liquid Glass effects react to each other in a container.
            // Use animations and components appearing and disappearing to obtain effects that look purposeful.
            .offset(x: -40.0, y: 0.0)
    }
}
```

Example 3 (swift):
```swift
let symbolSet: [String] = ["cloud.bolt.rain.fill", "sun.rain.fill", "moon.stars.fill", "moon.fill"]

GlassEffectContainer(spacing: 20.0) {
    HStack(spacing: 20.0) {
        ForEach(symbolSet.indices, id: \.self) { item in
            Image(systemName: symbolSet[item])
                .frame(width: 80.0, height: 80.0)
                .font(.system(size: 36))
                .glassEffect()
                .glassEffectUnion(id: item < 2 ? "1" : "2", namespace: namespace)
        }
    }
}
```

Example 4 (swift):
```swift
@State private var isExpanded: Bool = false
@Namespace private var namespace

var body: some View {
    GlassEffectContainer(spacing: 40.0) {
        HStack(spacing: 40.0) {
            Image(systemName: "scribble.variable")
                .frame(width: 80.0, height: 80.0)
                .font(.system(size: 36))
                .glassEffect()
                .glassEffectID("pencil", in: namespace)

            if isExpanded {
                Image(systemName: "eraser.fill")
                    .frame(width: 80.0, height: 80.0)
                    .font(.system(size: 36))
                    .glassEffect()
                    .glassEffectID("eraser", in: namespace)
            }
        }
    }

    Button("Toggle") {
        withAnimation {
            isExpanded.toggle()
        }
    }
    .buttonStyle(.glass)
}
```

---

## NSGlassEffectView

**URL:** https://sosumi.ai/documentation/AppKit/NSGlassEffectView?.md

**Contents:**
- Inherits From
- Conforms To
- Instance Properties
- Liquid Glass effects

---
title: NSGlassEffectView
description: A view that embeds its content view in a dynamic glass effect.
source: https://developer.apple.com/documentation/AppKit/NSGlassEffectView
timestamp: 2026-02-13T00:19:31.408Z
---

**Navigation:** [AppKit](/documentation/AppKit)

**Available on:** macOS 26.0+

> A view that embeds its content view in a dynamic glass effect.

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

- [contentView](/documentation/appkit/nsglasseffectview/contentview) The view to embed in glass.
- [cornerRadius](/documentation/appkit/nsglasseffectview/cornerradius) The amount of curvature for all corners of the glass.
- [style](/documentation/appkit/nsglasseffectview/style-swift.property) The style of glass this view uses.
- [tintColor](/documentation/appkit/nsglasseffectview/tintcolor) The color the glass effect view uses to tint the background and glass effect toward.

- [NSGlassEffectView.Style](/documentation/appkit/nsglasseffectview/style-swift.enum)
- [NSGlassEffectContainerView](/documentation/appkit/nsglasseffectcontainerview)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor class NSGlassEffectView
```

---

## matchedGeometry

**URL:** https://sosumi.ai/documentation/swiftui/glasseffecttransition/matchedgeometry?.md

**Contents:**
- Discussion

---
title: matchedGeometry
description: Returns the matched geometry glass effect transition.
source: https://developer.apple.com/documentation/swiftui/glasseffecttransition/matchedgeometry
timestamp: 2026-02-13T00:19:12.265Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [glasseffecttransition](/documentation/swiftui/glasseffecttransition)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> Returns the matched geometry glass effect transition.

The matched geometry transition allows the geometries of glass shapes during an appearance or disappearance phase of a transition to be derived from the geometry of a nearby shape within the glass container.

For example, if a newly appearing shape is within the spacing of any existing shape, it will use that shapes geometry to transition out of.

When using the [default](/documentation/swiftui/animation/default), this transition applies additional scale and offset effects to content when the identity of the shape does not change but its content does. Opt out of these additional animations by providing a specific animation like [spring](/documentation/swiftui/animation/spring).

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
static var matchedGeometry: GlassEffectTransition { get }
```

---

## glassEffectUnion(id:namespace:)

**URL:** https://sosumi.ai/documentation/swiftui/view/glasseffectunion(id:namespace:)?.md

**Contents:**
- Discussion

---
title: glassEffectUnion(id:namespace:)
description: Associates any Liquid Glass effects defined within this view to a union with the provided identifier.
source: https://developer.apple.com/documentation/swiftui/view/glasseffectunion(id:namespace:)
timestamp: 2026-02-13T00:18:57.759Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> Associates any Liquid Glass effects defined within this view to a union with the provided identifier.

You may want the geometries of multiple views to contribute to a single Liquid Glass effect shape. In these cases, you can use a [glassEffectUnion(id:namespace:)](/documentation/swiftui/view/glasseffectunion(id:namespace:)) to specify that a view should contribute to a union of Liquid Glass effects with a particular identifier. All Liquid Glass effects with the same shape and Liquid Glass variant will be combined into a single shape.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency func glassEffectUnion(id: (some Hashable & Sendable)?, namespace: Namespace.ID) -> some View
```

---

## GlassEffectContainer

**URL:** https://sosumi.ai/documentation/swiftui/glasseffectcontainer?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Styling views with Liquid Glass

---
title: GlassEffectContainer
description: A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
source: https://developer.apple.com/documentation/swiftui/glasseffectcontainer
timestamp: 2026-02-13T00:18:37.696Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.

Use a container with the [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:)) modifier. Each view with a Liquid Glass effect contributes a shape rendered with the effect to a set of shapes. SwiftUI renders the effects together, improving rendering performance and allowing the effects to interact with and morph into one another.

Configure how shapes interact with one another by customizing the default spacing value of the container. As shapes near one another, their paths start to blend into one another. The higher the spacing, the sooner blending begins as the shapes approach each other.

- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [View](/documentation/swiftui/view)

- [init(spacing:content:)](/documentation/swiftui/glasseffectcontainer/init(spacing:content:)) Creates a glass effect container with the provided spacing, extracting glass shapes from the provided content.

- [Applying Liquid Glass to custom views](/documentation/swiftui/applying-liquid-glass-to-custom-views)
- [Landmarks: Building an app with Liquid Glass](/documentation/swiftui/landmarks-building-an-app-with-liquid-glass)
- [glassEffect(_:in:)](/documentation/swiftui/view/glasseffect(_:in:))
- [interactive(_:)](/documentation/swiftui/glass/interactive(_:))
- [GlassEffectTransition](/documentation/swiftui/glasseffecttransition)
- [GlassButtonStyle](/documentation/swiftui/glassbuttonstyle)
- [GlassProminentButtonStyle](/documentation/swiftui/glassprominentbuttonstyle)
- [DefaultGlassEffectShape](/documentation/swiftui/defaultglasseffectshape)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency struct GlassEffectContainer<Content> where Content : View
```

---

## glassProminent

**URL:** https://sosumi.ai/documentation/swiftui/primitivebuttonstyle/glassprominent?.md

**Contents:**
- Discussion
- Getting built-in button styles

---
title: glassProminent
description: A button style that applies a prominent Liquid Glass effect based on the button’s context.
source: https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/glassprominent
timestamp: 2026-02-13T00:19:10.119Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [primitivebuttonstyle](/documentation/swiftui/primitivebuttonstyle)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+

> A button style that applies a prominent Liquid Glass effect based on the button’s context.

In tvOS, this button style applies a Liquid Glass effect regardless of whether the button has focus. This style is similar to the [bordered Prominent](/documentation/swiftui/primitivebuttonstyle/borderedprominent) style.

To apply this style to a button, or to a view that contains buttons, use the [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:)-66fbx) modifier.

- [automatic](/documentation/swiftui/primitivebuttonstyle/automatic)
- [accessoryBar](/documentation/swiftui/primitivebuttonstyle/accessorybar)
- [accessoryBarAction](/documentation/swiftui/primitivebuttonstyle/accessorybaraction)
- [bordered](/documentation/swiftui/primitivebuttonstyle/bordered)
- [borderedProminent](/documentation/swiftui/primitivebuttonstyle/borderedprominent)
- [borderless](/documentation/swiftui/primitivebuttonstyle/borderless)
- [card](/documentation/swiftui/primitivebuttonstyle/card)
- [glass](/documentation/swiftui/primitivebuttonstyle/glass)
- [glass(_:)](/documentation/swiftui/primitivebuttonstyle/glass(_:))
- [link](/documentation/swiftui/primitivebuttonstyle/link)
- [plain](/documentation/swiftui/primitivebuttonstyle/plain)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency static var glassProminent: GlassProminentButtonStyle { get }
```

---

## Complete Examples

### Toolbar with Glass Buttons

```swift
struct GlassToolbar: View {
    var body: some View {
        if #available(iOS 26, *) {
            GlassEffectContainer(spacing: 16) {
                HStack(spacing: 16) {
                    ToolbarButton(icon: "pencil", action: { })
                    ToolbarButton(icon: "eraser", action: { })
                    ToolbarButton(icon: "scissors", action: { })
                    Spacer()
                    ToolbarButton(icon: "square.and.arrow.up", action: { })
                }
                .padding(.horizontal)
            }
        } else {
            HStack(spacing: 16) {
                // ... fallback implementation
            }
        }
    }
}

struct ToolbarButton: View {
    let icon: String
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            Image(systemName: icon)
                .font(.title2)
                .frame(width: 44, height: 44)
        }
        .glassEffect(.regular.interactive(), in: .circle)
    }
}
```

### Card with Glass Effect

```swift
struct GlassCard: View {
    let title: String
    let subtitle: String

    var body: some View {
        if #available(iOS 26, *) {
            cardContent
                .glassEffect(.regular, in: .rect(cornerRadius: 20))
        } else {
            cardContent
                .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 20))
        }
    }

    private var cardContent: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(title)
                .font(.headline)
            Text(subtitle)
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}
```

### Segmented Control

```swift
struct GlassSegmentedControl: View {
    @Binding var selection: Int
    let options: [String]
    @Namespace private var animation

    var body: some View {
        if #available(iOS 26, *) {
            GlassEffectContainer(spacing: 4) {
                HStack(spacing: 4) {
                    ForEach(options.indices, id: \.self) { index in
                        Button(options[index]) {
                            withAnimation(.smooth) {
                                selection = index
                            }
                        }
                        .padding(.horizontal, 16)
                        .padding(.vertical, 8)
                        .glassEffect(
                            selection == index ? .regular.tint(.accentColor).interactive() : .regular.interactive(),
                            in: .capsule
                        )
                        .glassEffectID(selection == index ? "selected" : "option\(index)", in: animation)
                    }
                }
                .padding(4)
            }
        } else {
            Picker("Options", selection: $selection) {
                ForEach(options.indices, id: \.self) { index in
                    Text(options[index]).tag(index)
                }
            }
            .pickerStyle(.segmented)
        }
    }
}
```

## Fallback Strategies

For complete fallback guidance including material options and the `glassEffectWithFallback` modifier extension, see the "Availability & Fallbacks" section in the main `apple-liquid-glass-design` SKILL.md.
