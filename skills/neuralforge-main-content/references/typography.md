# Neuralforge-Main-Content - Typography

**Pages:** 10

---

## lineLimit(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/lineLimit(_:)?.md

**Contents:**
- Parameters
- Discussion
- Limiting line count for multiline text

---
title: lineLimit(_:)
description: Sets to a closed range the number of lines that text can occupy in this view.
source: https://developer.apple.com/documentation/swiftui/view/lineLimit(_:)
timestamp: 2026-02-13T03:42:56.169Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> Sets to a closed range the number of lines that text can occupy in this view.

Use this modifier to specify a closed range of lines that a [Text](/documentation/swiftui/text) view or a vertical [Text Field](/documentation/swiftui/textfield) can occupy. When the text of such views occupies more space than the provided limit, a [Text](/documentation/swiftui/text) view truncates its content while a [Text Field](/documentation/swiftui/textfield) becomes scrollable.

- [lineLimit(_:reservesSpace:)](/documentation/swiftui/view/linelimit(_:reservesspace:))
- [lineLimit](/documentation/swiftui/environmentvalues/linelimit)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func lineLimit(_ limit: ClosedRange<Int>) -> some View
```

Example 2 (swift):
```swift
Form {
    TextField("Title", text: $model.title)
    TextField("Notes", text: $model.notes, axis: .vertical)
        .lineLimit(1...3)
}
```

---

## multilineTextAlignment(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/multilineTextAlignment(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Formatting multiline text

---
title: multilineTextAlignment(_:)
description: Sets the alignment of a text view that contains multiple lines of text.
source: https://developer.apple.com/documentation/swiftui/view/multilineTextAlignment(_:)
timestamp: 2026-02-13T03:42:58.310Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the alignment of a text view that contains multiple lines of text.

A value that you use to align multiple lines of text within a view.

A view that aligns the lines of multiline [Text](/documentation/swiftui/text) instances it contains.

Use this modifier to set an alignment for a multiline block of text. For example, the modifier centers the contents of the following [Text](/documentation/swiftui/text) view:

The text in the above example spans more than one line because:

- The newline character introduces a line break.
- The frame modifier limits the space available to the text view, and by default a text view wraps lines that don’t fit in the available width. As a result, the text before the explicit line break wraps to three lines, and the text after uses two lines.

The modifier applies the alignment to the all the lines of text in the view, regardless of why wrapping occurs:

The modifier has no effect on a [Text](/documentation/swiftui/text) view that contains only one line of text, because a text view has a width that exactly matches the width of its widest line. If you want to align an entire text view rather than its contents, set the aligment of its container, like a [VStack](/documentation/swiftui/vstack) or a frame that you create with the [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:)) modifier.

> [!NOTE]
> You can use this modifier to control the alignment of a [Text](/documentation/swiftui/text) view that you create with the [init(_:style:)](/documentation/swiftui/text/init(_:style:)) initializer to display localized dates and times, including when the view uses only a single line, but only when that view appears in a widget.

The modifier also affects the content alignment of other text container types, like [Text Editor](/documentation/swiftui/texteditor) and [Text Field](/documentation/swiftui/textfield). In those cases, the modifier sets the alignment even when the view contains only a single line because view’s width isn’t dictated by the width of the text it contains.

The modifier operates by setting the [multiline Text Alignment](/documentation/swiftui/environmentvalues/multilinetextalignment) value in the environment, so it affects all the text containers in the modified view hierarchy. For example, you can apply the modifier to a [VStack](/documentation/swiftui/vstack) to configure all the text views inside the stack.

- [lineSpacing(_:)](/documentation/swiftui/view/linespacing(_:))
- [lineSpacing](/documentation/swiftui/environmentvalues/linespacing)
- [multilineTextAlignment](/documentation/swiftui/environmentvalues/multilinetextalignment)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func multilineTextAlignment(_ alignment: TextAlignment) -> some View
```

Example 2 (swift):
```swift
Text("This is a block of text that shows up in a text element as multiple lines.\("\n") Here we have chosen to center this text.")
    .frame(width: 200)
    .multilineTextAlignment(.center)
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
timestamp: 2026-02-13T03:44:13.672Z
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

## textSelection(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/textselection(_:)?.md

**Contents:**
- Discussion
- Selecting text

---
title: textSelection(_:)
description: Controls whether people can select text within this view.
source: https://developer.apple.com/documentation/swiftui/view/textselection(_:)
timestamp: 2026-02-13T03:43:00.298Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+

> Controls whether people can select text within this view.

People sometimes need to copy useful information from [Text](/documentation/swiftui/text) views — including error messages, serial numbers, or IP addresses — so they can then paste the text into another context. Enable text selection to let people select text in a platform-appropriate way.

You can apply this method to an individual text view, or to a container to make each contained text view selectable. In the following example, the person using the app can select text that shows the date of an event or the name or email of any of the event participants:

On macOS, people use the mouse or trackpad to select a range of text, which they can quickly copy by choosing Edit > Copy, or with the standard keyboard shortcut.

On iOS, the person using the app touches and holds on a selectable `Text` view, which brings up a system menu with menu items appropriate for the current context. These menu items operate on the entire contents of the `Text` view; the person can’t select a range of text like they can on macOS.

> [!NOTE]
> [Button](/documentation/swiftui/button) views don’t support text selection.

- [TextSelectability](/documentation/swiftui/textselectability)
- [TextSelection](/documentation/swiftui/textselection)
- [textSelectionAffinity(_:)](/documentation/swiftui/view/textselectionaffinity(_:))
- [textSelectionAffinity](/documentation/swiftui/environmentvalues/textselectionaffinity)
- [TextSelectionAffinity](/documentation/swiftui/textselectionaffinity)
- [AttributedTextSelection](/documentation/swiftui/attributedtextselection)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func textSelection<S>(_ selectability: S) -> some View where S : TextSelectability
```

Example 2 (swift):
```swift
var body: some View {
    VStack {
        Text("Event Invite")
            .font(.title)
        Text(invite.date.formatted(date: .long, time: .shortened))
            .textSelection(.enabled)

        List(invite.recipients) { recipient in
            VStack (alignment: .leading) {
                Text(recipient.name)
                Text(recipient.email)
                    .foregroundStyle(.secondary)
            }
        }
        .textSelection(.enabled)
    }
    .navigationTitle("New Invitation")
}
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
timestamp: 2026-02-13T03:42:51.834Z
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
timestamp: 2026-02-13T03:42:49.920Z
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
timestamp: 2026-02-13T03:43:52.154Z
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
timestamp: 2026-02-13T03:42:53.926Z
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

## navigationTitle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/navigationtitle(_:)?.md

**Contents:**
- Parameters
- Discussion
- Setting titles for navigation content

---
title: navigationTitle(_:)
description: Configures the view’s title for purposes of navigation, using a string binding.
source: https://developer.apple.com/documentation/swiftui/view/navigationtitle(_:)
timestamp: 2026-02-13T03:44:20.095Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> Configures the view’s title for purposes of navigation, using a string binding.

The text of the title.

In iOS, iPadOS, and macOS, this allows editing the navigation title when the title is displayed in the toolbar.

Refer to the [Configure-Your-Apps-Navigation](/documentation/swiftui/configure-your-apps-navigation-titles) article for more information on navigation title modifiers.

- [navigationSubtitle(_:)](/documentation/swiftui/view/navigationsubtitle(_:))
- [navigationDocument(_:)](/documentation/swiftui/view/navigationdocument(_:))
- [navigationDocument(_:preview:)](/documentation/swiftui/view/navigationdocument(_:preview:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func navigationTitle(_ title: Binding<String>) -> some View
```

---

## contextMenu(menuItems:)

**URL:** https://sosumi.ai/documentation/swiftui/view/contextmenu(menuitems:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Creating context menus

---
title: contextMenu(menuItems:)
description: Adds a context menu to a view.
source: https://developer.apple.com/documentation/swiftui/view/contextmenu(menuitems:)
timestamp: 2026-02-13T03:43:36.528Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+, watchOS 6.0+

> Adds a context menu to a view.

A closure that produces the menu’s contents. You can deactivate the context menu by returning nothing from the closure.

A view that can display a context menu.

Use this modifier to add a context menu to a view in your app’s user interface. Compose the menu by returning controls like [Button](/documentation/swiftui/button), [Toggle](/documentation/swiftui/toggle), and [Picker](/documentation/swiftui/picker) from the `menuItems` closure. You can also use [Menu](/documentation/swiftui/menu) to define submenus or [Section](/documentation/swiftui/section) to group items.

The following example creates a [Text](/documentation/swiftui/text) view that has a context menu with two buttons:

When someone activates the context menu with an action like touch and hold in iOS or iPadOS, the system displays the menu next to the content:

The system dismisses the menu if someone makes a selection, or taps or clicks outside the menu.

To customize the default preview, apply a [contentShape(_:_:eoFill:)](/documentation/swiftui/view/contentshape(_:_:eofill:)) with a [context Menu Preview](/documentation/swiftui/contentshapekinds/contextmenupreview) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

> [!NOTE]
> This view modifier produces a context menu on macOS, but that platform doesn’t display a preview.

If you want to show a different preview, you can use [contextMenu(menuItems:preview:)](/documentation/swiftui/view/contextmenu(menuitems:preview:)). To add a context menu to a container that supports selection, like a [List](/documentation/swiftui/list) or a [Table](/documentation/swiftui/table), and to distinguish between menu activation on a selection and activation in an empty area of the container, use [contextMenu(forSelectionType:menu:primaryAction:)](/documentation/swiftui/view/contextmenu(forselectiontype:menu:primaryaction:)).

- [contextMenu(menuItems:preview:)](/documentation/swiftui/view/contextmenu(menuitems:preview:))
- [contextMenu(forSelectionType:menu:primaryAction:)](/documentation/swiftui/view/contextmenu(forselectiontype:menu:primaryaction:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func contextMenu<MenuItems>(@ViewBuilder menuItems: () -> MenuItems) -> some View where MenuItems : View
```

Example 2 (swift):
```swift
Text("Turtle Rock")
    .padding()
    .contextMenu {
        Button {
            // Add this item to a list of favorites.
        } label: {
            Label("Add to Favorites", systemImage: "heart")
        }
        Button {
            // Open Maps and center it on this item.
        } label: {
            Label("Show in Maps", systemImage: "mappin")
        }
    }
```

---
