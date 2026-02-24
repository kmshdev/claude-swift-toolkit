# Neuralforge-Chat-Sidebar - Message Bubble

**Pages:** 16

---

## textFieldStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/textfieldstyle(_:)?.md

**Contents:**
- Getting text input

---
title: textFieldStyle(_:)
description: Sets the style for text fields within this view.
source: https://developer.apple.com/documentation/swiftui/view/textfieldstyle(_:)
timestamp: 2026-02-13T01:41:13.475Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the style for text fields within this view.

- [Building rich SwiftUI text experiences](/documentation/swiftui/building-rich-swiftui-text-experiences)
- [TextField](/documentation/swiftui/textfield)
- [SecureField](/documentation/swiftui/securefield)
- [TextEditor](/documentation/swiftui/texteditor)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func textFieldStyle<S>(_ style: S) -> some View where S : TextFieldStyle
```

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
timestamp: 2026-02-13T01:41:44.789Z
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

## background(_:in:fillStyle:)

**URL:** https://sosumi.ai/documentation/swiftui/view/background(_:in:fillstyle:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Layering views

---
title: background(_:in:fillStyle:)
description: Sets the view’s background to an insettable shape filled with a style.
source: https://developer.apple.com/documentation/swiftui/view/background(_:in:fillstyle:)
timestamp: 2026-02-13T01:41:38.828Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Sets the view’s background to an insettable shape filled with a style.

A [Shape Style](/documentation/swiftui/shapestyle) that SwiftUI uses to the fill the shape that you specify.

An instance of a type that conforms to [Insettable Shape](/documentation/swiftui/insettableshape) that SwiftUI draws behind the view.

The [Fill Style](/documentation/swiftui/fillstyle) to use when drawing the shape. The default style uses the nonzero winding number rule and antialiasing.

A view with the specified insettable shape drawn behind it.

Use this modifier to layer a type that conforms to the [Insettable Shape](/documentation/swiftui/insettableshape) protocol — like a [Rectangle](/documentation/swiftui/rectangle), [Circle](/documentation/swiftui/circle), or [Capsule](/documentation/swiftui/capsule) — behind a view. Specify the [Shape Style](/documentation/swiftui/shapestyle) that’s used to fill the shape. For example, you can place a [Rounded Rectangle](/documentation/swiftui/roundedrectangle) behind a [Label](/documentation/swiftui/label):

The [teal](/documentation/swiftui/shapestyle/teal) color fills the shape:

This modifier is a convenience method for placing a single shape behind a view. To create a background with other [View](/documentation/swiftui/view) types — or with a stack of views — use [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:)) instead. To add a [Shape Style](/documentation/swiftui/shapestyle) as a background, use [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:)).

- [Adding a background to your view](/documentation/swiftui/adding-a-background-to-your-view)
- [ZStack](/documentation/swiftui/zstack)
- [zIndex(_:)](/documentation/swiftui/view/zindex(_:))
- [background(alignment:content:)](/documentation/swiftui/view/background(alignment:content:))
- [background(_:ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(_:ignoressafeareaedges:))
- [background(ignoresSafeAreaEdges:)](/documentation/swiftui/view/background(ignoressafeareaedges:))
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
nonisolated func background<S, T>(_ style: S, in shape: T, fillStyle: FillStyle = FillStyle()) -> some View where S : ShapeStyle, T : InsettableShape
```

Example 2 (swift):
```swift
Label("Flag", systemImage: "flag.fill")
    .padding()
    .background(.teal, in: RoundedRectangle(cornerRadius: 8))
```

---

## TextField

**URL:** https://sosumi.ai/documentation/swiftui/textfield?.md

**Contents:**
- Overview
  - Text field prompts
  - Styling text fields
- Conforms To
- Creating a text field with a string
- Creating a scrollable text field
- Creating a text field with a value
- Deprecated initializers
- Initializers
- Getting text input

---
title: TextField
description: A control that displays an editable text interface.
source: https://developer.apple.com/documentation/swiftui/textfield
timestamp: 2026-02-13T01:41:09.922Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A control that displays an editable text interface.

You create a text field with a label and a binding to a value. If the value is a string, the text field updates this value continuously as the user types or otherwise edits the text in the field. For non-string types, it updates the value when the user commits their edits, such as by pressing the Return key.

The following example shows a text field to accept a username, and a [Text](/documentation/swiftui/text) view below it that shadows the continuously updated value of `username`. The [Text](/documentation/swiftui/text) view changes color as the user begins and ends editing. When the user submits their completed entry to the text field, the [onSubmit(of:_:)](/documentation/swiftui/view/onsubmit(of:_:)) modifier calls an internal `validate(name:)` method.

The bound value doesn’t have to be a string. By using a [Format Style](/documentation/Foundation/FormatStyle), you can bind the text field to a nonstring type, using the format style to convert the typed text into an instance of the bound type. The following example uses a [Format Style](/documentation/Foundation/PersonNameComponents/FormatStyle) to convert the name typed in the text field to a [Person Name Components](/documentation/Foundation/PersonNameComponents) instance. A [Text](/documentation/swiftui/text) view below the text field shows the debug description string of this instance.

You can set an explicit prompt on the text field to guide users on what text they should provide. Each text field style determines where and when the text field uses a prompt and label. For example, a form on macOS always places the label at the leading edge of the field and uses a prompt, when available, as placeholder text within the field itself. In the same context on iOS, the text field uses either the prompt or label as placeholder text, depending on whether the initializer provided a prompt.

The following example shows a [Form](/documentation/swiftui/form) with two text fields, each of which provides a prompt to indicate that the field is required, and a view builder to provide a label:

SwiftUI provides a default text field style that reflects an appearance and behavior appropriate to the platform. The default style also takes the current context into consideration, like whether the text field is in a container that presents text fields with a special style. Beyond this, you can customize the appearance and interaction of text fields using the [textFieldStyle(_:)](/documentation/swiftui/view/textfieldstyle(_:)) modifier, passing in an instance of [Text Field Style](/documentation/swiftui/textfieldstyle). The following example applies the [rounded Border](/documentation/swiftui/textfieldstyle/roundedborder) style to both text fields within a [VStack](/documentation/swiftui/vstack).

- [View](/documentation/swiftui/view)

- [init(_:text:)](/documentation/swiftui/textfield/init(_:text:)) Creates a text field with a text label generated from a localized title string.
- [init(_:text:prompt:)](/documentation/swiftui/textfield/init(_:text:prompt:)) Creates a text field with a text label generated from a localized title string.
- [init(text:prompt:label:)](/documentation/swiftui/textfield/init(text:prompt:label:)) Creates a text field with a prompt generated from a .

- [init(_:text:axis:)](/documentation/swiftui/textfield/init(_:text:axis:)) Creates a text field with a preferred axis and a text label generated from a localized title string.
- [init(_:text:prompt:axis:)](/documentation/swiftui/textfield/init(_:text:prompt:axis:)) Creates a text field with a preferred axis and a text label generated from a localized title string.
- [init(text:prompt:axis:label:)](/documentation/swiftui/textfield/init(text:prompt:axis:label:)) Creates a text field with a preferred axis and a prompt generated from a .

- [init(_:value:format:prompt:)](/documentation/swiftui/textfield/init(_:value:format:prompt:)) Creates a text field that applies a format style to a bound value, with a label generated from a localized title string.
- [init(value:format:prompt:label:)](/documentation/swiftui/textfield/init(value:format:prompt:label:)) Creates a text field that applies a format style to a bound value, with a label generated from a view builder.
- [init(_:value:formatter:)](/documentation/swiftui/textfield/init(_:value:formatter:)) Create an instance which binds over an arbitrary type, .
- [init(_:value:formatter:prompt:)](/documentation/swiftui/textfield/init(_:value:formatter:prompt:)) Creates a text field that applies a formatter to a bound value, with a label generated from a title string.
- [init(value:formatter:prompt:label:)](/documentation/swiftui/textfield/init(value:formatter:prompt:label:)) Creates a text field that applies a formatter to a bound optional value, with a label generated from a view builder.

- [Deprecated initializers](/documentation/swiftui/textfield-deprecated) Review deprecated text field initializers.

- [init(_:text:selection:prompt:axis:)](/documentation/swiftui/textfield/init(_:text:selection:prompt:axis:)) Creates a text field with a binding to the current selection and a text label generated from a localized title string.
- [init(text:selection:prompt:axis:label:)](/documentation/swiftui/textfield/init(text:selection:prompt:axis:label:)) Creates a text field with a binding to the current selection and a prompt generated from a .

- [Building rich SwiftUI text experiences](/documentation/swiftui/building-rich-swiftui-text-experiences)
- [textFieldStyle(_:)](/documentation/swiftui/view/textfieldstyle(_:))
- [SecureField](/documentation/swiftui/securefield)
- [TextEditor](/documentation/swiftui/texteditor)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct TextField<Label> where Label : View
```

Example 2 (swift):
```swift
@State private var username: String = ""
@FocusState private var emailFieldIsFocused: Bool = false

var body: some View {
    TextField(
        "User name (email address)",
        text: $username
    )
    .focused($emailFieldIsFocused)
    .onSubmit {
        validate(name: username)
    }
    .textInputAutocapitalization(.never)
    .disableAutocorrection(true)
    .border(.secondary)

    Text(username)
        .foregroundColor(emailFieldIsFocused ? .red : .blue)
}
```

Example 3 (swift):
```swift
@State private var nameComponents = PersonNameComponents()

var body: some View {
    TextField(
        "Proper name",
        value: $nameComponents,
        format: .name(style: .medium)
    )
    .onSubmit {
        validate(components: nameComponents)
    }
    .disableAutocorrection(true)
    .border(.secondary)
    Text(nameComponents.debugDescription)
}
```

Example 4 (swift):
```swift
Form {
    TextField(text: $username, prompt: Text("Required")) {
        Text("Username")
    }
    SecureField(text: $password, prompt: Text("Required")) {
        Text("Password")
    }
}
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
timestamp: 2026-02-13T01:41:07.848Z
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
timestamp: 2026-02-13T01:41:01.621Z
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
timestamp: 2026-02-13T01:40:59.672Z
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

## lineLimit(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/linelimit(_:)?.md

**Contents:**
- Parameters
- Discussion
- Limiting line count for multiline text

---
title: lineLimit(_:)
description: Sets to a closed range the number of lines that text can occupy in this view.
source: https://developer.apple.com/documentation/swiftui/view/linelimit(_:)
timestamp: 2026-02-13T01:41:05.680Z
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

## backgroundExtensionEffect()

**URL:** https://sosumi.ai/documentation/swiftui/view/backgroundextensioneffect()?.md

**Contents:**
- Discussion

---
title: backgroundExtensionEffect()
description: Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
source: https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect()
timestamp: 2026-02-13T01:42:52.932Z
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
timestamp: 2026-02-13T01:41:28.110Z
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
timestamp: 2026-02-13T01:41:32.353Z
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
timestamp: 2026-02-13T01:41:03.609Z
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

## TextEditor

**URL:** https://sosumi.ai/documentation/swiftui/texteditor?.md

**Contents:**
- Overview
- Conforms To
- Creating a text editor
- Initializers
- Getting text input

---
title: TextEditor
description: A view that can display and edit long-form text.
source: https://developer.apple.com/documentation/swiftui/texteditor
timestamp: 2026-02-13T01:41:11.561Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+

> A view that can display and edit long-form text.

A text editor view allows you to display and edit multiline, scrollable text in your app’s user interface. By default, the text editor view styles the text using characteristics inherited from the environment, like [font(_:)](/documentation/swiftui/view/font(_:)), [foregroundColor(_:)](/documentation/swiftui/view/foregroundcolor(_:)), and [multilineTextAlignment(_:)](/documentation/swiftui/view/multilinetextalignment(_:)).

You create a text editor by adding a `TextEditor` instance to the body of your view, and initialize it by passing in a [Binding](/documentation/swiftui/binding) to a string variable in your app:

To style the text, use the standard view modifiers to configure a system font, set a custom font, or change the color of the view’s text.

In this example, the view renders the editor’s text in gray with a custom font:

If you want to change the spacing or font scaling aspects of the text, you can use modifiers like [lineLimit(_:)](/documentation/swiftui/view/linelimit(_:)), [lineSpacing(_:)](/documentation/swiftui/view/linespacing(_:)), and [minimumScaleFactor(_:)](/documentation/swiftui/view/minimumscalefactor(_:)) to configure how the view displays text depending on the space constraints. For example, here the [lineSpacing(_:)](/documentation/swiftui/view/linespacing(_:)) modifier sets the spacing between lines to 5 points:

- [View](/documentation/swiftui/view)

- [init(text:)](/documentation/swiftui/texteditor/init(text:)) Creates a plain text editor.

- [init(text:selection:)](/documentation/swiftui/texteditor/init(text:selection:)) Creates a styled text editor.

- [Building rich SwiftUI text experiences](/documentation/swiftui/building-rich-swiftui-text-experiences)
- [TextField](/documentation/swiftui/textfield)
- [textFieldStyle(_:)](/documentation/swiftui/view/textfieldstyle(_:))
- [SecureField](/documentation/swiftui/securefield)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct TextEditor
```

Example 2 (swift):
```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
    }
}
```

Example 3 (swift):
```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
            .foregroundColor(Color.gray)
            .font(.custom("HelveticaNeue", size: 13))
    }
}
```

Example 4 (swift):
```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
            .foregroundColor(Color.gray)
            .font(.custom("HelveticaNeue", size: 13))
            .lineSpacing(5)
    }
}
```

---

## padding(_:_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/padding(_:_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Adding padding around a view

---
title: padding(_:_:)
description: Adds an equal padding amount to specific edges of this view.
source: https://developer.apple.com/documentation/swiftui/view/padding(_:_:)
timestamp: 2026-02-13T01:41:36.685Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds an equal padding amount to specific edges of this view.

The set of edges to pad for this view. The default is [all](/documentation/swiftui/edge/set/all).

An amount, given in points, to pad this view on the specified edges. If you set the value to `nil`, SwiftUI uses a platform-specific default amount. The default value of this parameter is `nil`.

A view that’s padded by the specified amount on the specified edges.

Use this modifier to add a specified amount of padding to one or more edges of the view. Indicate the edges to pad by naming either a single value from [Set](/documentation/swiftui/edge/set), or by specifying an [Option Set](/documentation/Swift/OptionSet) that contains edge values:

The order in which you apply modifiers matters. The example above applies the padding before applying the border to ensure that the border encompasses the padded region:

You can omit either or both of the parameters. If you omit the `length`, SwiftUI uses a default amount of padding. If you omit the `edges`, SwiftUI applies the padding to all edges. Omit both to add a default padding all the way around a view. SwiftUI chooses a default amount of padding that’s appropriate for the platform and the presentation context.

The example above looks like this in iOS under typical conditions:

To control the amount of padding independently for each edge, use [padding(_:)](/documentation/swiftui/view/padding(_:)-6pgqq). To pad all outside edges of a view by a specified amount, use [padding(_:)](/documentation/swiftui/view/padding(_:)-68shk).

- [padding(_:)](/documentation/swiftui/view/padding(_:))
- [padding3D(_:)](/documentation/swiftui/view/padding3d(_:))
- [padding3D(_:_:)](/documentation/swiftui/view/padding3d(_:_:))
- [scenePadding(_:)](/documentation/swiftui/view/scenepadding(_:))
- [scenePadding(_:edges:)](/documentation/swiftui/view/scenepadding(_:edges:))
- [ScenePadding](/documentation/swiftui/scenepadding)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func padding(_ edges: Edge.Set = .all, _ length: CGFloat? = nil) -> some View
```

Example 2 (swift):
```swift
VStack {
    Text("Text padded by 20 points on the bottom and trailing edges.")
        .padding([.bottom, .trailing], 20)
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
```

Example 3 (swift):
```swift
VStack {
    Text("Text with default padding.")
        .padding()
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
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
timestamp: 2026-02-13T01:41:55.255Z
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
timestamp: 2026-02-13T01:41:34.364Z
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
