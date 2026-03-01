---
name: apple-liquid-glass-design
description: Use when building UI with Apple's Liquid Glass material for iOS 26, iPadOS 26, macOS 26 - covers glassEffect, GlassEffectContainer, backgroundExtensionEffect, morph animations, toolbar grouping, button styles (.glass, .glassProminent), Icon Composer, ConcentricRectangle, scroll edge effects, and adoption best practices across SwiftUI, UIKit, and AppKit.
---

# Apple Liquid Glass Design

## Lifecycle Position

Phases 2-3 (Design → Implement). Related: `swiftui-components` (glass templates), `swiftui-material-api` (material backgrounds).

Reference for Apple's Liquid Glass design system introduced in iOS 26, iPadOS 26, and macOS 26. Liquid Glass is a dynamic material that combines optical properties of glass with fluidity, forming a functional layer for controls and navigation elements.

## When to Use This Skill

**Trigger conditions:**
- Applying Liquid Glass effects to custom SwiftUI views (`glassEffect`, `GlassEffectContainer`)
- Using background extension effects to stretch content under sidebars/inspectors
- Styling buttons with `.glass` or `.glassProminent` button styles
- Implementing morph animations between Liquid Glass elements
- Organizing toolbar items with `ToolbarSpacer(.fixed)` grouping
- Creating app icons with Icon Composer for Liquid Glass
- Extending horizontal scroll views under sidebars/inspectors
- Adding scroll edge effects for content legibility
- Implementing tab bar minimize behavior
- Using `ConcentricRectangle` for concentric corner radii
- Working with `UIGlassEffect` (UIKit) or `NSGlassEffectView` (AppKit)
- Adopting Liquid Glass in existing apps (migration from older SDK)
- Opting out via `UIDesignRequiresCompatibility` Info.plist key

**Do NOT use when:**
- Working with pre-iOS 26 glass effects (visionOS `glassBackgroundEffect` is a separate API)
- General SwiftUI layout questions unrelated to Liquid Glass

## Workflow Decision Tree

Choose the path that matches the request:

### 1) Review an existing feature
- Inspect where Liquid Glass should be used and where it should not.
- Verify correct modifier order, shape usage, and container placement.
- Check for iOS 26+ availability handling and sensible fallbacks.

### 2) Improve a feature using Liquid Glass
- Identify target components for glass treatment (surfaces, chips, buttons, cards).
- Refactor to use `GlassEffectContainer` where multiple glass elements appear.
- Introduce interactive glass only for tappable or focusable elements.

### 3) Implement a new feature using Liquid Glass
- Design the glass surfaces and interactions first (shape, prominence, grouping).
- Add glass modifiers after layout/appearance modifiers.
- Add morphing transitions only when the view hierarchy changes with animation.

## Review Checklist
- **Availability**: `#available(iOS 26, *)` present with fallback UI.
- **Composition**: Multiple glass views wrapped in `GlassEffectContainer`.
- **Modifier order**: `glassEffect` applied after layout/appearance modifiers.
- **Interactivity**: `interactive()` only where user interaction exists.
- **Transitions**: `glassEffectID` used with `@Namespace` for morphing.
- **Consistency**: Shapes, tinting, and spacing align across the feature.

## Implementation Checklist
- Define target elements and desired glass prominence.
- Wrap grouped glass elements in `GlassEffectContainer` and tune spacing.
- Use `.glassEffect(.regular.tint(...).interactive(), in: .rect(cornerRadius: ...))` as needed.
- Use `.buttonStyle(.glass)` / `.buttonStyle(.glassProminent)` for actions.
- Add morphing transitions with `glassEffectID` when hierarchy changes.
- Provide fallback materials and visuals for earlier iOS versions.

## Availability & Fallbacks

All Liquid Glass APIs require iOS 26 or later. Always provide fallbacks:

```swift
if #available(iOS 26, *) {
    content
        .padding()
        .glassEffect(.regular.interactive(), in: .rect(cornerRadius: 16))
} else {
    content
        .padding()
        .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
}
```

### Fallback Materials
- `.ultraThinMaterial` — Closest to glass appearance
- `.thinMaterial` — Slightly more opaque
- `.regularMaterial` — Standard blur
- `.thickMaterial` — More opaque
- `.ultraThickMaterial` — Most opaque

### Conditional Modifier Extension

```swift
extension View {
    @ViewBuilder
    func glassEffectWithFallback(
        _ style: Glass = .regular,
        in shape: some Shape = .rect,
        fallbackMaterial: Material = .ultraThinMaterial
    ) -> some View {
        if #available(iOS 26, *) {
            self.glassEffect(style, in: shape)
        } else {
            self.background(fallbackMaterial, in: shape)
        }
    }
}
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Liquid Glass** | Dynamic material that blurs content behind it, reflects color/light, and reacts to touch and pointer in real time |
| **Glass variants** | `.regular` (default), `.clear` (transparent), `.identity` (no effect) |
| **GlassEffectContainer** | Groups multiple glass effects for performance and morph animations |
| **Morph animation** | Shapes blend/separate fluidly when views appear/disappear within a container |
| **Background extension** | Mirrors and blurs edge content under sidebars/inspectors for edge-to-edge feel |
| **Icon Composer** | Xcode tool for creating multilayer Liquid Glass app icons |
| **ConcentricRectangle** | Shape that maintains concentric corner radii relative to its container |

## Quick Reference

### Apply Liquid Glass to a view (SwiftUI)

```swift
// Default: regular glass, capsule shape
Text("Hello")
    .padding()
    .glassEffect()

// Custom shape with rounded rectangle
Text("Hello")
    .padding()
    .glassEffect(in: .rect(cornerRadius: 16.0))

// Tinted + interactive (reacts to touch)
Text("Hello")
    .padding()
    .glassEffect(.regular.tint(.orange).interactive())
```

### Glass button styles

```swift
// Standard glass button
Button("Action") { }
    .buttonStyle(.glass)

// Prominent glass button (stronger visual weight)
Button("Primary") { }
    .buttonStyle(.glassProminent)

// Clear variant glass button
Button("Subtle") { }
    .buttonStyle(.glass(.clear))
```

### GlassEffectContainer with morph animation

```swift
@State private var isExpanded = false
@Namespace private var namespace

GlassEffectContainer(spacing: 40.0) {
    HStack(spacing: 40.0) {
        Image(systemName: "scribble.variable")
            .frame(width: 80, height: 80)
            .glassEffect()
            .glassEffectID("pencil", in: namespace)

        if isExpanded {
            Image(systemName: "eraser.fill")
                .frame(width: 80, height: 80)
                .glassEffect()
                .glassEffectID("eraser", in: namespace)
        }
    }
}

Button("Toggle") {
    withAnimation { isExpanded.toggle() }
}
.buttonStyle(.glass)
```

### Background extension effect

```swift
NavigationSplitView {
    // sidebar
} detail: {
    ZStack {
        Image(decorative: "hero")
            .backgroundExtensionEffect()
            .overlay(alignment: .bottom) {
                // Overlay goes AFTER the modifier so it
                // doesn't extend under the sidebar
                Text("Title").font(.largeTitle)
            }
    }
}
```

### Toolbar grouping with spacers

```swift
.toolbar {
    ToolbarSpacer(.flexible)
    ToolbarItem { ShareLink(item: item, preview: preview) }
    ToolbarSpacer(.fixed)
    ToolbarItemGroup {
        FavoriteButton(item: item)
        CollectionsMenu(item: item)
    }
    ToolbarSpacer(.fixed)
    ToolbarItem {
        Button("Info", systemImage: "info") { showInspector.toggle() }
    }
}
```

### Horizontal scroll under sidebar

```swift
ScrollView(.horizontal, showsIndicators: false) {
    LazyHStack(spacing: Constants.standardPadding) {
        Spacer().frame(width: Constants.standardPadding)
        ForEach(items) { item in
            ItemView(item: item)
        }
    }
}
// Ensure no padding on containing view so scroll touches sidebar edge
```

### Custom badge with glass effect

```swift
BadgeLabel(badge: badge)
    .glassEffect(.regular, in: .rect(cornerRadius: 12))
```

### Glass effect union (merge multiple shapes)

```swift
GlassEffectContainer(spacing: 20.0) {
    HStack(spacing: 20.0) {
        ForEach(items.indices, id: \.self) { i in
            Image(systemName: items[i])
                .frame(width: 80, height: 80)
                .glassEffect()
                .glassEffectUnion(id: i < 2 ? "group1" : "group2",
                                  namespace: namespace)
        }
    }
}
```

### Tab bar minimize on scroll

```swift
TabView {
    Tab("Numbers", systemImage: "number") {
        ScrollView { /* content */ }
    }
}
.tabBarMinimizeBehavior(.onScrollDown)
```

### Scroll edge effect

```swift
ScrollView {
    LazyVStack {
        ForEach(data) { item in RowView(item) }
    }
}
.scrollEdgeEffectStyle(.hard, for: .all)
```

### Concentric corner radii

```swift
ZStack {
    Color.cyan
        .fill(.rect(corners: .concentric(minimum: 12), isUniform: false))
        .padding(.all, padding)
}
.containerShape(.rect(cornerRadius: 24))
```

## API Quick Reference

| API | Framework | Purpose |
|-----|-----------|---------|
| `.glassEffect(_:in:)` | SwiftUI | Apply Liquid Glass to any view |
| `.glassEffect()` | SwiftUI | Apply default (regular, capsule) glass |
| `GlassEffectContainer` | SwiftUI | Combine glass effects for performance + morphing |
| `.glassEffectID(_:in:)` | SwiftUI | Identity for morph transitions |
| `.glassEffectTransition(_:)` | SwiftUI | Control transition type (`.matchedGeometry`, `.materialize`) |
| `.glassEffectUnion(id:namespace:)` | SwiftUI | Merge multiple shapes into one glass effect |
| `Glass` | SwiftUI | Config struct: `.regular`, `.clear`, `.identity` |
| `.interactive(_:)` | SwiftUI | Make glass react to touch/pointer |
| `.tint(_:)` | SwiftUI | Tint a glass effect |
| `.buttonStyle(.glass)` | SwiftUI | Standard glass button |
| `.buttonStyle(.glassProminent)` | SwiftUI | Prominent glass button |
| `.buttonStyle(.glass(.clear))` | SwiftUI | Clear variant glass button |
| `.backgroundExtensionEffect()` | SwiftUI | Extend view under sidebar/inspector |
| `UIBackgroundExtensionView` | UIKit | Background extension in UIKit |
| `NSBackgroundExtensionView` | AppKit | Background extension in AppKit |
| `UIGlassEffect` | UIKit | Glass visual effect in UIKit |
| `NSGlassEffectView` | AppKit | Glass effect view in AppKit |
| `ToolbarSpacer(.fixed)` | SwiftUI | Separate toolbar groups |
| `GlassEffectTransition` | SwiftUI | `.matchedGeometry`, `.materialize`, `.identity` |
| `DefaultGlassEffectShape` | SwiftUI | Default capsule shape for glass |
| `ConcentricRectangle` | SwiftUI | Concentric corner radius shape |
| `.tabBarMinimizeBehavior(_:)` | SwiftUI | Auto-minimize tab bar on scroll |
| `.scrollEdgeEffectStyle(_:for:)` | SwiftUI | Legibility effect at scroll edges |
| `UIDesignRequiresCompatibility` | Info.plist | Opt out of Liquid Glass (compatibility mode) |

## Common Mistakes

**Overusing Liquid Glass on custom controls.** Apple explicitly warns: "Avoid overusing Liquid Glass effects. Limit these effects to the most important functional elements." Too many glass elements distract from content.

**Not using GlassEffectContainer.** Applying `glassEffect` to multiple views without a container degrades performance. Always wrap related glass views in a `GlassEffectContainer`.

**Applying backgroundExtensionEffect with padding.** The view must touch the leading/trailing edges of the containing view. Remove padding from the view and its containers so the effect can extend under the sidebar.

**Putting overlays before backgroundExtensionEffect.** Apply `.backgroundExtensionEffect()` to the image first, then add `.overlay()` after, so that overlaid text/buttons don't extend under the sidebar.

**Hard-coding layout metrics for controls.** Controls have new shapes and sizes in iOS 26. If you hard-code dimensions, your controls won't adopt the new rounded forms automatically.

**Ignoring accessibility settings.** Liquid Glass adapts when users enable Reduce Transparency or Reduce Motion. Test with these settings on. Standard components handle this automatically; custom implementations need fallbacks.

**Custom backgrounds interfering with glass.** Remove custom backgrounds from bars, tab bars, toolbars, and split views. They overlay or interfere with the system Liquid Glass appearance.

**Not testing with `UIDesignRequiresCompatibility`.** To ship with the latest SDK while opting out temporarily, add this key to your Info.plist. Remove it when you're ready for the full Liquid Glass experience.

## Reference Files

Detailed documentation organized by topic in `references/`:

| File | Content | Pages |
|------|---------|-------|
| `getting_started.md` | Adopting Liquid Glass overview, Landmarks sample walkthrough, migration guide for existing apps | 2 |
| `background_extension.md` | `backgroundExtensionEffect()` API, UIKit (`UIBackgroundExtensionView`), AppKit (`NSBackgroundExtensionView`), alignment requirements | 4 |
| `custom_glass_views.md` | `glassEffect`, `Glass` struct, `GlassEffectContainer`, transitions, morph animations, button styles, union effects, UIKit/AppKit equivalents | 23 |
| `toolbar_glass.md` | `ToolbarSpacer`, toolbar grouping patterns | 2 |
| `horizontal_scrolling.md` | Extending horizontal ScrollView under sidebar/inspector | 1 |
| `activity_badges.md` | Custom badges with glass effects, morph animations, ViewModifier patterns | 1 |
| `navigation_and_layout.md` | `tabBarMinimizeBehavior`, `scrollEdgeEffectStyle` | 2 |
| `controls.md` | `ConcentricRectangle` shape, per-corner concentric radius control | 1 |
| `app_icons.md` | Icon Composer workflow: layers, groups, Liquid Glass material, platform variants | 1 |
| `platform_considerations.md` | `UIDesignRequiresCompatibility` Info.plist key for opting out | 1 |
| `other.md` | View styles overview, all Liquid Glass related SwiftUI style APIs | 1 |

## Working with This Skill

### Getting Started
Read `references/getting_started.md` for the adoption overview and Landmarks sample walkthrough. It covers the full scope: background extension, horizontal scrolling, toolbar glass, custom badges, and Icon Composer.

### For Specific Features
Each topic has a dedicated reference file. For custom glass views and animations, `custom_glass_views.md` is the most comprehensive (23 pages covering all SwiftUI glass APIs).

### Cross-Framework Implementation
- **SwiftUI**: Primary framework. Use `glassEffect`, `GlassEffectContainer`, etc.
- **UIKit**: Use `UIGlassEffect` and `UIBackgroundExtensionView`. See `custom_glass_views.md` and `background_extension.md`.
- **AppKit**: Use `NSGlassEffectView` and `NSBackgroundExtensionView`. See same reference files.

### Adoption Checklist
1. Build with latest Xcode SDK to see automatic Liquid Glass adoption
2. Remove custom backgrounds from bars, toolbars, split views
3. Test with accessibility settings (Reduce Transparency, Reduce Motion)
4. Group toolbar items with `ToolbarSpacer(.fixed)`
5. Add `backgroundExtensionEffect()` to hero images in split views
6. Wrap custom glass views in `GlassEffectContainer`
7. Create new app icon with Icon Composer
8. Test across all supported platforms

## Notes

- Documentation sourced from Apple Developer Documentation via sosumi.ai extraction
- All APIs require iOS 26.0+ / iPadOS 26.0+ / macOS 26.0+ unless otherwise noted
- visionOS glass background APIs (`glassBackgroundEffect`, `FeatheredGlassBackgroundEffect`) are separate from the Liquid Glass system described here
- watchOS and tvOS have limited Liquid Glass support; standard components adopt it automatically

## Cross-References

- `swiftui-26-api` — Non-glass iOS 26 APIs (WebView, TextEditor rich text, @Animatable macro, UIHostingSceneDelegate, dragContainer, windowResizeAnchor)
