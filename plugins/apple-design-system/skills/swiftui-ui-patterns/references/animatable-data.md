# Swiftui-Animations - Animatable Data

**Pages:** 5

---

## VectorArithmetic

**URL:** https://sosumi.ai/documentation/swiftui/vectorarithmetic?.md

**Contents:**
- Overview
- Inherits From
- Conforming Types
- Manipulating values
- Making data animatable

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

`VectorArithmetic` extends the `AdditiveArithmetic` protocol with scalar multiplication and a way to query the vector magnitude of the value. Use this type as the `animatableData` associated type of a type that conforms to the [Animatable](/documentation/swiftui/animatable) protocol.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol VectorArithmetic : AdditiveArithmetic
```

---

## Animatable

**URL:** https://sosumi.ai/documentation/swiftui/animatable?.md

**Contents:**
- Inherited By
- Conforming Types
- Animating data
- Making data animatable

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
protocol Animatable
```

---

## AnimatableValues

**URL:** https://sosumi.ai/documentation/swiftui/animatablevalues?.md

**Contents:**
- Conforms To
- Initializers
- Instance Properties
- Making data animatable

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct AnimatableValues<each Value> where repeat each Value : VectorArithmetic
```

---

## EmptyAnimatableData

**URL:** https://sosumi.ai/documentation/swiftui/emptyanimatabledata?.md

**Contents:**
- Overview
- Conforms To
- Creating the data
- Manipulating the data
- Making data animatable

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

This type is suitable for use as the `animatableData` property of types that do not have any animatable properties.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct EmptyAnimatableData
```

---

## AnimatablePair

**URL:** https://sosumi.ai/documentation/swiftui/animatablepair?.md

**Contents:**
- Conforms To
- Creating an animatable pair
- Getting the constituent animations
- Manipulating values
- Making data animatable

**Navigation:** [Swiftui](/documentation/swiftui)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@frozen struct AnimatablePair<First, Second> where First : VectorArithmetic, Second : VectorArithmetic
```

---
