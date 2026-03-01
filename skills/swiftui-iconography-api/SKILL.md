---
name: swiftui-iconography-api
description: This skill should be used when the user asks to "add SF Symbols", "animate icons", "use symbol effects", "apply symbol rendering mode", "add bounce/pulse effect", or needs SwiftUI iconography API reference. Provides SF Symbols usage, rendering modes (monochrome, hierarchical, multicolor, palette), symbol effects, and variable values.
---

# SF Symbols & Iconography API Reference

## Lifecycle Position

Phase 3 API Reference — load during implementation when using SF Symbols or custom icons. Dispatched from `autonomous-ui-workflow` Phase 2 research table.

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

## When to Use Which

| Need | Use |
|------|-----|
| Standard system icon | `Image(systemName: "star.fill")` |
| Icon with accessible label | `Label("Favorites", systemImage: "star.fill")` (preferred in buttons/toolbars) |
| Icon matching adjacent text weight | `.fontWeight(.semibold)` on Image to match Text |
| Animated symbol feedback | `.symbolEffect(.bounce, value: trigger)` |
| Progress/level indicator | `Image(systemName: "wifi", variableValue: 0.5)` |
| Multi-color system icon | `.symbolRenderingMode(.multicolor)` |
| Icon tinted to match theme | `.symbolRenderingMode(.palette)` with `foregroundStyle(.red, .blue)` |
| Custom app icon | Asset catalog → Symbol Image Set → export from SF Symbols app |

## Common Mistakes

1. `Image(systemName:)` without `Label` in buttons — no accessibility text for VoiceOver
2. Mismatched symbol weight with adjacent text — icons look too thin/thick next to text. Match with `.fontWeight()` or `.imageScale()`
3. Using `.resizable().frame()` for sizing instead of `.font()` — breaks alignment with text. Use `.font(.title)` to match text size
4. Missing `.symbolRenderingMode()` — defaults to monochrome which may not match design intent
5. Hardcoded symbol names without checking SF Symbols availability — some symbols require iOS 16+ or 17+

**Before (incorrect):**
```swift
Button(action: addFavorite) {
    Image(systemName: "star.fill")  // no label — VoiceOver reads nothing useful
}
```

**After (correct):**
```swift
Button(action: addFavorite) {
    Label("Add to Favorites", systemImage: "star.fill")
}
```

**Before (incorrect):**
```swift
Image(systemName: "heart.fill")
    .resizable()
    .frame(width: 24, height: 24)  // disrupts text baseline alignment
```

**After (correct):**
```swift
Image(systemName: "heart.fill")
    .font(.title2)  // scales with Dynamic Type and aligns with text
```

## Checklist

- [ ] Buttons and toolbar items use `Label("text", systemImage:)` not bare `Image`
- [ ] Icon weight matches adjacent text weight
- [ ] Icon sizing uses `.font()` or `.imageScale()` not `.resizable().frame()`
- [ ] Rendering mode explicitly set when multicolor or palette needed
- [ ] Symbol availability checked for newer symbols (`@available`)

## Cross-References

- `swiftui-colors-api` — `foregroundStyle()` for symbol tinting
- `swiftui-ui-patterns` — review checklist includes accessibility label checks
- `macos-app-design` — macOS toolbar icon conventions
