---
name: swiftui-iconography-api
description: Use when working with SF Symbols, symbol rendering modes, symbol effects, variable values, or custom icon images in SwiftUI - covers monochrome, hierarchical, multicolor, palette rendering and bounce, pulse, appear effects
---

# SF Symbols & Iconography API Reference

## Quick Reference

| API | Purpose |
|-----|---------|
| `Image(systemName:)` | System SF Symbol |
| `Image(systemName:variableValue:)` | Symbol with 0.0-1.0 value |
| `.symbolRenderingMode(_:)` | Set rendering mode |
| `.symbolVariant(_:)` | Add variant (.fill, .circle) |
| `.symbolEffect(_:)` | Animate symbol |
| `.foregroundStyle(_:_:)` | Palette colors (implies palette mode) |

## Rendering Modes

| Mode | Usage |
|------|-------|
| `.monochrome` | Single color: `.symbolRenderingMode(.monochrome).foregroundStyle(.purple)` |
| `.hierarchical` | Layered opacity: `.symbolRenderingMode(.hierarchical).foregroundStyle(.purple)` |
| `.multicolor` | Inherent colors: `.symbolRenderingMode(.multicolor)` |
| `.palette` | Custom per-layer: `.foregroundStyle(.yellow, .cyan)` |

## Symbol Effects

```swift
// Indefinite (repeating)
Image(systemName: "bolt.slash.fill").symbolEffect(.pulse)

// Active/inactive
Image(systemName: "wifi").symbolEffect(.pulse, isActive: isConnecting)

// Value-driven
Image(systemName: "bell").symbolEffect(.bounce, value: count)

// As transition
.transition(.symbolEffect(.appear))
```

## Variable Values

```swift
Image(systemName: "chart.bar.fill", variableValue: 0.3)  // partial
Image(systemName: "chart.bar.fill", variableValue: 1.0)  // full
```
