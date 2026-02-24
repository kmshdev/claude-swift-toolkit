# Neuralforge-Top-Navbar - Toolbar Apis

**Pages:** 11

---

## toolbarBackground(_:for:)

**URL:** https://sosumi.ai/documentation/swiftui/view/toolbarbackground(_:for:)?.md

**Contents:**
- Parameters
- Discussion
- Styling a toolbar

---
title: toolbarBackground(_:for:)
description: Specifies the preferred shape style of the background of a bar managed by SwiftUI.
source: https://developer.apple.com/documentation/swiftui/view/toolbarbackground(_:for:)
timestamp: 2026-02-13T03:55:48.207Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> Specifies the preferred shape style of the background of a bar managed by SwiftUI.

The style to display as the background of the bar.

The bars to use the style for or [automatic](/documentation/swiftui/toolbarplacement/automatic) if empty.

The preferred style flows up to the nearest container that renders a bar. This could be a [Navigation View](/documentation/swiftui/navigationview) or [Tab View](/documentation/swiftui/tabview) in iOS, or the root view of a [Window Group](/documentation/swiftui/windowgroup) in macOS. This example shows a view that renders the navigation bar with a blue background and dark color scheme.

You can provide multiple [Toolbar Placement](/documentation/swiftui/toolbarplacement) instances to customize multiple bars at once.

When used within a [Tab View](/documentation/swiftui/tabview), the specified style will be preferred while the tab is currently active. You can use a [Group](/documentation/swiftui/group) to specify the same preferred background for every tab.

Depending on the specified bars, the requested style may not be able to be fullfilled.

- [toolbarColorScheme(_:for:)](/documentation/swiftui/view/toolbarcolorscheme(_:for:))
- [toolbarForegroundStyle(_:for:)](/documentation/swiftui/view/toolbarforegroundstyle(_:for:))
- [windowToolbarStyle(_:)](/documentation/swiftui/scene/windowtoolbarstyle(_:))
- [WindowToolbarStyle](/documentation/swiftui/windowtoolbarstyle)
- [toolbarLabelStyle](/documentation/swiftui/environmentvalues/toolbarlabelstyle)
- [ToolbarLabelStyle](/documentation/swiftui/toolbarlabelstyle)
- [SpacerSizing](/documentation/swiftui/spacersizing)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func toolbarBackground<S>(_ style: S, for bars: ToolbarPlacement...) -> some View where S : ShapeStyle
```

Example 2 (swift):
```swift
NavigationView {
    ContentView()
        .toolbarBackground(.white)
        .toolbarColorScheme(.dark)
}
```

Example 3 (swift):
```swift
TabView {
    NavigationView {
        ContentView()
            .toolbarBackground(
                .blue, for: .navigationBar, .tabBar)
            .toolbarColorScheme(
                .dark, for: .navigationBar, .tabBar)
    }
}
```

Example 4 (swift):
```swift
TabView {
    Group {
        MainView()
        SettingsView()
    }
    .toolbarBackground(.blue, for: .tabBar)
}
```

---

## ToolbarItem

**URL:** https://sosumi.ai/documentation/swiftui/toolbaritem?.md

**Contents:**
- Conforms To
- Creating a toolbar item
- Populating a toolbar

---
title: ToolbarItem
description: A model that represents an item which can be placed in the toolbar or navigation bar.
source: https://developer.apple.com/documentation/swiftui/toolbaritem
timestamp: 2026-02-13T03:55:37.318Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A model that represents an item which can be placed in the toolbar or navigation bar.

- [Copyable](/documentation/Swift/Copyable)
- [CustomizableToolbarContent](/documentation/swiftui/customizabletoolbarcontent)
- [Identifiable](/documentation/Swift/Identifiable)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)

- [init(placement:content:)](/documentation/swiftui/toolbaritem/init(placement:content:)) Creates a toolbar item with the specified placement and content.
- [init(id:placement:content:)](/documentation/swiftui/toolbaritem/init(id:placement:content:)) Creates a toolbar item with the specified placement and content, which allows for user customization.
- [init(id:placement:showsByDefault:content:)](/documentation/swiftui/toolbaritem/init(id:placement:showsbydefault:content:)) Creates a toolbar item with the specified placement and content, which allows for user customization.

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:))
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup)
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder)
- [ToolbarSpacer](/documentation/swiftui/toolbarspacer)
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ToolbarItem<ID, Content> where Content : View
```

---

## toolbarColorScheme(_:for:)

**URL:** https://sosumi.ai/documentation/swiftui/view/toolbarcolorscheme(_:for:)?.md

**Contents:**
- Parameters
- Discussion
- Styling a toolbar

---
title: toolbarColorScheme(_:for:)
description: Specifies the preferred color scheme of a bar managed by SwiftUI.
source: https://developer.apple.com/documentation/swiftui/view/toolbarcolorscheme(_:for:)
timestamp: 2026-02-13T03:55:50.253Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> Specifies the preferred color scheme of a bar managed by SwiftUI.

The preferred color scheme of the background of the bar.

The bars to update the color scheme of or [automatic](/documentation/swiftui/toolbarplacement/automatic) if empty.

The preferred color scheme flows up to the nearest container that renders a bar. This could be a [Navigation View](/documentation/swiftui/navigationview) or [Tab View](/documentation/swiftui/tabview) in iOS, or the root view of a [Window Group](/documentation/swiftui/windowgroup) in macOS. Pass in a value of nil to match the current system’s color scheme.

This examples shows a view that renders the navigation bar with a blue background and dark color scheme:

You can provide multiple [Toolbar Placement](/documentation/swiftui/toolbarplacement) instances to customize multiple bars at once.

Note that the provided color scheme is only respected while a background is visible in the requested bar. As the background becomes visible, the bar transitions from the color scheme of the app to the requested color scheme. You can ensure that the color scheme is always respected by specifying that the background of the bar always be visible.

Depending on the specified bars, the requested color scheme may not be able to be fullfilled.

- [toolbarBackground(_:for:)](/documentation/swiftui/view/toolbarbackground(_:for:))
- [toolbarForegroundStyle(_:for:)](/documentation/swiftui/view/toolbarforegroundstyle(_:for:))
- [windowToolbarStyle(_:)](/documentation/swiftui/scene/windowtoolbarstyle(_:))
- [WindowToolbarStyle](/documentation/swiftui/windowtoolbarstyle)
- [toolbarLabelStyle](/documentation/swiftui/environmentvalues/toolbarlabelstyle)
- [ToolbarLabelStyle](/documentation/swiftui/toolbarlabelstyle)
- [SpacerSizing](/documentation/swiftui/spacersizing)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func toolbarColorScheme(_ colorScheme: ColorScheme?, for bars: ToolbarPlacement...) -> some View
```

Example 2 (swift):
```swift
TabView {
    NavigationView {
        ContentView()
            .toolbarBackground(.blue)
            .toolbarColorScheme(.dark)
    }
    // other tabs...
}
```

Example 3 (swift):
```swift
TabView {
    NavigationView {
        ContentView()
            .toolbarBackground(
                .blue, for: .navigationBar, .tabBar)
            .toolbarColorScheme(
                .dark, for: .navigationBar, .tabBar)
    }
}
```

Example 4 (swift):
```swift
NavigationView {
    ContentView()
        .toolbarBackground(.visible)
        .toolbarColorScheme(.dark)
}
```

---

## toolbar(content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/toolbar(content:)?.md

**Contents:**
- Parameters
- Discussion
- Populating a toolbar

---
title: toolbar(content:)
description: Populates the toolbar or navigation bar with the specified items.
source: https://developer.apple.com/documentation/swiftui/view/toolbar(content:)
timestamp: 2026-02-13T03:55:33.345Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Populates the toolbar or navigation bar with the specified items.

The items representing the content of the toolbar.

Use this method to populate a toolbar with a collection of views that you provide to a toolbar view builder.

The toolbar modifier expects a collection of toolbar items which you can provide either by supplying a collection of views with each view wrapped in a [Toolbar Item](/documentation/swiftui/toolbaritem), or by providing a collection of views as a [Toolbar Item Group](/documentation/swiftui/toolbaritemgroup). The example below uses a collection of [Toolbar Item](/documentation/swiftui/toolbaritem) views to create a macOS toolbar that supports text editing features:

Although it’s not mandatory, wrapping a related group of toolbar items together in a [Toolbar Item Group](/documentation/swiftui/toolbaritemgroup) provides a one-to-one mapping between controls and toolbar items which results in the correct layout and spacing on each platform. For design guidance on toolbars, see [toolbars](/design/Human-Interface-Guidelines/toolbars) in the Human Interface Guidelines.

- [ToolbarItem](/documentation/swiftui/toolbaritem)
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup)
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder)
- [ToolbarSpacer](/documentation/swiftui/toolbarspacer)
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem)

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

## toolbarVisibility(_:for:)

**URL:** https://sosumi.ai/documentation/swiftui/view/toolbarvisibility(_:for:)?.md

**Contents:**
- Parameters
- Discussion
- Setting toolbar visibility

---
title: toolbarVisibility(_:for:)
description: Specifies the visibility of a bar managed by SwiftUI.
source: https://developer.apple.com/documentation/swiftui/view/toolbarvisibility(_:for:)
timestamp: 2026-02-13T03:55:52.200Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

> Specifies the visibility of a bar managed by SwiftUI.

The preferred visibility of the bar.

The bars to update the visibility of or [automatic](/documentation/swiftui/toolbarplacement/automatic) if empty.

The preferred visibility flows up to the nearest container that renders a bar. This could be a [Navigation View](/documentation/swiftui/navigationview) or [Tab View](/documentation/swiftui/tabview) in iOS, or the root view of a [Window Group](/documentation/swiftui/windowgroup) in macOS.

This examples shows a view that hides the navigation bar on iOS, or the window toolbar items on macOS.

To hide the entire titlebar on macOS, use this modifier with [window Toolbar](/documentation/swiftui/toolbarplacement/windowtoolbar) placement.

You can provide multiple [Toolbar Placement](/documentation/swiftui/toolbarplacement) instances to hide multiple bars at once.

> [!NOTE]
> In macOS, if you provide [Toolbar Commands](/documentation/swiftui/toolbarcommands) to the scene of your app, this modifier disables the toolbar visibility command while the value of the modifier is not [automatic](/documentation/swiftui/toolbarplacement/automatic).

Depending on the specified bars, the requested visibility may not be able to be fulfilled.

- [toolbar(_:for:)](/documentation/swiftui/view/toolbar(_:for:))
- [toolbarBackgroundVisibility(_:for:)](/documentation/swiftui/view/toolbarbackgroundvisibility(_:for:))
- [ToolbarPlacement](/documentation/swiftui/toolbarplacement)
- [ContentToolbarPlacement](/documentation/swiftui/contenttoolbarplacement)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func toolbarVisibility(_ visibility: Visibility, for bars: ToolbarPlacement...) -> some View
```

Example 2 (swift):
```swift
NavigationView {
    ContentView()
        .toolbarVisibility(.hidden)
}
```

Example 3 (swift):
```swift
NavigationView {
    ContentView()
        .toolbarVisibility(.hidden, for: .windowToolbar)
}
```

Example 4 (swift):
```swift
TabView {
    NavigationView {
        ContentView()
            .toolbarVisibility(
                .hidden, for: .navigationBar, .tabBar)
    }
}
```

---

## Landmarks: Refining the system provided Liquid Glass effect in toolbars

**URL:** https://sosumi.ai/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars?.md

**Contents:**
- Overview
- Organize the toolbar items into logical groupings
- App features

---
title: Landmarks: Refining the system provided Liquid Glass effect in toolbars
description: Organize toolbars into related groupings to improve their appearance and utility.
source: https://developer.apple.com/documentation/swiftui/landmarks-refining-the-system-provided-glass-effect-in-toolbars
timestamp: 2026-02-13T03:56:32.967Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, macOS 26.0+, Xcode 26.0+

> Organize toolbars into related groupings to improve their appearance and utility.

The Landmarks app lets people explore interesting sites around the world. Whether it’s a national park near their home or a far-flung location on a different continent, the app provides a way for people to organize and mark their adventures and receive custom activity badges along the way.

This sample demonstrates how to refine the system provided glass effect in toolbars. In `LandmarkDetailView`, the sample adds toolbar items for:

- sharing a landmark
- adding or removing a landmark from a list of Favorites
- adding or removing a landmark from Collections
- showing or hiding the inspector

The system applies Liquid Glass to the toolbar items automatically.

To organize the toolbar items into logical groupings, the sample adds [Toolbar Spacer](/documentation/swiftui/toolbarspacer) items and passes [fixed](/documentation/swiftui/spacersizing/fixed) as the `sizing` parameter to divide the toolbar into sections:

- [Landmarks: Applying a background extension effect](/documentation/swiftui/landmarks-applying-a-background-extension-effect)
- [Landmarks: Extending horizontal scrolling under a sidebar or inspector](/documentation/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector)
- [Landmarks: Displaying custom activity badges](/documentation/swiftui/landmarks-displaying-custom-activity-badges)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
.toolbar {
    ToolbarSpacer(.flexible)

    ToolbarItem {
        ShareLink(item: landmark, preview: landmark.sharePreview)
    }

    ToolbarSpacer(.fixed)
    
    ToolbarItemGroup {
        LandmarkFavoriteButton(landmark: landmark)
        LandmarkCollectionsMenu(landmark: landmark)
    }
    
    ToolbarSpacer(.fixed)

    ToolbarItem {
        Button("Info", systemImage: "info") {
            modelData.selectedLandmark = landmark
            modelData.isLandmarkInspectorPresented.toggle()
        }
    }
}
```

---

## toolbarRole(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/toolbarrole(_:)?.md

**Contents:**
- Parameters
- Discussion
- Specifying the role of toolbar content

---
title: toolbarRole(_:)
description: Configures the semantic role for the content populating the toolbar.
source: https://developer.apple.com/documentation/swiftui/view/toolbarrole(_:)
timestamp: 2026-02-13T03:55:35.271Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> Configures the semantic role for the content populating the toolbar.

The role of the toolbar.

Use this modifier to configure the semantic role for content populating your app’s toolbar. SwiftUI uses this role when rendering the content of your app’s toolbar.

- [ToolbarRole](/documentation/swiftui/toolbarrole)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func toolbarRole(_ role: ToolbarRole) -> some View
```

Example 2 (swift):
```swift
ContentView()
    .navigationTitle("Browser")
    .toolbarRole(.browser)
    .toolbar {
        ToolbarItem(placement: .primaryAction) {
            AddButton()
        }
     }
```

---

## ToolbarItemPlacement

**URL:** https://sosumi.ai/documentation/swiftui/toolbaritemplacement?.md

**Contents:**
- Overview
- Getting semantic placement
- Getting placement for specific actions
- Getting explicit placement
- Deprecated symbols
- Type Properties
- Populating a toolbar

---
title: ToolbarItemPlacement
description: A structure that defines the placement of a toolbar item.
source: https://developer.apple.com/documentation/swiftui/toolbaritemplacement
timestamp: 2026-02-13T03:55:45.295Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A structure that defines the placement of a toolbar item.

There are two types of placements:

- Semantic placements, such as [principal](/documentation/swiftui/toolbaritemplacement/principal) and [navigation](/documentation/swiftui/toolbaritemplacement/navigation), denote the intent of the item being added. SwiftUI determines the appropriate placement for the item based on this intent and its surrounding context, like the current platform.
- Positional placements, such as [navigation Bar Leading](/documentation/swiftui/toolbaritemplacement/navigationbarleading), denote a precise placement for the item, usually for a particular platform.

In iOS, iPadOS, and macOS, the system uses the space available to the toolbar when determining how many items to render in the toolbar. If not all items fit in the available space, an overflow menu may be created and remaining items placed in that menu.

- [automatic](/documentation/swiftui/toolbaritemplacement/automatic) The system places the item automatically, depending on many factors including the platform, size class, or presence of other items.
- [principal](/documentation/swiftui/toolbaritemplacement/principal) The system places the item in the principal item section.
- [status](/documentation/swiftui/toolbaritemplacement/status) The item represents a change in status for the current context.

- [primaryAction](/documentation/swiftui/toolbaritemplacement/primaryaction) The item represents a primary action.
- [secondaryAction](/documentation/swiftui/toolbaritemplacement/secondaryaction) The item represents a secondary action.
- [confirmationAction](/documentation/swiftui/toolbaritemplacement/confirmationaction) The item represents a confirmation action for a modal interface.
- [cancellationAction](/documentation/swiftui/toolbaritemplacement/cancellationaction) The item represents a cancellation action for a modal interface.
- [destructiveAction](/documentation/swiftui/toolbaritemplacement/destructiveaction) The item represents a destructive action for a modal interface.
- [navigation](/documentation/swiftui/toolbaritemplacement/navigation) The item represents a navigation action.

- [topBarLeading](/documentation/swiftui/toolbaritemplacement/topbarleading) Places the item in the leading edge of the top bar.
- [topBarTrailing](/documentation/swiftui/toolbaritemplacement/topbartrailing) Places the item in the trailing edge of the top bar.
- [bottomBar](/documentation/swiftui/toolbaritemplacement/bottombar) Places the item in the bottom toolbar.
- [bottomOrnament](/documentation/swiftui/toolbaritemplacement/bottomornament) Places the item in an ornament under the window.
- [keyboard](/documentation/swiftui/toolbaritemplacement/keyboard) The item is placed in the keyboard section.
- [accessoryBar(id:)](/documentation/swiftui/toolbaritemplacement/accessorybar(id:)) Creates a unique accessory bar placement.

- [init(id:)](/documentation/swiftui/toolbaritemplacement/init(id:)) Creates a custom accessory bar item placement.
- [navigationBarLeading](/documentation/swiftui/toolbaritemplacement/navigationbarleading) Places the item in the leading edge of the navigation bar.
- [navigationBarTrailing](/documentation/swiftui/toolbaritemplacement/navigationbartrailing) Places the item in the trailing edge of the navigation bar.

- [largeSubtitle](/documentation/swiftui/toolbaritemplacement/largesubtitle) Places the item in the subtitle area of the navigation bar.
- [largeTitle](/documentation/swiftui/toolbaritemplacement/largetitle) Places the item in the title area of the navigation bar.
- [subtitle](/documentation/swiftui/toolbaritemplacement/subtitle) Places the item in the subtitle area of the navigation bar.
- [title](/documentation/swiftui/toolbaritemplacement/title) Places the item in the title area of the navigation bar.

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:))
- [ToolbarItem](/documentation/swiftui/toolbaritem)
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder)
- [ToolbarSpacer](/documentation/swiftui/toolbarspacer)
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ToolbarItemPlacement
```

---

## ToolbarItemGroup

**URL:** https://sosumi.ai/documentation/swiftui/toolbaritemgroup?.md

**Contents:**
- Conforms To
- Creating a toolbar item group
- Supporting types
- Populating a toolbar

---
title: ToolbarItemGroup
description: A model that represents a group of s which can be placed in the toolbar or navigation bar.
source: https://developer.apple.com/documentation/swiftui/toolbaritemgroup
timestamp: 2026-02-13T03:55:39.351Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A model that represents a group of s which can be placed in the toolbar or navigation bar.

- [ToolbarContent](/documentation/swiftui/toolbarcontent)

- [init(placement:content:)](/documentation/swiftui/toolbaritemgroup/init(placement:content:)) Creates a toolbar item group with a specified placement and content.
- [init(placement:content:label:)](/documentation/swiftui/toolbaritemgroup/init(placement:content:label:)) Creates a toolbar item group with the specified placement, content, and a label describing that content.

- [LabeledToolbarItemGroupContent](/documentation/swiftui/labeledtoolbaritemgroupcontent) A view that represents the view of a toolbar item group with a specified label.

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:))
- [ToolbarItem](/documentation/swiftui/toolbaritem)
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder)
- [ToolbarSpacer](/documentation/swiftui/toolbarspacer)
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ToolbarItemGroup<Content> where Content : View
```

---

## fixed

**URL:** https://sosumi.ai/documentation/swiftui/spacersizing/fixed?.md

---
title: fixed
description: The fixed spacer sizing behavior. The spacer will use a pre-defined size determined by the system and the context in which the spacer is used.
source: https://developer.apple.com/documentation/swiftui/spacersizing/fixed
timestamp: 2026-02-13T03:55:43.313Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [spacersizing](/documentation/swiftui/spacersizing)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+

> The fixed spacer sizing behavior. The spacer will use a pre-defined size determined by the system and the context in which the spacer is used.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
static let fixed: SpacerSizing
```

---

## ToolbarSpacer

**URL:** https://sosumi.ai/documentation/swiftui/toolbarspacer?.md

**Contents:**
- Overview
- Conforms To
- Initializers
- Populating a toolbar

---
title: ToolbarSpacer
description: A standard space item in toolbars.
source: https://developer.apple.com/documentation/swiftui/toolbarspacer
timestamp: 2026-02-13T03:55:41.372Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+

> A standard space item in toolbars.

A space item creates visual breaks in the toolbar between items. Spacers can have a standard fixed size or be flexible and push items apart.

Spacers can also be used in customizable toolbars:

Space items are customizable and can be added, removed, and rearranged by users. If a customizable toolbar supports a spacer of a given type, users can also add in multiple copies of that spacer from the customization panel.

- [CustomizableToolbarContent](/documentation/swiftui/customizabletoolbarcontent)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)

- [init(_:placement:)](/documentation/swiftui/toolbarspacer/init(_:placement:)) Creates a toolbar spacer item with the specified sizing behavior and placement.

- [toolbar(content:)](/documentation/swiftui/view/toolbar(content:))
- [ToolbarItem](/documentation/swiftui/toolbaritem)
- [ToolbarItemGroup](/documentation/swiftui/toolbaritemgroup)
- [ToolbarItemPlacement](/documentation/swiftui/toolbaritemplacement)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)
- [ToolbarContentBuilder](/documentation/swiftui/toolbarcontentbuilder)
- [DefaultToolbarItem](/documentation/swiftui/defaulttoolbaritem)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ToolbarSpacer
```

Example 2 (swift):
```swift
ContentView()
    .toolbar(id: "main-toolbar") {
        ToolbarItem(id: "tag") {
           TagButton()
        }
        ToolbarItem(id: "share") {
           ShareButton()
        }
        ToolbarSpacer(.fixed)
        ToolbarItem(id: "more") {
           MoreButton()
        }
    }
```

---
