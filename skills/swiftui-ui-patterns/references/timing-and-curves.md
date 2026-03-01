# Swiftui-Animations - Timing And Curves

**Pages:** 2

---

## UnitCurve

**URL:** https://sosumi.ai/documentation/swiftui/unitcurve?.md

**Contents:**
- Overview
- Conforms To
- Getting a linear curve
- Getting easing curves
- Creating a general Bezier curve
- Inverting a curve
- Getting curve characteristics
- Deprecated symbols
- Creating custom animations

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

The horizontal (x) axis defines the input progress: a single input progress value in the range [0,1] must be provided when evaluating a curve.

The vertical (y) axis maps to the output progress: when a curve is evaluated, the y component of the point that intersects the input progress is returned.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct UnitCurve
```

---

## Spring

**URL:** https://sosumi.ai/documentation/swiftui/spring?.md

**Contents:**
- Overview
- Conforms To
- Creating a spring
- Getting built-in springs
- Getting spring characteristics
- Getting spring state
- Setting spring state
- Calculating forces and durations
- Creating custom animations

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+

Use this type to convert between different representations of spring parameters:

You can also use it to query for a spring’s position and its other properties for a given set of inputs:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct Spring
```

Example 2 (swift):
```swift
let spring = Spring(duration: 0.5, bounce: 0.3)
let (mass, stiffness, damping) = (spring.mass, spring.stiffness, spring.damping)
// (1.0, 157.9, 17.6)

let spring2 = Spring(mass: 1, stiffness: 100, damping: 10)
let (duration, bounce) = (spring2.duration, spring2.bounce)
// (0.63, 0.5)
```

Example 3 (swift):
```swift
func unitPosition(time: TimeInterval) -> Double {
    let spring = Spring(duration: 0.5, bounce: 0.3)
    return spring.position(target: 1.0, time: time)
}
```

---
