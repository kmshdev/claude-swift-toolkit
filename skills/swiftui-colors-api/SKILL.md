---
name: swiftui-colors-api
description: This skill should be used when the user asks to "style with colors", "apply gradients", "use foregroundStyle", "add linear/radial gradient", "set tint color", or needs SwiftUI color and ShapeStyle API reference. Provides Color usage, foregroundStyle with hierarchical levels, gradients, system colors, and custom ShapeStyle patterns.
---

# Colors & ShapeStyle API Reference

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
