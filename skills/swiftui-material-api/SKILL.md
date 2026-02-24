---
name: swiftui-material-api
description: This skill should be used when the user asks to "add material background", "apply translucent overlay", "use .regularMaterial", "choose material thickness", "work with shapes", or needs SwiftUI material and structure API reference. Provides material types (ultraThin to ultraThick), shapes (Rectangle, Capsule, Circle), and layout containers.
---

# Material & Structure API Reference

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
