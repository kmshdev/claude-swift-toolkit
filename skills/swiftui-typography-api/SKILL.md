---
name: swiftui-typography-api
description: Use when setting fonts, text styles, weights, custom fonts, or Dynamic Type in SwiftUI - covers Font.TextStyle, Font.Design (serif, rounded, monospaced), Font.Weight, custom font registration, and ScaledMetric for adaptive sizing
---

# Typography API Reference

## System Text Styles

```swift
.font(.largeTitle)  .font(.title)    .font(.title2)   .font(.title3)
.font(.headline)    .font(.subheadline)  .font(.body)   .font(.callout)
.font(.footnote)    .font(.caption)  .font(.caption2)
```

## System Font with Design/Weight

```swift
.font(.system(.body, design: .serif, weight: .bold))
.font(.system(size: 17, weight: .semibold))
.font(.system(size: 17, weight: .bold, design: .serif))
```

**Designs:** `.default` (SF Pro), `.monospaced` (SF Mono), `.rounded`, `.serif` (New York)
**Weights:** `.ultraLight`, `.thin`, `.light`, `.regular`, `.medium`, `.semibold`, `.bold`, `.heavy`, `.black`

## Custom Fonts

```swift
.font(.custom("MyFont", size: 18))                      // scales with body
.font(.custom("MyFont", size: 32, relativeTo: .title))  // scales with title
.font(.custom("MyFont", fixedSize: 18))                  // no scaling
```

## Text Style Modifiers

| Modifier | Purpose |
|----------|---------|
| `.font(_:)` | Set font |
| `.fontDesign(_:)` | Font design |
| `.fontWeight(_:)` | Font weight |
| `.fontWidth(_:)` | Font width |
| `.bold()` | Bold |
| `.italic()` | Italic |
| `.monospaced()` | Fixed-width |
| `.monospacedDigit()` | Fixed-width digits only |
| `.strikethrough()` | Strikethrough |
| `.underline()` | Underline |
| `.textCase(_:)` | Transform case |

## Adaptive Sizing

```swift
@ScaledMetric(relativeTo: .body) var iconSize: CGFloat = 24
```
