# Swiftui-Components - Shapes And Drawing

**Pages:** 6

---

## RadialGradient

**URL:** https://sosumi.ai/documentation/swiftui/radialgradient?.md

**Contents:**
- Overview
- Conforms To
- Creating a radial gradient
- Supporting types

---
title: RadialGradient
description: A radial gradient.
source: https://developer.apple.com/documentation/swiftui/radialgradient
timestamp: 2026-02-13T19:34:24.269Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

The gradient applies the color function as the distance from a center point, scaled to fit within the defined start and end radii. The gradient maps the unit space center point into the bounding rectangle of each shape filled with the gradient.

When using a radial gradient as a shape style, you can also use [radialGradient(_:center:startRadius:endRadius:)](/documentation/swiftui/shapestyle/radialgradient(_:center:startradius:endradius:)).

- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [ShapeStyle](/documentation/swiftui/shapestyle)
- [View](/documentation/swiftui/view)

- [init(gradient:center:startRadius:endRadius:)](/documentation/swiftui/radialgradient/init(gradient:center:startradius:endradius:)) Creates a radial gradient from a base gradient.
- [init(colors:center:startRadius:endRadius:)](/documentation/swiftui/radialgradient/init(colors:center:startradius:endradius:)) Creates a radial gradient from a collection of colors.
- [init(stops:center:startRadius:endRadius:)](/documentation/swiftui/radialgradient/init(stops:center:startradius:endradius:)) Creates a radial gradient from a collection of color stops.

- [AngularGradient](/documentation/swiftui/angulargradient)
- [EllipticalGradient](/documentation/swiftui/ellipticalgradient)
- [LinearGradient](/documentation/swiftui/lineargradient)
- [Material](/documentation/swiftui/material)
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
@frozen struct RadialGradient
```

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
timestamp: 2026-02-13T19:34:04.211Z
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

## AngularGradient

**URL:** https://sosumi.ai/documentation/swiftui/angulargradient?.md

**Contents:**
- Overview
- Conforms To
- Creating a full rotation angular gradient
- Creating a partial rotation angular gradient
- Supporting types

---
title: AngularGradient
description: An angular gradient.
source: https://developer.apple.com/documentation/swiftui/angulargradient
timestamp: 2026-02-13T19:34:20.614Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> An angular gradient.

An angular gradient is also known as a “conic” gradient. This gradient applies the color function as the angle changes, relative to a center point and defined start and end angles. If `endAngle - startAngle > 2π`, the gradient only draws the last complete turn. If `endAngle - startAngle < 2π`, the gradient fills the missing area with the colors defined by gradient locations one and zero, transitioning between the two halfway across the missing area. The gradient maps the unit space center point into the bounding rectangle of each shape filled with the gradient.

When using an angular gradient as a shape style, you can also use [angularGradient(_:center:startAngle:endAngle:)](/documentation/swiftui/shapestyle/angulargradient(_:center:startangle:endangle:)), [conicGradient(_:center:angle:)](/documentation/swiftui/shapestyle/conicgradient(_:center:angle:)), or similar methods.

- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [ShapeStyle](/documentation/swiftui/shapestyle)
- [View](/documentation/swiftui/view)

- [init(gradient:center:angle:)](/documentation/swiftui/angulargradient/init(gradient:center:angle:)) Creates a conic gradient that completes a full turn.
- [init(colors:center:angle:)](/documentation/swiftui/angulargradient/init(colors:center:angle:)) Creates a conic gradient from a collection of colors that completes a full turn.
- [init(stops:center:angle:)](/documentation/swiftui/angulargradient/init(stops:center:angle:)) Creates a conic gradient from a collection of color stops that completes a full turn.

- [init(gradient:center:startAngle:endAngle:)](/documentation/swiftui/angulargradient/init(gradient:center:startangle:endangle:)) Creates an angular gradient.
- [init(colors:center:startAngle:endAngle:)](/documentation/swiftui/angulargradient/init(colors:center:startangle:endangle:)) Creates an angular gradient from a collection of colors.
- [init(stops:center:startAngle:endAngle:)](/documentation/swiftui/angulargradient/init(stops:center:startangle:endangle:)) Creates an angular gradient from a collection of color stops.

- [EllipticalGradient](/documentation/swiftui/ellipticalgradient)
- [LinearGradient](/documentation/swiftui/lineargradient)
- [RadialGradient](/documentation/swiftui/radialgradient)
- [Material](/documentation/swiftui/material)
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
@frozen struct AngularGradient
```

---

## Color

**URL:** https://sosumi.ai/documentation/swiftui/color?.md

**Contents:**
- Overview
- Conforms To
- Creating a color
- Creating a color from component values
- Creating a color from another color
- Getting standard colors
- Getting semantic colors
- Modifying a color
- Working with high dynamic range (HDR) colors
- Describing a color

---
title: Color
description: A representation of a color that adapts to a given context.
source: https://developer.apple.com/documentation/swiftui/color
timestamp: 2026-02-13T19:34:18.465Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A representation of a color that adapts to a given context.

You can create a color in one of several ways:

- Load a color from an Asset Catalog:

- Specify component values, like red, green, and blue; hue, saturation, and brightness; or white level:

- Create a color instance from another color, like a [UIColor](/documentation/UIKit/UIColor) or an [NSColor](/documentation/AppKit/NSColor):

- Use one of a palette of predefined colors, like [black](/documentation/swiftui/shapestyle/black), [green](/documentation/swiftui/shapestyle/green), and [purple](/documentation/swiftui/shapestyle/purple).

Some view modifiers can take a color as an argument. For example, [foregroundStyle(_:)](/documentation/swiftui/view/foregroundstyle(_:)) uses the color you provide to set the foreground color for view elements, like text or [sf](/design/Human-Interface-Guidelines/sf-symbols):

Because SwiftUI treats colors as [View](/documentation/swiftui/view) instances, you can also directly add them to a view hierarchy. For example, you can layer a rectangle beneath a sun image using colors defined above:

A color used as a view expands to fill all the space it’s given, as defined by the frame of the enclosing [ZStack](/documentation/swiftui/zstack) in the above example:

SwiftUI only resolves a color to a concrete value just before using it in a given environment. This enables a context-dependent appearance for system defined colors, or those that you load from an Asset Catalog. For example, a color can have distinct light and dark variants that the system chooses from at render time.

- [Copyable](/documentation/Swift/Copyable)
- [CustomStringConvertible](/documentation/Swift/CustomStringConvertible)
- [Equatable](/documentation/Swift/Equatable)
- [Hashable](/documentation/Swift/Hashable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [ShapeStyle](/documentation/swiftui/shapestyle)
- [Transferable](/documentation/CoreTransferable/Transferable)
- [View](/documentation/swiftui/view)

- [init(_:bundle:)](/documentation/swiftui/color/init(_:bundle:)) Creates a color from a color set that you indicate by name.
- [init(_:)](/documentation/swiftui/color/init(_:)) Creates a constant color with the values specified by the resolved color.
- [resolve(in:)](/documentation/swiftui/color/resolve(in:)) Evaluates this color to a resolved color given the current .

- [init(hue:saturation:brightness:opacity:)](/documentation/swiftui/color/init(hue:saturation:brightness:opacity:)) Creates a constant color from hue, saturation, and brightness values.
- [init(_:white:opacity:)](/documentation/swiftui/color/init(_:white:opacity:)) Creates a constant grayscale color.
- [init(_:red:green:blue:opacity:)](/documentation/swiftui/color/init(_:red:green:blue:opacity:)) Creates a constant color from red, green, and blue component values.
- [Color.RGBColorSpace](/documentation/swiftui/color/rgbcolorspace) A profile that specifies how to interpret a color value for display.

- [init(uiColor:)](/documentation/swiftui/color/init(uicolor:)) Creates a color from a UIKit color.
- [init(nsColor:)](/documentation/swiftui/color/init(nscolor:)) Creates a color from an AppKit color.
- [init(cgColor:)](/documentation/swiftui/color/init(cgcolor:)) Creates a color from a Core Graphics color.

- [black](/documentation/swiftui/color/black) A black color suitable for use in UI elements.
- [blue](/documentation/swiftui/color/blue) A context-dependent blue color suitable for use in UI elements.
- [brown](/documentation/swiftui/color/brown) A context-dependent brown color suitable for use in UI elements.
- [clear](/documentation/swiftui/color/clear) A clear color suitable for use in UI elements.
- [cyan](/documentation/swiftui/color/cyan) A context-dependent cyan color suitable for use in UI elements.
- [gray](/documentation/swiftui/color/gray) A context-dependent gray color suitable for use in UI elements.
- [green](/documentation/swiftui/color/green) A context-dependent green color suitable for use in UI elements.
- [indigo](/documentation/swiftui/color/indigo) A context-dependent indigo color suitable for use in UI elements.
- [mint](/documentation/swiftui/color/mint) A context-dependent mint color suitable for use in UI elements.
- [orange](/documentation/swiftui/color/orange) A context-dependent orange color suitable for use in UI elements.
- [pink](/documentation/swiftui/color/pink) A context-dependent pink color suitable for use in UI elements.
- [purple](/documentation/swiftui/color/purple) A context-dependent purple color suitable for use in UI elements.
- [red](/documentation/swiftui/color/red) A context-dependent red color suitable for use in UI elements.
- [teal](/documentation/swiftui/color/teal) A context-dependent teal color suitable for use in UI elements.
- [white](/documentation/swiftui/color/white) A white color suitable for use in UI elements.
- [yellow](/documentation/swiftui/color/yellow) A context-dependent yellow color suitable for use in UI elements.

- [accentColor](/documentation/swiftui/color/accentcolor) A color that reflects the accent color of the system or app.
- [primary](/documentation/swiftui/color/primary) The color to use for primary content.
- [secondary](/documentation/swiftui/color/secondary) The color to use for secondary content.

- [opacity(_:)](/documentation/swiftui/color/opacity(_:)) Multiplies the opacity of the color by the given amount.
- [gradient](/documentation/swiftui/color/gradient) Returns the standard gradient for the color .
- [mix(with:by:in:)](/documentation/swiftui/color/mix(with:by:in:)) Returns a version of self mixed with  by the amount specified by .
- [exposureAdjust(_:)](/documentation/swiftui/color/exposureadjust(_:)) Returns a new color with an exposure adjustment applied.
- [headroom(_:)](/documentation/swiftui/color/headroom(_:)) Creates a new color with specified HDR content headroom.

- [resolveHDR(in:)](/documentation/swiftui/color/resolvehdr(in:)) Evaluates this color to a resolved color with content headroom, given a set of environment values.
- [Color.ResolvedHDR](/documentation/swiftui/color/resolvedhdr) A concrete color value, including HDR headroom information.

- [description](/documentation/swiftui/color/description) A textual representation of the color.

- [==(_:_:)](/documentation/swiftui/color/==(_:_:)) Indicates whether two colors are equal.
- [hash(into:)](/documentation/swiftui/color/hash(into:)) Hashes the essential components of the color by feeding them into the given hash function.

- [cgColor](/documentation/swiftui/color/cgcolor) A Core Graphics representation of the color, if available.

- [ShapeStyle Implementations](/documentation/swiftui/color/shapestyle-implementations)
- [Transferable Implementations](/documentation/swiftui/color/transferable-implementations)

- [tint(_:)](/documentation/swiftui/view/tint(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Color
```

Example 2 (swift):
```swift
let aqua = Color("aqua") // Looks in your app's main bundle by default.
```

Example 3 (swift):
```swift
let skyBlue = Color(red: 0.4627, green: 0.8392, blue: 1.0)
let lemonYellow = Color(hue: 0.1639, saturation: 1, brightness: 1)
let steelGray = Color(white: 0.4745)
```

Example 4 (swift):
```swift
#if os(iOS)
let linkColor = Color(uiColor: .link)
#elseif os(macOS)
let linkColor = Color(nsColor: .linkColor)
#endif
```

---

## LinearGradient

**URL:** https://sosumi.ai/documentation/swiftui/lineargradient?.md

**Contents:**
- Overview
- Conforms To
- Creating a linear gradient
- Supporting types

---
title: LinearGradient
description: A linear gradient.
source: https://developer.apple.com/documentation/swiftui/lineargradient
timestamp: 2026-02-13T19:34:22.629Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

The gradient applies the color function along an axis, as defined by its start and end points. The gradient maps the unit space points into the bounding rectangle of each shape filled with the gradient.

When using a linear gradient as a shape style, you can also use [linearGradient(_:startPoint:endPoint:)](/documentation/swiftui/shapestyle/lineargradient(_:startpoint:endpoint:)).

- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [ShapeStyle](/documentation/swiftui/shapestyle)
- [View](/documentation/swiftui/view)

- [init(gradient:startPoint:endPoint:)](/documentation/swiftui/lineargradient/init(gradient:startpoint:endpoint:)) Creates a linear gradient from a base gradient.
- [init(colors:startPoint:endPoint:)](/documentation/swiftui/lineargradient/init(colors:startpoint:endpoint:)) Creates a linear gradient from a collection of colors.
- [init(stops:startPoint:endPoint:)](/documentation/swiftui/lineargradient/init(stops:startpoint:endpoint:)) Creates a linear gradient from a collection of color stops.

- [AngularGradient](/documentation/swiftui/angulargradient)
- [EllipticalGradient](/documentation/swiftui/ellipticalgradient)
- [RadialGradient](/documentation/swiftui/radialgradient)
- [Material](/documentation/swiftui/material)
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
@frozen struct LinearGradient
```

---

## Ellipse

**URL:** https://sosumi.ai/documentation/swiftui/ellipse?.md

**Contents:**
- Conforms To
- Creating an ellipse
- Creating circular shapes

---
title: Ellipse
description: An ellipse aligned inside the frame of the view containing it.
source: https://developer.apple.com/documentation/swiftui/ellipse
timestamp: 2026-02-13T19:34:05.811Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> An ellipse aligned inside the frame of the view containing it.

- [Animatable](/documentation/swiftui/animatable)
- [BitwiseCopyable](/documentation/Swift/BitwiseCopyable)
- [Copyable](/documentation/Swift/Copyable)
- [InsettableShape](/documentation/swiftui/insettableshape)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init()](/documentation/swiftui/ellipse/init()) Creates a new ellipse shape.

- [Circle](/documentation/swiftui/circle)
- [Capsule](/documentation/swiftui/capsule)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Ellipse
```

---
