# Swiftui-Animations - Geometry Synchronization

**Pages:** 5

---

## GeometryEffect

**URL:** https://sosumi.ai/documentation/swiftui/geometryeffect?.md

**Contents:**
- Overview
- Inherits From
- Applying effects
- Synchronizing geometries

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

The only change the effect makes to the view’s ancestors and descendants is to change the coordinate transform to and from them.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol GeometryEffect : Animatable, ViewModifier, _RemoveGlobalActorIsolation where Self.Body == Never
```

---

## MatchedGeometryProperties

**URL:** https://sosumi.ai/documentation/swiftui/matchedgeometryproperties?.md

**Contents:**
- Conforms To
- Matching properties
- Synchronizing geometries

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct MatchedGeometryProperties
```

---

## Namespace

**URL:** https://sosumi.ai/documentation/swiftui/namespace?.md

**Contents:**
- Conforms To
- Creating a namespace
- Getting the namespace
- Synchronizing geometries

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen @propertyWrapper struct Namespace
```

---

## matchedGeometryEffect(id:in:properties:anchor:isSource:)

**URL:** https://sosumi.ai/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Synchronizing geometries

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

The identifier, often derived from the identifier of the data being displayed by the view.

The namespace in which defines the `id`. New namespaces are created by adding an `@Namespace` variable to a [View](/documentation/swiftui/view) type and reading its value in the view’s body method.

The properties to copy from the source view.

The relative location in the view used to produce its shared position value.

True if the view should be used as the source of geometry for other views in the group.

A new view that defines an entry in the global database of views synchronizing their geometry.

This method sets the geometry of each view in the group from the inserted view with `isSource = true` (known as the “source” view), updating the values marked by `properties`.

If inserting a view in the same transaction that another view with the same key is removed, the system will interpolate their frame rectangles in window space to make it appear that there is a single view moving from its old position to its new position. The usual transition mechanisms define how each of the two views is rendered during the transition (e.g. fade in/out, scale, etc), the `matchedGeometryEffect()` modifier only arranges for the geometry of the views to be linked, not their rendering.

If the number of currently-inserted views in the group with `isSource = true` is not exactly one results are undefined, due to it not being clear which is the source view.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func matchedGeometryEffect<ID>(id: ID, in namespace: Namespace.ID, properties: MatchedGeometryProperties = .frame, anchor: UnitPoint = .center, isSource: Bool = true) -> some View where ID : Hashable
```

---

## geometryGroup()

**URL:** https://sosumi.ai/documentation/swiftui/view/geometrygroup()?.md

**Contents:**
- Discussion
- Synchronizing geometries

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

By default SwiftUI views push position and size changes down through the view hierarchy, so that only views that draw something (known as leaf views) apply the current animation to their frame rectangle. However in some cases this coalescing behavior can give undesirable results; inserting a geometry group can correct that. A group acts as a barrier between the parent view and its subviews, forcing the position and size values to be resolved and animated by the parent, before being passed down to each subview.

The example below shows one use of this function: ensuring that the member views of each row in the stack apply (and animate as) a single geometric transform from their ancestor view, rather than letting the effects of the ancestor views be applied separately to each leaf view. If the members of `ItemView` may be added and removed at different times the group ensures that they stay locked together as animations are applied.

Returns: a new view whose geometry is isolated from that of its parent view.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func geometryGroup() -> some View
```

Example 2 (swift):
```swift
VStack {
    ForEach(items) { item in
        ItemView(item: item)
            .geometryGroup()
    }
}
```

---
