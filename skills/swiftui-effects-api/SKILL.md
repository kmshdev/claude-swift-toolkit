---
name: swiftui-effects-api
description: This skill should be used when the user asks to "add blur effect", "apply shadow", "adjust opacity/brightness", "use blend modes", "create visual effects", or needs SwiftUI visual effects API reference. Provides view modifiers (blur, shadow, opacity), VisualEffect protocol, blend modes, and Canvas drawing.
---

# Visual Effects API Reference

## Lifecycle Position

Phase 3 API Reference — load during implementation when adding visual effects. Dispatched from `autonomous-ui-workflow` Phase 2 research table.

## View Modifiers

| Modifier | Purpose |
|----------|---------|
| `.blur(radius:opaque:)` | Gaussian blur |
| `.opacity(_:)` | Transparency (0-1) |
| `.brightness(_:)` | Brighten |
| `.contrast(_:)` | Adjust contrast |
| `.saturation(_:)` | Adjust saturation |
| `.grayscale(_:)` | Grayscale |
| `.hueRotation(_:)` | Rotate hue by angle |
| `.colorInvert()` | Invert colors |
| `.colorMultiply(_:)` | Multiply by color |
| `.luminanceToAlpha()` | Luminance to alpha |
| `.shadow(color:radius:x:y:)` | Drop shadow |

## VisualEffect (Geometry-Safe)

```swift
ContentRow()
    .visualEffect { content, proxy in
        content.offset(x: proxy.frame(in: .global).origin.y)
    }
```

Methods: `.blur()`, `.opacity()`, `.brightness()`, `.contrast()`, `.saturation()`, `.grayscale()`, `.hueRotation()`, `.colorEffect(shader:)`, `.distortionEffect(shader:)`, `.layerEffect(shader:)`

## Blend Modes

**Darken:** `.darken`, `.multiply`, `.colorBurn`, `.plusDarker`
**Lighten:** `.lighten`, `.screen`, `.colorDodge`, `.plusLighter`
**Contrast:** `.overlay`, `.softLight`, `.hardLight`
**Mix:** `.hue`, `.saturation`, `.color`, `.luminosity`

## Canvas (Immediate Mode)

```swift
Canvas { context, size in
    context.opacity = 0.5
    context.blendMode = .multiply
    context.fill(path, with: .color(.blue))
    context.addFilter(.blur(radius: 5))
    context.addFilter(.shadow(color: .black, radius: 3))
}
```

## When to Use Which

| Need | Use |
|------|-----|
| Frosted glass look | `.ultraThinMaterial` (see `swiftui-material-api`) or `.blur(radius:)` on background |
| Drop shadow on card/element | `.shadow(color:radius:x:y:)` |
| Inner glow/shadow | `overlay` with blurred shape |
| Complex custom drawing | `Canvas { context, size in }` with `drawingGroup()` |
| Animated visual effect | `.visualEffect { content, proxy in }` for geometry-aware transforms |
| GPU shader effects | `.colorEffect()`, `.distortionEffect()`, `.layerEffect()` |
| Compositing/blending | `.blendMode(.overlay)`, `.compositingGroup()` |

## Performance Cost Ranking

```
Cheapest → Most Expensive:
opacity → shadow → blur(small radius) → Canvas → blur(large radius) → Metal shaders
```

- Blur at radius > 20 is expensive — avoid in ScrollView rows
- Shadow on every list cell adds up — consider `drawingGroup()` for complex cells
- Canvas is faster than equivalent modifier stacks for 10+ shapes
- Always use `drawingGroup()` before Metal shader modifiers

## Common Mistakes

1. `.blur(radius: 50)` on every list row — kills scroll performance. Use sparingly or cache
2. Shadow on every cell without `drawingGroup()` — each shadow is a separate render pass
3. Canvas without `drawingGroup()` — doesn't rasterize to offscreen buffer, loses performance benefit
4. `.visualEffect` with layout-changing transforms — only use for visual transforms (scale, offset, opacity), not frame changes
5. Applying `.blendMode()` without `.compositingGroup()` — blend mode leaks to parent unless grouped

**Before (incorrect):**
```swift
// In a List or ScrollView row:
CardView()
    .blur(radius: 30)  // expensive, applied every frame per cell
```

**After (correct):**
```swift
// Apply blur outside ScrollView, or use material instead:
CardView()
    .background(.ultraThinMaterial)  // system-optimized frosted glass
```

**Before (incorrect):**
```swift
Text("Overlay")
    .blendMode(.overlay)  // leaks blend mode to parent layer
```

**After (correct):**
```swift
Text("Overlay")
    .blendMode(.overlay)
    .compositingGroup()  // isolates blend to this view's layer
```

## Checklist

- [ ] No blur in ScrollView/List row views (or explicitly justified)
- [ ] Canvas views use `drawingGroup()` for complex drawing
- [ ] `visualEffect` only uses visual transforms (not layout)
- [ ] `.compositingGroup()` wraps views using `.blendMode()`
- [ ] Metal shader effects gated with `#available` check

## Cross-References

- `swiftui-material-api` — material backgrounds (preferred over manual blur for frosted glass)
- `swiftui-colors-api` — colors used in gradients and Canvas drawing
- `apple-liquid-glass-design` — Liquid Glass effects (separate from standard SwiftUI effects)
