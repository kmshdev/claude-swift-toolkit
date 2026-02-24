# Neuralforge-Top-Navbar - Tab Bar Structure

**Pages:** 3

---

## Tab

**URL:** https://sosumi.ai/documentation/swiftui/tab?.md

**Contents:**
- Conforms To
- Creating a tab
- Creating a tab with label
- Creating a tab with system symbol
- Creating a tab with image
- Supporting types
- Presenting views in tabs

---
title: Tab
description: The content for a tab and the tab’s associated tab item in a tab view.
source: https://developer.apple.com/documentation/swiftui/tab
timestamp: 2026-02-13T03:55:28.942Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

> The content for a tab and the tab’s associated tab item in a tab view.

- [Copyable](/documentation/Swift/Copyable)
- [TabContent](/documentation/swiftui/tabcontent)

- [init(content:)](/documentation/swiftui/tab/init(content:)) Creates a new tab that you can use in a tab view, with an empty label.
- [init(value:content:)](/documentation/swiftui/tab/init(value:content:)) Creates a new tab that you can use in a tab view, with an empty label.
- [init(role:content:)](/documentation/swiftui/tab/init(role:content:)) Creates a new tab that you can use in a tab view, with an empty label.
- [init(value:role:content:)](/documentation/swiftui/tab/init(value:role:content:)) Creates a new tab with a label inferred from the role.

- [init(content:label:)](/documentation/swiftui/tab/init(content:label:)) Creates a new tab with a label that you can use in a tab view.
- [init(value:content:label:)](/documentation/swiftui/tab/init(value:content:label:)) Creates a new tab with a label that you can use in a tab view.
- [init(role:content:label:)](/documentation/swiftui/tab/init(role:content:label:)) Creates a new tab with a label that you can use in a tab view.
- [init(value:role:content:label:)](/documentation/swiftui/tab/init(value:role:content:label:)) Creates a new tab with a label that you can use in a tab view.

- [init(_:systemImage:content:)](/documentation/swiftui/tab/init(_:systemimage:content:)) Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.
- [init(_:systemImage:value:content:)](/documentation/swiftui/tab/init(_:systemimage:value:content:)) Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value using a system image for the tab’s tab item image, with a localized string key label.
- [init(_:systemImage:role:content:)](/documentation/swiftui/tab/init(_:systemimage:role:content:)) Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.
- [init(_:systemImage:value:role:content:)](/documentation/swiftui/tab/init(_:systemimage:value:role:content:)) Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value using a system image for the tab’s tab item image, with a localized string key label.

- [init(_:image:content:)](/documentation/swiftui/tab/init(_:image:content:)) Creates a new tab that you can use in a tab view, with a localized string key label.
- [init(_:image:value:content:)](/documentation/swiftui/tab/init(_:image:value:content:)) Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a localized string key label.
- [init(_:image:role:content:)](/documentation/swiftui/tab/init(_:image:role:content:)) Creates a new tab that you can use in a tab view, with a localized string key label.
- [init(_:image:value:role:content:)](/documentation/swiftui/tab/init(_:image:value:role:content:)) Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a localized string key label.

- [DefaultTabLabel](/documentation/swiftui/defaulttablabel) The default label to use for a tab or tab section.

- [Enhancing your app’s content with tab navigation](/documentation/swiftui/enhancing-your-app-content-with-tab-navigation)
- [TabView](/documentation/swiftui/tabview)
- [TabRole](/documentation/swiftui/tabrole)
- [TabSection](/documentation/swiftui/tabsection)
- [tabViewStyle(_:)](/documentation/swiftui/view/tabviewstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Tab<Value, Content, Label>
```

---

## TabView

**URL:** https://sosumi.ai/documentation/swiftui/tabview?.md

**Contents:**
- Overview
  - Using tab sections
  - Changing tab structure between horizontal and regular size classes
  - Adding support for customization
- Conforms To
- Creating a tab view
- Configuring search activation
- Presenting views in tabs

---
title: TabView
description: A view that switches between multiple child views using interactive user interface elements.
source: https://developer.apple.com/documentation/swiftui/tabview
timestamp: 2026-02-13T03:55:26.800Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 7.0+

> A view that switches between multiple child views using interactive user interface elements.

To create a user interface with tabs, place [Tab](/documentation/swiftui/tab)s  in a `TabView`. On iOS, you can also use one of the badge modifiers, like [badge(_:)](/documentation/swiftui/tabcontent/badge(_:)), to assign a badge to each of the tabs.

The following example creates a tab view with three tabs, each presenting a custom child view. The first tab has a numeric badge and the third has a string badge.

To programmatically select different tabs, use the [init(selection:content:)](/documentation/swiftui/tabview/init(selection:content:)) initializer. You can assign a selection value to each tab using a `Tab` initializer that takes a value. Each tab should have a unique selection value and all tabs should have the same selection value type. When people select a tab in the tab view, the tab view updates the selection binding to the value of the currently selected tab.

The following example creates a tab view that supports programatic selection and has 3 tabs.

You can use the [page](/documentation/swiftui/tabviewstyle/page) style to display a tab view with multiple scrolling pages of content.

The following example uses a `ForEach` to create a scrolling tab view that shows the temperatures of various cities.

The [sidebar Adaptable](/documentation/swiftui/tabviewstyle/sidebaradaptable) style supports declaring a secondary tab hierarchy by grouping tabs with a [Tab Section](/documentation/swiftui/tabsection).

On iPadOS, tab sections appear in both the sidebar and the tab bar. On iOS and the horizontally compact size class on iPadOS, secondary tabs appear in the tab bar. When secondary tabs appear in the tab bar, the section header doesn’t appear in the tab bar. Consider limiting the number of tabs on iOS and the iPadOS horizontal compact size class so all tabs fit in the tab bar.

The following example has 5 tabs, three of which are grouped within a [Tab Section](/documentation/swiftui/tabsection).

The following example shows a `TabView` with 4 tabs in compact and 5 tabs in regular. In compact, one of the tabs is a ‘Browse’ tab that displays a custom list view. This list view allows navigating to the destinations that are contained within the ‘Library’ and ‘Playlists’ sections in the horizontally regular size class. The navigation path and the selection state are updated when the number of tabs changes.

You can allow people to customize the tabs in a `TabView` by using `sidebarAdaptable` style with the [tabViewCustomization(_:)](/documentation/swiftui/view/tabviewcustomization(_:)) modifier. Customization allows people to drag tabs from the sidebar to the tab bar, hide tabs, and rearrange tabs in the sidebar.

All tabs and tab sections that support customization need to have a customization ID. You can mark a tab as being non-customizable by specifying a [disabled](/documentation/swiftui/tabcustomizationbehavior/disabled) behavior in all adaptable tab bar placements using [customizationBehavior(_:for:)](/documentation/swiftui/tabcontent/customizationbehavior(_:for:)).

On macOS, a default interaction is provided for reordering sections but not for controlling the visibility of individual tabs. A custom experience should be provided if desired by setting the visibility of the tab on the customization.

You can use `@AppStorage` or `@SceneStorage` to automatically persist any visibility or section order customizations a person makes.

The following example supports customizing all 4 tabs in the tab view and uses `@AppStorage` to persist the customizations a person makes.

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/tabview/init(content:)) Creates a tab view that uses a builder to create its tabs.
- [init(selection:content:)](/documentation/swiftui/tabview/init(selection:content:)) Creates a tab view that uses a builder to create and specify selection values for its tabs.

- [TabSearchActivation](/documentation/swiftui/tabsearchactivation) Configures the activation behavior of search in the search tab.

- [Enhancing your app’s content with tab navigation](/documentation/swiftui/enhancing-your-app-content-with-tab-navigation)
- [Tab](/documentation/swiftui/tab)
- [TabRole](/documentation/swiftui/tabrole)
- [TabSection](/documentation/swiftui/tabsection)
- [tabViewStyle(_:)](/documentation/swiftui/view/tabviewstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct TabView<SelectionValue, Content> where SelectionValue : Hashable, Content : View
```

Example 2 (swift):
```swift
TabView {
    Tab("Received", systemImage: "tray.and.arrow.down.fill") {
        ReceivedView()
    }
    .badge(2)

    Tab("Sent", systemImage: "tray.and.arrow.up.fill") {
        SentView()
    }

    Tab("Account", systemImage: "person.crop.circle.fill") {
        AccountView()
    }
    .badge("!")
}
```

Example 3 (swift):
```swift
TabView(selection: $selection) {
    Tab("Received", systemImage: "tray.and.arrow.down.fill", value: 0) {
        ReceivedView()
    }

    Tab("Sent", systemImage: "tray.and.arrow.up.fill", value: 1) {
        SentView()
    }

    Tab("Account", systemImage: "person.crop.circle.fill", value: 2) {
        AccountView()
    }
}
```

Example 4 (swift):
```swift
TabView {
    ForEach(cities) { city in
        TemperatureView(city)
    }
}
.tabViewStyle(.page)
```

---

## TabViewStyle

**URL:** https://sosumi.ai/documentation/swiftui/tabviewstyle?.md

**Contents:**
- Overview
- Conforming Types
- Getting built-in tab view styles
- Supporting types
- Styling navigation views

---
title: TabViewStyle
description: A specification for the appearance and interaction of a tab view.
source: https://developer.apple.com/documentation/swiftui/tabviewstyle
timestamp: 2026-02-13T03:55:31.034Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A specification for the appearance and interaction of a tab view.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

- [CarouselTabViewStyle](/documentation/swiftui/carouseltabviewstyle)
- [DefaultTabViewStyle](/documentation/swiftui/defaulttabviewstyle)
- [GroupedTabViewStyle](/documentation/swiftui/groupedtabviewstyle)
- [PageTabViewStyle](/documentation/swiftui/pagetabviewstyle)
- [SidebarAdaptableTabViewStyle](/documentation/swiftui/sidebaradaptabletabviewstyle)
- [TabBarOnlyTabViewStyle](/documentation/swiftui/tabbaronlytabviewstyle)
- [VerticalPageTabViewStyle](/documentation/swiftui/verticalpagetabviewstyle)

- [automatic](/documentation/swiftui/tabviewstyle/automatic) The default tab view style.
- [sidebarAdaptable](/documentation/swiftui/tabviewstyle/sidebaradaptable) A tab bar style that adapts to each platform.
- [tabBarOnly](/documentation/swiftui/tabviewstyle/tabbaronly) A tab view style that displays a tab bar when possible.
- [grouped](/documentation/swiftui/tabviewstyle/grouped) A tab view style that displays a tab bar that groups its tabs together.
- [page](/documentation/swiftui/tabviewstyle/page) A  that displays a paged scrolling .
- [page(indexDisplayMode:)](/documentation/swiftui/tabviewstyle/page(indexdisplaymode:)) A  that implements a paged scrolling  with an index display mode.
- [verticalPage](/documentation/swiftui/tabviewstyle/verticalpage) A  that displays a vertical page  interaction and appearance.
- [verticalPage(transitionStyle:)](/documentation/swiftui/tabviewstyle/verticalpage(transitionstyle:)) A  that implements the vertical page  interaction and appearance, and performs the specified transition.
- [carousel](/documentation/swiftui/tabviewstyle/carousel) A style that implements the carousel interaction and appearance.

- [DefaultTabViewStyle](/documentation/swiftui/defaulttabviewstyle) The default tab view style.
- [SidebarAdaptableTabViewStyle](/documentation/swiftui/sidebaradaptabletabviewstyle) A tab bar style that adapts to each platform.
- [TabBarOnlyTabViewStyle](/documentation/swiftui/tabbaronlytabviewstyle) A tab view style that displays a tab bar when possible.
- [GroupedTabViewStyle](/documentation/swiftui/groupedtabviewstyle) A tab view style that displays a tab bar that groups its tabs together.
- [PageTabViewStyle](/documentation/swiftui/pagetabviewstyle) A  that displays a paged scrolling .
- [VerticalPageTabViewStyle](/documentation/swiftui/verticalpagetabviewstyle) A  that displays a vertical  interaction and appearance.
- [CarouselTabViewStyle](/documentation/swiftui/carouseltabviewstyle) A style that implements the carousel interaction and appearance.

- [navigationSplitViewStyle(_:)](/documentation/swiftui/view/navigationsplitviewstyle(_:))
- [NavigationSplitViewStyle](/documentation/swiftui/navigationsplitviewstyle)
- [tabViewStyle(_:)](/documentation/swiftui/view/tabviewstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency protocol TabViewStyle
```

Example 2 (swift):
```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Example 3 (swift):
```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

---
