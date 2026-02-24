# Neuralforge-Chat-Sidebar - Streaming And Typing

**Pages:** 11

---

## progressViewStyle(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/progressviewstyle(_:)?.md

**Contents:**
- Parameters
- Discussion
- Indicating a value

---
title: progressViewStyle(_:)
description: Sets the style for progress views in this view.
source: https://developer.apple.com/documentation/swiftui/view/progressviewstyle(_:)
timestamp: 2026-02-13T01:42:02.569Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Sets the style for progress views in this view.

The progress view style to use for this view.

For example, the following code creates a progress view that uses the “circular” style:

- [Gauge](/documentation/swiftui/gauge)
- [gaugeStyle(_:)](/documentation/swiftui/view/gaugestyle(_:))
- [ProgressView](/documentation/swiftui/progressview)
- [DefaultDateProgressLabel](/documentation/swiftui/defaultdateprogresslabel)
- [DefaultButtonLabel](/documentation/swiftui/defaultbuttonlabel)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func progressViewStyle<S>(_ style: S) -> some View where S : ProgressViewStyle
```

Example 2 (swift):
```swift
ProgressView()
    .progressViewStyle(.circular)
```

---

## ProgressView

**URL:** https://sosumi.ai/documentation/swiftui/progressview?.md

**Contents:**
- Overview
  - Styling progress views
- Conforms To
- Creating an indeterminate progress view
- Creating a determinate progress view
- Create a progress view spanning a date range
- Initializers
- Indicating a value

---
title: ProgressView
description: A view that shows the progress toward completion of a task.
source: https://developer.apple.com/documentation/swiftui/progressview
timestamp: 2026-02-13T01:42:00.477Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> A view that shows the progress toward completion of a task.

Use a progress view to show that a task is incomplete but advancing toward completion. A progress view can show both determinate (percentage complete) and indeterminate (progressing or not) types of progress.

Create a determinate progress view by initializing a `ProgressView` with a binding to a numeric value that indicates the progress, and a `total` value that represents completion of the task. By default, the progress is `0.0` and the total is `1.0`.

The example below uses the state property `progress` to show progress in a determinate `ProgressView`. The progress view uses its default total of `1.0`, and because `progress` starts with an initial value of `0.5`, the progress view begins half-complete. A “More” button below the progress view allows people to increment the progress in increments of five percent:

To create an indeterminate progress view, use an initializer that doesn’t take a progress value:

You can also create a progress view that covers a closed range of [Date](/documentation/Foundation/Date) values. As long as the current date is within the range, the progress view automatically updates, filling or depleting the progress view as it nears the end of the range. The following example shows a five-minute timer whose start time is that of the progress view’s initialization:

You can customize the appearance and interaction of progress views by creating styles that conform to the [Progress View Style](/documentation/swiftui/progressviewstyle) protocol. To set a specific style for all progress view instances within a view, use the [progressViewStyle(_:)](/documentation/swiftui/view/progressviewstyle(_:)) modifier. In the following example, a custom style adds a rounded pink border to all progress views within the enclosing [VStack](/documentation/swiftui/vstack):

SwiftUI provides two built-in progress view styles, [linear](/documentation/swiftui/progressviewstyle/linear) and [circular](/documentation/swiftui/progressviewstyle/circular), as well as an automatic style that defaults to the most appropriate style in the current context. The following example shows a circular progress view that starts at 60 percent completed.

On platforms other than macOS, the circular style may appear as an indeterminate indicator instead.

- [View](/documentation/swiftui/view)

- [init()](/documentation/swiftui/progressview/init()) Creates a progress view for showing indeterminate progress, without a label.
- [init(label:)](/documentation/swiftui/progressview/init(label:)) Creates a progress view for showing indeterminate progress that displays a custom label.
- [init(_:)](/documentation/swiftui/progressview/init(_:)-6k5se) Creates a progress view for showing indeterminate progress that generates its label from a localized string.
- [init(_:)](/documentation/swiftui/progressview/init(_:)-3q5nf) Creates a progress view for showing indeterminate progress that generates its label from a string.

- [init(_:)](/documentation/swiftui/progressview/init(_:)-l5vj) Creates a progress view for visualizing the given progress instance.
- [init(value:total:)](/documentation/swiftui/progressview/init(value:total:)) Creates a progress view for showing determinate progress.
- [init(_:value:total:)](/documentation/swiftui/progressview/init(_:value:total:)) Creates a progress view for showing determinate progress that generates its label from a string.
- [init(value:total:label:)](/documentation/swiftui/progressview/init(value:total:label:)) Creates a progress view for showing determinate progress, with a custom label.
- [init(value:total:label:currentValueLabel:)](/documentation/swiftui/progressview/init(value:total:label:currentvaluelabel:)) Creates a progress view for showing determinate progress, with a custom label.

- [init(timerInterval:countsDown:)](/documentation/swiftui/progressview/init(timerinterval:countsdown:)) Creates a progress view for showing continuous progress as time passes.
- [init(timerInterval:countsDown:label:)](/documentation/swiftui/progressview/init(timerinterval:countsdown:label:)) Creates a progress view for showing continuous progress as time passes, with a descriptive label.
- [init(timerInterval:countsDown:label:currentValueLabel:)](/documentation/swiftui/progressview/init(timerinterval:countsdown:label:currentvaluelabel:)) Creates a progress view for showing continuous progress as time passes, with descriptive and current progress labels.

- [init(_:)](/documentation/swiftui/progressview/init(_:)) Creates a progress view based on a style configuration.

- [Gauge](/documentation/swiftui/gauge)
- [gaugeStyle(_:)](/documentation/swiftui/view/gaugestyle(_:))
- [progressViewStyle(_:)](/documentation/swiftui/view/progressviewstyle(_:))
- [DefaultDateProgressLabel](/documentation/swiftui/defaultdateprogresslabel)
- [DefaultButtonLabel](/documentation/swiftui/defaultbuttonlabel)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct ProgressView<Label, CurrentValueLabel> where Label : View, CurrentValueLabel : View
```

Example 2 (swift):
```swift
struct LinearProgressDemoView: View {
    @State private var progress = 0.5

    var body: some View {
        VStack {
            ProgressView(value: progress)
            Button("More") { progress += 0.05 }
        }
    }
}
```

Example 3 (swift):
```swift
var body: some View {
    ProgressView()
}
```

Example 4 (swift):
```swift
struct DateRelativeProgressDemoView: View {
    let workoutDateRange = Date()...Date().addingTimeInterval(5*60)

    var body: some View {
         ProgressView(timerInterval: workoutDateRange) {
             Text("Workout")
         }
    }
}
```

---

## onReceive(_:perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/onreceive(_:perform:)?.md

**Contents:**
- Parameters
- Return Value
- Responding to data changes

---
title: onReceive(_:perform:)
description: Adds an action to perform when this view detects data emitted by the given publisher.
source: https://developer.apple.com/documentation/swiftui/view/onreceive(_:perform:)
timestamp: 2026-02-13T01:42:14.951Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Adds an action to perform when this view detects data emitted by the given publisher.

The publisher to subscribe to.

The action to perform when an event is emitted by `publisher`. The event emitted by publisher is passed as a parameter to `action`.

A view that triggers `action` when `publisher` emits an event.

- [onChange(of:initial:_:)](/documentation/swiftui/view/onchange(of:initial:_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onReceive<P>(_ publisher: P, perform action: @escaping (P.Output) -> Void) -> some View where P : Publisher, P.Failure == Never
```

---

## phaseAnimator(_:content:animation:)

**URL:** https://sosumi.ai/documentation/swiftui/view/phaseanimator(_:content:animation:)?.md

**Contents:**
- Parameters
- Discussion
- Creating phase-based animation

---
title: phaseAnimator(_:content:animation:)
description: Animates effects that you apply to a view over a sequence of phases that change continuously.
source: https://developer.apple.com/documentation/swiftui/view/phaseanimator(_:content:animation:)
timestamp: 2026-02-13T01:43:03.592Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

> Animates effects that you apply to a view over a sequence of phases that change continuously.

The sequence of phases to cycle through. Ensure that the sequence isn’t empty. If it is, SwiftUI logs a runtime warning and also returns a visual warning as the output view.

A view builder closure that takes two parameters: a proxy value representing the modified view and the current phase. You can apply effects to the proxy based on the current phase.

A closure that takes the current phase as input. Return the animation to use when transitioning to the next phase. If you return `nil`, the transition doesn’t animate. If you don’t set this parameter, SwiftUI uses a default animation.

When the modified view first appears, this modifier renders its `content` closure using the first phase as input to the closure, along with a proxy for the modified view. Apply effects to the proxy — and thus to the modified view — in a way that’s appropriate for the first phase value.

Right away, the modifier provides its `content` closure with the value of the second phase. Update the effects that you apply to the proxy view accordingly, and the modifier animates the change for you. As soon as the animation completes, the procedure repeats using successive phases until reaching the last phase, at which point the modifier loops back to the first phase.

- [Controlling the timing and movements of your animations](/documentation/swiftui/controlling-the-timing-and-movements-of-your-animations)
- [phaseAnimator(_:trigger:content:animation:)](/documentation/swiftui/view/phaseanimator(_:trigger:content:animation:))
- [PhaseAnimator](/documentation/swiftui/phaseanimator)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func phaseAnimator<Phase>(_ phases: some Sequence, @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View, animation: @escaping (Phase) -> Animation? = { _ in .default }) -> some View where Phase : Equatable
```

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
timestamp: 2026-02-13T01:42:09.092Z
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

## transition(_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/transition(_:)?.md

**Contents:**
- Discussion
- Defining transitions

---
title: transition(_:)
description: Associates a transition with the view.
source: https://developer.apple.com/documentation/swiftui/view/transition(_:)
timestamp: 2026-02-13T01:42:06.867Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Associates a transition with the view.

When this view appears or disappears, the transition will be applied to it, allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or disappears, will use a slide transition to show it.

- [Transition](/documentation/swiftui/transition)
- [TransitionProperties](/documentation/swiftui/transitionproperties)
- [TransitionPhase](/documentation/swiftui/transitionphase)
- [AsymmetricTransition](/documentation/swiftui/asymmetrictransition)
- [AnyTransition](/documentation/swiftui/anytransition)
- [contentTransition(_:)](/documentation/swiftui/view/contenttransition(_:))
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
timestamp: 2026-02-13T01:42:04.769Z
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

## withAnimation(_:_:)

**URL:** https://sosumi.ai/documentation/swiftui/withanimation(_:_:)?.md

**Contents:**
- Discussion
- Adding state-based animation to an action

---
title: withAnimation(_:_:)
description: Returns the result of recomputing the view’s body with the provided animation.
source: https://developer.apple.com/documentation/swiftui/withanimation(_:_:)
timestamp: 2026-02-13T01:42:11.097Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

> Returns the result of recomputing the view’s body with the provided animation.

This function sets the given [Animation](/documentation/swiftui/animation) as the [animation](/documentation/swiftui/transaction/animation) property of the thread’s current [Transaction](/documentation/swiftui/transaction).

- [withAnimation(_:completionCriteria:_:completion:)](/documentation/swiftui/withanimation(_:completioncriteria:_:completion:))
- [AnimationCompletionCriteria](/documentation/swiftui/animationcompletioncriteria)
- [Animation](/documentation/swiftui/animation)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
func withAnimation<Result>(_ animation: Animation? = .default, _ body: () throws -> Result) rethrows -> Result
```

---

## task(priority:_:)

**URL:** https://sosumi.ai/documentation/swiftui/view/task(priority:_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion
- Responding to view life cycle updates

---
title: task(priority:_:)
description: Adds an asynchronous task to perform before this view appears.
source: https://developer.apple.com/documentation/swiftui/view/task(priority:_:)
timestamp: 2026-02-13T01:42:12.989Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> Adds an asynchronous task to perform before this view appears.

The task priority to use when creating the asynchronous task. The default priority is [user Initiated](/documentation/Swift/TaskPriority/userInitiated).

A closure that SwiftUI calls as an asynchronous task before the view appears. SwiftUI will automatically cancel the task at some point after the view disappears before the action completes.

A view that runs the specified action asynchronously before the view appears.

Use this modifier to perform an asynchronous task with a lifetime that matches that of the modified view. If the task doesn’t finish before SwiftUI removes the view or the view changes identity, SwiftUI cancels the task.

Use the `await` keyword inside the task to wait for an asynchronous call to complete, or to wait on the values of an [Async Sequence](/documentation/Swift/AsyncSequence) instance. For example, you can modify a [Text](/documentation/swiftui/text) view to start a task that loads content from a remote resource:

This example uses the [lines](/documentation/Foundation/URL/lines) method to get the content stored at the specified [URL](/documentation/Foundation/URL) as an asynchronous sequence of strings. When each new line arrives, the body of the `for`-`await`-`in` loop stores the line in an array of strings and updates the content of the text view to report the latest line count.

- [onAppear(perform:)](/documentation/swiftui/view/onappear(perform:))
- [onDisappear(perform:)](/documentation/swiftui/view/ondisappear(perform:))
- [task(id:priority:_:)](/documentation/swiftui/view/task(id:priority:_:))

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func task(priority: TaskPriority = .userInitiated, _ action: @escaping () async -> Void) -> some View
```

Example 2 (swift):
```swift
let url = URL(string: "https://example.com")!
@State private var message = "Loading..."

var body: some View {
    Text(message)
        .task {
            do {
                var receivedLines = [String]()
                for try await line in url.lines {
                    receivedLines.append(line)
                    message = "Received \(receivedLines.count) lines"
                }
            } catch {
                message = "Failed to load"
            }
        }
}
```

---

## TimelineView

**URL:** https://sosumi.ai/documentation/swiftui/timelineview?.md

**Contents:**
- Overview
- Conforms To
- Creating a timeline
- Deprecated symbols
- Initializers
- Updating a view on a schedule

---
title: TimelineView
description: A view that updates according to a schedule that you provide.
source: https://developer.apple.com/documentation/swiftui/timelineview
timestamp: 2026-02-13T01:43:01.692Z
---

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

> A view that updates according to a schedule that you provide.

A timeline view acts as a container with no appearance of its own. Instead, it redraws the content it contains at scheduled points in time. For example, you can update the face of an analog timer once per second:

The closure that creates the content receives an input of type [Context](/documentation/swiftui/timelineview/context) that you can use to customize the content’s appearance. The context includes the [date](/documentation/swiftui/timelineview/context/date) that triggered the update. In the example above, the timeline view sends that date to an analog timer that you create so the timer view knows how to draw the hands on its face.

The context also includes a [cadence-swift.property](/documentation/swiftui/timelineview/context/cadence-swift.property) property that you can use to hide unnecessary detail. For example, you can use the cadence to decide when it’s appropriate to display the timer’s second hand:

The system might use a cadence that’s slower than the schedule’s update rate. For example, a view on watchOS might remain visible when the user lowers their wrist, but update less frequently, and thus require less detail.

You can define a custom schedule by creating a type that conforms to the [Timeline Schedule](/documentation/swiftui/timelineschedule) protocol, or use one of the built-in schedule types:

- Use an [every Minute](/documentation/swiftui/timelineschedule/everyminute) schedule to update at the beginning of each minute.
- Use a [periodic(from:by:)](/documentation/swiftui/timelineschedule/periodic(from:by:)) schedule to update periodically with a custom start time and interval between updates.
- Use an [explicit(_:)](/documentation/swiftui/timelineschedule/explicit(_:)) schedule when you need a finite number, or irregular set of updates.

For a schedule containing only dates in the past, the timeline view shows the last date in the schedule. For a schedule containing only dates in the future, the timeline draws its content using the current date until the first scheduled date arrives.

- [Copyable](/documentation/Swift/Copyable)
- [View](/documentation/swiftui/view)

- [init(_:content:)](/documentation/swiftui/timelineview/init(_:content:)-1mlmj) Creates a new timeline view that uses the given schedule.
- [TimelineView.Context](/documentation/swiftui/timelineview/context) Information passed to a timeline view’s content callback.

- [init(_:content:)](/documentation/swiftui/timelineview/init(_:content:)-67h35) Creates a new timeline view that uses the given schedule.

- [init(_:content:)](/documentation/swiftui/timelineview/init(_:content:)) Creates a new timeline view that uses the given schedule.

- [Updating watchOS apps with timelines](/documentation/watchOS-Apps/updating-watchos-apps-with-timelines)
- [TimelineSchedule](/documentation/swiftui/timelineschedule)
- [TimelineViewDefaultContext](/documentation/swiftui/timelineviewdefaultcontext)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct TimelineView<Schedule, Content> where Schedule : TimelineSchedule
```

Example 2 (swift):
```swift
TimelineView(.periodic(from: startDate, by: 1)) { context in
    AnalogTimerView(date: context.date)
}
```

Example 3 (swift):
```swift
TimelineView(.periodic(from: startDate, by: 1.0)) { context in
    AnalogTimerView(
        date: context.date,
        showSeconds: context.cadence <= .seconds)
}
```

---

## onChange(of:perform:)

**URL:** https://sosumi.ai/documentation/swiftui/view/onchange(of:perform:)?.md

**Contents:**
- Discussion
- Input and events modifiers

---
title: onChange(of:perform:)
description: Adds an action to perform when the given value changes.
source: https://developer.apple.com/documentation/swiftui/view/onchange(of:perform:)
timestamp: 2026-02-13T01:42:16.872Z
---

**Navigation:** [Swiftui](/documentation/swiftui) › [view](/documentation/swiftui/view)

**Available on:** iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+

> Adds an action to perform when the given value changes.

Use this modifier to trigger a side effect when a value changes, like the value associated with an [Environment](/documentation/swiftui/environment) value or a [Binding](/documentation/swiftui/binding). For example, you can clear a cache when you notice that a scene moves to the background:

The system may call the action closure on the main actor, so avoid long-running tasks in the closure. If you need to perform such tasks, detach an asynchronous background task:

The system passes the new value into the closure. If you need the old value, capture it in the closure.

- [onTapGesture(count:coordinateSpace:perform:)](/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:)-36x9h)
- [onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)](/documentation/swiftui/view/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:))
- [onLongPressGesture(minimumDuration:pressing:perform:)](/documentation/swiftui/view/onlongpressgesture(minimumduration:pressing:perform:))
- [onPasteCommand(of:perform:)](/documentation/swiftui/view/onpastecommand(of:perform:)-4f78f)
- [onPasteCommand(of:validator:perform:)](/documentation/swiftui/view/onpastecommand(of:validator:perform:)-964k1)
- [onDrop(of:delegate:)](/documentation/swiftui/view/ondrop(of:delegate:)-2vr9o)
- [onDrop(of:isTargeted:perform:)](/documentation/swiftui/view/ondrop(of:istargeted:perform:))
- [focusable(_:onFocusChange:)](/documentation/swiftui/view/focusable(_:onfocuschange:))
- [onContinuousHover(coordinateSpace:perform:)](/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)-8gyrl)

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.*
*This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func onChange<V>(of value: V, perform action: @escaping (V) -> Void) -> some View where V : Equatable
```

Example 2 (swift):
```swift
struct MyScene: Scene {
    @Environment(\.scenePhase) private var scenePhase
    @StateObject private var cache = DataCache()

    var body: some Scene {
        WindowGroup {
            MyRootView()
        }
        .onChange(of: scenePhase) { newScenePhase in
            if newScenePhase == .background {
                cache.empty()
            }
        }
    }
}
```

Example 3 (swift):
```swift
.onChange(of: scenePhase) { newScenePhase in
    if newScenePhase == .background {
        Task.detached(priority: .background) {
            // ...
        }
    }
}
```

---
