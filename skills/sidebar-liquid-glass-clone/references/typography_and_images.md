# Sidebar-Liquid-Glass-Clone - Typography And Images

**Pages:** 4

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
timestamp: 2026-02-13T01:05:17.819Z
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

## Font

**URL:** https://sosumi.ai/documentation/swiftui/font?.md

**Contents:**
- Overview
- Conforms To
- Getting standard fonts
- Getting system fonts
- Creating custom fonts
- Getting a font from another font
- Styling a font
- Deprecated symbols
- Structures
- Instance Methods

---
title: Font
description: An environment-dependent font.
source: https://developer.apple.com/documentation/swiftui/font
timestamp: 2026-02-13T01:05:16.173Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> An environment-dependent font.

The system resolves a font’s value at the time it uses the font in a given environment because [Font](/documentation/swiftui/font) is a late-binding token.

- [Equatable](/documentation/Swift/Equatable)
- [Hashable](/documentation/Swift/Hashable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [extraLargeTitle2](/documentation/swiftui/font/extralargetitle2) Create a font with the second level extra large title text style.
- [extraLargeTitle](/documentation/swiftui/font/extralargetitle) Create a font with the extra large title text style.
- [largeTitle](/documentation/swiftui/font/largetitle) A font with the large title text style.
- [title](/documentation/swiftui/font/title) A font with the title text style.
- [title2](/documentation/swiftui/font/title2) Create a font for second level hierarchical headings.
- [title3](/documentation/swiftui/font/title3) Create a font for third level hierarchical headings.
- [headline](/documentation/swiftui/font/headline) A font with the headline text style.
- [subheadline](/documentation/swiftui/font/subheadline) A font with the subheadline text style.
- [body](/documentation/swiftui/font/body) A font with the body text style.
- [callout](/documentation/swiftui/font/callout) A font with the callout text style.
- [caption](/documentation/swiftui/font/caption) A font with the caption text style.
- [caption2](/documentation/swiftui/font/caption2) Create a font with the alternate caption text style.
- [footnote](/documentation/swiftui/font/footnote) A font with the footnote text style.

- [system(_:design:weight:)](/documentation/swiftui/font/system(_:design:weight:)) Gets a system font that uses the specified style, design, and weight.
- [system(size:weight:design:)](/documentation/swiftui/font/system(size:weight:design:)-697b2) Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.
- [Font.Design](/documentation/swiftui/font/design) A design to use for fonts.
- [Font.TextStyle](/documentation/swiftui/font/textstyle) A dynamic text style to use for fonts.
- [Font.Weight](/documentation/swiftui/font/weight) A weight to use for fonts.

- [custom(_:fixedSize:)](/documentation/swiftui/font/custom(_:fixedsize:)) Create a custom font with the given  and a fixed  that does not scale with Dynamic Type.
- [custom(_:size:relativeTo:)](/documentation/swiftui/font/custom(_:size:relativeto:)) Create a custom font with the given  and  that scales relative to the given .
- [custom(_:size:)](/documentation/swiftui/font/custom(_:size:)) Create a custom font with the given  and  that scales with the body text style.

- [init(_:)](/documentation/swiftui/font/init(_:)) Creates a custom font from a platform font instance.

- [bold()](/documentation/swiftui/font/bold()) Adds bold or emphasized styling to the font.
- [italic()](/documentation/swiftui/font/italic()) Adds italics to the font.
- [monospaced()](/documentation/swiftui/font/monospaced()) Returns a fixed-width font from the same family as the base font.
- [monospacedDigit()](/documentation/swiftui/font/monospaceddigit()) Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.
- [smallCaps()](/documentation/swiftui/font/smallcaps()) Adjusts the font to enable all small capitals.
- [lowercaseSmallCaps()](/documentation/swiftui/font/lowercasesmallcaps()) Adjusts the font to enable lowercase small capitals.
- [uppercaseSmallCaps()](/documentation/swiftui/font/uppercasesmallcaps()) Adjusts the font to enable uppercase small capitals.
- [weight(_:)](/documentation/swiftui/font/weight(_:)) Sets the weight of the font.
- [width(_:)](/documentation/swiftui/font/width(_:)) Sets the width of the font.
- [Font.Width](/documentation/swiftui/font/width) A width to use for fonts that have multiple widths.
- [leading(_:)](/documentation/swiftui/font/leading(_:)) Adjusts the line spacing of a font.
- [Font.Leading](/documentation/swiftui/font/leading) A line spacing adjustment that you can apply to a font.

- [system(_:design:)](/documentation/swiftui/font/system(_:design:)) Gets a system font with the given text style and design.
- [system(size:weight:design:)](/documentation/swiftui/font/system(size:weight:design:)-73a88) Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.

- [Font.Context](/documentation/swiftui/font/context) Information used to resolve a font.
- [Font.Resolved](/documentation/swiftui/font/resolved) A concrete font value.

- [bold(_:)](/documentation/swiftui/font/bold(_:)) Adds or removes bold or emphasized styling on the font.
- [italic(_:)](/documentation/swiftui/font/italic(_:)) Adds/removes italics on the font.
- [lowercaseSmallCaps(_:)](/documentation/swiftui/font/lowercasesmallcaps(_:)) Adjusts the font to enable/disable lowercase small capitals.
- [monospaced(_:)](/documentation/swiftui/font/monospaced(_:)) Returns a font adding or removing fixed-width design from the same family as the base font.
- [pointSize(_:)](/documentation/swiftui/font/pointsize(_:)) Sets the point size of the font explicitly.
- [resolve(in:)](/documentation/swiftui/font/resolve(in:)) Evaluates this font to a resolved font given the current context.
- [scaled(by:)](/documentation/swiftui/font/scaled(by:)) Scales the point size of the font.
- [smallCaps(_:)](/documentation/swiftui/font/smallcaps(_:)) Adjusts the font to enable/disable all small capitals.
- [uppercaseSmallCaps(_:)](/documentation/swiftui/font/uppercasesmallcaps(_:)) Adjusts the font to enable/disable uppercase small capitals.

- [default](/documentation/swiftui/font/default) The effective SwiftUI font used in any given environment.

- [system(size:weight:design:)](/documentation/swiftui/font/system(size:weight:design:)) Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.

- [Applying custom fonts to text](/documentation/swiftui/applying-custom-fonts-to-text)
- [font(_:)](/documentation/swiftui/view/font(_:))
- [fontDesign(_:)](/documentation/swiftui/view/fontdesign(_:))
- [fontWeight(_:)](/documentation/swiftui/view/fontweight(_:))
- [fontWidth(_:)](/documentation/swiftui/view/fontwidth(_:))
- [font](/documentation/swiftui/environmentvalues/font)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Font
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
timestamp: 2026-02-13T01:05:22.501Z
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
timestamp: 2026-02-13T01:05:41.231Z
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
