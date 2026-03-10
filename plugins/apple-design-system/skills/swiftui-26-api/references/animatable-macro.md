# @Animatable Macro
Macro for auto-synthesizing animatableData on Shape types. Use @AnimatableIgnored to exclude non-animatable properties.

## Animatable()

**URL:** https://sosumi.ai/documentation/SwiftUI/Animatable()?.md

**Contents:**
- Overview
- Animating data

**Navigation:** [SwiftUI](/documentation/SwiftUI)

**Available on:** iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+

In the above code, `animatableData` will be synthesized using `width` and `angle` properties of `CoolShape` structure.  Since changes to `isOpaque` property cannot be animated, it is annotated with `@AnimatableIgnored`.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
@attached(extension, conformances: Animatable) @attached(member, names: named(animatableData)) macro Animatable()
```

Example 2 (swift):
```swift
@Animatable
struct CoolShape: Shape {
    var width: CGFloat
    var angle: Angle
    @AnimatableIgnored var isOpaque: Bool

    // ...
}
```

## Migration: Manual animatableData → @Animatable Macro

**Why migrate:** Eliminates manual `animatableData` boilerplate. Macro handles `VectorArithmetic` synthesis automatically.

**Before:** Manual animatableData implementation
```swift
struct MyShape: Shape {
    var progress: CGFloat
    var animatableData: CGFloat {
        get { progress }
        set { progress = newValue }
    }
}
```

**After:** @Animatable macro
```swift
@Animatable
struct MyShape: Shape {
    var progress: CGFloat
    @AnimatableIgnored var isActive: Bool
    // animatableData auto-synthesized from progress
}
```

**Gotcha:** All stored properties must be `VectorArithmetic`-conforming or marked `@AnimatableIgnored`. Forgetting the annotation causes a compiler error.

## Anti-Pattern

| Don't | What Happens | Do Instead |
|-------|-------------|-----------|
| Omit `@AnimatableIgnored` on non-numeric properties | Compiler error — macro tries to synthesize from all stored properties | Mark `Bool`, `String`, and non-`VectorArithmetic` properties with `@AnimatableIgnored` |

## Reading Paths

**Path F — Custom Animation (this file is step 1):**
Next → `apple-liquid-glass-design` skill (if animating glass shapes)
