---
name: swiftui-liquid-glass-api
description: This skill should be used when the user asks to "add glass effects", "implement Liquid Glass", "use .glassEffect modifier", "create glass buttons", "morph glass shapes", or needs SwiftUI Liquid Glass API reference for macOS 26. Provides glass effect patterns, GlassEffectContainer usage, morph transitions, and performance optimization.
---

# Liquid Glass API Reference

## Quick Reference

| API | Purpose |
|-----|---------|
| `.glassEffect()` | Apply Liquid Glass (default: `.regular` + `Capsule`) |
| `.glassEffect(in: .rect(cornerRadius: 16))` | Custom shape |
| `.glassEffect(.regular.tint(.orange).interactive())` | Tinted + interactive |
| `GlassEffectContainer(spacing:)` | Combine + morph multiple shapes |
| `.glassEffectID(_:in:)` | Identity for morph transitions |
| `.glassEffectUnion(id:namespace:)` | Merge geometries into one capsule |
| `.buttonStyle(.glass)` | Glass button style |
| `.buttonStyle(.glassProminent)` | Prominent glass button |

## Glass Variants

- `.regular` — Standard Liquid Glass
- `.clear` — Clear variant
- `.identity` — No effect (passthrough)

## Apply Effects

```swift
Text("Hello").font(.title).padding().glassEffect()
Text("Hello").font(.title).padding().glassEffect(in: .rect(cornerRadius: 16.0))
Text("Hello").font(.title).padding().glassEffect(.regular.tint(.orange).interactive())
```

## Container (Combine + Morph)

```swift
GlassEffectContainer(spacing: 40.0) {
    HStack(spacing: 40.0) {
        Image(systemName: "scribble.variable")
            .frame(width: 80, height: 80).font(.system(size: 36))
            .glassEffect()
        Image(systemName: "eraser.fill")
            .frame(width: 80, height: 80).font(.system(size: 36))
            .glassEffect()
    }
}
```

**Spacing:** Larger = shapes blend sooner. Container spacing > layout spacing = blend at rest.

## Morph Transitions

```swift
@Namespace private var namespace

GlassEffectContainer(spacing: 40.0) {
    HStack(spacing: 40.0) {
        Image(systemName: "pencil").glassEffect().glassEffectID("pencil", in: namespace)
        if isExpanded {
            Image(systemName: "eraser").glassEffect().glassEffectID("eraser", in: namespace)
        }
    }
}
Button("Toggle") { withAnimation { isExpanded.toggle() } }.buttonStyle(.glass)
```

**Transitions:** `.matchedGeometry` (nearby, default), `.materialize` (distant, fade)

## Union (Merge Geometries)

```swift
.glassEffect().glassEffectUnion(id: groupID, namespace: namespace)
```

## Performance

Limit glass effects onscreen. Use `GlassEffectContainer` to combine. Too many standalone effects degrades rendering.
