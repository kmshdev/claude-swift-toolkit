---
name: swiftui-material-api
description: This skill should be used when the user asks to "add material background", "apply translucent overlay", "use .regularMaterial", "choose material thickness", "work with shapes", or needs SwiftUI material and structure API reference. Provides material types (ultraThin to ultraThick), shapes (Rectangle, Capsule, Circle), and layout containers.
---

# Material & Structure API Reference

## Lifecycle Position

Phase 3 API Reference — load during implementation when working with materials, shapes, or container backgrounds. Dispatched from `autonomous-ui-workflow` Phase 2 research table.

## Material Types

| Material | Translucency | Usage |
|----------|-------------|-------|
| `.ultraThinMaterial` | Mostly translucent | Subtle overlays |
| `.thinMaterial` | More translucent | Light overlays |
| `.regularMaterial` | Somewhat translucent | Standard overlays |
| `.thickMaterial` | More opaque | Heavy overlays |
| `.ultraThickMaterial` | Mostly opaque | Dense overlays |
| `.bar` | System toolbar style | Toolbars, nav bars |

```swift
Text("Hello").padding().background(.regularMaterial)
Rectangle().fill(.thickMaterial)
```

## macOS Active Appearance

```swift
Text("Hello").containerBackground(
    Material.regular.materialActiveAppearance(.active), for: .window)
```

Default: `window` + `bar` materials appear inactive when window inactive. Others always active.

## Shapes

| Shape | Notes |
|-------|-------|
| `Rectangle` | Fills frame |
| `RoundedRectangle(cornerRadius:)` | Rounded corners |
| `UnevenRoundedRectangle` | Different corner radii |
| `Capsule` | Pill shape |
| `Circle` | Perfect circle |
| `Ellipse` | Oval |
| `Path` | Custom 2D outline |
| `ContainerRelativeShape` | Matches container |

## Layout Containers

**Stacks:** `HStack`, `VStack`, `ZStack`, `HSplitView`, `VSplitView`
**Grids:** `Grid`+`GridRow`, `LazyHGrid`, `LazyVGrid`
**Lists:** `List`, `Form`, `ScrollView`+`ScrollViewReader`
**Navigation:** `NavigationSplitView`, `NavigationStack`, `TabView`

## When to Use Which

| Material | When to Use |
|----------|-------------|
| `.ultraThinMaterial` | Overlays where content behind must be clearly visible (e.g., floating controls, HUD) |
| `.thinMaterial` | Sidebars, toolbars where partial visibility is wanted |
| `.regularMaterial` | Default cards, popovers, general surfaces |
| `.thickMaterial` | High-contrast surfaces where readability is critical |
| `.ultraThickMaterial` | Opaque-like surfaces that still respond to dark/light mode |
| `.bar` | Navigation bars, tab bars, toolbars (system-matched) |

## Background Patterns

```swift
// Shape-clipped background (preferred for cards)
.background(.regularMaterial, in: RoundedRectangle(cornerRadius: 12))

// Full-bleed background
.background(.thinMaterial)

// Widget/Live Activity container background
.containerBackground(.thickMaterial, for: .widget)

// Stroke vs strokeBorder
RoundedRectangle(cornerRadius: 12)
    .stroke(.blue, lineWidth: 2)      // Straddles the edge (half inside, half outside)
RoundedRectangle(cornerRadius: 12)
    .strokeBorder(.blue, lineWidth: 2) // Entirely inside the shape
```

## Common Mistakes

1. Material without sufficient text contrast — always test both light and dark mode. Add `.shadow()` to text if needed
2. `background(.regularMaterial)` without shape parameter — no corner radius clipping. Use `background(_:in:)` variant
3. Using `clipShape()` + `background()` separately instead of `background(_:in:)` — the `in:` parameter handles clipping
4. `stroke()` when `strokeBorder()` is intended — stroke bleeds outside the frame by half the line width
5. Applying material to views inside `ScrollView` without `drawingGroup()` — performance cost compounds

## Checklist

- [ ] Material thickness matches content importance (thicker = more readable)
- [ ] Using `background(_:in:)` with shape for clipped material backgrounds
- [ ] `strokeBorder` used instead of `stroke` when border must stay inside frame
- [ ] Materials tested in both light and dark mode
- [ ] Widget backgrounds use `containerBackground(_:for:)` not `background()`

## Cross-References

- `apple-liquid-glass-design` — Liquid Glass replaces materials in many cases on iOS 26+
- `swiftui-effects-api` — blur and shadow effects that complement materials
- `swiftui-colors-api` — colors layered under/over materials
