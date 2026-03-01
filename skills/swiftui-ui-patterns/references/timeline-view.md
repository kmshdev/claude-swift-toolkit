# Swiftui-Animations - Timeline View

**Pages:** 3

---

## TimelineSchedule

**URL:** https://sosumi.ai/documentation/swiftui/timelineschedule?.md

**Contents:**
- Overview
- Conforming Types
- Getting built-in schedules
- Getting a sequence of dates
- Specifying a mode
- Supporting types
- Updating a view on a schedule

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

Types that conform to this protocol implement a particular kind of schedule by defining an [entries(from:mode:)](/documentation/swiftui/timelineschedule/entries(from:mode:)) method that returns a sequence of dates. Use a timeline schedule type when you initialize a [Timeline View](/documentation/swiftui/timelineview). For example, you can create a timeline view that updates every second, starting from some `startDate`, using a periodic schedule returned by [periodic(from:by:)](/documentation/swiftui/timelineschedule/periodic(from:by:)):

You can also create custom timeline schedules. The timeline view updates its content according to the sequence of dates produced by the schedule.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol TimelineSchedule
```

Example 2 (swift):
```swift
TimelineView(.periodic(from: startDate, by: 1.0)) { context in
    // View content goes here.
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

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

A timeline view acts as a container with no appearance of its own. Instead, it redraws the content it contains at scheduled points in time. For example, you can update the face of an analog timer once per second:

The closure that creates the content receives an input of type [Context](/documentation/swiftui/timelineview/context) that you can use to customize the content’s appearance. The context includes the [date](/documentation/swiftui/timelineview/context/date) that triggered the update. In the example above, the timeline view sends that date to an analog timer that you create so the timer view knows how to draw the hands on its face.

The context also includes a [cadence-swift.property](/documentation/swiftui/timelineview/context/cadence-swift.property) property that you can use to hide unnecessary detail. For example, you can use the cadence to decide when it’s appropriate to display the timer’s second hand:

The system might use a cadence that’s slower than the schedule’s update rate. For example, a view on watchOS might remain visible when the user lowers their wrist, but update less frequently, and thus require less detail.

You can define a custom schedule by creating a type that conforms to the [Timeline Schedule](/documentation/swiftui/timelineschedule) protocol, or use one of the built-in schedule types:

For a schedule containing only dates in the past, the timeline view shows the last date in the schedule. For a schedule containing only dates in the future, the timeline draws its content using the current date until the first scheduled date arrives.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

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

## TimelineViewDefaultContext

**URL:** https://sosumi.ai/documentation/swiftui/timelineviewdefaultcontext?.md

**Contents:**
- Discussion
- Updating a view on a schedule

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

The context includes both the date from the schedule that triggered the callback, and a cadence that you can use to customize the appearance of your view. For example, you might choose to display the second hand of an analog clock only when the cadence is [seconds](/documentation/swiftui/timelineview/context/cadence-swift.enum/seconds) or faster.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
typealias TimelineViewDefaultContext = TimelineView<EveryMinuteTimelineSchedule, Never>.Context
```

---
