# Text Editing APIs
APIs for rich text editing, attributed string support, text selection, formatting definitions, and find contexts.

## Table of Contents

- [TextEditor](#texteditor)
- [AttributedTextSelection](#attributedtextselection)
- [AttributedTextFormattingDefinition](#attributedtextformattingdefinition)
- [AttributedString](#attributedstring)

## TextEditor

**URL:** https://sosumi.ai/documentation/SwiftUI/TextEditor?.md

**Contents:**
- Overview
- Conforms To
- Creating a text editor
- Initializers
- Getting text input

**Navigation:** [SwiftUI](/documentation/SwiftUI)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+

A text editor view allows displaying and editing multiline, scrollable text in the app's user interface. By default, the text editor view styles the text using characteristics inherited from the environment, like [font(*:)](/documentation/swiftui/view/font(*:)), [foregroundColor(*:)](/documentation/swiftui/view/foregroundcolor(*:)), and [multilineTextAlignment(*:)](/documentation/swiftui/view/multilinetextalignment(*:)).

Create a text editor by adding a `TextEditor` instance to the body of the view, and initialize it by passing in a [Binding](/documentation/swiftui/binding) to a string variable in the app:

To style the text, use the standard view modifiers to configure a system font, set a custom font, or change the color of the view's text.

In this example, the view renders the editor's text in gray with a custom font:

To change the spacing or font scaling aspects of the text, use modifiers like [lineLimit(*:)](/documentation/swiftui/view/linelimit(*:)), [lineSpacing(*:)](/documentation/swiftui/view/linespacing(*:)), and [minimumScaleFactor(*:)](/documentation/swiftui/view/minimumscalefactor(*:)) to configure how the view displays text depending on the space constraints. For example, here the [lineSpacing(*:)](/documentation/swiftui/view/linespacing(*:)) modifier sets the spacing between lines to 5 points:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

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

## AttributedTextSelection

**URL:** https://sosumi.ai/documentation/SwiftUI/AttributedTextSelection?.md

**Contents:**
- Overview
- Conforms To
- Structures
- Initializers
- Instance Methods
- Enumerations
- Selecting text

**Navigation:** [SwiftUI](/documentation/SwiftUI)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+

A selection is either an insertion point (e.g. a cursor in the text), or spans over a range of characters. While that range is always visually contiguous, it may not be logically contiguous in the text storage. Specifically, a single selection value cannot represent multiple cursors.

This is frequently used to represent selection of text in a `TextEditor`. The following example shows a text editor that leverages text selection to offer live suggestions based on the current selection.

The [textSelectionAffinity(*:)](/documentation/swiftui/view/textselectionaffinity(*:)) modifier can also be used to specify a selection affinity on the given hierarchy:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct AttributedTextSelection
```

Example 2 (swift):
```swift
struct SuggestionTextEditor: View {
    @State var text: AttributedString = ""
    @State var selection = AttributedTextSelection()

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(substrings: getSubstrings(
                text: text, indices: selection.indices(in: text))
        }
    }

    private func getSubstrings(
        text: String, indices: AttributedTextSelection.Indices
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

Example 3 (swift):
```swift
struct SuggestionTextEditor: View {
    @State var text: AttributedString = ""
    @State var selection = AttributedTextSelection()

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(substrings: getSubstrings(
                text: text, indices: selection.indices(in: text))
        }
        .textSelectionAffinity(.upstream)
    }

    private func getSubstrings(
        text: String, indices: AttributedTextSelection.Indices
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

---

## AttributedTextFormattingDefinition

**URL:** https://sosumi.ai/documentation/SwiftUI/AttributedTextFormattingDefinition?.md

**Contents:**
- Overview
- Inherited By
- Conforming Types
- Associated Types
- Instance Properties
- Instance Methods
- Type Aliases
- Controlling text style

**Navigation:** [SwiftUI](/documentation/SwiftUI)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+

A formatting definition consists of an attribute scope and a number of value constraints. It is applied to a view hierarchy using the [attributedTextFormattingDefinition(*:)](/documentation/swiftui/view/attributedtextformattingdefinition(*:)-81jn6) view modifier and affects nested [Text](/documentation/swiftui/text) and [Text Editor](/documentation/swiftui/texteditor) views when initialized with [Attributed String](/documentation/Foundation/AttributedString).

Create a formatting definition by first choosing an attribute scope that contains all attributes relevant for the view. All other attributes will be ignored by value constraints and by the affected views.

Use the `Foundation/AttributeScopes/SwiftUIAttributes` for the default set of attributes supported by SwiftUI. It is possible to create a custom scope listing only a subset of the attributes in SwiftUI's attribute scope, and to include custom attributes in the scope. This allows taking advantage of advanced attributed string features, such as [run Boundaries](/documentation/Foundation/AttributedStringKey/runBoundaries).

Custom attributes also allow separating semantic information stored on the text, e.g. the information that a sequence of characters refers to a specific person in contacts, from how this part of the text is to be formatted, e.g. with the foreground color "purple". The rules defining what values attributes can have, are called [Attributed Text Value Constraint](/documentation/swiftui/attributedtextvalueconstraint)s.

While associating formatting with custom semantic attributes is one important use case, value constraints are a generic mechanism for constraining the formatting that is available in a text editor - with or without dependencies on other attributes. For example, a value constraint could also be used to only allow a single, solid underline, but not a double underline or a dashed underline.

SwiftUI validates formatting UI provided by the system to the user to make sure only controls that are compatible with the formatting definition and its constraints are visible and enabled. If the system formatting UI does not provide sufficient utility based on the formatting definition, or custom UI is provided that is better tailored to the text editing experience, consider hiding the system-provided UI using the [textInputFormattingControlVisibility(*:for:)](/documentation/swiftui/view/textinputformattingcontrolvisibility(*:for:)) view modifier.

To declare the attributed text formatting definition, specify the attribute scope in the generic of the [body](/documentation/swiftui/attributedtextformattingdefinition/body-1b01t)'s type, and list all value constraints inside the [body](/documentation/swiftui/attributedtextformattingdefinition/body-1b01t) using result builder syntax:

Use the [attributedTextFormattingDefinition(*:)](/documentation/swiftui/view/attributedtextformattingdefinition(*:)-81jn6) view modifier to apply the definition to a view.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol AttributedTextFormattingDefinition<Scope>
```

Example 2 (swift):
```swift
struct ContactsArePurple: AttributedTextValueConstraint {
    typealias Scope = MyScope
    typealias AttributeKey = Scope.ForegroundColorAttribute

    func constrain(_ container: inout Attributes) {
        if container.annotation == .contact {
            container.foregroundColor = .purple
        } else {
            container.foregroundColor = nil
        }
    }
}
```

Example 3 (swift):
```swift
struct MyTextFormattingDefinition: AttributedTextFormattingDefinition {
    var body: some AttributedTextFormattingDefinition<
        AttributeScopes.SwiftUIAttributes
    > {
        ValueConstraint(
            for: \.underlineStyle,
            values: [nil, .single],
            default: .single)
        MyAttributedTextValueConstraint()
        ContactsArePurple()
    }
}
```

---

## AttributedString

**URL:** https://sosumi.ai/documentation/Foundation/AttributedString?.md

**Contents:**
- Overview
  - String Attributes
  - Creating Attributed Strings with Markdown
  - Attribute Scopes
- Conforms To
- Creating an Attributed String
- Creating a Localized Attributed String
- Creating a Localized Attributed String with a Default Value
- Creating an Attributed String from Markdown
- Creating an Attributed String from a Reference Type

**Navigation:** [Foundation](/documentation/Foundation)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

Attributed strings are character strings that have attributes for individual characters or ranges of characters. Attributes provide traits like visual styles for display, accessibility for guided access, and hyperlink data for linking between data sources. Attribute keys provide the name and value type of each attribute. System frameworks like Foundation and SwiftUI define common keys, and custom keys can be defined in custom extensions.

An attribute can be applied to an entire string, or to a range within the string. The string represents each range with consistent attributes as a *run*.

[Attributed String](/documentation/foundation/attributedstring) uses subscripts and dynamic member lookup to simplify working with attributes from call points. In its most verbose form, set an attribute by creating an [Attribute Container](/documentation/foundation/attributecontainer) and merging it into an existing attributed string, like this:

Using the attributed string's [subscript(*:)](/documentation/foundation/attributedstringprotocol/subscript(*:)-4thnp) method, it is possible to omit the explicit use of an [Attribute Container](/documentation/foundation/attributecontainer) and set the attribute directly by its type:

Because an [Attributed String](/documentation/foundation/attributedstring) supports dynamic member lookup — as described under [Attributes.html](https://docs.swift.org/swift-book/ReferenceManual/Attributes.html) in [](https://docs.swift.org/swift-book/) — its subscripts are accessible with dot syntax instead. When combined with properties like [foreground Color](/documentation/foundation/attributescopes/appkitattributes/foregroundcolor) that return the attribute key type, this final form offers a natural way to set an attribute that applies to an entire string:

This example works because AppKit defines an [Attribute Scope](/documentation/foundation/attributescope), [App Kit Attributes](/documentation/foundation/attributescopes/appkitattributes), in which the property [foreground Color](/documentation/foundation/attributescopes/appkitattributes/foregroundcolor) returns the type `AttributeScopes.AppKitAttributes.ForegroundColorAttribute`. Because AppKit's attribute scope implements [Attribute Dynamic Lookup](/documentation/foundation/attributedynamiclookup), the dot syntax resolves to an equivalent subscript expression, allowing `attributedString.foregroundColor` to replace `attributedString[AttributeScopes.AppKitAttributes.ForegroundColorAttribute.self]`.

An attribute can also be set to apply only to part of an attributed string, by applying the attribute to a range, as seen here:

Portions of the string with unique combinations of attributes are accessible by iterating over the string's `runs` property.

Define custom attributes by creating types that conform to [Attributed String Key](/documentation/foundation/attributedstringkey), and collecting them in an [Attribute Scope](/documentation/foundation/attributescope). Custom keys should also extend [Attribute Dynamic Lookup](/documentation/foundation/attributedynamiclookup), so callers can use dot-syntax to access the attribute.

Create an attributed string by passing a standard [String](/documentation/Swift/String) or [Data](/documentation/foundation/data) instance that contains Markdown to initializers like [init(markdown:options:baseURL:)](/documentation/foundation/attributedstring/init(markdown:options:baseurl:)-52n3u). The attributed string creates attributes by parsing the markup in the string.

Localized strings loaded from strings files with initializers like [init(localized:options:table:bundle:locale:comment:)](/documentation/foundation/attributedstring/init(localized:options:table:bundle:locale:comment:)-8dlnl) can also contain Markdown to add styling. In addition, these localized attributed string initializers can apply the [replacement Index](/documentation/foundation/attributescopes/foundationattributes/replacementindex) attribute, which allows determining the range of replacement strings, whose order may vary between languages.

By declaring new attributes that conform to [Markdown Decodable Attributed String Key](/documentation/foundation/markdowndecodableattributedstringkey), it is possible to add attributes invoked using Apple's Markdown extension syntax: `^[text](name:value, name:value, …)`. See the sample code project doc:building-a-localized-food-ordering-app for an example of creating custom attributes and using them with Markdown.

Localized attributed strings can also use the extension syntax to indicate parts of the string where the system can apply automatic grammar agreement. See the initializers that take a `localized:` parameter for examples of this extension syntax, as used with automatic grammar agreement.

The [Attributed String](/documentation/foundation/attributedstring) API defines keys for common uses, such as text styling, semantically marking up formattable types like dates and numbers, and hyperlinking. These are available in the [Attribute Scopes](/documentation/foundation/attributescopes) enumeration, which contains attributes for AppKit, Foundation, SwiftUI, and UIKit.

Define custom attributes by implementing [Attributed String Key](/documentation/foundation/attributedstringkey), and reference them by name by collecting them in an [Attribute Scope](/documentation/foundation/attributescope).

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@dynamicMemberLookup struct AttributedString
```

Example 2 (swift):
```swift
var attributedString = AttributedString("This is a string with empty attributes.")
var container = AttributeContainer()
container[AttributeScopes.AppKitAttributes.ForegroundColorAttribute.self] = .red
attributedString.mergeAttributes(container, mergePolicy: .keepNew)
```

Example 3 (swift):
```swift
attributedString[AttributeScopes.AppKitAttributes.ForegroundColorAttribute.self] = .yellow
```

Example 4 (swift):
```swift
attributedString.foregroundColor = .green
```

---

## Reading Paths

**Path B — Rich Text Editor (this file is step 1):**
Next → `find-context.md` (adding find/replace)

**Anti-Pattern:** `TextEditor(text: $attributed, selection: $sel)` with a `String` binding causes a compile error — selection tracking requires `AttributedString` binding. Use `@State var text: AttributedString`, not `String`.
