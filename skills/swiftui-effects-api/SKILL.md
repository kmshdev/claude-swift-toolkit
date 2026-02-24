---
name: swiftui-effects-api
description: Use when applying visual effects like blur, shadow, opacity, brightness, contrast, saturation, grayscale, or blend modes in SwiftUI - covers view graphical modifiers, VisualEffect protocol for geometry-safe effects, GraphicsContext blend modes, and Canvas drawing
---

# Visual Effects API Reference

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
