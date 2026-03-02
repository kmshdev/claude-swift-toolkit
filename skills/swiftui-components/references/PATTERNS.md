# Swiftui-Components - Patterns

**Pages:** 18

---

## preference(key:value:)

**URL:** https://sosumi.ai/documentation/swiftui/view/preference(key:value:)?.md

**Contents:**
- Setting preferences

---
title: preference(key:value:)
description: Sets a value for the given preference.
source: https://developer.apple.com/documentation/swiftui/view/preference(key:value:)
timestamp: 2026-02-13T19:35:55.258Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets a value for the given preference.

- [transformPreference(_:_:)](/documentation/swiftui/view/transformpreference(_:_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func preference<K>(key: K.Type = K.self, value: K.Value) -> some View where K : PreferenceKey
```

---

## ViewBuilder

**URL:** https://sosumi.ai/documentation/swiftui/viewbuilder?.md

**Contents:**
- Overview
- Building content
- Conditionally building content
- Creating a view

---
title: ViewBuilder
description: A custom parameter attribute that constructs views from closures.
source: https://developer.apple.com/documentation/swiftui/viewbuilder
timestamp: 2026-02-13T19:31:22.236Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A custom parameter attribute that constructs views from closures.

You typically use [View Builder](/documentation/swiftui/viewbuilder) as a parameter attribute for child view-producing closure parameters, allowing those closures to provide multiple child views. For example, the following `contextMenu` function accepts a closure that produces one or more views via the view builder.

Clients of this function can use multiple-statement closures to provide several child views, as shown in the following example:

- [buildBlock()](/documentation/swiftui/viewbuilder/buildblock()) Builds an empty view from a block containing no statements.
- [buildBlock(_:)](/documentation/swiftui/viewbuilder/buildblock(_:)) Passes a single view written as a child view through unmodified.
- [buildExpression(_:)](/documentation/swiftui/viewbuilder/buildexpression(_:)) Builds an expression within the builder.

- [buildEither(first:)](/documentation/swiftui/viewbuilder/buildeither(first:)) Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildEither(second:)](/documentation/swiftui/viewbuilder/buildeither(second:)) Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildIf(_:)](/documentation/swiftui/viewbuilder/buildif(_:)) Produces an optional view for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [buildLimitedAvailability(_:)](/documentation/swiftui/viewbuilder/buildlimitedavailability(_:)) Processes view content for a conditional compiler-control statement that performs an availability check.

- [Declaring a custom view](/documentation/swiftui/declaring-a-custom-view)
- [View](/documentation/swiftui/view)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@resultBuilder struct ViewBuilder
```

Example 2 (swift):
```swift
func contextMenu<MenuItems: View>(
    @ViewBuilder menuItems: () -> MenuItems
) -> some View
```

Example 3 (swift):
```swift
myView.contextMenu {
    Text("Cut")
    Text("Copy")
    Text("Paste")
    if isSymbol {
        Text("Jump to Definition")
    }
}
```

---

## AnyLayout

**URL:** https://sosumi.ai/documentation/swiftui/anylayout?.md

**Contents:**
- Overview
- Conforms To
- Creating the layout
- Transitioning between layout types

---
title: AnyLayout
description: A type-erased instance of the layout protocol.
source: https://developer.apple.com/documentation/swiftui/anylayout
timestamp: 2026-02-13T19:32:03.254Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> A type-erased instance of the layout protocol.

Use an `AnyLayout` instance to enable dynamically changing the type of a layout container without destroying the state of the subviews. For example, you can create a layout that changes between horizontal and vertical layouts based on the current Dynamic Type setting:

The types that you use with `AnyLayout` must conform to the [Layout](/documentation/swiftui/layout) protocol. The above example chooses between the [HStack Layout](/documentation/swiftui/hstacklayout) and [VStack Layout](/documentation/swiftui/vstacklayout) types, which are versions of the built-in [HStack](/documentation/swiftui/hstack) and [VStack](/documentation/swiftui/vstack) containers that conform to the protocol. You can also use custom layout types that you define.

- [Animatable](/documentation/swiftui/animatable)
- [Layout](/documentation/swiftui/layout)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [init(_:)](/documentation/swiftui/anylayout/init(_:)) Creates a type-erased value that wraps the specified layout.

- [HStackLayout](/documentation/swiftui/hstacklayout)
- [VStackLayout](/documentation/swiftui/vstacklayout)
- [ZStackLayout](/documentation/swiftui/zstacklayout)
- [GridLayout](/documentation/swiftui/gridlayout)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct AnyLayout
```

Example 2 (swift):
```swift
struct DynamicLayoutExample: View {
    @Environment(\.dynamicTypeSize) var dynamicTypeSize

    var body: some View {
        let layout = dynamicTypeSize <= .medium ?
            AnyLayout(HStackLayout()) : AnyLayout(VStackLayout())

        layout {
            Text("First label")
            Text("Second label")
        }
    }
}
```

---

## Layout

**URL:** https://sosumi.ai/documentation/swiftui/layout?.md

**Contents:**
- Overview
  - Support additional behaviors
  - Add input parameters
  - Interact with subviews through their proxies
  - Access layout values
- Inherits From
- Conforming Types
- Sizing the container and placing subviews
- Reporting layout container characteristics
- Managing a cache

---
title: Layout
description: A type that defines the geometry of a collection of views.
source: https://developer.apple.com/documentation/swiftui/layout
timestamp: 2026-02-13T19:32:05.195Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> A type that defines the geometry of a collection of views.

You traditionally arrange views in your app’s user interface using built-in layout containers like [HStack](/documentation/swiftui/hstack) and [Grid](/documentation/swiftui/grid). If you need more complex layout behavior, you can define a custom layout container by creating a type that conforms to the `Layout` protocol and implementing its required methods:

- [sizeThatFits(proposal:subviews:cache:)](/documentation/swiftui/layout/sizethatfits(proposal:subviews:cache:)) reports the size of the composite layout view.
- [placeSubviews(in:proposal:subviews:cache:)](/documentation/swiftui/layout/placesubviews(in:proposal:subviews:cache:)) assigns positions to the container’s subviews.

You can define a basic layout type with only these two methods:

Use your layout the same way you use a built-in layout container, by providing a [View Builder](/documentation/swiftui/viewbuilder) with the list of subviews to arrange:

You can optionally implement other protocol methods and properties to provide more layout container features:

- Define explicit horizontal and vertical layout guides for the container by implementing [explicitAlignment(of:in:proposal:subviews:cache:)](/documentation/swiftui/layout/explicitalignment(of:in:proposal:subviews:cache:)) for each dimension.
- Establish the preferred spacing around the container by implementing [spacing(subviews:cache:)](/documentation/swiftui/layout/spacing(subviews:cache:)).
- Indicate the axis of orientation for a container that has characteristics of a stack by implementing the [layout Properties](/documentation/swiftui/layout/layoutproperties) static property.
- Create and manage a cache to store computed values across different layout protocol calls by implementing [makeCache(subviews:)](/documentation/swiftui/layout/makecache(subviews:)).

The protocol provides default implementations for these symbols if you don’t implement them. See each method or property for details.

You can define parameters as inputs to the layout, like you might for a [View](/documentation/swiftui/view):

Set the parameters at the point where you instantiate the layout:

If the layout provides default values for its parameters, you can omit the parameters at the call site, but you might need to keep the parentheses after the name of the layout, depending on how you specify the defaults. For example, suppose you set a default alignment for the basic stack in the parameter declaration:

To instantiate this layout using the default center alignment, you don’t have to specify the alignment value, but you do need to add empty parentheses:

The Swift compiler requires the parentheses in this case because of how the layout protocol implements this call site syntax. Specifically, the layout’s [callAsFunction(_:)](/documentation/swiftui/layout/callasfunction(_:)) method looks for an initializer with exactly zero input arguments when you omit the parentheses from the call site. You can enable the simpler call site for a layout that doesn’t have an implicit initializer of this type by explicitly defining one:

For information about Swift initializers, see [Initialization.html](https://docs.swift.org/swift-book/LanguageGuide/Initialization.html) in *The Swift Programming Language*.

To perform layout, you need information about all of its subviews, which are the views that your container arranges. While your layout can’t interact directly with its subviews, it can access a set of subview proxies through the [Subviews](/documentation/swiftui/layout/subviews) collection that each protocol method receives as an input parameter. That type is an alias for the [Layout Subviews](/documentation/swiftui/layoutsubviews) collection type, which in turn contains [Layout Subview](/documentation/swiftui/layoutsubview) instances that are the subview proxies.

You can get information about each subview from its proxy, like its dimensions and spacing preferences. This enables you to measure subviews before you commit to placing them. You also assign a position to each subview by calling its proxy’s [place(at:anchor:proposal:)](/documentation/swiftui/layoutsubview/place(at:anchor:proposal:)) method. Call the method on each subview from within your implementation of the layout’s [placeSubviews(in:proposal:subviews:cache:)](/documentation/swiftui/layout/placesubviews(in:proposal:subviews:cache:)) method.

Views have layout values that you set with view modifiers. Layout containers can choose to condition their behavior accordingly. For example, a built-in [HStack](/documentation/swiftui/hstack) allocates space to its subviews based in part on the priorities that you set with the [layoutPriority(_:)](/documentation/swiftui/view/layoutpriority(_:)) view modifier. Your layout container accesses this value for a subview by reading the proxy’s [priority](/documentation/swiftui/layoutsubview/priority) property.

You can also create custom layout values by creating a layout key. Set a value on a view with the [layoutValue(key:value:)](/documentation/swiftui/view/layoutvalue(key:value:)) view modifier. Read the corresponding value from the subview’s proxy using the key as an index on the subview. For more information about creating, setting, and accessing custom layout values, see [Layout Value Key](/documentation/swiftui/layoutvaluekey).

- [Animatable](/documentation/swiftui/animatable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [AnyLayout](/documentation/swiftui/anylayout)
- [GridLayout](/documentation/swiftui/gridlayout)
- [HStackLayout](/documentation/swiftui/hstacklayout)
- [SpatialContainer](/documentation/swiftui/spatialcontainer)
- [VStackLayout](/documentation/swiftui/vstacklayout)
- [ZStackLayout](/documentation/swiftui/zstacklayout)

- [sizeThatFits(proposal:subviews:cache:)](/documentation/swiftui/layout/sizethatfits(proposal:subviews:cache:)) Returns the size of the composite view, given a proposed size and the view’s subviews.
- [placeSubviews(in:proposal:subviews:cache:)](/documentation/swiftui/layout/placesubviews(in:proposal:subviews:cache:)) Assigns positions to each of the layout’s subviews.
- [Layout.Subviews](/documentation/swiftui/layout/subviews) A collection of proxies for the subviews of a layout view.

- [explicitAlignment(of:in:proposal:subviews:cache:)](/documentation/swiftui/layout/explicitalignment(of:in:proposal:subviews:cache:)) Returns the position of the specified horizontal alignment guide along the x axis.
- [spacing(subviews:cache:)](/documentation/swiftui/layout/spacing(subviews:cache:)) Returns the preferred spacing values of the composite view.
- [layoutProperties](/documentation/swiftui/layout/layoutproperties) Properties of a layout container.

- [makeCache(subviews:)](/documentation/swiftui/layout/makecache(subviews:)) Creates and initializes a cache for a layout instance.
- [updateCache(_:subviews:)](/documentation/swiftui/layout/updatecache(_:subviews:)) Updates the layout’s cache when something changes.
- [Cache](/documentation/swiftui/layout/cache) Cached values associated with the layout instance.

- [callAsFunction(_:)](/documentation/swiftui/layout/callasfunction(_:)) Combines the specified views into a single composite view using the layout algorithms of the custom layout container.

- [depthAlignment(_:)](/documentation/swiftui/layout/depthalignment(_:)) Sets the depth alignment for this layout.
- [depthAlignment(_:content:)](/documentation/swiftui/layout/depthalignment(_:content:)) Creates a layout view with the specified depth alignment.

- [Composing custom layouts with SwiftUI](/documentation/swiftui/composing-custom-layouts-with-swiftui)
- [LayoutSubview](/documentation/swiftui/layoutsubview)
- [LayoutSubviews](/documentation/swiftui/layoutsubviews)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@preconcurrency protocol Layout : Sendable, Animatable
```

Example 2 (swift):
```swift
struct BasicVStack: Layout {
    func sizeThatFits(
        proposal: ProposedViewSize,
        subviews: Subviews,
        cache: inout ()
    ) -> CGSize {
        // Calculate and return the size of the layout container.
    }

    func placeSubviews(
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Subviews,
        cache: inout ()
    ) {
        // Tell each subview where to appear.
    }
}
```

Example 3 (swift):
```swift
BasicVStack {
    Text("A Subview")
    Text("Another Subview")
}
```

Example 4 (swift):
```swift
struct BasicVStack: Layout {
    var alignment: HorizontalAlignment

    // ...
}
```

---

## onPreferenceChange(_:perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/onpreferencechange(_:perform:)?.md

**Contents:**
- Parameters
- Return Value

---
title: onPreferenceChange(_:perform:)
description: Adds an action to perform when the specified preference key’s value changes.
source: https://developer.apple.com/documentation/swiftui/view/onpreferencechange(_:perform:)
timestamp: 2026-02-13T19:35:57.367Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds an action to perform when the specified preference key’s value changes.

The key to monitor for value changes.

The action to perform when the value for `key` changes. The `action` closure passes the new value as its parameter.

A view that triggers `action` when the value for `key` changes.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onPreferenceChange<K>(_ key: K.Type = K.self, perform action: @escaping (K.Value) -> Void) -> some View where K : PreferenceKey, K.Value : Equatable
```

---

## ControlGroup

**URL:** https://sosumi.ai/documentation/swiftui/controlgroup?.md

**Contents:**
- Overview
- Conforms To
- Creating a control group
- Creating a control group with an image
- Creating a configured control group
- Supporting types
- Presenting a group of controls

---
title: ControlGroup
description: A container view that displays semantically-related controls in a visually-appropriate manner for the context
source: https://developer.apple.com/documentation/swiftui/controlgroup
timestamp: 2026-02-13T19:32:59.052Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+

> A container view that displays semantically-related controls in a visually-appropriate manner for the context

You can provide an optional label to this view that describes its children. This view may be used in different ways depending on the surrounding context. For example, when you place the control group in a toolbar item, SwiftUI uses the label when the group is moved to the toolbar’s overflow menu.

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/controlgroup/init(content:)) Creates a new ControlGroup with the specified children
- [init(content:label:)](/documentation/swiftui/controlgroup/init(content:label:)) Creates a new control group with the specified content and a label.
- [init(_:content:)](/documentation/swiftui/controlgroup/init(_:content:)) Creates a new control group with the specified content that generates its label from a string.

- [init(_:image:content:)](/documentation/swiftui/controlgroup/init(_:image:content:)) Creates a new control group with the specified content that generates its label from a string and image name.
- [init(_:systemImage:content:)](/documentation/swiftui/controlgroup/init(_:systemimage:content:)) Creates a new control group with the specified content that generates its label from a string and image name.

- [init(_:)](/documentation/swiftui/controlgroup/init(_:)) Creates a control group based on a style configuration.

- [LabeledControlGroupContent](/documentation/swiftui/labeledcontrolgroupcontent) A view that represents the body of a control group with a specified label.

- [controlGroupStyle(_:)](/documentation/swiftui/view/controlgroupstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ControlGroup<Content> where Content : View
```

Example 2 (swift):
```swift
ContentView()
    .toolbar(id: "items") {
        ToolbarItem(id: "media") {
            ControlGroup {
                MediaButton()
                ChartButton()
                GraphButton()
            } label: {
                Label("Plus", systemImage: "plus")
            }
        }
    }
```

---

## transformPreference(_:_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/transformpreference(_:_:)?.md

**Contents:**
- Setting preferences

---
title: transformPreference(_:_:)
description: Applies a transformation to a preference value.
source: https://developer.apple.com/documentation/swiftui/view/transformpreference(_:_:)
timestamp: 2026-02-13T19:35:59.389Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Applies a transformation to a preference value.

- [preference(key:value:)](/documentation/swiftui/view/preference(key:value:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func transformPreference<K>(_ key: K.Type = K.self, _ callback: @escaping (inout K.Value) -> Void) -> some View where K : PreferenceKey
```

---

## containerRelativeFrame(_:alignment:)

**URL:** https://sosumi.ai/documentation/swiftui/view/containerrelativeframe(_:alignment:)?.md

**Contents:**
- Discussion
- Influencing a view’s size

---
title: containerRelativeFrame(_:alignment:)
description: Positions this view within an invisible frame with a size relative to the nearest container.
source: https://developer.apple.com/documentation/swiftui/view/containerrelativeframe(_:alignment:)
timestamp: 2026-02-13T19:32:09.401Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

> Positions this view within an invisible frame with a size relative to the nearest container.

Use this modifier to specify a size for a view’s width, height, or both that is dependent on the size of the nearest container. Different things can represent a “container” including:

- The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.
- A column of a NavigationSplitView
- A NavigationStack
- A tab of a TabView
- A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones listed above subtracting any safe area insets that might be applied to that container.

The following example will have each purple rectangle occupy the full size of the screen on iOS:

Use the [containerRelativeFrame(_:count:span:spacing:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:count:span:spacing:alignment:)) modifier to size a view such that multiple views will be visible in the container. When using this modifier, the count refers to the total number of rows or columns that the length of the container size in a particular axis should be divided into. The span refers to the number of rows or columns that the modified view should actually occupy. Thus the size of the element can be described like so:

The following example only uses the nearest container size in the horizontal axis, allowing the vertical axis to be determined using the [aspectRatio(_:contentMode:)](/documentation/swiftui/view/aspectratio(_:contentmode:)) modifier.

Use the [containerRelativeFrame(_:alignment:_:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:_:)) modifier to apply your own custom logic to adjust the size of the nearest container for your view. The following example will result in the container frame’s width being divided by 3 and using that value as the width of the purple rectangle.

- [frame(width:height:alignment:)](/documentation/swiftui/view/frame(width:height:alignment:))
- [frame(depth:alignment:)](/documentation/swiftui/view/frame(depth:alignment:))
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:))
- [frame(minDepth:idealDepth:maxDepth:alignment:)](/documentation/swiftui/view/frame(mindepth:idealdepth:maxdepth:alignment:))
- [containerRelativeFrame(_:alignment:_:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:_:))
- [containerRelativeFrame(_:count:span:spacing:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:count:span:spacing:alignment:))
- [fixedSize()](/documentation/swiftui/view/fixedsize())
- [fixedSize(horizontal:vertical:)](/documentation/swiftui/view/fixedsize(horizontal:vertical:))
- [layoutPriority(_:)](/documentation/swiftui/view/layoutpriority(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func containerRelativeFrame(_ axes: Axis.Set, alignment: Alignment = .center) -> some View
```

Example 2 (swift):
```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 0.0) {
        ForEach(items) { item in
            Rectangle()
                .fill(.purple)
                .containerRelativeFrame([.horizontal, .vertical])
        }
    }
}
```

Example 3 (swift):
```swift
let availableWidth = (containerWidth - (spacing * (count - 1)))
let columnWidth = (availableWidth / count)
let itemWidth = (columnWidth * span) + ((span - 1) * spacing)
```

Example 4 (swift):
```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 10.0) {
        ForEach(items) { item in
            Rectangle()
                .fill(.purple)
                .aspectRatio(3.0 / 2.0, contentMode: .fit)
                .containerRelativeFrame(
                    .horizontal, count: 4, span: 3, spacing: 10.0)
        }
    }
}
.safeAreaPadding(.horizontal, 20.0)
```

---

## groupBoxStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/groupboxstyle(_:)?.md

**Contents:**
- Parameters
- Grouping views into a box

---
title: groupBoxStyle(_:)
description: Sets the style for group boxes within this view.
source: https://developer.apple.com/documentation/swiftui/view/groupboxstyle(_:)
timestamp: 2026-02-13T19:36:13.627Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+

> Sets the style for group boxes within this view.

The style to apply to boxes within this view.

- [GroupBox](/documentation/swiftui/groupbox)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func groupBoxStyle<S>(_ style: S) -> some View where S : GroupBoxStyle
```

---

## ViewThatFits

**URL:** https://sosumi.ai/documentation/swiftui/viewthatfits?.md

**Contents:**
- Overview
- Conforms To
- Creating a view that fits

---
title: ViewThatFits
description: A view that adapts to the available space by providing the first child view that fits.
source: https://developer.apple.com/documentation/swiftui/viewthatfits
timestamp: 2026-02-13T19:32:01.333Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> A view that adapts to the available space by providing the first child view that fits.

`ViewThatFits` evaluates its child views in the order you provide them to the initializer. It selects the first child whose ideal size on the constrained axes fits within the proposed size. This means that you provide views in order of preference. Usually this order is largest to smallest, but since a view might fit along one constrained axis but not the other, this isn’t always the case. By default, `ViewThatFits` constrains in both the horizontal and vertical axes.

The following example shows an `UploadProgressView` that uses `ViewThatFits` to display the upload progress in one of three ways. In order, it attempts to display:

- An [HStack](/documentation/swiftui/hstack) that contains a [Text](/documentation/swiftui/text) view and a [Progress View](/documentation/swiftui/progressview).
- Only the `ProgressView`.
- Only the `Text` view.

The progress views are fixed to a 100-point width.

This use of `ViewThatFits` evaluates sizes only on the horizontal axis. The following code fits the `UploadProgressView` to several fixed widths:

- [View](/documentation/swiftui/view)

- [init(in:content:)](/documentation/swiftui/viewthatfits/init(in:content:)) Produces a view constrained in the given axes from one of several alternatives provided by a view builder.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct ViewThatFits<Content> where Content : View
```

Example 2 (swift):
```swift
struct UploadProgressView: View {
    var uploadProgress: Double

    var body: some View {
        ViewThatFits(in: .horizontal) {
            HStack {
                Text("\(uploadProgress.formatted(.percent))")
                ProgressView(value: uploadProgress)
                    .frame(width: 100)
            }
            ProgressView(value: uploadProgress)
                .frame(width: 100)
            Text("\(uploadProgress.formatted(.percent))")
        }
    }
}
```

Example 3 (swift):
```swift
VStack {
    UploadProgressView(uploadProgress: 0.75)
        .frame(maxWidth: 200)
    UploadProgressView(uploadProgress: 0.75)
        .frame(maxWidth: 100)
    UploadProgressView(uploadProgress: 0.75)
        .frame(maxWidth: 50)
}
```

---

## Group

**URL:** https://sosumi.ai/documentation/swiftui/group?.md

**Contents:**
- Overview
- Conforms To
- Creating a group
- Initializers
- Grouping views into a container

---
title: Group
description: A type that collects multiple instances of a content type — like views, scenes, or commands — into a single unit.
source: https://developer.apple.com/documentation/swiftui/group
timestamp: 2026-02-13T19:31:34.551Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A type that collects multiple instances of a content type — like views, scenes, or commands — into a single unit.

Use a group to collect multiple views into a single instance, without affecting the layout of those views, like an [HStack](/documentation/swiftui/hstack), [VStack](/documentation/swiftui/vstack), or [Section](/documentation/swiftui/section) would. After creating a group, any modifier you apply to the group affects all of that group’s members. For example, the following code applies the [headline](/documentation/swiftui/font/headline) font to three views in a group.

Because you create a group of views with a [View Builder](/documentation/swiftui/viewbuilder), you can use the group’s initializer to produce different kinds of views from a conditional, and then optionally apply modifiers to them. The following example uses a `Group` to add a navigation bar title, regardless of the type of view the conditional produces:

The modifier applies to all members of the group — and not to the group itself. For example, if you apply [onAppear(perform:)](/documentation/swiftui/view/onappear(perform:)) to the above group, it applies to all of the views produced by the `if isLoggedIn` conditional, and it executes every time `isLoggedIn` changes.

Because a group of views itself is a view, you can compose a group within other view builders, including nesting within other groups. This allows you to add large numbers of views to different view builder containers. The following example uses a `Group` to collect 10 [Text](/documentation/swiftui/text) instances, meaning that the vertical stack’s view builder returns only two views — the group, plus an additional [Text](/documentation/swiftui/text):

You can initialize groups with several types other than [View](/documentation/swiftui/view), such as [Scene](/documentation/swiftui/scene) and [Toolbar Content](/documentation/swiftui/toolbarcontent). The closure you provide to the group initializer uses the corresponding builder type ([Scene Builder](/documentation/swiftui/scenebuilder), [Toolbar Content Builder](/documentation/swiftui/toolbarcontentbuilder), and so on), and the capabilities of these builders vary between types. For example, you can use groups to return large numbers of scenes or toolbar content instances, but not to return different scenes or toolbar content based on conditionals.

- [AccessibilityRotorContent](/documentation/swiftui/accessibilityrotorcontent)
- [Commands](/documentation/swiftui/commands)
- [Copyable](/documentation/Swift/Copyable)
- [CustomizableToolbarContent](/documentation/swiftui/customizabletoolbarcontent)
- [MapContent](/documentation/MapKit/MapContent)
- [Scene](/documentation/swiftui/scene)
- [TabContent](/documentation/swiftui/tabcontent)
- [TableColumnContent](/documentation/swiftui/tablecolumncontent)
- [TableRowContent](/documentation/swiftui/tablerowcontent)
- [ToolbarContent](/documentation/swiftui/toolbarcontent)
- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/group/init(content:)) Creates an instance that generates Rotor content by combining, in order, all the Rotor content specified in the passed-in result builder.

- [init(sections:transform:)](/documentation/swiftui/group/init(sections:transform:)) Constructs a group from the sections of the given view.
- [init(subviews:transform:)](/documentation/swiftui/group/init(subviews:transform:)) Constructs a group from the subviews of the given view.

- [Creating custom container views](/documentation/swiftui/creating-custom-container-views)
- [GroupElementsOfContent](/documentation/swiftui/groupelementsofcontent)
- [GroupSectionsOfContent](/documentation/swiftui/groupsectionsofcontent)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Group<Content>
```

Example 2 (swift):
```swift
Group {
    Text("SwiftUI")
    Text("Combine")
    Text("Swift System")
}
.font(.headline)
```

Example 3 (swift):
```swift
Group {
    if isLoggedIn {
        WelcomeView()
    } else {
        LoginView()
    }
}
.navigationBarTitle("Start")
```

Example 4 (swift):
```swift
var body: some View {
    VStack {
        Group {
            Text("1")
            Text("2")
            Text("3")
            Text("4")
            Text("5")
            Text("6")
            Text("7")
            Text("8")
            Text("9")
            Text("10")
        }
        Text("11")
    }
}
```

---

## ViewModifier

**URL:** https://sosumi.ai/documentation/swiftui/viewmodifier?.md

**Contents:**
- Overview
- Inherited By
- Conforming Types
- Creating a view modifier
- Adding animations to a view
- Handling view taps and gestures
- Modifying a view

---
title: ViewModifier
description: A modifier that you apply to a view or another view modifier, producing a different version of the original value.
source: https://developer.apple.com/documentation/swiftui/viewmodifier
timestamp: 2026-02-13T19:31:20.271Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A modifier that you apply to a view or another view modifier, producing a different version of the original value.

Adopt the [View Modifier](/documentation/swiftui/viewmodifier) protocol when you want to create a reusable modifier that you can apply to any view. The example below combines several modifiers to create a new modifier that you can use to create blue caption text surrounded by a rounded rectangle:

You can apply [modifier(_:)](/documentation/swiftui/view/modifier(_:)) directly to a view, but a more common and idiomatic approach uses [modifier(_:)](/documentation/swiftui/view/modifier(_:)) to define an extension to [View](/documentation/swiftui/view) itself that incorporates the view modifier:

You can then apply the bordered caption to any view, similar to this:

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

- [AnimatableModifier](/documentation/swiftui/animatablemodifier)
- [EnvironmentalModifier](/documentation/swiftui/environmentalmodifier)
- [GeometryEffect](/documentation/swiftui/geometryeffect)

- [AccessibilityAttachmentModifier](/documentation/swiftui/accessibilityattachmentmodifier)
- [EmptyModifier](/documentation/swiftui/emptymodifier)
- [LayoutRotationUnaryLayout](/documentation/swiftui/layoutrotationunarylayout)
- [ManipulableModifier](/documentation/swiftui/manipulablemodifier)
- [ManipulableResponderModifier](/documentation/swiftui/manipulablerespondermodifier)
- [ManipulableTransformBindingModifier](/documentation/swiftui/manipulabletransformbindingmodifier)
- [ManipulationGeometryModifier](/documentation/swiftui/manipulationgeometrymodifier)
- [ManipulationGestureModifier](/documentation/swiftui/manipulationgesturemodifier)
- [ManipulationUsingGestureStateModifier](/documentation/swiftui/manipulationusinggesturestatemodifier)
- [ModifiedContent](/documentation/swiftui/modifiedcontent)

- [body(content:)](/documentation/swiftui/viewmodifier/body(content:)) Gets the current body of the caller.
- [Body](/documentation/swiftui/viewmodifier/body) The type of view representing the body.
- [ViewModifier.Content](/documentation/swiftui/viewmodifier/content) The content view type passed to .

- [animation(_:)](/documentation/swiftui/viewmodifier/animation(_:)) Returns a new version of the modifier that will apply  to all animatable values within the modifier.
- [concat(_:)](/documentation/swiftui/viewmodifier/concat(_:)) Returns a new modifier that is the result of concatenating  with .

- [transaction(_:)](/documentation/swiftui/viewmodifier/transaction(_:)) Returns a new version of the modifier that will apply the transaction mutation function  to all transactions within the modifier.

- [Configuring views](/documentation/swiftui/configuring-views)
- [Reducing view modifier maintenance](/documentation/swiftui/reducing-view-modifier-maintenance)
- [modifier(_:)](/documentation/swiftui/view/modifier(_:))
- [EmptyModifier](/documentation/swiftui/emptymodifier)
- [ModifiedContent](/documentation/swiftui/modifiedcontent)
- [EnvironmentalModifier](/documentation/swiftui/environmentalmodifier)
- [ManipulableModifier](/documentation/swiftui/manipulablemodifier)
- [ManipulableResponderModifier](/documentation/swiftui/manipulablerespondermodifier)
- [ManipulableTransformBindingModifier](/documentation/swiftui/manipulabletransformbindingmodifier)
- [ManipulationGeometryModifier](/documentation/swiftui/manipulationgeometrymodifier)
- [ManipulationGestureModifier](/documentation/swiftui/manipulationgesturemodifier)
- [ManipulationUsingGestureStateModifier](/documentation/swiftui/manipulationusinggesturestatemodifier)
- [Manipulable](/documentation/swiftui/manipulable)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency protocol ViewModifier
```

Example 2 (swift):
```swift
struct BorderedCaption: ViewModifier {
    func body(content: Content) -> some View {
        content
            .font(.caption2)
            .padding(10)
            .overlay(
                RoundedRectangle(cornerRadius: 15)
                    .stroke(lineWidth: 1)
            )
            .foregroundColor(Color.blue)
    }
}
```

Example 3 (swift):
```swift
extension View {
    func borderedCaption() -> some View {
        modifier(BorderedCaption())
    }
}
```

Example 4 (swift):
```swift
Image(systemName: "bus")
    .resizable()
    .frame(width:50, height:50)
Text("Downtown Bus")
    .borderedCaption()
```

---

## GroupBox

**URL:** https://sosumi.ai/documentation/swiftui/groupbox?.md

**Contents:**
- Overview
- Conforms To
- Creating a group box
- Creating a group box from a configuration
- Deprecated initializers
- Grouping views into a box

---
title: GroupBox
description: A stylized view, with an optional label, that visually collects a logical grouping of content.
source: https://developer.apple.com/documentation/swiftui/groupbox
timestamp: 2026-02-13T19:33:03.413Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, visionOS 1.0+

> A stylized view, with an optional label, that visually collects a logical grouping of content.

Use a group box when you want to visually distinguish a portion of your user interface with an optional title for the boxed content.

The following example sets up a `GroupBox` with the label “End-User Agreement”, and a long `agreementText` string in a [Text](/documentation/swiftui/text) view wrapped by a [Scroll View](/documentation/swiftui/scrollview). The box also contains a [Toggle](/documentation/swiftui/toggle) for the user to interact with after reading the text.

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/groupbox/init(content:)) Creates an unlabeled group box with the provided view content.
- [init(content:label:)](/documentation/swiftui/groupbox/init(content:label:)) Creates a group box with the provided label and view content.
- [init(_:content:)](/documentation/swiftui/groupbox/init(_:content:)) Creates a group box with the provided view content and title.

- [init(_:)](/documentation/swiftui/groupbox/init(_:)) Creates a group box based on a style configuration.

- [init(label:content:)](/documentation/swiftui/groupbox/init(label:content:))

- [groupBoxStyle(_:)](/documentation/swiftui/view/groupboxstyle(_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct GroupBox<Label, Content> where Label : View, Content : View
```

Example 2 (swift):
```swift
var body: some View {
    GroupBox(label:
        Label("End-User Agreement", systemImage: "building.columns")
    ) {
        ScrollView(.vertical, showsIndicators: true) {
            Text(agreementText)
                .font(.footnote)
        }
        .frame(height: 100)
        Toggle(isOn: $userAgreed) {
            Text("I agree to the above terms")
        }
    }
}
```

---

## EmptyModifier

**URL:** https://sosumi.ai/documentation/swiftui/emptymodifier?.md

**Contents:**
- Overview
- Conforms To
- Creating an empty modifier
- Getting the identity modifier
- Modifying a view

---
title: EmptyModifier
description: An empty, or identity, modifier, used during development to switch modifiers at compile time.
source: https://developer.apple.com/documentation/swiftui/emptymodifier
timestamp: 2026-02-13T19:31:26.359Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> An empty, or identity, modifier, used during development to switch modifiers at compile time.

Use the empty modifier to switch modifiers at compile time during development. In the example below, in a debug build the [Text](/documentation/swiftui/text) view inside `ContentView` has a yellow background and a red border. A non-debug build reflects the default system, or container supplied appearance.

- [BitwiseCopyable](/documentation/Swift/BitwiseCopyable)
- [Copyable](/documentation/Swift/Copyable)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)
- [ViewModifier](/documentation/swiftui/viewmodifier)

- [init()](/documentation/swiftui/emptymodifier/init())

- [identity](/documentation/swiftui/emptymodifier/identity)

- [Configuring views](/documentation/swiftui/configuring-views)
- [Reducing view modifier maintenance](/documentation/swiftui/reducing-view-modifier-maintenance)
- [modifier(_:)](/documentation/swiftui/view/modifier(_:))
- [ViewModifier](/documentation/swiftui/viewmodifier)
- [ModifiedContent](/documentation/swiftui/modifiedcontent)
- [EnvironmentalModifier](/documentation/swiftui/environmentalmodifier)
- [ManipulableModifier](/documentation/swiftui/manipulablemodifier)
- [ManipulableResponderModifier](/documentation/swiftui/manipulablerespondermodifier)
- [ManipulableTransformBindingModifier](/documentation/swiftui/manipulabletransformbindingmodifier)
- [ManipulationGeometryModifier](/documentation/swiftui/manipulationgeometrymodifier)
- [ManipulationGestureModifier](/documentation/swiftui/manipulationgesturemodifier)
- [ManipulationUsingGestureStateModifier](/documentation/swiftui/manipulationusinggesturestatemodifier)
- [Manipulable](/documentation/swiftui/manipulable)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct EmptyModifier
```

Example 2 (swift):
```swift
struct EmphasizedLayout: ViewModifier {
    func body(content: Content) -> some View {
        content
            .background(Color.yellow)
            .border(Color.red)
    }
}

struct ContentView: View {
    var body: some View {
        Text("Hello, World!")
            .modifier(modifier)
    }

    var modifier: some ViewModifier {
        #if DEBUG
            return EmphasizedLayout()
        #else
            return EmptyModifier()
        #endif
    }
}
```

---

## layoutPriority(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/layoutpriority(_:)?.md

**Contents:**
- Parameters
- Discussion
- Influencing a view’s size

---
title: layoutPriority(_:)
description: Sets the priority by which a parent layout should apportion space to this child.
source: https://developer.apple.com/documentation/swiftui/view/layoutpriority(_:)
timestamp: 2026-02-13T19:32:13.211Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Sets the priority by which a parent layout should apportion space to this child.

The priority by which a parent layout apportions space to the child.

Views typically have a default priority of `0` which causes space to be apportioned evenly to all sibling views. Raising a view’s layout priority encourages the higher priority view to shrink later when the group is shrunk and stretch sooner when the group is stretched.

In the example above, the first [Text](/documentation/swiftui/text) element has the default priority `0` which causes its view to shrink dramatically due to the higher priority of the second [Text](/documentation/swiftui/text) element, even though all of their other attributes (font, font size and character count) are the same.

A parent layout offers the child views with the highest layout priority all the space offered to the parent minus the minimum space required for all its lower-priority children.

- [frame(width:height:alignment:)](/documentation/swiftui/view/frame(width:height:alignment:))
- [frame(depth:alignment:)](/documentation/swiftui/view/frame(depth:alignment:))
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](/documentation/swiftui/view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:))
- [frame(minDepth:idealDepth:maxDepth:alignment:)](/documentation/swiftui/view/frame(mindepth:idealdepth:maxdepth:alignment:))
- [containerRelativeFrame(_:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:))
- [containerRelativeFrame(_:alignment:_:)](/documentation/swiftui/view/containerrelativeframe(_:alignment:_:))
- [containerRelativeFrame(_:count:span:spacing:alignment:)](/documentation/swiftui/view/containerrelativeframe(_:count:span:spacing:alignment:))
- [fixedSize()](/documentation/swiftui/view/fixedsize())
- [fixedSize(horizontal:vertical:)](/documentation/swiftui/view/fixedsize(horizontal:vertical:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func layoutPriority(_ value: Double) -> some View
```

Example 2 (swift):
```swift
HStack {
    Text("This is a moderately long string.")
        .font(.largeTitle)
        .border(Color.gray)

    Spacer()

    Text("This is a higher priority string.")
        .font(.largeTitle)
        .layoutPriority(1)
        .border(Color.gray)
}
```

---

## modifier(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/modifier(_:)?.md

**Contents:**
- Parameters
- Discussion
- Modifying a view

---
title: modifier(_:)
description: Applies a modifier to a view and returns a new view.
source: https://developer.apple.com/documentation/swiftui/view/modifier(_:)
timestamp: 2026-02-13T19:31:24.320Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Applies a modifier to a view and returns a new view.

The modifier to apply to this view.

Use this modifier to combine a [View](/documentation/swiftui/view) and a [View Modifier](/documentation/swiftui/viewmodifier), to create a new view. For example, if you create a view modifier for a new kind of caption with blue text surrounded by a rounded rectangle:

You can use [modifier(_:)](/documentation/swiftui/view/modifier(_:)) to extend [View](/documentation/swiftui/view) to create new modifier for applying the `BorderedCaption` defined above:

Then you can apply the bordered caption to any view:

- [Configuring views](/documentation/swiftui/configuring-views)
- [Reducing view modifier maintenance](/documentation/swiftui/reducing-view-modifier-maintenance)
- [ViewModifier](/documentation/swiftui/viewmodifier)
- [EmptyModifier](/documentation/swiftui/emptymodifier)
- [ModifiedContent](/documentation/swiftui/modifiedcontent)
- [EnvironmentalModifier](/documentation/swiftui/environmentalmodifier)
- [ManipulableModifier](/documentation/swiftui/manipulablemodifier)
- [ManipulableResponderModifier](/documentation/swiftui/manipulablerespondermodifier)
- [ManipulableTransformBindingModifier](/documentation/swiftui/manipulabletransformbindingmodifier)
- [ManipulationGeometryModifier](/documentation/swiftui/manipulationgeometrymodifier)
- [ManipulationGestureModifier](/documentation/swiftui/manipulationgesturemodifier)
- [ManipulationUsingGestureStateModifier](/documentation/swiftui/manipulationusinggesturestatemodifier)
- [Manipulable](/documentation/swiftui/manipulable)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func modifier<T>(_ modifier: T) -> ModifiedContent<Self, T>
```

Example 2 (swift):
```swift
struct BorderedCaption: ViewModifier {
    func body(content: Content) -> some View {
        content
            .font(.caption2)
            .padding(10)
            .overlay(
                RoundedRectangle(cornerRadius: 15)
                    .stroke(lineWidth: 1)
            )
            .foregroundColor(Color.blue)
    }
}
```

Example 3 (swift):
```swift
extension View {
    func borderedCaption() -> some View {
        modifier(BorderedCaption())
    }
}
```

Example 4 (swift):
```swift
Image(systemName: "bus")
    .resizable()
    .frame(width:50, height:50)
Text("Downtown Bus")
    .borderedCaption()
```

---

## PreferenceKey

**URL:** https://sosumi.ai/documentation/swiftui/preferencekey?.md

**Contents:**
- Overview
- Conforming Types
- Getting the default value
- Combining preferences

---
title: PreferenceKey
description: A named value produced by a view.
source: https://developer.apple.com/documentation/swiftui/preferencekey
timestamp: 2026-02-13T19:35:53.222Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A named value produced by a view.

A view with multiple children automatically combines its values for a given preference into a single value visible to its ancestors.

- [PreferredColorSchemeKey](/documentation/swiftui/preferredcolorschemekey)
- [Text.LayoutKey](/documentation/swiftui/text/layoutkey)

- [defaultValue](/documentation/swiftui/preferencekey/defaultvalue) The default value of the preference.
- [Value](/documentation/swiftui/preferencekey/value) The type of value produced by this preference.

- [reduce(value:nextValue:)](/documentation/swiftui/preferencekey/reduce(value:nextvalue:)) Combines a sequence of values by modifying the previously-accumulated value with the result of a closure that provides the next value.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol PreferenceKey
```

---

## EquatableView

**URL:** https://sosumi.ai/documentation/swiftui/equatableview?.md

**Contents:**
- Conforms To
- Creating an equatable view
- Supporting view types

---
title: EquatableView
description: A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
source: https://developer.apple.com/documentation/swiftui/equatableview
timestamp: 2026-02-13T19:31:28.271Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.

- [View](/documentation/swiftui/view)

- [init(content:)](/documentation/swiftui/equatableview/init(content:))
- [content](/documentation/swiftui/equatableview/content)

- [AnyView](/documentation/swiftui/anyview)
- [EmptyView](/documentation/swiftui/emptyview)
- [SubscriptionView](/documentation/swiftui/subscriptionview)
- [TupleView](/documentation/swiftui/tupleview)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct EquatableView<Content> where Content : Equatable, Content : View
```

---
