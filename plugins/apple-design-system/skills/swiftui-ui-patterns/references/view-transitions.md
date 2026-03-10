# Swiftui-Animations - View Transitions

**Pages:** 13

---

## Transition

**URL:** https://sosumi.ai/documentation/swiftui/transition?.md

**Contents:**
- Overview
- Conforming Types
- Getting built-in transitions
- Configuring a transition
- Using a transition
- Creating a custom transition
- Supporting types
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

A transition should generally be made by applying one or more modifiers to the `content`. For symmetric transitions, the `isIdentity` property on `phase` can be used to change the properties of modifiers. For asymmetric transitions, the phase itself can be used to change those properties. Transitions should not use any identity-affecting changes like `.id`, `if`, and `switch` on the `content`, since doing so would reset the state of the view they’re applied to, causing wasted work and potentially surprising behavior when it appears and disappears.

The following code defines a transition that can be used to change the opacity and rotation when a view appears and disappears.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@MainActor @preconcurrency protocol Transition
```

Example 2 (swift):
```swift
struct RotatingFadeTransition: Transition {
    func body(content: Content, phase: TransitionPhase) -> some View {
        content
          .opacity(phase.isIdentity ? 1.0 : 0.0)
          .rotationEffect(phase.rotation)
    }
}
extension TransitionPhase {
    fileprivate var rotation: Angle {
        switch self {
        case .willAppear: return .degrees(30)
        case .identity: return .zero
        case .didDisappear: return .degrees(-30)
        }
    }
}
```

Example 3 (swift):
```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Example 4 (swift):
```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

---

## TransitionProperties

**URL:** https://sosumi.ai/documentation/swiftui/transitionproperties?.md

**Contents:**
- Overview
- Conforms To
- Creating the transition properties
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

A transition can have properties that specify high level information about it. This can determine how a transition interacts with other features like Accessibility settings.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct TransitionProperties
```

---

## matchedTransitionSource(id:in:configuration:)

**URL:** https://sosumi.ai/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:)?.md

**Contents:**
- Parameters
- Discussion
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

The identifier, often derived from the identifier of the data being displayed by the view.

The namespace in which defines the `id`. New namespaces are created by adding an [Namespace](/documentation/swiftui/namespace) variable to a [View](/documentation/swiftui/view) type and reading its value in the view’s body method.

A closure that you can use to apply styling to the source.

The appearance of the source can be configured using the `configuration` trailing closure. Any modifiers applied will be smoothly interpolated when a zoom transition originates from this matched transition source.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func matchedTransitionSource(id: some Hashable, in namespace: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View
```

Example 2 (swift):
```swift
MyView()
    .matchedTransitionSource(id: someID, in: someNamespace) { source in
        source
            .cornerRadius(8.0)
    }
```

---

## MatchedTransitionSourceConfiguration

**URL:** https://sosumi.ai/documentation/swiftui/matchedtransitionsourceconfiguration?.md

**Contents:**
- Inherits From
- Conforming Types
- Instance Methods
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol MatchedTransitionSourceConfiguration : Sendable
```

---

## contentTransition(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/contenttransition(_:)?.md

**Contents:**
- Parameters
- Discussion
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

The transition to apply when animating the content change.

This modifier allows you to perform a transition that animates a change within a single view. The provided [Content Transition](/documentation/swiftui/contenttransition) can present an opacity animation for content changes, an interpolated animation of the content’s paths as they change, or perform no animation at all.

In the following example, a [Button](/documentation/swiftui/button) changes the color and font size of a [Text](/documentation/swiftui/text) view. Since both of these properties apply to the paths of the text, the [interpolate](/documentation/swiftui/contenttransition/interpolate) transition can animate a gradual change to these properties through the entire transition. By contrast, the [opacity](/documentation/swiftui/contenttransition/opacity) transition would simply fade between the start and end states.

This example uses an ease-in–ease-out animation with a five-second duration to make it easier to see the effect of the interpolation. The figure below shows the `Text` at the beginning of the animation, halfway through, and at the end.

| Time | Display | | --- | --- | | Start | ![The text Content transition in a small red font.](https://docs-assets.developer.apple.com/published/eba2db780339b6fbbd97763e652ad3b2/ContentTransition-1%402x.png) | | Middle | ![The text Content transition in a medium brown font.](https://docs-assets.developer.apple.com/published/746174d6317e87efbfe56c78d5e18a17/ContentTransition-2%402x.png) | | End | ![The text Content transition in a large green font.](https://docs-assets.developer.apple.com/published/534b62d2cd433733bbf2df631ad7fb5c/ContentTransition-3%402x.png) |

To control whether content transitions use GPU-accelerated rendering, set the value of the [content Transition Adds Drawing Group](/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup) environment variable.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

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

## AsymmetricTransition

**URL:** https://sosumi.ai/documentation/swiftui/asymmetrictransition?.md

**Contents:**
- Conforms To
- Creating the transition
- Getting transition properties
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct AsymmetricTransition<Insertion, Removal> where Insertion : Transition, Removal : Transition
```

---

## transition(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/transition(_:)?.md

**Contents:**
- Discussion
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

When this view appears or disappears, the transition will be applied to it, allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or disappears, will use a slide transition to show it.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func transition(_ t: AnyTransition) -> some View
```

Example 2 (swift):
```swift
if isActive {
    MyView()
        .transition(.slide)
}
Button("Toggle") {
    withAnimation {
        isActive.toggle()
    }
}
```

---

## AnyTransition

**URL:** https://sosumi.ai/documentation/swiftui/anytransition?.md

**Contents:**
- Overview
- Getting built-in transitions
- Combining and configuring transitions
- Creating a custom transition
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct AnyTransition
```

---

## EmptyMatchedTransitionSourceConfiguration

**URL:** https://sosumi.ai/documentation/swiftui/emptymatchedtransitionsourceconfiguration?.md

**Contents:**
- Conforms To
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct EmptyMatchedTransitionSourceConfiguration
```

---

## matchedTransitionSource(id:in:)

**URL:** https://sosumi.ai/documentation/swiftui/view/matchedtransitionsource(id:in:)?.md

**Contents:**
- Parameters
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

The identifier, often derived from the identifier of the data being displayed by the view.

The namespace in which defines the `id`. New namespaces are created by adding an [Namespace](/documentation/swiftui/namespace) variable to a [View](/documentation/swiftui/view) type and reading its value in the view’s body method.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func matchedTransitionSource(id: some Hashable, in namespace: Namespace.ID) -> some View
```

---

## navigationTransition(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/navigationtransition(_:)?.md

**Contents:**
- Discussion
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

Add this modifier to a view that appears within a [Navigation Stack](/documentation/swiftui/navigationstack) or a sheet, outside of any containers such as [VStack](/documentation/swiftui/vstack).

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func navigationTransition(_ style: some NavigationTransition) -> some View
```

Example 2 (swift):
```swift
struct ContentView: View {
    @Namespace private var namespace
    var body: some View {
        NavigationStack {
            NavigationLink {
                DetailView()
                    .navigationTransition(.zoom(sourceID: "world", in: namespace))
            } label: {
                Image(systemName: "globe")
                    .matchedTransitionSource(id: "world", in: namespace)
            }
        }
    }
}
```

---

## ContentTransition

**URL:** https://sosumi.ai/documentation/swiftui/contenttransition?.md

**Contents:**
- Overview
- Conforms To
- Getting content transitions
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

Set the behavior of content transitions within a view with the [contentTransition(*:)](/documentation/swiftui/view/contenttransition(*:)) modifier, passing in one of the defined transitions, such as [opacity](/documentation/swiftui/contenttransition/opacity) or [interpolate](/documentation/swiftui/contenttransition/interpolate) as the parameter.

Content transitions only take effect within the context of an [Animation](/documentation/swiftui/animation) block.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ContentTransition
```

---

## NavigationTransition

**URL:** https://sosumi.ai/documentation/swiftui/navigationtransition?.md

**Contents:**
- Conforming Types
- Getting built-in transitions
- Supporting Types
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol NavigationTransition
```

---
