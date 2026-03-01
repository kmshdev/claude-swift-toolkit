# Swiftui-Animations - State Based Animation

**Pages:** 17

---

## AnimationCompletionCriteria

**URL:** https://sosumi.ai/documentation/swiftui/animationcompletioncriteria?.md

**Contents:**
- Conforms To
- Getting the completion criteria
- Adding state-based animation to an action

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct AnimationCompletionCriteria
```

---

## Animations

**URL:** https://sosumi.ai/documentation/swiftui/animations?.md

**Contents:**
- Overview
- Adding state-based animation to an action
- Adding state-based animation to a view
- Creating phase-based animation
- Creating keyframe-based animation
- Creating custom animations
- Making data animatable
- Updating a view on a schedule
- Synchronizing geometries
- Defining transitions

**Navigation:** [Swiftui](/documentation/swiftui)

You tell SwiftUI how to draw your app’s user interface for different states, and then rely on SwiftUI to make interface updates when the state changes.

![](https://docs-assets.developer.apple.com/published/634da5b7eb74a20fee434a105cebd3c7/animations-hero%402x.png)

To avoid abrupt visual transitions when the state changes, add animation in one of the following ways:

SwiftUI animates the effects that many built-in view modifiers produce, like those that set a scale or opacity value. You can animate other values by making your custom views conform to the [Animatable](/documentation/swiftui/animatable) protocol, and telling SwiftUI about the value you want to animate.

When an animated state change results in adding or removing a view to or from the view hierarchy, you can tell SwiftUI how to transition the view into or out of place using built-in transitions that [Any Transition](/documentation/swiftui/anytransition) defines, like [slide](/documentation/swiftui/anytransition/slide) or [scale](/documentation/swiftui/anytransition/scale). You can also create custom transitions.

For design guidance, see [motion](/design/Human-Interface-Guidelines/motion) in the Human Interface Guidelines.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

---

## AnimationState

**URL:** https://sosumi.ai/documentation/swiftui/animationstate?.md

**Contents:**
- Overview
  - Storing state for secondary animations
- Creating animation state
- Accessing custom keys
- Creating custom animations

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

An [Animation Context](/documentation/swiftui/animationcontext) uses this type to store state for a [Custom Animation](/documentation/swiftui/customanimation). To retrieve the stored state of a context, you can use the [state](/documentation/swiftui/animationcontext/state) property. However, a more convenient way to access the animation state is to define an [Animation State Key](/documentation/swiftui/animationstatekey) and extend [Animation Context](/documentation/swiftui/animationcontext) with a computed property that gets and sets the animation state, as shown in the following code:

When creating an [Animation State Key](/documentation/swiftui/animationstatekey), it’s convenient to define the state values that your custom animation needs. For example, the following code adds the properties `paused` and `pauseTime` to the `PausableState` animation state key:

To access the pausable state in a `PausableAnimation`, the follow code calls `pausableState` instead of using the context’s [state](/documentation/swiftui/animationcontext/state) property. And because the animation state key `PausableState` defines properties for state values, the custom animation can read and write those values.

A custom animation can also use `AnimationState` to store the state of a secondary animation. For example, the following code creates an [Animation State Key](/documentation/swiftui/animationstatekey) that includes the property `secondaryState`, which a custom animation can use to store other state:

The custom animation `TargetAnimation` uses `TargetState` to store state data in `secondaryState` for another animation that runs as part of the target animation.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct AnimationState<Value> where Value : VectorArithmetic
```

Example 2 (swift):
```swift
private struct PausableState<Value: VectorArithmetic>: AnimationStateKey {
    static var defaultValue: Self { .init() }
}

extension AnimationContext {
    fileprivate var pausableState: PausableState<Value> {
        get { state[PausableState<Value>.self] }
        set { state[PausableState<Value>.self] = newValue }
    }
}
```

Example 3 (swift):
```swift
private struct PausableState<Value: VectorArithmetic>: AnimationStateKey {
    var paused = false
    var pauseTime: TimeInterval = 0.0

    static var defaultValue: Self { .init() }
}
```

Example 4 (swift):
```swift
struct PausableAnimation: CustomAnimation {
    let base: Animation

    func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic {
        let paused = context.environment.animationPaused

        let pausableState = context.pausableState
        var pauseTime = pausableState.pauseTime
        if pausableState.paused != paused {
            pauseTime = time - pauseTime
            context.pausableState = PausableState(paused: paused, pauseTime: pauseTime)
        }

        let effectiveTime = paused ? pauseTime : time - pauseTime
        let result = base.animate(value: value, time: effectiveTime, context: &context)
        return result
    }
}
```

---

## CustomAnimation

**URL:** https://sosumi.ai/documentation/swiftui/customanimation?.md

**Contents:**
- Overview
- Inherits From
- Animating a value
- Getting the velocity
- Determining whether to merge
- Creating custom animations

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

Use this protocol to create a type that changes an animatable value over time, which produces a custom visual transition of a view. For example, the follow code changes an animatable value using an elastic ease-in ease-out function:

To create an [Animation](/documentation/swiftui/animation) instance of a custom animation, use the [init(*:)](/documentation/swiftui/animation/init(*:)) initializer, passing in an instance of a custom animation; for example:

To help make view code more readable, extend [Animation](/documentation/swiftui/animation) and add a static property and function that returns an `Animation` instance of a custom animation. For example, the following code adds the static property `elasticEaseInEaseOut` that returns the elastic ease-in ease-out animation with a default duration of `0.35` seconds. Next, the code adds a method that returns the animation with a specified duration.

To animate a view with the elastic ease-in ease-out animation, a view calls either `.elasticEaseInEaseOut` or `.elasticEaseInEaseOut(duration:)`. For example, the follow code includes an Animate button that, when clicked, animates a circle as it moves from one edge of the view to the other, using the elastic ease-in ease-out animation with a duration of `5` seconds:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@preconcurrency protocol CustomAnimation : Hashable, Sendable
```

Example 2 (swift):
```swift
struct ElasticEaseInEaseOutAnimation: CustomAnimation {
    let duration: TimeInterval

    func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic {
        if time > duration { return nil } // The animation has finished.

        let p = time / duration
        let s = sin((20 * p - 11.125) * ((2 * Double.pi) / 4.5))
        if p < 0.5 {
            return value.scaled(by: -(pow(2, 20 * p - 10) * s) / 2)
        } else {
            return value.scaled(by: (pow(2, -20 * p + 10) * s) / 2 + 1)
        }
    }
}
```

Example 3 (swift):
```swift
Animation(ElasticEaseInEaseOutAnimation(duration: 5.0))
```

Example 4 (swift):
```swift
extension Animation {
    static var elasticEaseInEaseOut: Animation { elasticEaseInEaseOut(duration: 0.35) }
    static func elasticEaseInEaseOut(duration: TimeInterval) -> Animation {
        Animation(ElasticEaseInEaseOutAnimation(duration: duration))
    }
}
```

---

## Animation

**URL:** https://sosumi.ai/documentation/swiftui/animation?.md

**Contents:**
- Overview
- Conforms To
- Getting the default animation
- Getting linear animations
- Getting eased animations
- Getting built-in spring animations
- Customizing spring animations
- Creating custom animations
- Configuring an animation
- Instance Properties

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

An `Animation` provides a visual transition of a view when a state value changes from one value to another. The characteristics of this transition vary according to the animation type. For instance, a [linear](/documentation/swiftui/animation/linear) animation provides a mechanical feel to the animation because its speed is consistent from start to finish. In contrast, an animation that uses easing, like [ease Out](/documentation/swiftui/animation/easeout), offers a more natural feel by varying the acceleration of the animation.

To apply an animation to a view, add the [animation(*:value:)](/documentation/swiftui/view/animation(*:value:)) modifier, and specify both an animation type and the value to animate. For instance, the [Circle](/documentation/swiftui/circle) view in the following code performs an [ease In](/documentation/swiftui/animation/easein) animation each time the state variable `scale` changes:

When the value of `scale` changes, the modifier [scaleEffect(*:anchor:)](/documentation/swiftui/view/scaleeffect(*:anchor:)) resizes [Circle](/documentation/swiftui/circle) according to the new value. SwiftUI can animate the transition between sizes because [Circle](/documentation/swiftui/circle) conforms to the [Shape](/documentation/swiftui/shape) protocol. Shapes in SwiftUI conform to the [Animatable](/documentation/swiftui/animatable) protocol, which describes how to animate a property of a view.

In addition to adding an animation to a view, you can also configure the animation by applying animation modifiers to the animation type. For example, you can:

For example, the [Circle](/documentation/swiftui/circle) view in the following code repeats the [ease In](/documentation/swiftui/animation/easein) animation three times by using the [repeatCount(*:autoreverses:)](/documentation/swiftui/animation/repeatcount(*:autoreverses:)) modifier:

A view can also perform an animation when a binding value changes. To specify the animation type on a binding, call its [animation(*:)](/documentation/swiftui/binding/animation(*:)) method. For example, the view in the following code performs a [linear](/documentation/swiftui/animation/linear) animation, moving the box truck between the leading and trailing edges of the view. The truck moves each time a person clicks the [Toggle](/documentation/swiftui/toggle) control, which changes the value of the `$isTrailing` binding.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Animation
```

Example 2 (swift):
```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scaleEffect(scale)
                .animation(.easeIn, value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
        .padding()
    }
```

Example 3 (swift):
```swift
struct ContentView: View {
    @State private var scale = 0.5

    var body: some View {
        VStack {
            Circle()
                .scaleEffect(scale)
                .animation(.easeIn.repeatCount(3), value: scale)
            HStack {
                Button("+") { scale += 0.1 }
                Button("-") { scale -= 0.1 }
            }
        }
        .padding()
    }
}
```

Example 4 (swift):
```swift
struct ContentView: View {
    @State private var isTrailing = false

    var body: some View {
       VStack(alignment: isTrailing ? .trailing : .leading) {
            Image(systemName: "box.truck")
                .font(.system(size: 64))

            Toggle("Move to trailing edge",
                   isOn: $isTrailing.animation(.linear))
        }
    }
}
```

---

## animation(_:)

**URL:** https://sosumi.ai/documentation/swiftui/binding/animation(_:)?.md

**Contents:**
- Parameters
- Return Value
- Managing changes

**Navigation:** [Swiftui](/documentation/swiftui) › [binding](/documentation/swiftui/binding)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

An animation sequence performed when the binding value changes.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
func animation(_ animation: Animation? = .default) -> Binding<Value>
```

---

## phaseAnimator(_:content:animation:)

**URL:** https://sosumi.ai/documentation/swiftui/view/phaseanimator(_:content:animation:)?.md

**Contents:**
- Parameters
- Discussion
- Creating phase-based animation

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

The sequence of phases to cycle through. Ensure that the sequence isn’t empty. If it is, SwiftUI logs a runtime warning and also returns a visual warning as the output view.

A view builder closure that takes two parameters: a proxy value representing the modified view and the current phase. You can apply effects to the proxy based on the current phase.

A closure that takes the current phase as input. Return the animation to use when transitioning to the next phase. If you return `nil`, the transition doesn’t animate. If you don’t set this parameter, SwiftUI uses a default animation.

When the modified view first appears, this modifier renders its `content` closure using the first phase as input to the closure, along with a proxy for the modified view. Apply effects to the proxy — and thus to the modified view — in a way that’s appropriate for the first phase value.

Right away, the modifier provides its `content` closure with the value of the second phase. Update the effects that you apply to the proxy view accordingly, and the modifier animates the change for you. As soon as the animation completes, the procedure repeats using successive phases until reaching the last phase, at which point the modifier loops back to the first phase.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func phaseAnimator<Phase>(_ phases: some Sequence, @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View, animation: @escaping (Phase) -> Animation? = { _ in .default }) -> some View where Phase : Equatable
```

---

## animation(_:value:)

**URL:** https://sosumi.ai/documentation/swiftui/view/animation(_:value:)?.md

**Contents:**
- Parameters
- Return Value
- Adding state-based animation to a view

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

A value to monitor for changes.

A view that applies `animation` to this view whenever `value` changes.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func animation<V>(_ animation: Animation?, value: V) -> some View where V : Equatable
```

---

## withAnimation(_:_:)

**URL:** https://sosumi.ai/documentation/swiftui/withanimation(_:_:)?.md

**Contents:**
- Discussion
- Adding state-based animation to an action

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

This function sets the given [Animation](/documentation/swiftui/animation) as the [animation](/documentation/swiftui/transaction/animation) property of the thread’s current [Transaction](/documentation/swiftui/transaction).

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
func withAnimation<Result>(_ animation: Animation? = .default, _ body: () throws -> Result) rethrows -> Result
```

---

## Transaction

**URL:** https://sosumi.ai/documentation/swiftui/transaction?.md

**Contents:**
- Overview
- Creating a transaction
- Managing animations
- Managing window dismissal
- Getting information about a transaction
- Instance Properties
- Moving an animation to another view

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

Use a transaction to pass an animation between views in a view hierarchy.

The root transaction for a state change comes from the binding that changed, plus any global values set by calling [withTransaction(*:*:)](/documentation/swiftui/withtransaction(*:*:)) or [withAnimation(*:*:)](/documentation/swiftui/withanimation(*:*:)).

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct Transaction
```

---

## AnimationContext

**URL:** https://sosumi.ai/documentation/swiftui/animationcontext?.md

**Contents:**
- Overview
- Managing state
- Retrieving view environment values
- Creating context
- Instance Properties
- Creating custom animations

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

The system provides an `AnimationContext` to a [Custom Animation](/documentation/swiftui/customanimation) instance so that the animation can store and retrieve values in an instance of [Animation State](/documentation/swiftui/animationstate). To access these values, use the context’s [state](/documentation/swiftui/animationcontext/state) property.

For more convenient access to state, create an [Animation State Key](/documentation/swiftui/animationstatekey) and extend `AnimationContext` to include a computed property that gets and sets the [Animation State](/documentation/swiftui/animationstate) value. Then use this property instead of [state](/documentation/swiftui/animationcontext/state) to retrieve the state of a custom animation. For example, the following code creates an animation state key named `PausableState`. Then the code extends `AnimationContext` to include the `pausableState` property:

To access the pausable state, the custom animation `PausableAnimation` uses the `pausableState` property instead of the [state](/documentation/swiftui/animationcontext/state) property:

The animation can also retrieve environment values of the view that created the animation. To retrieve a view’s environment value, use the context’s [environment](/documentation/swiftui/animationcontext/environment) property. For instance, the following code creates a custom [Environment Values](/documentation/swiftui/environmentvalues) property named `animationPaused`, and the view `PausableAnimationView` uses the property to store the paused state:

Then the custom animation `PausableAnimation` retrieves the paused state from the view’s environment using the [environment](/documentation/swiftui/animationcontext/environment) property:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct AnimationContext<Value> where Value : VectorArithmetic
```

Example 2 (swift):
```swift
private struct PausableState<Value: VectorArithmetic>: AnimationStateKey {
    var paused = false
    var pauseTime: TimeInterval = 0.0

    static var defaultValue: Self { .init() }
}

extension AnimationContext {
    fileprivate var pausableState: PausableState<Value> {
        get { state[PausableState<Value>.self] }
        set { state[PausableState<Value>.self] = newValue }
    }
}
```

Example 3 (swift):
```swift
struct PausableAnimation: CustomAnimation {
    let base: Animation

    func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic {
        let paused = context.environment.animationPaused

        let pausableState = context.pausableState
        var pauseTime = pausableState.pauseTime
        if pausableState.paused != paused {
            pauseTime = time - pauseTime
            context.pausableState = PausableState(paused: paused, pauseTime: pauseTime)
        }

        let effectiveTime = paused ? pauseTime : time - pauseTime
        let result = base.animate(value: value, time: effectiveTime, context: &context)
        return result
    }
}
```

Example 4 (swift):
```swift
extension EnvironmentValues {
    @Entry var animationPaused: Bool = false
}

struct PausableAnimationView: View {
    @State private var paused = false

    var body: some View {
        VStack {
            ...
        }
        .environment(\.animationPaused, paused)
    }
}
```

---

## Controlling the timing and movements of your animations

**URL:** https://sosumi.ai/documentation/swiftui/controlling-the-timing-and-movements-of-your-animations?.md

**Contents:**
- Overview
- Create a simple bounce animation
- Bounce with a phase animator
- Add more phases to the animation
- Gain more control with a keyframe animator
- Creating phase-based animation

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 15.0+

SwiftUI provides a collection of useful animations that you can use in your app. These animations help enhance the user experience of your app by providing visual transitions of views and user interface elements. While these standard animations provide a great way to enhancement the user interaction of your app, there are times when you need to have more control over the timing and movement of a visual element. [Phase Animator](/documentation/swiftui/phaseanimator) and [Keyframe Animator](/documentation/swiftui/keyframeanimator) help give you that control.

A phase animator allows you to define an animation as a collection of discrete steps called phases. The animator cycles through these phases to create a visual transition. With keyframe animator, you create keyframes that define animation values at specific times during the visual transition.

To better understand how to create animations using a [Phase Animator](/documentation/swiftui/phaseanimator) or [Keyframe Animator](/documentation/swiftui/keyframeanimator), start with a simple example that uses standard SwiftUI animations. The following code moves an emoji upwards by setting its offset to `-40.0`. To provide a smooth transition of the movement, the code uses the [withAnimation(*:*:)](/documentation/swiftui/withanimation(*:*:)) function to apply a [bouncy](/documentation/swiftui/animation/bouncy) animation after someone taps the emoji.

This animation has a single, discrete step: move the emoji upward. However, an animation can have multiple steps, such as moving an emoji upwards then back to its original position. For example, the following code sets the offset to `-40.0` to move the emoji upward, and then sets the offset (`0.0`) to return the emoji back to its original position:

This code uses the [withAnimation(*:completionCriteria:*:completion:)](/documentation/swiftui/withanimation(*:completioncriteria:*:completion:)) function to animate the two steps of the visual transition. The first step occurs in the `body` closure of the function, setting the offset to `-40.0`. The second step occurs in the `completion` closure, setting the offset to `0.0`.

However, `EmojiView` actually goes through three steps. The first step happens when the view appears for the first time. The offset of the `EmojiView` view is `0.0`. When someone taps the view, the offset changes to `-40.0`; this is the second step. When that animation completes, the third step changes the offset back to `0.0`. However, there are only two discrete steps, based on the offset values (`0.0` and `-40.0`).

While this implementation certainly works as expected, using a [Phase Animator](/documentation/swiftui/phaseanimator) is a more convenient way to define discrete steps as phases of an animation.

A [Phase Animator](/documentation/swiftui/phaseanimator) automatically advances through a set of given phases to create an animated transition. Use the [phaseAnimator(*:content:animation:)](/documentation/swiftui/view/phaseanimator(*:content:animation:)) modifier to provide the animator the phases for changing the animation value. For example, the emoji bounce animation shown earlier has two phases: move up and move back. You can represent these phases using the Boolean values, `true` and `false`. When the phase is `true`, the emoji moves up to `-40.0`. When the phase is `false`, the emoji moves back to the original position by setting the offset to `0.0`.

The phase animator cycles through the list of phases in the order that you provide to the [phaseAnimator(*:content:animation:)](/documentation/swiftui/view/phaseanimator(*:content:animation:)) modifier. When the view first appears, the phase animator invokes the `content` closure passing in the first phase. Then the animator calls the closure with the value of the second phase. The animator continues to call the `content` closure for each additional phase. After reaching the last phase, the animator calls `content` one more time with the value of the first phase.

This means that in the previous code, the phase animator calls `content` with the phase value of `false` when the view first appears. This sets the emoji’s offset to `0.0`. The phase animator then calls `content` with the `true` phase. This phase sets the offset to `-40.0`, causing the emoji to move upwards. After reaching that offset position, the animator calls `content` with the phase of `false`. This causes the emoji to move back to its original position by setting its offset to `0.0`.

This animation starts when the view appears. To start the animation based on an event, use the [phaseAnimator(*:trigger:content:animation:)](/documentation/swiftui/view/phaseanimator(*:trigger:content:animation:)) modifier and provide a `trigger` value that animator observes for changes. The animator starts the animation when the value changes. For example, the following code increments the state variable `likeCount` each time a person taps the emoji. The code uses `likeCount` as the value that the phase animator observes for changes. Now whenever someone taps the emoji, it moves up and returns to its original position.

So far, the phase animator uses the [default](/documentation/swiftui/animation/default) animation to move the emoji. You can change that behavior by providing the `phaseAnimator` modifier an animation closure. In this closure, specify the type of animation to apply for each phase. For instance, the following code applies a [bouncy](/documentation/swiftui/animation/bouncy) animation when the phase is `true`; otherwise, it applies the [default](/documentation/swiftui/animation/default) animation:

While this bounce effect is nice, you can add more pizzazz to it. For instance, you could make the emoji increase in size as it moves upward, and then shrink back to normal size. To do this, you’ll add a third phase to the animation: scale.

To define the phases, create a custom type that lists the possible phases; for example:

Next, to help simplify logic and reduce complexity, define computed properties that return the values to animate. For instance, to set the vertical offset to move the emoji, create a computed property that returns the offset based on the current phase:

When at the initial phase, the offset is `0`, which is the original screen location for the emoji. But when the phase is `move` or `scale`, the offset is `-64`.

You can use the same approach (creating a computed property) for the scale effect to change the size of the emoji. Initially, the emoji appears at its original size, but increases in size during the move and scale phase, as shown here:

To animate an emoji, apply the [phaseAnimator(*:trigger:content:animation:)](/documentation/swiftui/view/phaseanimator(*:trigger:content:animation:)) modifier to the `EmojiView`. Provide the animator all cases from the custom `AnimationPhase` type. Then change the content based on the phase by applying the [scaleEffect(*:anchor:)](/documentation/swiftui/view/scaleeffect(*:anchor:)) and [offset(x:y:)](/documentation/swiftui/view/offset(x:y:)) modifiers. The values passed into these modifiers come from the computed properties, which helps keep the view code more readable.

The code also applies different animation types based on the phase in the `animation` closure to give the full animation that pizzazz you were looking for.

A [Phase Animator](/documentation/swiftui/phaseanimator) gives you control of an animation based on discrete phases, which helps you add extra polish to an animation. But if you find that you need even more control over the timing and movement of an animation, use a [Keyframe Animator](/documentation/swiftui/keyframeanimator).

You can define complex, coordinated animations with complete control over timing and movement using a [Keyframe Animator](/documentation/swiftui/keyframeanimator). This animator allows you to create keyframes that define values at specific times during an animation. The animator use these values to generate interpolated values in between each frame of the animation.

Unlike a phase animator, in which you model separate, discrete states, a keyframe animator generates interpolated values of the type that you specify. While an animation is in progress, the animator provides you with a value of this type on every frame so you can update the animating view by applying modifiers to it.

You define the type as a structure that contains the properties that you want to independently animate. For example, the following code defines four properties that determine the scale, stretch, position, and angle of an emoji:

To create a animation using a keyframe animator, apply either the [keyframeAnimator(initialValue:repeating:content:keyframes:)](/documentation/swiftui/view/keyframeanimator(initialvalue:repeating:content:keyframes:)) or [keyframeAnimator(initialValue:trigger:content:keyframes:)](/documentation/swiftui/view/keyframeanimator(initialvalue:trigger:content:keyframes:)) modifier to the view that you want to animate. For instance, the following code applies the second modifier to `EmojiView`. The initial value for the animation is a new instance of `AnimationValues`, and the state variable `likeCount` is the value that the animator observes for changes as it did in the previous phase animation example.

To apply modifiers to a view during the animation, provide a `content` closure to the keyframe animator. This closure includes two parameters:

Use these parameters to apply modifiers to the view that SwiftUI is animating. For example, the following code uses these parameters to rotate, scale, stretch, and move an emoji:

Next, define the keyframes. Keyframes let you build sophisticated animations with different keyframe for different properties. To make this possible, you organize the keyframes into tracks. Each track controls a different property of the type that you are animating. You associate a property to a track by providing the key path to the property when creating the track. For example, the following code adds a [Keyframe Track](/documentation/swiftui/keyframetrack) for the `scale` property:

When creating a track, you use the declarative syntax in SwiftUI to add keyframes to the track. There are different kinds of keyframes, such as [Cubic Keyframe](/documentation/swiftui/cubickeyframe), [Linear Keyframe](/documentation/swiftui/linearkeyframe), and [Spring Keyframe](/documentation/swiftui/springkeyframe). You can mix and match the different kinds of keyframes within a track. For example, the following code adds a track for the `scale` property that performs a combination of linear and spring animations:

Each keyframe type receives a value. The animator uses this value to generate interpolated values between frames and sets the property specified in the track’s key path before calling the animator’s content closure. For instance, in the previous code listing, the scale value is `1.0` during the linear keyframes, which keeps the emoji at its original size. Then the scale changes to `1.5` during the first spring keyframe. This causes the emoji to grow in size. The final spring keyframe sets the scale to `1.0`, which returns the emoji back to its original size.

When implementing a keyframe animation, include a track for each property that you want to animate. For instance, `AnimationValues` has four properties:

To animate all four, the animator needs four keyframe tracks as shown in the following code:

The combination of these keyframe tracks creates an animation that squishes and stretches the emoji, before bouncing it upwards. As the emoji moves towards its peak, it grows larger. When the emoji reaches its peak, it gives a little wiggle. Then the emoji returns to its original location with a slight bounce as it settles back into its original position.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct SimpleAnimationView: View {
    var emoji: String
    @State private var offset = 0.0

    var body: some View {
        EmojiView(emoji: emoji)
            .offset(y: offset)
            .onTapGesture {
                withAnimation(.bouncy) {
                    offset = -40.0
                }
            }
    }
}
```

Example 2 (swift):
```swift
struct SimpleAnimationView: View {
    var emoji: String
    @State private var offset = 0.0

    var body: some View {
        EmojiView(emoji: emoji)
            .offset(y: offset)
            .onTapGesture {
                withAnimation(.bouncy) {
                    offset = -40.0
                } completion: {
                    withAnimation {
                        offset = 0.0
                    }
                }
            }
    }
}
```

Example 3 (swift):
```swift
struct TwoPhaseAnimationView: View {
    var emoji: String
    
    var body: some View {
        EmojiView(emoji: emoji)
            .phaseAnimator([false, true]) { content, phase in
                content.offset(y: phase ? -40.0 : 0.0)
            }
    }
}
```

Example 4 (swift):
```swift
struct TwoPhaseAnimationView: View {
    var emoji: String
    @State private var likeCount = 1
    
    var body: some View {
        EmojiView(emoji: emoji)
            .phaseAnimator([false, true], trigger: likeCount) { content, phase in
                content.offset(y: phase ? -40.0 : 0.0)
            }
            .onTapGesture {
                likeCount += 1
            }
    }
}
```

---

## AnimationStateKey

**URL:** https://sosumi.ai/documentation/swiftui/animationstatekey?.md

**Contents:**
- Overview
- Setting the default value
- Creating custom animations

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

To access animation state from an [Animation Context](/documentation/swiftui/animationcontext) in a custom animation, create an `AnimationStateKey`. For example, the following code creates an animation state key named `PausableState` and sets the value for the required [default Value](/documentation/swiftui/animationstatekey/defaultvalue) property. The code also defines properties for state values that the custom animation needs when calculating animation values. Keeping the state values in the animation state key makes it more convenient to read and write those values in the implementation of a [Custom Animation](/documentation/swiftui/customanimation).

To make accessing the value of the animation state key more convenient, define a property for it by extending [Animation Context](/documentation/swiftui/animationcontext):

Then, you can read and write your state in an instance of `CustomAnimation` using the [Animation Context](/documentation/swiftui/animationcontext):

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol AnimationStateKey
```

Example 2 (swift):
```swift
private struct PausableState<Value: VectorArithmetic>: AnimationStateKey {
    var paused = false
    var pauseTime: TimeInterval = 0.0

    static var defaultValue: Self { .init() }
}
```

Example 3 (swift):
```swift
extension AnimationContext {
    fileprivate var pausableState: PausableState<Value> {
        get { state[PausableState<Value>.self] }
        set { state[PausableState<Value>.self] = newValue }
    }
}
```

Example 4 (swift):
```swift
struct PausableAnimation: CustomAnimation {
    let base: Animation

    func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic {
        let paused = context.environment.animationPaused

        let pausableState = context.pausableState
        var pauseTime = pausableState.pauseTime
        if pausableState.paused != paused {
            pauseTime = time - pauseTime
            context.pausableState = PausableState(paused: paused, pauseTime: pauseTime)
        }

        let effectiveTime = paused ? pauseTime : time - pauseTime
        let result = base.animate(value: value, time: effectiveTime, context: &context)
        return result
    }
}
```

---

## animation(_:body:)

**URL:** https://sosumi.ai/documentation/swiftui/view/animation(_:body:)?.md

**Contents:**
- Discussion
- Adding state-based animation to a view

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

Any modifiers applied to the content of `body` will be applied to this view, and the `animation` will only be used on the modifiers defined in the `body`.

The following code animates the opacity changing with an easeInOut animation, while the contents of MyView are animated with the implicit transaction’s animation:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func animation<V>(_ animation: Animation?, @ViewBuilder body: (PlaceholderContentView<Self>) -> V) -> some View where V : View
```

Example 2 (swift):
```swift
MyView(isActive: isActive)
    .animation(.easeInOut) { content in
        content.opacity(isActive ? 1.0 : 0.0)
    }
```

---

## withAnimation(_:completionCriteria:_:completion:)

**URL:** https://sosumi.ai/documentation/swiftui/withanimation(_:completioncriteria:_:completion:)?.md

**Contents:**
- Discussion
- Adding state-based animation to an action

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

This function sets the given [Animation](/documentation/swiftui/animation) as the [animation](/documentation/swiftui/transaction/animation) property of the thread’s current [Transaction](/documentation/swiftui/transaction) as well as calling `Transaction/addAnimationCompletion` with the specified completion.

The completion callback will always be fired exactly one time. If no animations are created by the changes in `body`, then the callback will be called immediately after `body`.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
func withAnimation<Result>(_ animation: Animation? = .default, completionCriteria: AnimationCompletionCriteria = .logicallyComplete, _ body: () throws -> Result, completion: @escaping () -> Void) rethrows -> Result
```

---

## phaseAnimator(_:trigger:content:animation:)

**URL:** https://sosumi.ai/documentation/swiftui/view/phaseanimator(_:trigger:content:animation:)?.md

**Contents:**
- Parameters
- Discussion
- Creating phase-based animation

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

The sequence of phases to cycle through. Ensure that the sequence isn’t empty. If it is, SwiftUI logs a runtime warning and also returns a visual warning as the output view.

A value whose changes cause the animator to use the next phase.

A view builder closure that takes two parameters: a proxy value representing the modified view and the current phase. You can apply effects to the proxy based on the current phase.

A closure that takes the current phase as input. Return the animation to use when transitioning to the next phase. If you return `nil`, the transition doesn’t animate. If you don’t set this parameter, SwiftUI uses a default animation.

When the modified view first appears, this modifier renders its `content` closure using the first phase as input to the closure, along with a proxy for the modified view. Apply effects to the proxy — and thus to the modified view — in a way that’s appropriate for the first phase value.

Later, when the value of the `trigger` input changes, the modifier provides its `content` closure with the value of the second phase. Update the effects that you apply to the proxy view accordingly, and the modifier animates the change for you. The next time the `trigger` input changes, this procedure repeats using successive phases until reaching the last phase, at which point the modifier loops back to the first phase.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func phaseAnimator<Phase>(_ phases: some Sequence, trigger: some Equatable, @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View, animation: @escaping (Phase) -> Animation? = { _ in .default }) -> some View where Phase : Equatable
```

---

## animation(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/animation(_:)?.md

**Contents:**
- Parameters
- Return Value
- Adding state-based animation to a view

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

The animation to apply. If `animation` is `nil`, the view doesn’t animate.

A view that applies `animation` to this view whenever it changes.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func animation(_ animation: Animation?) -> some View
```

---
