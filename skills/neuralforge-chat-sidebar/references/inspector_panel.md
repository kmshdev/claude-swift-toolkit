# Neuralforge-Chat-Sidebar - Inspector Panel

**Pages:** 7

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
timestamp: 2026-02-13T01:42:27.146Z
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
timestamp: 2026-02-13T01:42:25.099Z
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

## safeAreaInset(edge:alignment:spacing:content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/safeareainset(edge:alignment:spacing:content:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Staying in the safe areas

---
title: safeAreaInset(edge:alignment:spacing:content:)
description: Shows the specified content beside the modified view.
source: https://developer.apple.com/documentation/swiftui/view/safeareainset(edge:alignment:spacing:content:)
timestamp: 2026-02-13T01:42:38.757Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Shows the specified content beside the modified view.

The horizontal edge of the view to inset by the width of `content`, to make space for `content`.

The alignment guide used to position `content` vertically.

Extra distance placed between the two views, or nil to use the default amount of spacing.

A view builder function providing the view to display in the inset space of the modified view.

A new view that displays `content` beside the modified view, making space for the `content` view by horizontally insetting the modified view.

The `content` view is anchored to the specified horizontal edge in the parent view, aligning its vertical axis to the specified alignment guide. The modified view is inset by the width of `content`, from `edge`, with its safe area increased by the same amount.

- [ignoresSafeArea(_:edges:)](/documentation/swiftui/view/ignoressafearea(_:edges:))
- [safeAreaPadding(_:)](/documentation/swiftui/view/safeareapadding(_:))
- [safeAreaPadding(_:_:)](/documentation/swiftui/view/safeareapadding(_:_:))
- [SafeAreaRegions](/documentation/swiftui/safearearegions)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment = .center, spacing: CGFloat? = nil, @ViewBuilder content: () -> V) -> some View where V : View
```

Example 2 (swift):
```swift
struct ScrollableViewWithSideBar: View {
    var body: some View {
        ScrollView {
            ScrolledContent()
        }
        .safeAreaInset(edge: .leading, spacing: 0) {
            SideBarContent()
        }
    }
}
```

---

## inspector(isPresented:content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/inspector(ispresented:content:)?.md

**Contents:**
- Parameters
- Discussion
- Presenting an inspector

---
title: inspector(isPresented:content:)
description: Inserts an inspector at the applied position in the view hierarchy.
source: https://developer.apple.com/documentation/swiftui/view/inspector(ispresented:content:)
timestamp: 2026-02-13T01:42:18.961Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+

> Inserts an inspector at the applied position in the view hierarchy.

A binding to `Bool` controlling the presented state.

The inspector content.

Apply this modifier to declare an inspector with a context-dependent presentation. For example, an inspector can present as a trailing column in a horizontally regular size class, but adapt to a sheet in a horizontally compact size class.

> [!NOTE]
> Trailing column inspectors have their presentation state restored by the framework.

> [!NOTE]
> [Inspector Commands](/documentation/swiftui/inspectorcommands) for including the default inspector commands and keyboard shortcuts.

- [inspectorColumnWidth(_:)](/documentation/swiftui/view/inspectorcolumnwidth(_:))
- [inspectorColumnWidth(min:ideal:max:)](/documentation/swiftui/view/inspectorcolumnwidth(min:ideal:max:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func inspector<V>(isPresented: Binding<Bool>, @ViewBuilder content: () -> V) -> some View where V : View
```

Example 2 (swift):
```swift
struct ShapeEditor: View {
    @State var presented: Bool = false
    var body: some View {
        MyEditorView()
            .inspector(isPresented: $presented) {
                TextTraitsInspectorView()
            }
    }
}
```

---

## safeAreaBar(edge:alignment:spacing:content:)

**URL:** https://sosumi.ai/documentation/swiftui/view/safeareabar(edge:alignment:spacing:content:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Configuring scroll edge effects

---
title: safeAreaBar(edge:alignment:spacing:content:)
description: Shows the specified content as a custom bar beside the modified view.
source: https://developer.apple.com/documentation/swiftui/view/safeareabar(edge:alignment:spacing:content:)
timestamp: 2026-02-13T01:42:40.745Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+

> Shows the specified content as a custom bar beside the modified view.

The horizontal edge of the view on which `content` is placed.

The alignment guide used to position `content` vertically.

Extra distance placed between the two views, or nil to use the default amount of spacing.

A view builder function providing the view to display as a custom bar.

A new view that displays `content` beside the modified view, making space for the `content` view by horizontally insetting the modified view, adjusting the safe area and scroll edge effects to match.

Similar to the [safeAreaInset(edge:alignment:spacing:content:)](/documentation/swiftui/view/safeareainset(edge:alignment:spacing:content:)-6gwby) modifier, the `content` view is anchored to the specified horizontal edge of the parent view and its width insets the safe area.

Additionally, it extends the edge effect of any scroll views affected by the inset safe area.

- [scrollEdgeEffectStyle(_:for:)](/documentation/swiftui/view/scrolledgeeffectstyle(_:for:))
- [scrollEdgeEffectHidden(_:for:)](/documentation/swiftui/view/scrolledgeeffecthidden(_:for:))
- [ScrollEdgeEffectStyle](/documentation/swiftui/scrolledgeeffectstyle)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func safeAreaBar(edge: HorizontalEdge, alignment: VerticalAlignment = .center, spacing: CGFloat? = nil, @ViewBuilder content: () -> some View) -> some View
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
timestamp: 2026-02-13T01:42:23.035Z
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
timestamp: 2026-02-13T01:42:20.926Z
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
