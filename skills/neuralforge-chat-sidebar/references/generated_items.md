# Neuralforge-Chat-Sidebar - Generated Items

**Pages:** 7

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
timestamp: 2026-02-13T01:41:47.042Z
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

## badge(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/badge(_:)?.md

**Contents:**
- Parameters
- Discussion
- Displaying a badge on a list item

---
title: badge(_:)
description: Generates a badge for the view from an integer value.
source: https://developer.apple.com/documentation/swiftui/view/badge(_:)
timestamp: 2026-02-13T01:42:31.050Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+

> Generates a badge for the view from an integer value.

An integer value to display in the badge. Set the value to zero to hide the badge.

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

The following example shows a [List](/documentation/swiftui/list) with the value of `recentItems.count` represented by a badge on one of the rows:

- [badgeProminence(_:)](/documentation/swiftui/view/badgeprominence(_:))
- [badgeProminence](/documentation/swiftui/environmentvalues/badgeprominence)
- [BadgeProminence](/documentation/swiftui/badgeprominence)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func badge(_ count: Int) -> some View
```

Example 2 (swift):
```swift
List {
    Text("Recents")
        .badge(recentItems.count)
    Text("Favorites")
}
```

---

## tint(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/tint(_:)?.md

**Contents:**
- Parameters
- Discussion
- Setting a color

---
title: tint(_:)
description: Sets the tint color within this view.
source: https://developer.apple.com/documentation/swiftui/view/tint(_:)
timestamp: 2026-02-13T01:42:33.050Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Sets the tint color within this view.

The tint [Color](/documentation/swiftui/color) to apply.

Use this method to override the default accent color for this view. Unlike an app’s accent color, which can be overridden by user preference, the tint color is always respected and should be used as a way to provide additional meaning to the control.

This example shows Answer and Decline buttons with [green](/documentation/swiftui/shapestyle/green) and [red](/documentation/swiftui/shapestyle/red) tint colors, respectively.

Some controls adapt to the tint color differently based on their style, the current platform, and the surrounding context. For example, in macOS, a button with the [bordered](/documentation/swiftui/primitivebuttonstyle/bordered) style doesn’t tint its background, but one with the [bordered Prominent](/documentation/swiftui/primitivebuttonstyle/borderedprominent) style does. In macOS, neither of these button styles tint their label, but they do in other platforms.

- [Color](/documentation/swiftui/color)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func tint(_ tint: Color?) -> some View
```

Example 2 (swift):
```swift
struct ControlTint: View {
    var body: some View {
        HStack {
            Button {
                // Answer the call
            } label: {
                Label("Answer", systemImage: "phone")
            }
            .tint(.green)
            Button {
                // Decline the call
            } label: {
                Label("Decline", systemImage: "phone.down")
            }
            .tint(.red)
        }
        .buttonStyle(.borderedProminent)
        .padding()
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
timestamp: 2026-02-13T01:41:48.979Z
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

## Label

**URL:** https://sosumi.ai/documentation/swiftui/label?.md

**Contents:**
- Overview
- Conforms To
- Creating a label
- Displaying text

---
title: Label
description: A standard label for user interface items, consisting of an icon with a title.
source: https://developer.apple.com/documentation/swiftui/label
timestamp: 2026-02-13T01:42:29.108Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A standard label for user interface items, consisting of an icon with a title.

One of the most common and recognizable user interface components is the combination of an icon and a label. This idiom appears across many kinds of apps and shows up in collections, lists, menus of action items, and disclosable lists, just to name a few.

You create a label, in its simplest form, by providing a title and the name of an image, such as an icon from the [sf](/design/Human-Interface-Guidelines/sf-symbols) collection:

You can also apply styles to labels in several ways. In the case of dynamic changes to the view after device rotation or change to a window size you might want to show only the text portion of the label using the [title Only](/documentation/swiftui/labelstyle/titleonly) label style:

Conversely, there’s also an icon-only label style:

Some containers might apply a different default label style, such as only showing icons within toolbars on macOS and iOS. To opt in to showing both the title and the icon, you can apply the [title And Icon](/documentation/swiftui/labelstyle/titleandicon) label style:

You can also create a customized label style by modifying an existing style; this example adds a red border to the default label style:

For more extensive customization or to create a completely new label style, you’ll need to adopt the [Label Style](/documentation/swiftui/labelstyle) protocol and implement a [Label Style Configuration](/documentation/swiftui/labelstyleconfiguration) for the new style.

To apply a common label style to a group of labels, apply the style to the view hierarchy that contains the labels:

It’s also possible to make labels using views to compose the label’s icon programmatically, rather than using a pre-made image. In this example, the icon portion of the label uses a filled [Circle](/documentation/swiftui/circle) overlaid with the user’s initials:

- [View](/documentation/swiftui/view)

- [init(_:image:)](/documentation/swiftui/label/init(_:image:)) Creates a label with an icon image and a title generated from a localized string.
- [init(_:systemImage:)](/documentation/swiftui/label/init(_:systemimage:)) Creates a label with a system icon image and a title generated from a localized string.
- [init(title:icon:)](/documentation/swiftui/label/init(title:icon:)) Creates a label with a custom title and icon.
- [init(_:)](/documentation/swiftui/label/init(_:)) Creates a label representing a family activity application.
- [init(_:image:)](/documentation/swiftui/label/init(_:image:)) Creates a label with an icon image and a title generated from a localized string.

- [Text](/documentation/swiftui/text)
- [labelStyle(_:)](/documentation/swiftui/view/labelstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Label<Title, Icon> where Title : View, Icon : View
```

Example 2 (swift):
```swift
Label("Lightning", systemImage: "bolt.fill")
```

Example 3 (swift):
```swift
Label("Lightning", systemImage: "bolt.fill")
    .labelStyle(.titleOnly)
```

Example 4 (swift):
```swift
Label("Lightning", systemImage: "bolt.fill")
    .labelStyle(.iconOnly)
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
timestamp: 2026-02-13T01:42:46.699Z
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

## onTapGesture(count:perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/ontapgesture(count:perform:)?.md

**Contents:**
- Parameters
- Discussion
- Recognizing tap gestures

---
title: onTapGesture(count:perform:)
description: Adds an action to perform when this view recognizes a tap gesture.
source: https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:perform:)
timestamp: 2026-02-13T01:41:58.382Z
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
