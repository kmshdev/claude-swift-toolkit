---
name: swiftui-typography-api
description: This skill should be used when the user asks to "set font", "use text styles", "apply font weight", "use custom fonts", "implement Dynamic Type", or needs SwiftUI typography API reference. Provides Font.TextStyle, Font.Design (serif, rounded, monospaced), Font.Weight, custom font usage, and ScaledMetric for adaptive sizing.
---

# Typography API Reference

## Lifecycle Position

Phase 3 API Reference — load during implementation when working with fonts, text styles, or text layout. Dispatched from `autonomous-ui-workflow` Phase 2 research table.

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

## When to Use Which

| Need | Use |
|------|-----|
| Primary content text | `.font(.body)` |
| Section headers | `.font(.headline)` or `.font(.title3)` |
| Screen titles | `.font(.largeTitle)` or `.font(.title)` |
| Secondary/metadata text | `.font(.subheadline)` or `.font(.caption)` |
| Monospaced code/data | `.font(.body.monospaced())` or `.monospaced()` |
| Custom sized text that scales | `@ScaledMetric(relativeTo: .body) var size = 16` |
| Rich text with formatting | `Text("**bold** and *italic*")` (markdown in Text) |
| Attributed text | `Text(attributedString)` with `AttributedString` |

## Text Layout Control

```swift
// Truncation
Text(longString)
    .lineLimit(2)
    .truncationMode(.tail)  // Default; also .head, .middle

// Line spacing
Text(paragraph)
    .lineSpacing(4)

// Selectable text (macOS, iOS 15+)
Text(content)
    .textSelection(.enabled)

// Dynamic Type floor (prevent text from getting too small)
Text("Label")
    .font(.caption)
    .minimumScaleFactor(0.8)  // Won't shrink below 80% of font size
```

## HIG Style Pairing Guide

| UI Element | Recommended Style |
|------------|-------------------|
| Navigation bar title | `.largeTitle` or `.headline` |
| List row primary text | `.body` |
| List row secondary text | `.subheadline` with `.foregroundStyle(.secondary)` |
| Toolbar button labels | `.body` (system default) |
| Badges/counts | `.caption2` or `.footnote` |
| Empty state message | `.title3` with `.foregroundStyle(.secondary)` |

## Common Mistakes

1. Hardcoded font sizes (`.font(.system(size: 14))`) — breaks Dynamic Type. Use system text styles
2. `.lineLimit(1)` without `.truncationMode()` — defaults to tail truncation which may not be intended
3. Missing `minimumScaleFactor` on constrained labels — text disappears instead of shrinking
4. Using `String(format:)` instead of `Text(value, format:)` — misses localization and accessibility
5. Custom fonts without `@ScaledMetric` spacing — font scales but surrounding spacing doesn't

## Checklist

- [ ] No hardcoded font sizes — using system text styles (`.body`, `.headline`, etc.)
- [ ] `lineLimit` paired with `truncationMode` when truncation matters
- [ ] `minimumScaleFactor` set on space-constrained labels
- [ ] `@ScaledMetric` used for custom spacing that should scale with Dynamic Type
- [ ] Number/date display uses `Text(value, format:)` not string formatting

## Cross-References

- `swiftui-colors-api` — `foregroundStyle()` for text color
- `swiftui-iconography-api` — matching icon weight with text weight
- `swiftui-ui-patterns` — modern text formatting patterns
