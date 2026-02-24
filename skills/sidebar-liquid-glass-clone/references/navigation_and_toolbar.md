# Sidebar-Liquid-Glass-Clone - Navigation And Toolbar

**Pages:** 4

---

## Button

**URL:** https://sosumi.ai/documentation/swiftui/button?.md

**Contents:**
- Overview
  - Adding buttons to containers
  - Assigning a role
  - Styling buttons
- Conforms To
- Creating a button
- Creating a button with a role
- Creating a button from a configuration
- Creating a button to perform an App Intent
- Initializers

---
title: Button
description: A control that initiates an action.
source: https://developer.apple.com/documentation/swiftui/button
timestamp: 2026-02-13T01:05:38.996Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A control that initiates an action.

You create a button by providing an action and a label. The action is either a method or closure property that does something when a user clicks or taps the button. The label is a view that describes the button’s action — for example, by showing text, an icon, or both.

The label of a button can be any kind of view, such as a [Text](/documentation/swiftui/text) view for text-only labels:

Or a [Label](/documentation/swiftui/label) view, for buttons with both a title and an icon:

For those common cases, you can also use the convenience initializers that take a title string or [Localized String Key](/documentation/swiftui/localizedstringkey) as their first parameter, and optionally a system image name or `ImageResource` as their second parameter, instead of a trailing closure:

Prefer to use these convenience initializers, or a [Label](/documentation/swiftui/label) view, when providing both a title and an icon. This allows the button to dynamically adapt its appearance to render its title and icon correctly in containers such as toolbars and menus. For example, on iOS, buttons only display their icons by default when placed in toolbars, but show both a leading title and trailing icon in menus. Defining labels this way also helps with accessibility — for example, applying the [labelStyle(_:)](/documentation/swiftui/view/labelstyle(_:)) modifier with an [icon Only](/documentation/swiftui/labelstyle/icononly) style to the button will cause it to only visually display its icon, but still use its title to describe the button in accessibility modes like VoiceOver:

Avoid labels that only use images or exclusively visual components without an accessibility label.

How the user activates the button varies by platform:

- In iOS and watchOS, the user taps the button.
- In macOS, the user clicks the button.
- In tvOS, the user presses “select” on an external remote, like the Siri Remote, while focusing on the button.

The appearance of the button depends on factors like where you place it, whether you assign it a role, and how you style it.

Use buttons for any user interface element that initiates an action. Buttons automatically adapt their visual style to match the expected style within these different containers and contexts. For example, to create a [List](/documentation/swiftui/list) cell that initiates an action when selected by the user, add a button to the list’s content:

Similarly, to create a context menu item that initiates an action, add a button to the [contextMenu(_:)](/documentation/swiftui/view/contextmenu(_:)) modifier’s content closure:

This pattern extends to most other container views in SwiftUI that have customizable, interactive content, like [Form](/documentation/swiftui/form) instances.

You can optionally initialize a button with a [Button Role](/documentation/swiftui/buttonrole) that characterizes the button’s purpose. For example, you can create a [destructive](/documentation/swiftui/buttonrole/destructive) button for a deletion action:

The system uses the button’s role to style the button appropriately in every context. For example, a destructive button in a contextual menu appears with a red foreground color:

If you don’t specify a role for a button, the system applies an appropriate default appearance.

You can customize a button’s appearance using one of the standard button styles, like [bordered](/documentation/swiftui/primitivebuttonstyle/bordered), and apply the style with the [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:)) modifier:

If you apply the style to a container view, as in the example above, all the buttons in the container use the style:

You can also create custom styles. To add a custom appearance with standard interaction behavior, create a style that conforms to the [Button Style](/documentation/swiftui/buttonstyle) protocol. To customize both appearance and interaction behavior, create a style that conforms to the [Primitive Button Style](/documentation/swiftui/primitivebuttonstyle) protocol. Custom styles can also read the button’s role and use it to adjust the button’s appearance.

- [View](/documentation/swiftui/view)

- [init(action:label:)](/documentation/swiftui/button/init(action:label:)) Creates a button that displays a custom label.
- [init(_:action:)](/documentation/swiftui/button/init(_:action:)) Creates a button that generates its label from a localized string key.
- [init(_:image:action:)](/documentation/swiftui/button/init(_:image:action:)) Creates a button that generates its label from a localized string key and image resource.
- [init(_:systemImage:action:)](/documentation/swiftui/button/init(_:systemimage:action:)) Creates a button that generates its label from a localized string key and system image name.

- [init(role:action:label:)](/documentation/swiftui/button/init(role:action:label:)) Creates a button with a specified role that displays a custom label.
- [init(_:role:action:)](/documentation/swiftui/button/init(_:role:action:)) Creates a button with a specified role that generates its label from a localized string key.
- [init(_:image:role:action:)](/documentation/swiftui/button/init(_:image:role:action:)) Creates a button with a specified role that generates its label from a localized string key and an image resource.
- [init(_:systemImage:role:action:)](/documentation/swiftui/button/init(_:systemimage:role:action:)) Creates a button with a specified role that generates its label from a localized string key and a system image.

- [init(_:)](/documentation/swiftui/button/init(_:)) Creates a button based on a configuration for a style with a custom appearance and custom interaction behavior.

- [init(_:intent:)](/documentation/swiftui/button/init(_:intent:)) Creates a button that performs an  and generates its label from a localized string key.
- [init(intent:label:)](/documentation/swiftui/button/init(intent:label:)) Creates a button that performs an .
- [init(_:role:intent:)](/documentation/swiftui/button/init(_:role:intent:)) Creates a button with a specified role that performs an  and generates its label from a string.
- [init(role:intent:label:)](/documentation/swiftui/button/init(role:intent:label:)) Creates a button with a specified role that performs an .
- [init(_:image:role:intent:)](/documentation/swiftui/button/init(_:image:role:intent:)) Creates a button with a specified role that generates its label from a string and an image resource.
- [init(_:systemImage:role:intent:)](/documentation/swiftui/button/init(_:systemimage:role:intent:)) Creates a button with a specified role that generates its label from a string and a system image.

- [init(role:action:)](/documentation/swiftui/button/init(role:action:)) Creates a button that displays a default label.

- [buttonStyle(_:)](/documentation/swiftui/view/buttonstyle(_:))
- [buttonBorderShape(_:)](/documentation/swiftui/view/buttonbordershape(_:))
- [buttonRepeatBehavior(_:)](/documentation/swiftui/view/buttonrepeatbehavior(_:))
- [buttonRepeatBehavior](/documentation/swiftui/environmentvalues/buttonrepeatbehavior)
- [ButtonBorderShape](/documentation/swiftui/buttonbordershape)
- [ButtonRole](/documentation/swiftui/buttonrole)
- [ButtonRepeatBehavior](/documentation/swiftui/buttonrepeatbehavior)
- [ButtonSizing](/documentation/swiftui/buttonsizing)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Button<Label> where Label : View
```

Example 2 (swift):
```swift
Button(action: signIn) {
    Text("Sign In")
}
```

Example 3 (swift):
```swift
Button(action: signIn) {
    Label("Sign In", systemImage: "arrow.up")
}
```

Example 4 (swift):
```swift
Button("Sign In", systemImage: "arrow.up", action: signIn)
```

---

## scrollIndicators(_:axes:)

**URL:** https://sosumi.ai/documentation/swiftui/view/scrollindicators(_:axes:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Showing scroll indicators

---
title: scrollIndicators(_:axes:)
description: Sets the visibility of scroll indicators within this view.
source: https://developer.apple.com/documentation/swiftui/view/scrollindicators(_:axes:)
timestamp: 2026-02-13T01:06:01.467Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> Sets the visibility of scroll indicators within this view.

The visibility to apply to scrollable views.

The axes of scrollable views that the visibility applies to.

A view with the specified scroll indicator visibility.

Use this modifier to hide or show scroll indicators on scrollable content in views like a [Scroll View](/documentation/swiftui/scrollview), [List](/documentation/swiftui/list), or [Text Editor](/documentation/swiftui/texteditor). This modifier applies the preferred visibility to any scrollable content within a view hierarchy.

Use the [hidden](/documentation/swiftui/scrollindicatorvisibility/hidden) value to indicate that you prefer that views never show scroll indicators along a given axis. Use [visible](/documentation/swiftui/scrollindicatorvisibility/visible) when you prefer that views show scroll indicators. Depending on platform conventions, visible scroll indicators might only appear while scrolling. Pass [automatic](/documentation/swiftui/scrollindicatorvisibility/automatic) to allow views to decide whether or not to show their indicators.

- [scrollIndicatorsFlash(onAppear:)](/documentation/swiftui/view/scrollindicatorsflash(onappear:))
- [scrollIndicatorsFlash(trigger:)](/documentation/swiftui/view/scrollindicatorsflash(trigger:))
- [horizontalScrollIndicatorVisibility](/documentation/swiftui/environmentvalues/horizontalscrollindicatorvisibility)
- [verticalScrollIndicatorVisibility](/documentation/swiftui/environmentvalues/verticalscrollindicatorvisibility)
- [ScrollIndicatorVisibility](/documentation/swiftui/scrollindicatorvisibility)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func scrollIndicators(_ visibility: ScrollIndicatorVisibility, axes: Axis.Set = [.vertical, .horizontal]) -> some View
```

Example 2 (swift):
```swift
ScrollView {
    VStack(alignment: .leading) {
        ForEach(0..<100) {
            Text("Row \($0)")
        }
    }
}
.scrollIndicators(.hidden)
```

---

## toolbar(content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/toolbar(content:)-5w0tj?.md

**Contents:**
- Parameters
- Discussion

---
title: toolbar(content:)
description: Populates the toolbar or navigation bar with the specified items.
source: https://developer.apple.com/documentation/swiftui/view/toolbar(content:)-5w0tj
timestamp: 2026-02-13T01:05:54.013Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Populates the toolbar or navigation bar with the specified items.

The items representing the content of the toolbar.

Use this method to populate a toolbar with a collection of views that you provide to a toolbar view builder.

The toolbar modifier expects a collection of toolbar items which you can provide either by supplying a collection of views with each view wrapped in a [Toolbar Item](/documentation/swiftui/toolbaritem), or by providing a collection of views as a [Toolbar Item Group](/documentation/swiftui/toolbaritemgroup). The example below uses a collection of [Toolbar Item](/documentation/swiftui/toolbaritem) views to create a macOS toolbar that supports text editing features:

Although it’s not mandatory, wrapping a related group of toolbar items together in a [Toolbar Item Group](/documentation/swiftui/toolbaritemgroup) provides a one-to-one mapping between controls and toolbar items which results in the correct layout and spacing on each platform. For design guidance on toolbars, see [toolbars](/design/Human-Interface-Guidelines/toolbars) in the Human Interface Guidelines.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func toolbar<Content>(@ToolbarContentBuilder content: () -> Content) -> some View where Content : ToolbarContent
```

Example 2 (swift):
```swift
struct StructToolbarItemGroupView: View {
    @State private var text = ""
    @State private var bold = false
    @State private var italic = false
    @State private var fontSize = 12.0

    var displayFont: Font {
        let font = Font.system(size: CGFloat(fontSize),
                               weight: bold == true ? .bold : .regular)
        return italic == true ? font.italic() : font
    }

    var body: some View {
        TextEditor(text: $text)
            .font(displayFont)
            .toolbar {
                ToolbarItemGroup {
                    Slider(
                        value: $fontSize,
                        in: 8...120,
                        minimumValueLabel:
                            Text("A").font(.system(size: 8)),
                        maximumValueLabel:
                            Text("A").font(.system(size: 16))
                    ) {
                        Text("Font Size (\(Int(fontSize)))")
                    }
                    .frame(width: 150)
                    Toggle(isOn: $bold) {
                        Image(systemName: "bold")
                    }
                    Toggle(isOn: $italic) {
                        Image(systemName: "italic")
                    }
                }
            }
            .navigationTitle("My Note")
    }
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
timestamp: 2026-02-13T01:05:51.876Z
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
