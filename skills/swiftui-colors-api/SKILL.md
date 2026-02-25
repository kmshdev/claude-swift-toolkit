---
name: swiftui-colors-api
description: This skill should be used when the user asks to "style with colors", "apply gradients", "use foregroundStyle", "add linear/radial gradient", "set tint color", or needs SwiftUI color and ShapeStyle API reference. Provides Color usage, foregroundStyle with hierarchical levels, gradients, system colors, and custom ShapeStyle patterns.
---

# Colors & ShapeStyle API Reference

## Lifecycle Position

Phase 3 API Reference — load during implementation when working with colors, gradients, or tints. Dispatched from `autonomous-ui-workflow` Phase 2 research table.

## Foreground Styling

```swift
.foregroundStyle(.teal)                          // single
.foregroundStyle(.blue, .gray)                   // primary + secondary
.foregroundStyle(.blue, .gray, .gray.opacity(0.5))  // + tertiary
```

Hierarchical: `.primary`, `.secondary`, `.tertiary`, `.quaternary`

## System Colors

`.black`, `.blue`, `.brown`, `.clear`, `.cyan`, `.gray`, `.green`, `.indigo`, `.mint`, `.orange`, `.pink`, `.purple`, `.red`, `.teal`, `.white`, `.yellow`

## Tint

```swift
Button("Answer") { }.tint(.green)
Gauge(value: 75, in: 0...100) { }.tint(Gradient(colors: [.blue, .red]))
```

## Background

```swift
.background(.regularMaterial)
.backgroundStyle(.blue.gradient)
Image(systemName: "swift").padding().background(in: Circle()).backgroundStyle(.blue.gradient)
```

## Gradients

```swift
.linearGradient(colors: [.yellow, .blue], startPoint: .top, endPoint: .bottom)
.radialGradient(Gradient(colors: [.yellow, .red]), center: .topLeading, startRadius: 15, endRadius: 80)
Color.blue.gradient  // standard gradient from color
```

## Color Modifiers

```swift
Color.blue.opacity(0.5)
Color.red.mix(with: .blue, by: 0.5)
```

## Custom ShapeStyle

```swift
struct MyStyle: ShapeStyle {
    func resolve(in environment: EnvironmentValues) -> some ShapeStyle {
        environment.colorScheme == .light ? Color.red.blendMode(.lighten) : Color.red.blendMode(.darken)
    }
}
```

## When to Use Which

| Need | Use |
|------|-----|
| Text, icons that adapt to dark mode | `foregroundStyle(.primary)`, `.secondary`, `.tertiary` |
| Brand colors shared across views | Asset catalog `Color("BrandRed")` |
| Tinting interactive elements | `.tint(.accentColor)` |
| Multi-color text/icon styling | `foregroundStyle(.red, .blue, .green)` (primary, secondary, tertiary) |
| Gradient backgrounds | `LinearGradient`, `RadialGradient`, `AngularGradient`, or `.gradient` suffix |
| Platform-bridged colors | `Color(nsColor:)` for macOS, `Color(uiColor:)` for iOS |
| Dynamic color based on scheme | `@Environment(\.colorScheme)` with conditional |

## Common Mistakes

1. Using `Color.black`/`Color.white` instead of `.primary`/semantic colors — breaks in dark mode
2. Hardcoding hex colors instead of asset catalog — no dark mode variant, no accessibility
3. Using `foregroundColor()` instead of `foregroundStyle()` — deprecated API
4. Applying `.tint()` and `.foregroundStyle()` together — tint overrides foregroundStyle on controls
5. Missing `.opacity()` consideration — semantic colors already have built-in opacity levels

**Before (incorrect):**
```swift
Text("Hello")
    .foregroundColor(.black)  // deprecated, breaks dark mode
```

**After (correct):**
```swift
Text("Hello")
    .foregroundStyle(.primary)  // adapts to dark mode automatically
```

**Before (incorrect):**
```swift
Color(hex: "#FF3B30")  // hardcoded, no dark mode variant
```

**After (correct):**
```swift
Color("BrandRed")  // defined in asset catalog with Light/Dark variants
```

## Checklist

- [ ] No hardcoded `Color.black`/`Color.white` for text or backgrounds
- [ ] Using `foregroundStyle()` not `foregroundColor()`
- [ ] Brand colors defined in asset catalog with dark mode variants
- [ ] Gradient direction matches reading direction (leading → trailing)
- [ ] Color contrast meets WCAG AA (4.5:1 for normal text, 3:1 for large text)

## Cross-References

- `swiftui-effects-api` — blur, shadow, opacity effects that interact with colors
- `swiftui-material-api` — material backgrounds that adapt to underlying colors
- `swiftui-expert-skill` — modern API checklist includes `foregroundStyle()` migration
