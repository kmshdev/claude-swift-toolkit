# Neuralforge-Main-Content - Buttons And Menus

**Pages:** 5

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
timestamp: 2026-02-13T03:43:08.842Z
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

## onTapGesture(count:perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/onTapGesture(count:perform:)?.md

**Contents:**
- Parameters
- Discussion
- Recognizing tap gestures

---
title: onTapGesture(count:perform:)
description: Adds an action to perform when this view recognizes a tap gesture.
source: https://developer.apple.com/documentation/swiftui/view/onTapGesture(count:perform:)
timestamp: 2026-02-13T03:43:41.835Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 16.0+, visionOS 1.0+, watchOS 6.0+

> Adds an action to perform when this view recognizes a tap gesture.

The number of taps or clicks required to trigger the action closure provided in `action`. Defaults to `1`.

The action to perform.

Use this method to perform the specified `action` when the user clicks or taps on the view or container `count` times.

> [!NOTE]
> If you create a control that’s functionally equivalent to a [Button](/documentation/swiftui/button), use [Button Style](/documentation/swiftui/buttonstyle) to create a customized button instead.

In the example below, the color of the heart images changes to a random color from the `colors` array whenever the user clicks or taps on the view twice:

- [onTapGesture(count:coordinateSpace:perform:)](/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:))
- [TapGesture](/documentation/swiftui/tapgesture)
- [SpatialTapGesture](/documentation/swiftui/spatialtapgesture)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onTapGesture(count: Int = 1, perform action: @escaping () -> Void) -> some View
```

Example 2 (swift):
```swift
struct TapGestureExample: View {
    let colors: [Color] = [.gray, .red, .orange, .yellow,
                           .green, .blue, .purple, .pink]
    @State private var fgColor: Color = .gray

    var body: some View {
        Image(systemName: "heart.fill")
            .resizable()
            .frame(width: 200, height: 200)
            .foregroundColor(fgColor)
            .onTapGesture(count: 2) {
                fgColor = colors.randomElement()!
            }
    }
}
```

---

## buttonStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/buttonstyle(_:)?.md

**Contents:**
- Discussion
- Creating buttons

---
title: buttonStyle(_:)
description: Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
source: https://developer.apple.com/documentation/swiftui/view/buttonstyle(_:)
timestamp: 2026-02-13T03:43:10.985Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.

Use this modifier to set a specific style for all button instances within a view:

You can also use this modifier to set the style for controls that acquire a button style through composition, like the [Menu](/documentation/swiftui/menu) and [Toggle](/documentation/swiftui/toggle) views in the following example:

The [menuStyle(_:)](/documentation/swiftui/view/menustyle(_:)) modifier causes the Terms and Conditions menu to render as a button. Similarly, the [toggleStyle(_:)](/documentation/swiftui/view/togglestyle(_:)) modifier causes the two toggles to render as buttons. The button style modifier then causes not only the explicit Sign In [Button](/documentation/swiftui/button), but also the menu and toggles with button styling, to render with the bordered button style.

- [Button](/documentation/swiftui/button)
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
nonisolated func buttonStyle<S>(_ style: S) -> some View where S : ButtonStyle
```

Example 2 (swift):
```swift
HStack {
    Button("Sign In", action: signIn)
    Button("Register", action: register)
}
.buttonStyle(.bordered)
```

Example 3 (swift):
```swift
VStack {
    Menu("Terms and Conditions") {
        Button("Open in Preview", action: openInPreview)
        Button("Save as PDF", action: saveAsPDF)
    }
    Toggle("Remember Password", isOn: $isToggleOn)
    Toggle("Flag", isOn: $flagged)
    Button("Sign In", action: signIn)
}
.menuStyle(.button)
.toggleStyle(.button)
.buttonStyle(.bordered)
```

---

## Menu

**URL:** https://sosumi.ai/documentation/swiftui/menu?.md

**Contents:**
- Overview
  - Primary action
  - Styling menus
- Conforms To
- Creating a menu from content
- Creating a menu with a primary action
- Creating a menu from a configuration
- Creating a menu

---
title: Menu
description: A control for presenting a menu of actions.
source: https://developer.apple.com/documentation/swiftui/menu
timestamp: 2026-02-13T03:43:12.373Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+, visionOS 1.0+

> A control for presenting a menu of actions.

The following example presents a menu of three buttons and a submenu, which contains three buttons of its own.

You can create the menu’s title with a [Localized String Key](/documentation/swiftui/localizedstringkey), as seen in the previous example, or with a view builder that creates multiple views, such as an image and a text view:

To support subtitles on menu items, initialize your `Button` with a view builder that creates multiple `Text` views where the first text represents the title and the second text represents the subtitle. The same approach applies to other controls such as `Toggle`:

> [!NOTE]
> This behavior does not apply to buttons outside of a menu’s content.

Menus can be created with a custom primary action. The primary action will be performed when the user taps or clicks on the body of the control, and the menu presentation will happen on a secondary gesture, such as on long press or on click of the menu indicator. The following example creates a menu that adds bookmarks, with advanced options that are presented in a menu.

Use the [menuStyle(_:)](/documentation/swiftui/view/menustyle(_:)) modifier to change the style of all menus in a view. The following example shows how to apply a custom style:

- [View](/documentation/swiftui/view)

- [init(_:content:)](/documentation/swiftui/menu/init(_:content:)) Creates a menu that generates its label from a localized string key.
- [init(content:label:)](/documentation/swiftui/menu/init(content:label:)) Creates a menu with a custom label.
- [init(_:image:content:)](/documentation/swiftui/menu/init(_:image:content:)) Creates a menu that generates its label from a localized string key and image resource.
- [init(_:systemImage:content:)](/documentation/swiftui/menu/init(_:systemimage:content:)) Creates a menu that generates its label from a localized string key and system image.

- [init(_:content:primaryAction:)](/documentation/swiftui/menu/init(_:content:primaryaction:)) Creates a menu with a custom primary action that generates its label from a localized string key.
- [init(content:label:primaryAction:)](/documentation/swiftui/menu/init(content:label:primaryaction:)) Creates a menu with a custom primary action and custom label.
- [init(_:image:content:primaryAction:)](/documentation/swiftui/menu/init(_:image:content:primaryaction:)) Creates a menu with a custom primary action that generates its label from a localized string key.
- [init(_:systemImage:content:primaryAction:)](/documentation/swiftui/menu/init(_:systemimage:content:primaryaction:)) Creates a menu with a custom primary action that generates its label from a localized string key and system image.

- [init(_:)](/documentation/swiftui/menu/init(_:)) Creates a menu based on a style configuration.

- [Populating SwiftUI menus with adaptive controls](/documentation/swiftui/populating-swiftui-menus-with-adaptive-controls)
- [menuStyle(_:)](/documentation/swiftui/view/menustyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Menu<Label, Content> where Label : View, Content : View
```

Example 2 (swift):
```swift
Menu("Actions") {
    Button("Duplicate", action: duplicate)
    Button("Rename", action: rename)
    Button("Delete…", action: delete)
    Menu("Copy") {
        Button("Copy", action: copy)
        Button("Copy Formatted", action: copyFormatted)
        Button("Copy Library Path", action: copyPath)
    }
}
```

Example 3 (swift):
```swift
Menu {
    Button("Open in Preview", action: openInPreview)
    Button("Save as PDF", action: saveAsPDF)
} label: {
    Label("PDF", systemImage: "doc.fill")
}
```

Example 4 (swift):
```swift
Menu {
    Button(action: openInPreview) {
        Text("Open in Preview")
        Text("View the document in Preview")
    }
    Button(action: saveAsPDF) {
        Text("Save as PDF")
        Text("Export the document as a PDF file")
    }
} label: {
    Label("PDF", systemImage: "doc.fill")
}
```

---

## onHover(perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/onhover(perform:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Responding to hover events

---
title: onHover(perform:)
description: Adds an action to perform when the user moves the pointer over or away from the view’s frame.
source: https://developer.apple.com/documentation/swiftui/view/onhover(perform:)
timestamp: 2026-02-13T03:43:38.712Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+

> Adds an action to perform when the user moves the pointer over or away from the view’s frame.

The action to perform whenever the pointer enters or exits this view’s frame. If the pointer is in the view’s frame, the `action` closure passes `true` as a parameter; otherwise, `false`.

A view that triggers `action` when the pointer enters or exits this view’s frame.

Calling this method defines a region for detecting pointer movement with the size and position of this view.

- [onContinuousHover(coordinateSpace:perform:)](/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:))
- [hoverEffect(_:isEnabled:)](/documentation/swiftui/view/hovereffect(_:isenabled:))
- [hoverEffectDisabled(_:)](/documentation/swiftui/view/hovereffectdisabled(_:))
- [defaultHoverEffect(_:)](/documentation/swiftui/view/defaulthovereffect(_:))
- [isHoverEffectEnabled](/documentation/swiftui/environmentvalues/ishovereffectenabled)
- [HoverPhase](/documentation/swiftui/hoverphase)
- [HoverEffectPhaseOverride](/documentation/swiftui/hovereffectphaseoverride)
- [OrnamentHoverContentEffect](/documentation/swiftui/ornamenthovercontenteffect)
- [OrnamentHoverEffect](/documentation/swiftui/ornamenthovereffect)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onHover(perform action: @escaping (Bool) -> Void) -> some View
```

---
