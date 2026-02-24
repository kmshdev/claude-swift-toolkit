# Neuralforge-Top-Navbar - Tab Animations

**Pages:** 4

---

## contentTransition(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/contenttransition(_:)?.md

**Contents:**
- Parameters
- Discussion
- Defining transitions

---
title: contentTransition(_:)
description: Modifies the view to use a given transition as its method of animating changes to the contents of its views.
source: https://developer.apple.com/documentation/swiftui/view/contenttransition(_:)
timestamp: 2026-02-13T03:56:09.805Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

> Modifies the view to use a given transition as its method of animating changes to the contents of its views.

The transition to apply when animating the content change.

This modifier allows you to perform a transition that animates a change within a single view. The provided [Content Transition](/documentation/swiftui/contenttransition) can present an opacity animation for content changes, an interpolated animation of the content’s paths as they change, or perform no animation at all.

> [!TIP]
> The `contentTransition(_:)` modifier only has an effect within the context of an [Animation](/documentation/swiftui/animation).

In the following example, a [Button](/documentation/swiftui/button) changes the color and font size of a [Text](/documentation/swiftui/text) view. Since both of these properties apply to the paths of the text, the [interpolate](/documentation/swiftui/contenttransition/interpolate) transition can animate a gradual change to these properties through the entire transition. By contrast, the [opacity](/documentation/swiftui/contenttransition/opacity) transition would simply fade between the start and end states.

This example uses an ease-in–ease-out animation with a five-second duration to make it easier to see the effect of the interpolation. The figure below shows the `Text` at the beginning of the animation, halfway through, and at the end.

| Time | Display |
| --- | --- |
| Start |  |
| Middle |  |
| End |  |

To control whether content transitions use GPU-accelerated rendering, set the value of the [content Transition Adds Drawing Group](/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup) environment variable.

- [transition(_:)](/documentation/swiftui/view/transition(_:))
- [Transition](/documentation/swiftui/transition)
- [TransitionProperties](/documentation/swiftui/transitionproperties)
- [TransitionPhase](/documentation/swiftui/transitionphase)
- [AsymmetricTransition](/documentation/swiftui/asymmetrictransition)
- [AnyTransition](/documentation/swiftui/anytransition)
- [contentTransition](/documentation/swiftui/environmentvalues/contenttransition)
- [contentTransitionAddsDrawingGroup](/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup)
- [ContentTransition](/documentation/swiftui/contenttransition)
- [PlaceholderContentView](/documentation/swiftui/placeholdercontentview)
- [navigationTransition(_:)](/documentation/swiftui/view/navigationtransition(_:))
- [NavigationTransition](/documentation/swiftui/navigationtransition)
- [matchedTransitionSource(id:in:)](/documentation/swiftui/view/matchedtransitionsource(id:in:))
- [matchedTransitionSource(id:in:configuration:)](/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:))
- [MatchedTransitionSourceConfiguration](/documentation/swiftui/matchedtransitionsourceconfiguration)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func contentTransition(_ transition: ContentTransition) -> some View
```

Example 2 (swift):
```swift
private static let font1 = Font.system(size: 20)
private static let font2 = Font.system(size: 45)

@State private var color = Color.red
@State private var currentFont = font1

var body: some View {
    VStack {
        Text("Content transition")
            .foregroundColor(color)
            .font(currentFont)
            .contentTransition(.interpolate)
        Spacer()
        Button("Change") {
            withAnimation(Animation.easeInOut(duration: 5.0)) {
                color = (color == .red) ? .green : .red
                currentFont = (currentFont == font1) ? font2 : font1
            }
        }
    }
}
```

---

## Namespace

**URL:** https://sosumi.ai/documentation/swiftui/namespace?.md

**Contents:**
- Conforms To
- Creating a namespace
- Getting the namespace
- Synchronizing geometries

---
title: Namespace
description: A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
source: https://developer.apple.com/documentation/swiftui/namespace
timestamp: 2026-02-13T03:56:16.158Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).

- [BitwiseCopyable](/documentation/Swift/BitwiseCopyable)
- [Copyable](/documentation/Swift/Copyable)
- [DynamicProperty](/documentation/swiftui/dynamicproperty)
- [Sendable](/documentation/Swift/Sendable)
- [SendableMetatype](/documentation/Swift/SendableMetatype)

- [init()](/documentation/swiftui/namespace/init())

- [wrappedValue](/documentation/swiftui/namespace/wrappedvalue)
- [Namespace.ID](/documentation/swiftui/namespace/id) A namespace defined by the persistent identity of an  dynamic property.

- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:))
- [MatchedGeometryProperties](/documentation/swiftui/matchedgeometryproperties)
- [GeometryEffect](/documentation/swiftui/geometryeffect)
- [geometryGroup()](/documentation/swiftui/view/geometrygroup())

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen @propertyWrapper struct Namespace
```

---

## animation(_:value:)

**URL:** https://sosumi.ai/documentation/swiftui/view/animation(_:value:)?.md

**Contents:**
- Parameters
- Return Value
- Adding state-based animation to a view

---
title: animation(_:value:)
description: Applies the given animation to this view when the specified value changes.
source: https://developer.apple.com/documentation/swiftui/view/animation(_:value:)
timestamp: 2026-02-13T03:56:12.059Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Applies the given animation to this view when the specified value changes.

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

A value to monitor for changes.

A view that applies `animation` to this view whenever `value` changes.

- [animation(_:)](/documentation/swiftui/view/animation(_:))
- [animation(_:body:)](/documentation/swiftui/view/animation(_:body:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func animation<V>(_ animation: Animation?, value: V) -> some View where V : Equatable
```

---

## matchedGeometryEffect(id:in:properties:anchor:isSource:)

**URL:** https://sosumi.ai/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Synchronizing geometries

---
title: matchedGeometryEffect(id:in:properties:anchor:isSource:)
description: Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
source: https://developer.apple.com/documentation/swiftui/view/matchedgeometryeffect(id:in:properties:anchor:issource:)
timestamp: 2026-02-13T03:56:14.185Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Defines a group of views with synchronized geometry using an identifier and namespace that you provide.

The identifier, often derived from the identifier of the data being displayed by the view.

The namespace in which defines the `id`. New namespaces are created by adding an `@Namespace` variable to a [View](/documentation/swiftui/view) type and reading its value in the view’s body method.

The properties to copy from the source view.

The relative location in the view used to produce its shared position value.

True if the view should be used as the source of geometry for other views in the group.

A new view that defines an entry in the global database of views synchronizing their geometry.

This method sets the geometry of each view in the group from the inserted view with `isSource = true` (known as the “source” view), updating the values marked by `properties`.

If inserting a view in the same transaction that another view with the same key is removed, the system will interpolate their frame rectangles in window space to make it appear that there is a single view moving from its old position to its new position. The usual transition mechanisms define how each of the two views is rendered during the transition (e.g. fade in/out, scale, etc), the `matchedGeometryEffect()` modifier only arranges for the geometry of the views to be linked, not their rendering.

If the number of currently-inserted views in the group with `isSource = true` is not exactly one results are undefined, due to it not being clear which is the source view.

- [MatchedGeometryProperties](/documentation/swiftui/matchedgeometryproperties)
- [GeometryEffect](/documentation/swiftui/geometryeffect)
- [Namespace](/documentation/swiftui/namespace)
- [geometryGroup()](/documentation/swiftui/view/geometrygroup())

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func matchedGeometryEffect<ID>(id: ID, in namespace: Namespace.ID, properties: MatchedGeometryProperties = .frame, anchor: UnitPoint = .center, isSource: Bool = true) -> some View where ID : Hashable
```

---
