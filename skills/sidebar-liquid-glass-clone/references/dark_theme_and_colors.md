# Sidebar-Liquid-Glass-Clone - Dark Theme And Colors

**Pages:** 8

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
timestamp: 2026-02-13T01:05:45.250Z
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

## environment(_:_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/environment(_:_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Modifying the environment of a view

---
title: environment(_:_:)
description: Sets the environment value of the specified key path to the given value.
source: https://developer.apple.com/documentation/swiftui/view/environment(_:_:)
timestamp: 2026-02-13T01:05:48.403Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the environment value of the specified key path to the given value.

A key path that indicates the property of the [Environment Values](/documentation/swiftui/environmentvalues) structure to update.

The new value to set for the item specified by `keyPath`.

A view that has the given value set in its environment.

Use this modifier to set one of the writable properties of the [Environment Values](/documentation/swiftui/environmentvalues) structure, including custom values that you create. For example, you can set the value associated with the [truncation Mode](/documentation/swiftui/environmentvalues/truncationmode) key:

You then read the value inside `MyView` or one of its descendants using the [Environment](/documentation/swiftui/environment) property wrapper:

SwiftUI provides dedicated view modifiers for setting most environment values, like the [truncationMode(_:)](/documentation/swiftui/view/truncationmode(_:)) modifier which sets the [truncation Mode](/documentation/swiftui/environmentvalues/truncationmode) value:

Prefer the dedicated modifier when available, and offer your own when defining custom environment values, as described in [Entry()](/documentation/swiftui/entry()).

This modifier affects the given view, as well as that view’s descendant views. It has no effect outside the view hierarchy on which you call it.

- [environment(_:)](/documentation/swiftui/view/environment(_:))
- [transformEnvironment(_:transform:)](/documentation/swiftui/view/transformenvironment(_:transform:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func environment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, _ value: V) -> some View
```

Example 2 (swift):
```swift
MyView()
    .environment(\.truncationMode, .head)
```

Example 3 (swift):
```swift
struct MyView: View {
    @Environment(\.truncationMode) var truncationMode: Text.TruncationMode

    var body: some View { ... }
}
```

Example 4 (swift):
```swift
MyView()
    .truncationMode(.head)
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
timestamp: 2026-02-13T01:05:13.740Z
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

## background(_:ignoresSafeAreaEdges:)

**URL:** https://sosumi.ai/documentation/swiftui/view/background(_:ignoressafeareaedges:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Layering views

---
title: background(_:ignoresSafeAreaEdges:)
description: Sets the view’s background to a style.
source: https://developer.apple.com/documentation/swiftui/view/background(_:ignoressafeareaedges:)
timestamp: 2026-02-13T01:04:43.567Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Sets the view’s background to a style.

An instance of a type that conforms to [Shape Style](/documentation/swiftui/shapestyle) that SwiftUI draws behind the modified view.

The set of edges for which to ignore safe area insets when adding the background. The default value is [all](/documentation/swiftui/edge/set/all). Specify an empty set to respect safe area insets on all edges.

A view with the specified style drawn behind it.

Use this modifier to place a type that conforms to the [Shape Style](/documentation/swiftui/shapestyle) protocol — like a [Color](/documentation/swiftui/color), [Material](/documentation/swiftui/material), or [Hierarchical Shape Style](/documentation/swiftui/hierarchicalshapestyle) — behind a view. For example, you can add the [regular Material](/documentation/swiftui/shapestyle/regularmaterial) behind a [Label](/documentation/swiftui/label):

SwiftUI anchors the style to the view’s bounds. For the example above, the background fills the entirety of the label’s frame, which includes the padding:

SwiftUI limits the background style’s extent to the modified view’s container-relative shape. You can see this effect if you constrain the `FlagLabel` view with a [containerShape(_:)](/documentation/swiftui/view/containershape(_:)) modifier:

The background takes on the specified container shape:

By default, the background ignores safe area insets on all edges, but you can provide a specific set of edges to ignore, or an empty set to respect safe area insets on all edges:

If you want to specify a [View](/documentation/swiftui/view) or a stack of views as the background, use [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:)) instead. To specify a [Shape](/documentation/swiftui/shape) or [Insettable Shape](/documentation/swiftui/insettableshape), use [background(_:in:fillStyle:)](/documentation/swiftui/view/background(_:in:fillstyle:)) . To configure the background of a presentation, like a sheet, use [presentationBackground(_:)](/documentation/swiftui/view/presentationbackground(_:)).

- [Adding a background to your view](/documentation/swiftui/adding-a-background-to-your-view)
- [ZStack](/documentation/swiftui/zstack)
- [zIndex(_:)](/documentation/swiftui/view/zindex(_:))
- [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:))
- [background(ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(ignoressafeareaedges:))
- [background(_:in:fillStyle:)](/documentation/swiftui/view/background(_:in:fillstyle:))
- [background(in:fillStyle:)](/documentation/swiftui/view/background(in:fillstyle:))
- [overlay(alignment:content:)](/documentation/swiftui/view/overlay(alignment:content:))
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
nonisolated func background<S>(_ style: S, ignoresSafeAreaEdges edges: Edge.Set = .all) -> some View where S : ShapeStyle
```

Example 2 (swift):
```swift
struct FlagLabel: View {
    var body: some View {
        Label("Flag", systemImage: "flag.fill")
            .padding()
            .background(.regularMaterial)
    }
}
```

Example 3 (swift):
```swift
FlagLabel()
    .containerShape(RoundedRectangle(cornerRadius: 16))
```

Example 4 (swift):
```swift
Rectangle()
    .background(
        .regularMaterial,
        ignoresSafeAreaEdges: []) // Ignore no safe area insets.
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
timestamp: 2026-02-13T01:05:46.815Z
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

## colorScheme

**URL:** https://sosumi.ai/documentation/swiftui/environmentvalues/colorscheme?.md

**Contents:**
- Discussion
- Detecting and requesting the light or dark appearance

---
title: colorScheme
description: The color scheme of this environment.
source: https://developer.apple.com/documentation/swiftui/environmentvalues/colorscheme
timestamp: 2026-02-13T01:05:49.930Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [environmentvalues](/documentation/swiftui/environmentvalues)

**Instance Property**

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> The color scheme of this environment.

Read this environment value from within a view to find out if SwiftUI is currently displaying the view using the [light](/documentation/swiftui/colorscheme/light) or [dark](/documentation/swiftui/colorscheme/dark) appearance. The value that you receive depends on whether the user has enabled Dark Mode, possibly superseded by the configuration of the current presentation’s view hierarchy.

You can set the `colorScheme` environment value directly, but that usually isn’t what you want. Doing so changes the color scheme of the given view and its child views but *not* the views above it in the view hierarchy. Instead, set a color scheme using the [preferredColorScheme(_:)](/documentation/swiftui/view/preferredcolorscheme(_:)) modifier, which also propagates the value up through the view hierarchy to the enclosing presentation, like a sheet or a window.

When adjusting your app’s user interface to match the color scheme, consider also checking the [color Scheme Contrast](/documentation/swiftui/environmentvalues/colorschemecontrast) property, which reflects a system-wide contrast setting that the user controls. For information, see [accessibility#Color-and](/design/Human-Interface-Guidelines/accessibility#Color-and-effects) in the Human Interface Guidelines.

> [!NOTE]
> If you only need to provide different colors or images for different color scheme and contrast settings, do that in your app’s Asset Catalog. See [asset](/documentation/Xcode/asset-management).

- [preferredColorScheme(_:)](/documentation/swiftui/view/preferredcolorscheme(_:))
- [ColorScheme](/documentation/swiftui/colorscheme)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
var colorScheme: ColorScheme { get set }
```

Example 2 (swift):
```swift
@Environment(\.colorScheme) private var colorScheme

var body: some View {
    Text(colorScheme == .dark ? "Dark" : "Light")
}
```

---

## foregroundStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/foregroundstyle(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Styling content

---
title: foregroundStyle(_:)
description: Sets a view’s foreground elements to use a given style.
source: https://developer.apple.com/documentation/swiftui/view/foregroundstyle(_:)
timestamp: 2026-02-13T01:05:20.337Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Sets a view’s foreground elements to use a given style.

The color or pattern to use when filling in the foreground elements. To indicate a specific value, use [Color](/documentation/swiftui/color) or [image(_:sourceRect:scale:)](/documentation/swiftui/shapestyle/image(_:sourcerect:scale:)), or one of the gradient types, like [linearGradient(colors:startPoint:endPoint:)](/documentation/swiftui/shapestyle/lineargradient(colors:startpoint:endpoint:)). To set a style that’s relative to the containing view’s style, use one of the semantic styles, like [primary](/documentation/swiftui/shapestyle/primary).

A view that uses the given foreground style.

Use this method to style foreground content like text, shapes, and template images (including symbols):

The example above creates a row of [teal](/documentation/swiftui/shapestyle/teal) foreground elements:

You can use any style that conforms to the [Shape Style](/documentation/swiftui/shapestyle) protocol, like the [teal](/documentation/swiftui/shapestyle/teal) color in the example above, or the [linearGradient(colors:startPoint:endPoint:)](/documentation/swiftui/shapestyle/lineargradient(colors:startpoint:endpoint:)) gradient shown below:

> [!TIP]
> If you want to fill a single [Shape](/documentation/swiftui/shape) instance with a style, use the [fill(style:)](/documentation/swiftui/shape/fill(style:)) shape modifier instead because it’s more efficient.

SwiftUI creates a context-dependent render for a given style. For example, a [Color](/documentation/swiftui/color) that you load from an asset catalog can have different light and dark appearances, while some styles also vary by platform.

Hierarchical foreground styles like `ShapeStyle/secondary` don’t impose a style of their own, but instead modify other styles. In particular, they modify the primary level of the current foreground style to the degree given by the hierarchical style’s name. To find the current foreground style to modify, SwiftUI looks for the innermost containing style that you apply with the `foregroundStyle(_:)` or the [foregroundColor(_:)](/documentation/swiftui/view/foregroundcolor(_:)) modifier. If you haven’t specified a style, SwiftUI uses the default foreground style, as in the following example:

If you add a foreground style on the enclosing [VStack](/documentation/swiftui/vstack), the hierarchical styling responds accordingly:

When you apply a custom style to a view, the view disables the vibrancy effect for foreground elements in that view, or in any of its child views, that it would otherwise gain from adding a background material — for example, using the [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:)) modifier. However, hierarchical styles applied to the default foreground don’t disable vibrancy.

- [border(_:width:)](/documentation/swiftui/view/border(_:width:))
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
nonisolated func foregroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
```

Example 2 (swift):
```swift
HStack {
    Image(systemName: "triangle.fill")
    Text("Hello, world!")
    RoundedRectangle(cornerRadius: 5)
        .frame(width: 40, height: 20)
}
.foregroundStyle(.teal)
```

Example 3 (swift):
```swift
Text("Gradient Text")
    .font(.largeTitle)
    .foregroundStyle(
        .linearGradient(
            colors: [.yellow, .blue],
            startPoint: .top,
            endPoint: .bottom
        )
    )
```

Example 4 (swift):
```swift
VStack(alignment: .leading) {
    Label("Primary", systemImage: "1.square.fill")
    Label("Secondary", systemImage: "2.square.fill")
        .foregroundStyle(.secondary)
}
```

---

## scrollContentBackground(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/scrollcontentbackground(_:)?.md

**Contents:**
- Parameters
- Discussion
- Managing content visibility

---
title: scrollContentBackground(_:)
description: Specifies the visibility of the background for scrollable views within this view.
source: https://developer.apple.com/documentation/swiftui/view/scrollcontentbackground(_:)
timestamp: 2026-02-13T01:05:59.558Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+

> Specifies the visibility of the background for scrollable views within this view.

The visibility to use for the background.

The following example hides the standard system background of the List.

On macOS 15.0 and later, the visibility of the scroll background helps achieve the seamless window/titlebar appearance for scroll views that fill the window’s content view, or a pane’s full width and height. `List` and `Form` have the seamless appearance by default, configurable by hiding the scroll background. `ScrollView` can become seamless by making the background visible.

- [scrollClipDisabled(_:)](/documentation/swiftui/view/scrollclipdisabled(_:))
- [ScrollContentOffsetAdjustmentBehavior](/documentation/swiftui/scrollcontentoffsetadjustmentbehavior)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func scrollContentBackground(_ visibility: Visibility) -> some View
```

Example 2 (swift):
```swift
List {
    Text("One")
    Text("Two")
    Text("Three")
}
.scrollContentBackground(.hidden)
```

---
