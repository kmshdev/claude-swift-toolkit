# Neuralforge-Chat-Sidebar - Color And Theming

**Pages:** 2

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
timestamp: 2026-02-13T01:42:34.843Z
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

## preferredColorScheme(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/preferredcolorscheme(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Detecting and requesting the light or dark appearance

---
title: preferredColorScheme(_:)
description: Sets the preferred color scheme for this presentation.
source: https://developer.apple.com/documentation/swiftui/view/preferredcolorscheme(_:)
timestamp: 2026-02-13T01:42:36.758Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the preferred color scheme for this presentation.

The preferred color scheme for this view, or `nil` to indicate no preference.

A view that sets the color scheme.

Use one of the values in [Color Scheme](/documentation/swiftui/colorscheme) with this modifier to set a preferred color scheme for the nearest enclosing presentation, like a popover, a sheet, or a window. The value that you set overrides the user’s Dark Mode selection for that presentation. In the example below, the [Toggle](/documentation/swiftui/toggle) controls an `isDarkMode` state variable, which in turn controls the color scheme of the sheet that contains the toggle:

If you apply the modifier to any of the views in the sheet — which in this case are a [List](/documentation/swiftui/list) and a [Toggle](/documentation/swiftui/toggle) — the value that you set propagates up through the view hierarchy to the enclosing presentation, or until another color scheme modifier higher in the hierarchy overrides it. The value you set also flows down to all child views of the enclosing presentation.

Pass `nil` to indicate that there is no preferred color scheme for this view. This is useful in cases where a preferred color scheme should only be applied conditionally. In the previous example, the sheet will prefer dark mode when `isDarkMode` is set to `true`, but otherwise defer to the color scheme as determined by the system.

Multiple views in the same view hierarchy can set a preferred color scheme. Applying this modifier overrides any existing preferred color scheme set for the view, such as by one of its subviews. If there are conflicting, non-`nil` color scheme preferences set by parallel branches of the view hierarchy, the system will prioritize the first non-`nil` preference based on the order of the views. In the example below, the preferred color scheme for the entire view will resolve to `.dark`, from the second view:

A common use for this modifier is to create side-by-side previews of the same view with light and dark appearances:

If you need to detect the color scheme that currently applies to a view, read the [color Scheme](/documentation/swiftui/environmentvalues/colorscheme) environment value:

- [colorScheme](/documentation/swiftui/environmentvalues/colorscheme)
- [ColorScheme](/documentation/swiftui/colorscheme)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func preferredColorScheme(_ colorScheme: ColorScheme?) -> some View
```

Example 2 (swift):
```swift
@State private var isPresented = false
@State private var isDarkMode = true

var body: some View {
    Button("Show Sheet") {
        isPresented = true
    }
    .sheet(isPresented: $isPresented) {
        List {
            Toggle("Dark Mode", isOn: $isDarkMode)
        }
        .preferredColorScheme(isDarkMode ? .dark : nil)
    }
}
```

Example 3 (swift):
```swift
VStack {
    Text("First")
        .preferredColorScheme(.light)
        .preferredColorScheme(nil) // overrides `.light`

    Text("Second")
        .preferredColorScheme(.dark)

    Text("Third")
        .preferredColorScheme(.light)
}
```

Example 4 (swift):
```swift
struct MyView_Previews: PreviewProvider {
    static var previews: some View {
        MyView().preferredColorScheme(.light)
        MyView().preferredColorScheme(.dark)
    }
}
```

---
