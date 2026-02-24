# Sidebar-Liquid-Glass-Clone - Sidebar Structure

**Pages:** 8

---

## Section

**URL:** https://sosumi.ai/documentation/swiftui/section?.md

**Contents:**
- Overview
  - Collapsible sections
- Conforms To
- Creating a section
- Adding headers and footers
- Controlling collapsibility
- Deprecated symbols
- Organizing views into sections

---
title: Section
description: A container view that you can use to add hierarchy within certain views.
source: https://developer.apple.com/documentation/swiftui/section
timestamp: 2026-02-13T01:04:18.118Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A container view that you can use to add hierarchy within certain views.

Use `Section` instances in views like [List](/documentation/swiftui/list), [Picker](/documentation/swiftui/picker), and [Form](/documentation/swiftui/form) to organize content into separate sections. Each section has custom content that you provide on a per-instance basis. You can also provide headers and footers for each section.

Create sections that expand and collapse by using an initializer that accepts an `isExpanded` binding. A collapsible section in a [List](/documentation/swiftui/list) that uses the [sidebar](/documentation/swiftui/liststyle/sidebar) style shows a disclosure indicator next to the section’s header. Tapping on the disclosure indicator toggles the appearance of the section’s content.

> [!NOTE]
> Not all contexts provide a default control to trigger collapse or expansion.

- [Copyable](/documentation/Swift/Copyable)
- [TableRowContent](/documentation/swiftui/tablerowcontent)
- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/section/init(content:)) Creates a section with the provided section content.
- [init(_:content:)](/documentation/swiftui/section/init(_:content:)) Creates a section with the provided section content.

- [init(content:header:)](/documentation/swiftui/section/init(content:header:)) Creates a section with a header and the provided section content.
- [init(content:footer:)](/documentation/swiftui/section/init(content:footer:)) Creates a section with a footer and the provided section content.
- [init(content:header:footer:)](/documentation/swiftui/section/init(content:header:footer:)) Creates a section with a header, footer, and the provided section content.

- [init(_:isExpanded:content:)](/documentation/swiftui/section/init(_:isexpanded:content:)) Creates a section with the provided section content.
- [init(isExpanded:content:header:)](/documentation/swiftui/section/init(isexpanded:content:header:)) Creates a section with a header, the provided section content, and a binding representing the section’s expansion state.

- [init(header:content:)](/documentation/swiftui/section/init(header:content:)) Creates a section with a header and the provided section content.
- [init(footer:content:)](/documentation/swiftui/section/init(footer:content:)) Creates a section with a footer and the provided section content.
- [init(header:footer:content:)](/documentation/swiftui/section/init(header:footer:content:)) Creates a section with a header, footer, and the provided section content.
- [collapsible(_:)](/documentation/swiftui/section/collapsible(_:)) Sets whether a section can be collapsed by the user.

- [SectionCollection](/documentation/swiftui/sectioncollection)
- [SectionConfiguration](/documentation/swiftui/sectionconfiguration)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Section<Parent, Content, Footer>
```

---

## NavigationSplitViewStyle

**URL:** https://sosumi.ai/documentation/swiftui/navigationsplitviewstyle?.md

**Contents:**
- Overview
- Conforming Types
- Creating built-in styles
- Creating custom styles
- Supporting types
- Styling navigation views

---
title: NavigationSplitViewStyle
description: A type that specifies the appearance and interaction of navigation split views within a view hierarchy.
source: https://developer.apple.com/documentation/swiftui/navigationsplitviewstyle
timestamp: 2026-02-13T01:04:13.673Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> A type that specifies the appearance and interaction of navigation split views within a view hierarchy.

To configure the navigation split view style for a view hierarchy, use the [navigationSplitViewStyle(_:)](/documentation/swiftui/view/navigationsplitviewstyle(_:)) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

- [AutomaticNavigationSplitViewStyle](/documentation/swiftui/automaticnavigationsplitviewstyle)
- [BalancedNavigationSplitViewStyle](/documentation/swiftui/balancednavigationsplitviewstyle)
- [ProminentDetailNavigationSplitViewStyle](/documentation/swiftui/prominentdetailnavigationsplitviewstyle)

- [automatic](/documentation/swiftui/navigationsplitviewstyle/automatic) A navigation split style that resolves its appearance automatically based on the current context.
- [balanced](/documentation/swiftui/navigationsplitviewstyle/balanced) A navigation split style that reduces the size of the detail content to make room when showing the leading column or columns.
- [prominentDetail](/documentation/swiftui/navigationsplitviewstyle/prominentdetail) A navigation split style that attempts to maintain the size of the detail content when hiding or showing the leading columns.

- [makeBody(configuration:)](/documentation/swiftui/navigationsplitviewstyle/makebody(configuration:)) Creates a view that represents the body of a navigation split view.
- [NavigationSplitViewStyle.Configuration](/documentation/swiftui/navigationsplitviewstyle/configuration) The properties of a navigation split view instance.
- [Body](/documentation/swiftui/navigationsplitviewstyle/body) A view that represents the body of a navigation split view.

- [AutomaticNavigationSplitViewStyle](/documentation/swiftui/automaticnavigationsplitviewstyle) A navigation split style that resolves its appearance automatically based on the current context.
- [BalancedNavigationSplitViewStyle](/documentation/swiftui/balancednavigationsplitviewstyle) A navigation split style that reduces the size of the detail content to make room when showing the leading column or columns.
- [ProminentDetailNavigationSplitViewStyle](/documentation/swiftui/prominentdetailnavigationsplitviewstyle) A navigation split style that attempts to maintain the size of the detail content when hiding or showing the leading columns.
- [NavigationSplitViewStyleConfiguration](/documentation/swiftui/navigationsplitviewstyleconfiguration) The properties of a navigation split view instance.

- [navigationSplitViewStyle(_:)](/documentation/swiftui/view/navigationsplitviewstyle(_:))
- [tabViewStyle(_:)](/documentation/swiftui/view/tabviewstyle(_:))
- [TabViewStyle](/documentation/swiftui/tabviewstyle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency protocol NavigationSplitViewStyle
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

## List

**URL:** https://sosumi.ai/documentation/swiftui/list?.md

**Contents:**
- Overview
  - Supporting selection in lists
  - Refreshing the list content
  - Supporting multidimensional lists
  - Creating hierarchical lists
  - Styling lists
- Conforms To
- Creating a list from a set of views
- Creating a list from enumerated data
- Creating a list from hierarchical data

---
title: List
description: A container that presents rows of data arranged in a single column, optionally providing the ability to select one or more members.
source: https://developer.apple.com/documentation/swiftui/list
timestamp: 2026-02-13T01:04:15.868Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A container that presents rows of data arranged in a single column, optionally providing the ability to select one or more members.

In its simplest form, a `List` creates its contents statically, as shown in the following example:

More commonly, you create lists dynamically from an underlying collection of data. The following example shows how to create a simple list from an array of an `Ocean` type which conforms to [Identifiable](/documentation/Swift/Identifiable):

To make members of a list selectable, provide a binding to a selection variable. Binding to a single instance of the list data’s `Identifiable.ID` type creates a single-selection list. Binding to a [Set](/documentation/Swift/Set) creates a list that supports multiple selections. The following example shows how to add multiselect to the previous example:

When people make a single selection by tapping or clicking, the selected cell changes its appearance to indicate the selection. To enable multiple selections with tap gestures, put the list into edit mode by either modifying the [edit Mode](/documentation/swiftui/environmentvalues/editmode) value, or adding an [Edit Button](/documentation/swiftui/editbutton) to your app’s interface. When you put the list into edit mode, the list shows a circle next to each list item. The circle contains a checkmark when the user selects the associated item. The example above uses an Edit button, which changes its title to Done while in edit mode:

People can make multiple selections without needing to enter edit mode on devices that have a keyboard and mouse or trackpad, like Mac and iPad.

To make the content of the list refreshable using the standard refresh control, use the [refreshable(action:)](/documentation/swiftui/view/refreshable(action:)) modifier.

The following example shows how to add a standard refresh control to a list. When the user drags the top of the list downward, SwiftUI reveals the refresh control and executes the specified action. Use an `await` expression inside the `action` closure to refresh your data. The refresh indicator remains visible for the duration of the awaited operation.

To create two-dimensional lists, group items inside [Section](/documentation/swiftui/section) instances. The following example creates sections named after the world’s oceans, each of which has [Text](/documentation/swiftui/text) views named for major seas attached to those oceans. The example also allows for selection of a single list item, identified by the `id` of the example’s `Sea` type.

Because this example uses single selection, people can make selections outside of edit mode on all platforms.

> [!NOTE]
> In iOS 15, iPadOS 15, and tvOS 15 and earlier, lists support selection only in edit mode, even for single selections.

You can also create a hierarchical list of arbitrary depth by providing tree-structured data and a `children` parameter that provides a key path to get the child nodes at any level. The following example uses a deeply-nested collection of a custom `FileItem` type to simulate the contents of a file system. The list created from this data uses collapsing cells to allow the user to navigate the tree structure.

SwiftUI chooses a display style for a list based on the platform and the view type in which it appears. Use the [listStyle(_:)](/documentation/swiftui/view/liststyle(_:)) modifier to apply a different [List Style](/documentation/swiftui/liststyle) to all lists within a view. For example, adding `.listStyle(.plain)` to the example shown in the “Creating Multidimensional Lists” topic applies the [plain](/documentation/swiftui/liststyle/plain) style, the following screenshot shows:

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/list/init(content:)) Creates a list with the given content.
- [init(selection:content:)](/documentation/swiftui/list/init(selection:content:)) Creates a list with the given content that supports selecting a single row that cannot be deselected.

- [init(_:rowContent:)](/documentation/swiftui/list/init(_:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data.
- [init(_:selection:rowContent:)](/documentation/swiftui/list/init(_:selection:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data, optionally allowing users to select a single row.
- [init(_:id:rowContent:)](/documentation/swiftui/list/init(_:id:rowcontent:)) Creates a list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:selection:rowContent:)](/documentation/swiftui/list/init(_:id:selection:rowcontent:)) Creates a list that identifies its rows based on a key path to the identifier of the underlying data, optionally allowing users to select a single row.

- [init(_:children:rowContent:)](/documentation/swiftui/list/init(_:children:rowcontent:)) Creates a hierarchical list that computes its rows on demand from a binding to an underlying collection of identifiable data.
- [init(_:children:selection:rowContent:)](/documentation/swiftui/list/init(_:children:selection:rowcontent:)) Creates a hierarchical list that computes its rows on demand from a binding to an underlying collection of identifiable data and allowing users to have exactly one row always selected.
- [init(_:id:children:rowContent:)](/documentation/swiftui/list/init(_:id:children:rowcontent:)) Creates a hierarchical list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:children:selection:rowContent:)](/documentation/swiftui/list/init(_:id:children:selection:rowcontent:)) Creates a hierarchical list that identifies its rows based on a key path to the identifier of the underlying data and allowing users to have exactly one row always selected.

- [init(_:editActions:rowContent:)](/documentation/swiftui/list/init(_:editactions:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.
- [init(_:editActions:selection:rowContent:)](/documentation/swiftui/list/init(_:editactions:selection:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.
- [init(_:id:editActions:rowContent:)](/documentation/swiftui/list/init(_:id:editactions:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.
- [init(_:id:editActions:selection:rowContent:)](/documentation/swiftui/list/init(_:id:editactions:selection:rowcontent:)) Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.

- [body](/documentation/swiftui/list/body) The content of the list.

- [Displaying data in lists](/documentation/swiftui/displaying-data-in-lists)
- [listStyle(_:)](/documentation/swiftui/view/liststyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency struct List<SelectionValue, Content> where SelectionValue : Hashable, Content : View
```

Example 2 (swift):
```swift
var body: some View {
    List {
        Text("A List Item")
        Text("A Second List Item")
        Text("A Third List Item")
    }
}
```

Example 3 (swift):
```swift
struct Ocean: Identifiable {
    let name: String
    let id = UUID()
}

private var oceans = [
    Ocean(name: "Pacific"),
    Ocean(name: "Atlantic"),
    Ocean(name: "Indian"),
    Ocean(name: "Southern"),
    Ocean(name: "Arctic")
]

var body: some View {
    List(oceans) {
        Text($0.name)
    }
}
```

Example 4 (swift):
```swift
struct Ocean: Identifiable, Hashable {
    let name: String
    let id = UUID()
}

private var oceans = [
    Ocean(name: "Pacific"),
    Ocean(name: "Atlantic"),
    Ocean(name: "Indian"),
    Ocean(name: "Southern"),
    Ocean(name: "Arctic")
]

@State private var multiSelection = Set<UUID>()

var body: some View {
    NavigationView {
        List(oceans, selection: $multiSelection) {
            Text($0.name)
        }
        .navigationTitle("Oceans")
        .toolbar { EditButton() }
    }
    Text("\(multiSelection.count) selections")
}
```

---

## listStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/liststyle(_:)?.md

**Contents:**
- Creating a list

---
title: listStyle(_:)
description: Sets the style for lists within this view.
source: https://developer.apple.com/documentation/swiftui/view/liststyle(_:)
timestamp: 2026-02-13T01:04:37.436Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the style for lists within this view.

- [Displaying data in lists](/documentation/swiftui/displaying-data-in-lists)
- [List](/documentation/swiftui/list)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func listStyle<S>(_ style: S) -> some View where S : ListStyle
```

---

## listRowSeparator(_:edges:)

**URL:** https://sosumi.ai/documentation/swiftui/view/listrowseparator(_:edges:)?.md

**Contents:**
- Parameters
- Discussion
- Configuring separators

---
title: listRowSeparator(_:edges:)
description: Sets the display mode for the separator associated with this specific row.
source: https://developer.apple.com/documentation/swiftui/view/listrowseparator(_:edges:)
timestamp: 2026-02-13T01:04:34.384Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS 1.0+

> Sets the display mode for the separator associated with this specific row.

The visibility of this row’s separators.

The set of row edges for which this preference applies. The list style might already decide to not display separators for some edges, typically the top edge. The default is [all](/documentation/swiftui/verticaledge/set/all).

Separators can be presented above and below a row. You can specify to which edge this preference should apply.

This modifier expresses a preference to the containing [List](/documentation/swiftui/list). The list style is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose row separators are hidden:

To change the color of a row separators, use [listRowSeparatorTint(_:edges:)](/documentation/swiftui/view/listrowseparatortint(_:edges:)). To hide or change the tint color for a section separators, use [listSectionSeparator(_:edges:)](/documentation/swiftui/view/listsectionseparator(_:edges:)) and [listSectionSeparatorTint(_:edges:)](/documentation/swiftui/view/listsectionseparatortint(_:edges:)).

- [listRowSeparatorTint(_:edges:)](/documentation/swiftui/view/listrowseparatortint(_:edges:))
- [listSectionSeparatorTint(_:edges:)](/documentation/swiftui/view/listsectionseparatortint(_:edges:))
- [listSectionSeparator(_:edges:)](/documentation/swiftui/view/listsectionseparator(_:edges:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func listRowSeparator(_ visibility: Visibility, edges: VerticalEdge.Set = .all) -> some View
```

Example 2 (swift):
```swift
List {
    ForEach(garage.cars) { car in
        Text(car.model)
            .listRowSeparator(.hidden)
    }
}
.listStyle(.grouped)
```

---

## tabViewSidebarBottomBar(content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/tabviewsidebarbottombar(content:)?.md

**Contents:**
- Discussion
- Configuring a tab bar

---
title: tabViewSidebarBottomBar(content:)
description: Adds a custom bottom bar to the sidebar of a tab view.
source: https://developer.apple.com/documentation/swiftui/view/tabviewsidebarbottombar(content:)
timestamp: 2026-02-13T01:04:32.324Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+

> Adds a custom bottom bar to the sidebar of a tab view.

The content is pinned at the bottom of the sidebar, so it’s always visible when the sidebar is visible and doesn’t scroll with the content.

The following example adds an account button to the bottom of the sidebar:

- [defaultAdaptableTabBarPlacement(_:)](/documentation/swiftui/view/defaultadaptabletabbarplacement(_:))
- [tabViewSidebarHeader(content:)](/documentation/swiftui/view/tabviewsidebarheader(content:))
- [tabViewSidebarFooter(content:)](/documentation/swiftui/view/tabviewsidebarfooter(content:))
- [AdaptableTabBarPlacement](/documentation/swiftui/adaptabletabbarplacement)
- [tabBarPlacement](/documentation/swiftui/environmentvalues/tabbarplacement)
- [TabBarPlacement](/documentation/swiftui/tabbarplacement)
- [isTabBarShowingSections](/documentation/swiftui/environmentvalues/istabbarshowingsections)
- [TabBarMinimizeBehavior](/documentation/swiftui/tabbarminimizebehavior)
- [TabViewBottomAccessoryPlacement](/documentation/swiftui/tabviewbottomaccessoryplacement)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func tabViewSidebarBottomBar<Content>(@ViewBuilder content: () -> Content) -> some View where Content : View
```

Example 2 (swift):
```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }

    Tab("Browse", systemImage: "list.bullet") {
        MyBrowseView()
    }
}
.tabViewStyle(.sidebarAdaptable)
.tabViewSidebarBottomBar {
    AccountButton()
}
```

---

## SidebarListStyle

**URL:** https://sosumi.ai/documentation/swiftui/sidebarliststyle?.md

**Contents:**
- Overview
- Conforms To
- Creating the list style
- Supporting types

---
title: SidebarListStyle
description: The list style that describes the behavior and appearance of a sidebar list.
source: https://developer.apple.com/documentation/swiftui/sidebarliststyle
timestamp: 2026-02-13T01:04:39.420Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, visionOS 1.0+

> The list style that describes the behavior and appearance of a sidebar list.

You can also use [sidebar](/documentation/swiftui/liststyle/sidebar) to construct this style.

- [ListStyle](/documentation/swiftui/liststyle)

- [init()](/documentation/swiftui/sidebarliststyle/init()) Creates a sidebar list style.

- [DefaultListStyle](/documentation/swiftui/defaultliststyle)
- [BorderedListStyle](/documentation/swiftui/borderedliststyle)
- [CarouselListStyle](/documentation/swiftui/carouselliststyle)
- [EllipticalListStyle](/documentation/swiftui/ellipticalliststyle)
- [GroupedListStyle](/documentation/swiftui/groupedliststyle)
- [InsetListStyle](/documentation/swiftui/insetliststyle)
- [InsetGroupedListStyle](/documentation/swiftui/insetgroupedliststyle)
- [PlainListStyle](/documentation/swiftui/plainliststyle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct SidebarListStyle
```

---

## NavigationSplitView

**URL:** https://sosumi.ai/documentation/swiftui/navigationsplitview?.md

**Contents:**
- Overview
  - Control column visibility
  - Collapsed split views
  - Customize a split view
- Conforms To
- Creating a navigation split view
- Hiding columns in a navigation split view
- Specifying a preferred compact column
- Specifying a preferred compact column and column visibility
- Presenting views in columns

---
title: NavigationSplitView
description: A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.
source: https://developer.apple.com/documentation/swiftui/navigationsplitview
timestamp: 2026-02-13T01:04:11.352Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.

You create a navigation split view with two or three columns, and typically use it as the root view in a [Scene](/documentation/swiftui/scene). People choose one or more items in a leading column to display details about those items in subsequent columns.

To create a two-column navigation split view, use the [init(sidebar:detail:)](/documentation/swiftui/navigationsplitview/init(sidebar:detail:)) initializer:

In the above example, the navigation split view coordinates with the [List](/documentation/swiftui/list) in its first column, so that when people make a selection, the detail view updates accordingly. Programmatic changes that you make to the selection property also affect both the list appearance and the presented detail view.

To create a three-column view, use the [init(sidebar:content:detail:)](/documentation/swiftui/navigationsplitview/init(sidebar:content:detail:)) initializer. The selection in the first column affects the second, and the selection in the second column affects the third. For example, you can show a list of departments, the list of employees in the selected department, and the details about all of the selected employees:

You can also embed a [Navigation Stack](/documentation/swiftui/navigationstack) in a column. Tapping or clicking a [Navigation Link](/documentation/swiftui/navigationlink) that appears in an earlier column sets the view that the stack displays over its root view. Activating a link in the same column adds a view to the stack. Either way, the link must present a data type for which the stack has a corresponding [navigationDestination(for:destination:)](/documentation/swiftui/view/navigationdestination(for:destination:)) modifier.

On watchOS and tvOS, and with narrow sizes like on iPhone or on iPad in Slide Over, the navigation split view collapses all of its columns into a stack, and shows the last column that displays useful information. For example, the three-column example above shows the list of departments to start, the employees in the department after someone selects a department, and the employee details when someone selects an employee. For rows in a list that have [Navigation Link](/documentation/swiftui/navigationlink) instances, the list draws disclosure chevrons while in the collapsed state.

You can programmatically control the visibility of navigation split view columns by creating a [State](/documentation/swiftui/state) value of type [Navigation Split View Visibility](/documentation/swiftui/navigationsplitviewvisibility). Then pass a [Binding](/documentation/swiftui/binding) to that state to the appropriate initializer — such as [init(columnVisibility:sidebar:detail:)](/documentation/swiftui/navigationsplitview/init(columnvisibility:sidebar:detail:)) for two columns, or the [init(columnVisibility:sidebar:content:detail:)](/documentation/swiftui/navigationsplitview/init(columnvisibility:sidebar:content:detail:)) for three columns.

The following code updates the first example above to always hide the first column when the view appears:

The split view ignores the visibility control when it collapses its columns into a stack.

At narrow size classes, such as on iPhone or Apple Watch, a navigation split view collapses into a single stack. Typically SwiftUI automatically chooses the view to show on top of this single stack, based on the content of the split view’s columns.

For custom navigation experiences, you can provide more information to help SwiftUI choose the right column. Create a `State` value of type [Navigation Split View Column](/documentation/swiftui/navigationsplitviewcolumn). Then pass a `Binding` to that state to the appropriate initializer, such as [init(preferredCompactColumn:sidebar:detail:)](/documentation/swiftui/navigationsplitview/init(preferredcompactcolumn:sidebar:detail:)) or [init(preferredCompactColumn:sidebar:content:detail:)](/documentation/swiftui/navigationsplitview/init(preferredcompactcolumn:sidebar:content:detail:)).

The following code shows the blue detail view when run on iPhone. When the person using the app taps the back button, they’ll see the yellow view. The value of `preferredPreferredCompactColumn` will change from `.detail` to `.sidebar`:

To specify a preferred column width in a navigation split view, use the [navigationSplitViewColumnWidth(_:)](/documentation/swiftui/view/navigationsplitviewcolumnwidth(_:)) modifier. To set minimum, maximum, and ideal sizes for a column, use [navigationSplitViewColumnWidth(min:ideal:max:)](/documentation/swiftui/view/navigationsplitviewcolumnwidth(min:ideal:max:)). You can specify a different modifier in each column. The navigation split view does its best to accommodate the preferences that you specify, but might make adjustments based on other constraints.

To specify how columns in a navigation split view interact, use the [navigationSplitViewStyle(_:)](/documentation/swiftui/view/navigationsplitviewstyle(_:)) modifier with a [Navigation Split View Style](/documentation/swiftui/navigationsplitviewstyle) value. For example, you can specify whether to emphasize the detail column or to give all of the columns equal prominence.

On some platforms, `NavigationSplitView` adds a [sidebar Toggle](/documentation/swiftui/toolbardefaultitemkind/sidebartoggle) toolbar item. Use the [toolbar(removing:)](/documentation/swiftui/view/toolbar(removing:)) modifier to remove the default item.

- [View](/documentation/swiftui/view)

- [init(sidebar:detail:)](/documentation/swiftui/navigationsplitview/init(sidebar:detail:)) Creates a two-column navigation split view.
- [init(sidebar:content:detail:)](/documentation/swiftui/navigationsplitview/init(sidebar:content:detail:)) Creates a three-column navigation split view.

- [init(columnVisibility:sidebar:detail:)](/documentation/swiftui/navigationsplitview/init(columnvisibility:sidebar:detail:)) Creates a two-column navigation split view that enables programmatic control of the sidebar’s visibility.
- [init(columnVisibility:sidebar:content:detail:)](/documentation/swiftui/navigationsplitview/init(columnvisibility:sidebar:content:detail:)) Creates a three-column navigation split view that enables programmatic control of leading columns’ visibility.

- [init(preferredCompactColumn:sidebar:detail:)](/documentation/swiftui/navigationsplitview/init(preferredcompactcolumn:sidebar:detail:)) Creates a two-column navigation split view that enables programmatic control over which column appears on top when the view collapses into a single column in narrow sizes.
- [init(preferredCompactColumn:sidebar:content:detail:)](/documentation/swiftui/navigationsplitview/init(preferredcompactcolumn:sidebar:content:detail:)) Creates a three-column navigation split view that enables programmatic control over which column appears on top when the view collapses into a single column in narrow sizes.

- [init(columnVisibility:preferredCompactColumn:sidebar:detail:)](/documentation/swiftui/navigationsplitview/init(columnvisibility:preferredcompactcolumn:sidebar:detail:)) Creates a two-column navigation split view that enables programmatic control of the sidebar’s visibility in regular sizes and which column appears on top when the view collapses into a single column in narrow sizes.
- [init(columnVisibility:preferredCompactColumn:sidebar:content:detail:)](/documentation/swiftui/navigationsplitview/init(columnvisibility:preferredcompactcolumn:sidebar:content:detail:)) Creates a three-column navigation split view that enables programmatic control of leading columns’ visibility in regular sizes and which column appears on top when the view collapses into a single column in narrow sizes.

- [Bringing robust navigation structure to your SwiftUI app](/documentation/swiftui/bringing-robust-navigation-structure-to-your-swiftui-app)
- [Migrating to new navigation types](/documentation/swiftui/migrating-to-new-navigation-types)
- [navigationSplitViewStyle(_:)](/documentation/swiftui/view/navigationsplitviewstyle(_:))
- [navigationSplitViewColumnWidth(_:)](/documentation/swiftui/view/navigationsplitviewcolumnwidth(_:))
- [navigationSplitViewColumnWidth(min:ideal:max:)](/documentation/swiftui/view/navigationsplitviewcolumnwidth(min:ideal:max:))
- [NavigationSplitViewVisibility](/documentation/swiftui/navigationsplitviewvisibility)
- [NavigationLink](/documentation/swiftui/navigationlink)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct NavigationSplitView<Sidebar, Content, Detail> where Sidebar : View, Content : View, Detail : View
```

Example 2 (swift):
```swift
@State private var employeeIds: Set<Employee.ID> = []

var body: some View {
    NavigationSplitView {
        List(model.employees, selection: $employeeIds) { employee in
            Text(employee.name)
        }
    } detail: {
        EmployeeDetails(for: employeeIds)
    }
}
```

Example 3 (swift):
```swift
@State private var departmentId: Department.ID? // Single selection.
@State private var employeeIds: Set<Employee.ID> = [] // Multiple selection.

var body: some View {
    NavigationSplitView {
        List(model.departments, selection: $departmentId) { department in
            Text(department.name)
        }
    } content: {
        if let department = model.department(id: departmentId) {
            List(department.employees, selection: $employeeIds) { employee in
                Text(employee.name)
            }
        } else {
            Text("Select a department")
        }
    } detail: {
        EmployeeDetails(for: employeeIds)
    }
}
```

Example 4 (swift):
```swift
@State private var employeeIds: Set<Employee.ID> = []
@State private var columnVisibility =
    NavigationSplitViewVisibility.detailOnly

var body: some View {
    NavigationSplitView(columnVisibility: $columnVisibility) {
        List(model.employees, selection: $employeeIds) { employee in
            Text(employee.name)
        }
    } detail: {
        EmployeeDetails(for: employeeIds)
    }
}
```

---
