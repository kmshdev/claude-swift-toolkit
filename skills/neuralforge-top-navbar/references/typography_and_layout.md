# Neuralforge-Top-Navbar - Typography And Layout

**Pages:** 7

---

## frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)

**URL:** https://sosumi.ai/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Influencing a view’s size

---
title: frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)
description: Positions this view within an invisible frame having the specified size constraints.
source: https://developer.apple.com/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:)
timestamp: 2026-02-13T03:56:54.455Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Positions this view within an invisible frame having the specified size constraints.

The minimum width of the resulting frame.

The ideal width of the resulting frame.

The maximum width of the resulting frame.

The minimum height of the resulting frame.

The ideal height of the resulting frame.

The maximum height of the resulting frame.

The alignment of this view inside the resulting frame. Note that most alignment values have no apparent effect when the size of the frame happens to match that of this view.

A view with flexible dimensions given by the call’s non-`nil` parameters.

Always specify at least one size characteristic when calling this method. Pass `nil` or leave out a characteristic to indicate that the frame should adopt this view’s sizing behavior, constrained by the other non-`nil` arguments.

The size proposed to this view is the size proposed to the frame, limited by any constraints specified, and with any ideal dimensions specified replacing any corresponding unspecified dimensions in the proposal.

If no minimum or maximum constraint is specified in a given dimension, the frame adopts the sizing behavior of its child in that dimension. If both constraints are specified in a dimension, the frame unconditionally adopts the size proposed for it, clamped to the constraints. Otherwise, the size of the frame in either dimension is:

- If a minimum constraint is specified and the size proposed for the frame by the parent is less than the size of this view, the proposed size, clamped to that minimum.
- If a maximum constraint is specified and the size proposed for the frame by the parent is greater than the size of this view, the proposed size, clamped to that maximum.
- Otherwise, the size of this view.

- [frame(width:height:alignment:)](/documentation/swiftui/view/frame(width:height:alignment:))
- [frame(depth:alignment:)](/documentation/swiftui/view/frame(depth:alignment:))
- [frame(minDepth:idealDepth:maxDepth:alignment:)](/documentation/swiftui/view/frame(mindepth:idealdepth:maxdepth:alignment:))
- [containerRelativeFrame(_:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:))
- [containerRelativeFrame(_:alignment:_:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:_:))
- [containerRelativeFrame(_:count:span:spacing:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:count:span:spacing:alignment:))
- [fixedSize()](/documentation/swiftui/view/fixedsize())
- [fixedSize(horizontal:vertical:)](/documentation/swiftui/view/fixedsize(horizontal:vertical:))
- [layoutPriority(_:)](/documentation/swiftui/view/layoutpriority(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func frame(minWidth: CGFloat? = nil, idealWidth: CGFloat? = nil, maxWidth: CGFloat? = nil, minHeight: CGFloat? = nil, idealHeight: CGFloat? = nil, maxHeight: CGFloat? = nil, alignment: Alignment = .center) -> some View
```

---

## font(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/font(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Setting a font

---
title: font(_:)
description: Sets the default font for text in this view.
source: https://developer.apple.com/documentation/swiftui/view/font(_:)
timestamp: 2026-02-13T03:56:50.078Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the default font for text in this view.

The default font to use in this view.

A view with the default font set to the value you supply.

Use `font(_:)` to apply a specific font to all of the text in a view.

The example below shows the effects of applying fonts to individual views and to view hierarchies. Font information flows down the view hierarchy as part of the environment, and remains in effect unless overridden at the level of an individual view or view container.

Here, the outermost [VStack](/documentation/swiftui/vstack) applies a 16-point system font as a default font to views contained in that [VStack](/documentation/swiftui/vstack). Inside that stack, the example applies a [large Title](/documentation/swiftui/font/largetitle) font to just the first text view; this explicitly overrides the default. The remaining stack and the views contained with it continue to use the 16-point system font set by their containing view:

- [Applying custom fonts to text](/documentation/swiftui/applying-custom-fonts-to-text)
- [fontDesign(_:)](/documentation/swiftui/view/fontdesign(_:))
- [fontWeight(_:)](/documentation/swiftui/view/fontweight(_:))
- [fontWidth(_:)](/documentation/swiftui/view/fontwidth(_:))
- [font](/documentation/swiftui/environmentvalues/font)
- [Font](/documentation/swiftui/font)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func font(_ font: Font?) -> some View
```

Example 2 (swift):
```swift
VStack {
    Text("Font applied to a text view.")
        .font(.largeTitle)

    VStack {
        Text("These 2 text views have the same font")
        Text("applied to their parent hierarchy")
    }
}
.font(.system(size: 16, weight: .light, design: .default))
```

---

## Text

**URL:** https://sosumi.ai/documentation/swiftui/text?.md

**Contents:**
- Overview
  - Localizing strings
- Conforms To
- Creating a text view
- Choosing a font
- Styling the view’s text
- Fitting text into available space
- Localizing text
- Configuring voiceover
- Providing accessibility information

---
title: Text
description: A view that displays one or more lines of read-only text.
source: https://developer.apple.com/documentation/swiftui/text
timestamp: 2026-02-13T03:56:47.830Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A view that displays one or more lines of read-only text.

A text view draws a string in your app’s user interface using a [body](/documentation/swiftui/font/body) font that’s appropriate for the current platform. You can choose a different standard font, like [title](/documentation/swiftui/font/title) or [caption](/documentation/swiftui/font/caption), using the [font(_:)](/documentation/swiftui/view/font(_:)) view modifier.

If you need finer control over the styling of the text, you can use the same modifier to configure a system font or choose a custom font. You can also apply view modifiers like [bold()](/documentation/swiftui/text/bold()) or [italic()](/documentation/swiftui/text/italic()) to further adjust the formatting.

To apply styling within specific portions of the text, you can create the text view from an [Attributed String](/documentation/Foundation/AttributedString), which in turn allows you to use Markdown to style runs of text. You can mix string attributes and SwiftUI modifiers, with the string attributes taking priority.

A text view always uses exactly the amount of space it needs to display its rendered contents, but you can affect the view’s layout. For example, you can use the [frame(width:height:alignment:)](/documentation/swiftui/view/frame(width:height:alignment:)) modifier to propose specific dimensions to the view. If the view accepts the proposal but the text doesn’t fit into the available space, the view uses a combination of wrapping, tightening, scaling, and truncation to make it fit. With a width of `100` points but no constraint on the height, a text view might wrap a long string:

Use modifiers like [lineLimit(_:)](/documentation/swiftui/view/linelimit(_:)), [allowsTightening(_:)](/documentation/swiftui/view/allowstightening(_:)), [minimumScaleFactor(_:)](/documentation/swiftui/view/minimumscalefactor(_:)), and [truncationMode(_:)](/documentation/swiftui/view/truncationmode(_:)) to configure how the view handles space constraints. For example, combining a fixed width and a line limit of `1` results in truncation for text that doesn’t fit in that space:

If you initialize a text view with a string literal, the view uses the [init(_:tableName:bundle:comment:)](/documentation/swiftui/text/init(_:tablename:bundle:comment:)) initializer, which interprets the string as a localization key and searches for the key in the table you specify, or in the default table if you don’t specify one.

For an app localized in both English and Spanish, the above view displays “pencil” and “lápiz” for English and Spanish users, respectively. If the view can’t perform localization, it displays the key instead. For example, if the same app lacks Danish localization, the view displays “pencil” for users in that locale. Similarly, an app that lacks any localization information displays “pencil” in any locale.

To explicitly bypass localization for a string literal, use the [init(verbatim:)](/documentation/swiftui/text/init(verbatim:)) initializer.

If you initialize a text view with a variable value, the view uses the [init(_:)](/documentation/swiftui/text/init(_:)-9d1g4) initializer, which doesn’t localize the string. However, you can request localization by creating a [Localized String Key](/documentation/swiftui/localizedstringkey) instance first, which triggers the [init(_:tableName:bundle:comment:)](/documentation/swiftui/text/init(_:tablename:bundle:comment:)) initializer instead:

When localizing a string variable, you can use the default table by omitting the optional initialization parameters — as in the above example — just like you might for a string literal.

When composing a complex string, where there is a need to assemble multiple pieces of text, use string interpolation:

This would look up the `"Hello, %@"` localization key in the localized string file and replace the format specifier `%@` with the value of `name` before rendering the text on screen.

Using string interpolation ensures that the text in your app can be localized correctly in all locales, especially in right-to-left languages.

If you desire to style only parts of interpolated text while ensuring that the content can still be localized correctly, interpolate `Text` or [Attributed String](/documentation/Foundation/AttributedString):

The example above uses [appendInterpolation(_:)](/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:)-4qyfo) and will look up the `"Hello, %@"` in the localized string file and interpolate a bold text rendering the value of  `name`.

Using [appendInterpolation(_:)](/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:)-5m52e) you can interpolate [Image](/documentation/swiftui/image) in text.

- [Copyable](/documentation/Swift/Copyable)
- [Equatable](/documentation/Swift/Equatable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [View](/documentation/swiftui/view)

- [init(_:tableName:bundle:comment:)](/documentation/swiftui/text/init(_:tablename:bundle:comment:)) Creates a text view that displays localized content identified by a key.
- [init(_:)](/documentation/swiftui/text/init(_:)) Creates a text view that displays styled attributed content.
- [init(verbatim:)](/documentation/swiftui/text/init(verbatim:)) Creates a text view that displays a string literal without localization.
- [init(_:style:)](/documentation/swiftui/text/init(_:style:)) Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](/documentation/swiftui/text/init(_:format:)) Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](/documentation/swiftui/text/init(_:formatter:)) Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval:pauseTime:countsDown:showsHours:)](/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:)) Creates an instance that displays a timer counting within the provided interval.

- [font(_:)](/documentation/swiftui/text/font(_:)) Sets the default font for text in the view.
- [fontWeight(_:)](/documentation/swiftui/text/fontweight(_:)) Sets the font weight of the text.
- [fontDesign(_:)](/documentation/swiftui/text/fontdesign(_:)) Sets the font design of the text.
- [fontWidth(_:)](/documentation/swiftui/text/fontwidth(_:)) Sets the font width of the text.

- [foregroundStyle(_:)](/documentation/swiftui/text/foregroundstyle(_:)) Sets the style of the text displayed by this view.
- [bold()](/documentation/swiftui/text/bold()) Applies a bold or emphasized treatment to the fonts of the text.
- [bold(_:)](/documentation/swiftui/text/bold(_:)) Applies a bold font weight to the text.
- [italic()](/documentation/swiftui/text/italic()) Applies italics to the text.
- [italic(_:)](/documentation/swiftui/text/italic(_:)) Applies italics to the text.
- [strikethrough(_:color:)](/documentation/swiftui/text/strikethrough(_:color:)) Applies a strikethrough to the text.
- [strikethrough(_:pattern:color:)](/documentation/swiftui/text/strikethrough(_:pattern:color:)) Applies a strikethrough to the text.
- [underline(_:color:)](/documentation/swiftui/text/underline(_:color:)) Applies an underline to the text.
- [underline(_:pattern:color:)](/documentation/swiftui/text/underline(_:pattern:color:)) Applies an underline to the text.
- [monospaced(_:)](/documentation/swiftui/text/monospaced(_:)) Modifies the font of the text to use the fixed-width variant of the current font, if possible.
- [monospacedDigit()](/documentation/swiftui/text/monospaceddigit()) Modifies the text view’s font to use fixed-width digits, while leaving other characters proportionally spaced.
- [kerning(_:)](/documentation/swiftui/text/kerning(_:)) Sets the spacing, or kerning, between characters.
- [tracking(_:)](/documentation/swiftui/text/tracking(_:)) Sets the tracking for the text.
- [baselineOffset(_:)](/documentation/swiftui/text/baselineoffset(_:)) Sets the vertical offset for the text relative to its baseline.
- [Text.Case](/documentation/swiftui/text/case) A scheme for transforming the capitalization of characters within text.
- [Text.DateStyle](/documentation/swiftui/text/datestyle) A predefined style used to display a .
- [Text.LineStyle](/documentation/swiftui/text/linestyle) Description of the style used to draw the line for  and .

- [textScale(_:isEnabled:)](/documentation/swiftui/text/textscale(_:isenabled:)) Applies a text scale to the text.
- [Text.Scale](/documentation/swiftui/text/scale) Defines text scales
- [Text.TruncationMode](/documentation/swiftui/text/truncationmode) The type of truncation to apply to a line of text when it’s too long to fit in the available space.

- [typesettingLanguage(_:isEnabled:)](/documentation/swiftui/text/typesettinglanguage(_:isenabled:)) Specifies the language for typesetting.

- [speechAdjustedPitch(_:)](/documentation/swiftui/text/speechadjustedpitch(_:)) Raises or lowers the pitch of spoken text.
- [speechAlwaysIncludesPunctuation(_:)](/documentation/swiftui/text/speechalwaysincludespunctuation(_:)) Sets whether VoiceOver should always speak all punctuation in the text view.
- [speechAnnouncementsQueued(_:)](/documentation/swiftui/text/speechannouncementsqueued(_:)) Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [speechSpellsOutCharacters(_:)](/documentation/swiftui/text/speechspellsoutcharacters(_:)) Sets whether VoiceOver should speak the contents of the text view character by character.

- [accessibilityHeading(_:)](/documentation/swiftui/text/accessibilityheading(_:)) Sets the accessibility level of this heading.
- [accessibilityLabel(_:)](/documentation/swiftui/text/accessibilitylabel(_:)) Adds a label to the view that describes its contents.
- [accessibilityTextContentType(_:)](/documentation/swiftui/text/accessibilitytextcontenttype(_:)) Sets an accessibility text content type.

- [+(_:_:)](/documentation/swiftui/text/+(_:_:)) Concatenates the text in two text views in a new text view.

- [foregroundColor(_:)](/documentation/swiftui/text/foregroundcolor(_:)) Sets the color of the text displayed by this view.

- [Text.AlignmentStrategy](/documentation/swiftui/text/alignmentstrategy) The way SwiftUI infers the appropriate text alignment if no value is explicitly provided.
- [Text.Layout](/documentation/swiftui/text/layout) A value describing the layout and custom attributes of a tree of  views.
- [Text.LayoutKey](/documentation/swiftui/text/layoutkey) A preference key that provides the  values for all text views in the queried subtree.
- [Text.WritingDirectionStrategy](/documentation/swiftui/text/writingdirectionstrategy) The way SwiftUI infers the appropriate writing direction if no value is explicitly provided.

- [customAttribute(_:)](/documentation/swiftui/text/customattribute(_:)) Adds a custom attribute to the text view.
- [textVariant(_:)](/documentation/swiftui/text/textvariant(_:)) Controls the way text size variants are chosen.

- [Label](/documentation/swiftui/label)
- [labelStyle(_:)](/documentation/swiftui/view/labelstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Text
```

Example 2 (swift):
```swift
Text("Hamlet")
    .font(.title)
```

Example 3 (swift):
```swift
Text("by William Shakespeare")
    .font(.system(size: 12, weight: .light, design: .serif))
    .italic()
```

Example 4 (swift):
```swift
let attributedString = try! AttributedString(
    markdown: "_Hamlet_ by William Shakespeare")

var body: some View {
    Text(attributedString)
        .font(.system(size: 12, weight: .light, design: .serif))
}
```

---

## clipShape(_:style:)

**URL:** https://sosumi.ai/documentation/swiftui/view/clipshape(_:style:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Masking and clipping

---
title: clipShape(_:style:)
description: Sets a clipping shape for this view.
source: https://developer.apple.com/documentation/swiftui/view/clipshape(_:style:)
timestamp: 2026-02-13T03:56:56.687Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets a clipping shape for this view.

The clipping shape to use for this view. The `shape` fills the view’s frame, while maintaining its aspect ratio.

The fill style to use when rasterizing `shape`.

A view that clips this view to `shape`, using `style` to define the shape’s rasterization.

Use `clipShape(_:style:)` to clip the view to the provided shape. By applying a clipping shape to a view, you preserve the parts of the view covered by the shape, while eliminating other parts of the view. The clipping shape itself isn’t visible.

For example, this code applies a circular clipping shape to a `Text` view:

The resulting view shows only the portion of the text that lies within the bounds of the circle.

- [mask(alignment:_:)](/documentation/swiftui/view/mask(alignment:_:))
- [clipped(antialiased:)](/documentation/swiftui/view/clipped(antialiased:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func clipShape<S>(_ shape: S, style: FillStyle = FillStyle()) -> some View where S : Shape
```

Example 2 (swift):
```swift
Text("Clipped text in a circle")
    .frame(width: 175, height: 100)
    .foregroundColor(Color.white)
    .background(Color.black)
    .clipShape(Circle())
```

---

## Capsule

**URL:** https://sosumi.ai/documentation/swiftui/capsule?.md

**Contents:**
- Overview
- Conforms To
- Creating a capsule
- Getting the shape’s characteristics
- Creating circular shapes

---
title: Capsule
description: A capsule shape aligned inside the frame of the view containing it.
source: https://developer.apple.com/documentation/swiftui/capsule
timestamp: 2026-02-13T03:56:58.803Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A capsule shape aligned inside the frame of the view containing it.

A capsule shape is equivalent to a rounded rectangle where the corner radius is chosen as half the length of the rectangle’s smallest edge.

- [Animatable](/documentation/swiftui/animatable)
- [Copyable](/documentation/Swift/Copyable)
- [InsettableShape](/documentation/swiftui/insettableshape)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init(style:)](/documentation/swiftui/capsule/init(style:)) Creates a new capsule shape.

- [style](/documentation/swiftui/capsule/style)

- [Circle](/documentation/swiftui/circle)
- [Ellipse](/documentation/swiftui/ellipse)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Capsule
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
timestamp: 2026-02-13T03:56:52.258Z
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

## RoundedRectangle

**URL:** https://sosumi.ai/documentation/swiftui/roundedrectangle?.md

**Contents:**
- Conforms To
- Creating a rounded rectangle
- Getting the shape’s characteristics
- Supporting types
- Creating rectangular shapes

---
title: RoundedRectangle
description: A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
source: https://developer.apple.com/documentation/swiftui/roundedrectangle
timestamp: 2026-02-13T03:57:00.711Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A rectangular shape with rounded corners, aligned inside the frame of the view containing it.

- [Animatable](/documentation/swiftui/animatable)
- [Copyable](/documentation/Swift/Copyable)
- [InsettableShape](/documentation/swiftui/insettableshape)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [Shape](/documentation/swiftui/shape)
- [View](/documentation/swiftui/view)

- [init(cornerRadius:style:)](/documentation/swiftui/roundedrectangle/init(cornerradius:style:)) Creates a new rounded rectangle shape.
- [init(cornerSize:style:)](/documentation/swiftui/roundedrectangle/init(cornersize:style:)) Creates a new rounded rectangle shape.

- [cornerSize](/documentation/swiftui/roundedrectangle/cornersize) The width and height of the rounded rectangle’s corners.
- [style](/documentation/swiftui/roundedrectangle/style) The style of corners drawn by the rounded rectangle.

- [animatableData](/documentation/swiftui/roundedrectangle/animatabledata) The data to animate.

- [Rectangle](/documentation/swiftui/rectangle)
- [RoundedCornerStyle](/documentation/swiftui/roundedcornerstyle)
- [RoundedRectangularShape](/documentation/swiftui/roundedrectangularshape)
- [RoundedRectangularShapeCorners](/documentation/swiftui/roundedrectangularshapecorners)
- [UnevenRoundedRectangle](/documentation/swiftui/unevenroundedrectangle)
- [RectangleCornerRadii](/documentation/swiftui/rectanglecornerradii)
- [RectangleCornerInsets](/documentation/swiftui/rectanglecornerinsets)
- [ConcentricRectangle](/documentation/swiftui/concentricrectangle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct RoundedRectangle
```

---
