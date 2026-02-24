# Neuralforge-Main-Content - Adaptive Layout

**Pages:** 3

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
timestamp: 2026-02-13T03:44:03.007Z
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
timestamp: 2026-02-13T03:44:05.199Z
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
timestamp: 2026-02-13T03:44:01.013Z
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
