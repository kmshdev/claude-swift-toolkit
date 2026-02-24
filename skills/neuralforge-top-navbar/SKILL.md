---
name: neuralforge-top-navbar
description: Use this skill when building a SwiftUI top navigation tab bar with closable tabs displaying issue/ticket IDs and titles, horizontal scrolling tab strips, active tab highlighting, and Liquid Glass toolbar styling. Covers TabView, toolbar customization, ToolbarSpacer, scroll edge effects, and dark-themed tab bar patterns for macOS Tahoe and iOS 26 project management interfaces.
---

# Neuralforge Top Navbar

SwiftUI reference for building a top navigation tab bar with closable tabs, horizontal scrolling, active tab highlighting, Liquid Glass toolbar styling, and dark-themed tab bar patterns targeting macOS Tahoe and iOS 26 project management interfaces.

Synthesized from Apple Developer Documentation (via sosumi.ai) covering SwiftUI Tab, TabView, toolbar APIs, Liquid Glass effects, scroll behaviors, animations, drag/drop interactions, and typography/layout primitives.

## When to Use This Skill

**Trigger conditions:**
- Building a horizontally scrolling tab strip displaying issue/ticket IDs and titles
- Implementing closable tabs with close buttons in a SwiftUI toolbar or navigation bar
- Adding Liquid Glass material effects to toolbars or custom tab bars (iOS 26+ / macOS 26+)
- Customizing `TabView` beyond standard bottom tab bars (top-positioned, programmatic selection)
- Using `ToolbarSpacer` to group toolbar items into logical Liquid Glass sections
- Animating tab switching with `matchedGeometryEffect`, `contentTransition`, or `Namespace`
- Implementing tab drag-and-drop reordering with `draggable`/`onDrop`
- Adding context menus to individual tabs (close, close others, close all)
- Styling scroll edge effects under toolbars with `scrollEdgeEffectStyle`
- Building dark-themed or custom-colored toolbar backgrounds

**Do NOT use when:**
- Building a standard bottom tab bar with no customization (use SwiftUI defaults)
- Working with UIKit `UITabBarController` exclusively
- Building navigation that doesn't involve tabs (use standard NavigationStack/NavigationSplitView docs)

## Key Concepts

### Tab Bar Architecture

The tab bar is built from several SwiftUI primitives layered together:

| Layer | Component | Purpose |
|-------|-----------|---------|
| Container | `TabView` or custom `HStack`/`LazyHStack` | Holds tabs, manages selection |
| Tab Item | `Tab` (iOS 18+) or custom `Button` | Individual tab with label and content |
| Toolbar | `.toolbar { }` modifier | Hosts toolbar items above content |
| Spacing | `ToolbarSpacer(.fixed)` / `ToolbarSpacer(.flexible)` | Groups toolbar items into Liquid Glass sections |
| Glass | `.glassEffect()` / `GlassEffectContainer` | Applies Liquid Glass material (iOS/macOS 26+) |
| Scroll | `ScrollView(.horizontal)` + `LazyHStack` | Enables horizontal scrolling for many tabs |
| Animation | `matchedGeometryEffect` + `Namespace` | Smooth tab switching animations |

### Liquid Glass (iOS 26+ / macOS 26+)

Liquid Glass is a dynamic material that forms a distinct functional layer for controls and navigation. Key principles:
- Standard components (toolbars, tab bars) adopt Liquid Glass **automatically** when built with the latest SDK
- Use `GlassEffectContainer` to combine multiple glass shapes for performance and morphing animations
- Avoid overusing custom Liquid Glass effects — limit to the most important functional elements
- Use `ToolbarSpacer(.fixed)` to create visual groupings within Liquid Glass toolbars
- Test with accessibility settings (reduce transparency, reduce motion)

### TabView vs Custom Tab Strip

| Approach | When to Use |
|----------|-------------|
| `TabView` with `Tab` | Standard tab navigation, sidebar-adaptable, system-managed |
| Custom `ScrollView(.horizontal)` + `HStack` | Full control: closable tabs, reorder, custom layout |
| `TabView` + `.tabViewStyle(.page)` | Paged/swipeable content |

## Quick Reference

### Basic TabView with Programmatic Selection

```swift
@State private var selection = 0

TabView(selection: $selection) {
    Tab("Received", systemImage: "tray.and.arrow.down.fill", value: 0) {
        ReceivedView()
    }
    Tab("Sent", systemImage: "tray.and.arrow.up.fill", value: 1) {
        SentView()
    }
    Tab("Account", systemImage: "person.crop.circle.fill", value: 2) {
        AccountView()
    }
}
```

### Toolbar with Liquid Glass Groupings

Use `ToolbarSpacer(.fixed)` to separate items into distinct Liquid Glass sections:

```swift
.toolbar {
    ToolbarSpacer(.flexible)

    ToolbarItem {
        ShareLink(item: landmark, preview: landmark.sharePreview)
    }

    ToolbarSpacer(.fixed)

    ToolbarItemGroup {
        LandmarkFavoriteButton(landmark: landmark)
        LandmarkCollectionsMenu(landmark: landmark)
    }

    ToolbarSpacer(.fixed)

    ToolbarItem {
        Button("Info", systemImage: "info") {
            showInspector.toggle()
        }
    }
}
```

### Horizontal Scrolling Tab Strip

For a custom scrollable tab bar with many tabs:

```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 10.0) {
        ForEach(items) { item in
            ItemView(item)
        }
    }
    .scrollTargetLayout()
}
.scrollTargetBehavior(.viewAligned)
.safeAreaPadding(.horizontal, 20.0)
```

### Applying Liquid Glass to Custom Views

```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()
```

Use `GlassEffectContainer` to combine multiple glass shapes:

```swift
GlassEffectContainer(spacing: 8) {
    // Multiple views with .glassEffect() morph into each other
}
```

### Toolbar Background and Color Scheme

```swift
TabView {
    NavigationView {
        ContentView()
            .toolbarBackground(.blue, for: .navigationBar, .tabBar)
            .toolbarColorScheme(.dark, for: .navigationBar, .tabBar)
    }
}
```

### Customizable Toolbar with Spacers

```swift
ContentView()
    .toolbar(id: "main-toolbar") {
        ToolbarItem(id: "tag") { TagButton() }
        ToolbarItem(id: "share") { ShareButton() }
        ToolbarSpacer(.fixed)
        ToolbarItem(id: "more") { MoreButton() }
    }
```

### Matched Geometry Tab Animation

Animate a selection indicator moving between tabs:

```swift
@Namespace var tabNamespace

// In the selected tab:
.matchedGeometryEffect(id: "activeTab", in: tabNamespace)
```

### Content Transition for Tab Label Changes

```swift
Text("Tab Title")
    .contentTransition(.interpolate)
```

Wrap state changes in `withAnimation` for the transition to take effect.

### Context Menu on Tabs

```swift
Text("Issue-123")
    .contextMenu {
        Button {
            // close this tab
        } label: {
            Label("Close Tab", systemImage: "xmark")
        }
        Button(role: .destructive) {
            // close all tabs
        } label: {
            Label("Close All", systemImage: "xmark.circle")
        }
    }
```

### Scroll Edge Effect for Toolbar Legibility

Maintain legibility when content scrolls beneath Liquid Glass toolbars:

```swift
ScrollView {
    LazyVStack {
        ForEach(data) { item in
            RowView(item)
        }
    }
}
.scrollEdgeEffectStyle(.hard, for: .all)
```

## API Quick Reference

### Tab Bar Structure

| API | Min Version | Purpose |
|-----|-------------|---------|
| `Tab` | iOS 18 / macOS 15 | Tab content + tab item in a `TabView` |
| `TabView` | iOS 13 / macOS 10.15 | Switches between child views with tab UI |
| `TabViewStyle` | iOS 14 / macOS 11 | Configures tab appearance (`.page`, `.sidebarAdaptable`, etc.) |

### Toolbar APIs

| API | Min Version | Purpose |
|-----|-------------|---------|
| `.toolbar(content:)` | iOS 14 / macOS 11 | Populate toolbar/navigation bar |
| `ToolbarItem` | iOS 14 / macOS 11 | Single toolbar item with placement |
| `ToolbarItemGroup` | iOS 14 / macOS 11 | Group of related toolbar items |
| `ToolbarSpacer` | iOS 26 / macOS 26 | Fixed or flexible spacing between items |
| `ToolbarItemPlacement` | iOS 14 / macOS 11 | Semantic/positional placement (`topBarLeading`, `principal`, etc.) |
| `.toolbarBackground(_:for:)` | iOS 16 / macOS 13 | Custom toolbar background style |
| `.toolbarColorScheme(_:for:)` | iOS 16 / macOS 13 | Dark/light scheme for toolbar |
| `.toolbarVisibility(_:for:)` | iOS 18 / macOS 15 | Show/hide toolbar bars |
| `.toolbarRole(_:)` | iOS 16 / macOS 13 | Semantic role (`.browser`, etc.) |

### Liquid Glass APIs (iOS 26+ / macOS 26+)

| API | Purpose |
|-----|---------|
| `.glassEffect(_:in:)` | Apply Liquid Glass material to a view |
| `.glassEffectID(_:in:)` | Identity for glass shape transitions |
| `GlassEffectContainer` | Combine glass shapes for morphing + performance |
| `GlassButtonStyle` / `.glass` | Button style with glass artwork |
| `.backgroundExtensionEffect()` | Extend content under sidebar/inspector |
| `.safeAreaBar(edge:...)` | Custom bar with scroll edge integration |
| `.scrollEdgeEffectStyle(_:for:)` | Configure scroll edge effect (`.hard`, `.soft`) |

### Horizontal Scrolling

| API | Min Version | Purpose |
|-----|-------------|---------|
| `ScrollView(.horizontal)` | iOS 13 / macOS 10.15 | Horizontal scrollable container |
| `LazyHStack` | iOS 14 / macOS 11 | Lazy horizontal layout (create items on demand) |
| `HStack` | iOS 13 / macOS 10.15 | Eagerly-rendered horizontal layout |
| `ScrollViewReader` | iOS 14 / macOS 11 | Programmatic scroll to specific child |
| `.scrollTargetBehavior(_:)` | iOS 17 / macOS 14 | Paging or view-aligned scroll snapping |
| `.scrollTargetLayout()` | iOS 17 / macOS 14 | Mark layout for view-aligned behavior |

### Tab Animations

| API | Min Version | Purpose |
|-----|-------------|---------|
| `.animation(_:value:)` | iOS 13 / macOS 10.15 | Animate when value changes |
| `.contentTransition(_:)` | iOS 16 / macOS 13 | Animate content changes (`.interpolate`, `.opacity`) |
| `@Namespace` | iOS 14 / macOS 11 | Create namespace for matched geometry |
| `.matchedGeometryEffect(id:in:)` | iOS 14 / macOS 11 | Sync geometry between views in transitions |

### Tab Interactions

| API | Min Version | Purpose |
|-----|-------------|---------|
| `Button` | iOS 13 / macOS 10.15 | Tab click/tap action, close button |
| `.buttonStyle(_:)` | iOS 13 / macOS 10.15 | Style buttons (`.bordered`, `.glass`) |
| `.onHover(perform:)` | iOS 13.4 / macOS 10.15 | Pointer hover detection (macOS tab highlights) |
| `.contextMenu(menuItems:)` | iOS 13 / macOS 10.15 | Right-click/long-press menu on tabs |
| `.draggable(_:)` | iOS 16 / macOS 13 | Make tab draggable for reordering |
| `.onDrop(of:...)` | iOS 14 / macOS 11 | Drop target for tab reorder |

### Typography and Layout

| API | Purpose |
|-----|---------|
| `Text` | Display tab titles, issue IDs |
| `.font(_:)` | Set tab label font size/weight |
| `.foregroundStyle(_:)` | Color active/inactive tab labels |
| `.frame(min/ideal/max...)` | Constrain tab width |
| `.clipShape(_:)` | Clip tab backgrounds (Capsule, RoundedRectangle) |
| `Capsule` | Pill-shaped tab background |
| `RoundedRectangle` | Rounded tab background |

## Reference Files

Detailed documentation organized by topic in `references/`:

| File | Pages | Content |
|------|-------|---------|
| `tab_bar_structure.md` | 3 | **Tab**, **TabView**, **TabViewStyle** — Core tab bar primitives, `init` variants, selection binding, `.page`/`.sidebarAdaptable` styles |
| `toolbar_apis.md` | 11 | **toolbar(content:)**, **ToolbarItem**, **ToolbarItemGroup**, **ToolbarSpacer**, **ToolbarItemPlacement**, **toolbarBackground**, **toolbarColorScheme**, **toolbarVisibility**, **toolbarRole**, Landmarks Liquid Glass toolbar example |
| `liquid_glass_toolbar.md` | 7 | **glassEffect**, **GlassEffectContainer**, **glassEffectID**, **backgroundExtensionEffect**, **safeAreaBar**, **scrollEdgeEffectStyle**, Adopting Liquid Glass overview |
| `horizontal_scrolling.md` | 5 | **LazyHStack**, **HStack**, **ScrollView**, **ScrollViewReader**, **scrollTargetBehavior** — Horizontal scroll, programmatic scroll, paging/view-aligned |
| `tab_animations.md` | 4 | **contentTransition**, **Namespace**, **animation(_:value:)**, **matchedGeometryEffect** — Tab switch animations, geometry sync |
| `tab_interactions.md` | 8 | **Button**, **buttonStyle**, **GlassButtonStyle**, **onHover**, **contextMenu**, **draggable**, **onDrop**, **onDrag** — User interaction patterns |
| `typography_and_layout.md` | 7 | **Text**, **font**, **foregroundStyle**, **frame**, **clipShape**, **Capsule**, **RoundedRectangle** — Tab label styling and layout |

Read specific reference files when you need full API signatures, all `init` variants, or detailed parameter descriptions.

## Working with This Skill

### Getting Started
1. Read this SKILL.md for architecture overview and quick reference
2. Start with `tab_bar_structure.md` to understand `Tab` and `TabView` fundamentals
3. Review `toolbar_apis.md` for toolbar population and styling

### Building a Custom Tab Strip
1. Use `horizontal_scrolling.md` for `ScrollView` + `LazyHStack` patterns
2. Use `tab_interactions.md` for close buttons, context menus, drag reorder
3. Use `tab_animations.md` for smooth tab switching with `matchedGeometryEffect`
4. Use `typography_and_layout.md` for tab label styling

### Adding Liquid Glass
1. Read `liquid_glass_toolbar.md` for `glassEffect`, `GlassEffectContainer`, scroll edge effects
2. Check `toolbar_apis.md` for the Landmarks toolbar grouping example with `ToolbarSpacer`
3. Review the "Adopting Liquid Glass" overview in `liquid_glass_toolbar.md` for platform guidance

### Platform Considerations
- **iOS 26+ / macOS 26+**: Full Liquid Glass support, `ToolbarSpacer`, `GlassButtonStyle`, `scrollEdgeEffectStyle`
- **iOS 18+ / macOS 15+**: `Tab` struct with typed selection, `toolbarVisibility`
- **iOS 17+ / macOS 14+**: `scrollTargetBehavior` for view-aligned scrolling
- **iOS 16+ / macOS 13+**: `toolbarBackground`, `toolbarColorScheme`, `draggable`, `contentTransition`
- **iOS 14+ / macOS 11+**: `toolbar(content:)`, `ToolbarItem`, `LazyHStack`, `ScrollViewReader`, `Namespace`

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Overusing `.glassEffect()` on every element | Apply sparingly to key functional elements only |
| Hiding views inside toolbar items instead of hiding the item | Use `.toolbarVisibility(.hidden)` on the entire bar, or conditionally include `ToolbarItem` |
| Using `HStack` for large tab counts | Use `LazyHStack` inside `ScrollView(.horizontal)` for performance |
| Forgetting `withAnimation` for `contentTransition` | `contentTransition(_:)` requires an animation context to take effect |
| Hard-coding toolbar layout metrics | Use system spacing and `ToolbarSpacer` so Liquid Glass groupings work correctly |
| Not providing accessibility labels for icon-only tabs | Always set `.accessibilityLabel()` even when displaying only icons |
| Using `ScrollViewProxy.scrollTo` inside content builder | Only call proxy methods from actions/gestures/onChange, never during view building |

## Source Information

All reference documentation was extracted from Apple Developer Documentation via [sosumi.ai](https://sosumi.ai). This is unofficial content — all documentation belongs to Apple Inc. Source confidence is **medium** across all files (scraped documentation, not direct codebase analysis).

When in doubt, consult the official Apple Developer Documentation directly for the most current API details.
