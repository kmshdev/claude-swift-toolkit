# Neuralforge-Top-Navbar - Tab Interactions

**Pages:** 8

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
timestamp: 2026-02-13T03:56:05.728Z
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

## onDrop(of:isTargeted:perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/ondrop(of:istargeted:perform:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Moving items using item providers

---
title: onDrop(of:isTargeted:perform:)
description: Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
source: https://developer.apple.com/documentation/swiftui/view/ondrop(of:istargeted:perform:)
timestamp: 2026-02-13T03:56:43.475Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+

> Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.

**supportedContentTypes**

The uniform type identifiers that describe the types of content this view can accept through drag and drop. If the drag-and-drop operation doesn’t contain any of the supported types, then this drop destination doesn’t activate and `isTargeted` doesn’t update.

A binding that updates when a drag and drop operation enters or exits the drop target area. The binding’s value is `true` when the cursor is inside the area, and `false` when the cursor is outside.

A closure that takes the dropped content and responds appropriately. The parameter to `action` contains the dropped items, with types specified by `supportedContentTypes`. Return `true` if the drop operation was successful; otherwise, return `false`.

A view that provides a drop destination for a drag operation of the specified types.

The drop destination is the same size and position as this view.

Make sure to start loading the contents of `NSItemProvider` instances within the scope of the `action` closure. Do not perform loading asynchronously on a different actor. Loading the contents may finish later, but it must start here. For security reasons, the drop receiver can access the dropped payload only before this closure returns.

- [itemProvider(_:)](/documentation/swiftui/view/itemprovider(_:))
- [onDrag(_:preview:)](/documentation/swiftui/view/ondrag(_:preview:))
- [onDrag(_:)](/documentation/swiftui/view/ondrag(_:))
- [onDrop(of:delegate:)](/documentation/swiftui/view/ondrop(of:delegate:))
- [DropDelegate](/documentation/swiftui/dropdelegate)
- [DropProposal](/documentation/swiftui/dropproposal)
- [DropOperation](/documentation/swiftui/dropoperation)
- [DropInfo](/documentation/swiftui/dropinfo)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onDrop(of supportedContentTypes: [UTType], isTargeted: Binding<Bool>?, perform action: @escaping ([NSItemProvider]) -> Bool) -> some View
```

---

## draggable(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/draggable(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Moving transferable items

---
title: draggable(_:)
description: Activates this view as the source of a drag and drop operation.
source: https://developer.apple.com/documentation/swiftui/view/draggable(_:)
timestamp: 2026-02-13T03:56:45.506Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+

> Activates this view as the source of a drag and drop operation.

A closure that returns a single instance or a value conforming to [Transferable](/documentation/CoreTransferable/Transferable) that represents the draggable data from this view.

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

To customize the default preview, apply a [contentShape(_:_:eoFill:)](/documentation/swiftui/view/contentshape(_:_:eofill:)) with a [drag Preview](/documentation/swiftui/contentshapekinds/dragpreview) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

- [draggable(_:preview:)](/documentation/swiftui/view/draggable(_:preview:))
- [dropDestination(for:action:isTargeted:)](/documentation/swiftui/view/dropdestination(for:action:istargeted:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some View where T : Transferable
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
timestamp: 2026-02-13T03:56:07.893Z
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
timestamp: 2026-02-13T03:56:24.742Z
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
timestamp: 2026-02-13T03:56:36.954Z
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
timestamp: 2026-02-13T03:56:38.976Z
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

## onDrag(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/ondrag(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Moving items using item providers

---
title: onDrag(_:)
description: Activates this view as the source of a drag and drop operation.
source: https://developer.apple.com/documentation/swiftui/view/ondrag(_:)
timestamp: 2026-02-13T03:56:41.240Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+

> Activates this view as the source of a drag and drop operation.

A closure that returns a single [NSItem Provider](/documentation/Foundation/NSItemProvider) that represents the draggable data from this view.

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

Applying the `onDrag(_:)` modifier adds the appropriate gestures for drag and drop to this view. When a drag operation begins, a rendering of this view is generated and used as the preview image.

To customize the default preview, apply a [contentShape(_:_:eoFill:)](/documentation/swiftui/view/contentshape(_:_:eofill:)) with a [drag Preview](/documentation/swiftui/contentshapekinds/dragpreview) kind. For example, you can change the preview’s corner radius or use a nested view as the preview.

If you want to show a different preview, you can use [onDrag(_:preview:)](/documentation/swiftui/view/ondrag(_:preview:)).

- [itemProvider(_:)](/documentation/swiftui/view/itemprovider(_:))
- [onDrag(_:preview:)](/documentation/swiftui/view/ondrag(_:preview:))
- [onDrop(of:isTargeted:perform:)](/documentation/swiftui/view/ondrop(of:istargeted:perform:))
- [onDrop(of:delegate:)](/documentation/swiftui/view/ondrop(of:delegate:))
- [DropDelegate](/documentation/swiftui/dropdelegate)
- [DropProposal](/documentation/swiftui/dropproposal)
- [DropOperation](/documentation/swiftui/dropoperation)
- [DropInfo](/documentation/swiftui/dropinfo)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onDrag(_ data: @escaping () -> NSItemProvider) -> some View
```

---
