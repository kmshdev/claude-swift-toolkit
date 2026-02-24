---
name: sidebar-liquid-glass-clone
description: Use this skill when building a dark-themed sidebar navigation UI with Liquid Glass effects in SwiftUI for macOS Tahoe / iOS 26. Covers NavigationSplitView, hierarchical workspace trees with OutlineGroup/DisclosureGroup, badge notifications, ⌘K search bar, pinned bottom bars with upgrade CTAs, user avatars, status dot indicators, and glass material effects. Based on the NeuralForge sidebar reference design: dark translucent sidebar with workspace tree, queue badges, AI assistant nav, and promotional upgrade card.
---

# Sidebar Liquid Glass Clone

Build a dark-themed sidebar navigation UI with Liquid Glass effects in SwiftUI, targeting macOS Tahoe (macOS 26) and iOS 26. This skill synthesizes official Apple documentation for SwiftUI components needed to replicate the NeuralForge sidebar reference design: a dark translucent sidebar with workspace tree, queue badges, AI assistant navigation, and a promotional upgrade card.

## When to Use This Skill

Trigger this skill when:

- **Building a sidebar navigation** using `NavigationSplitView` with a dark translucent glass appearance
- **Creating hierarchical workspace trees** with `OutlineGroup` or `DisclosureGroup` for collapsible sections
- **Adding badge notifications** to list rows or tab items (e.g., queue counts, unread indicators)
- **Implementing a command palette / search bar** (⌘K pattern) with `searchable` and `FocusState`
- **Designing pinned bottom bars** in sidebars with upgrade CTAs, user avatars, or account buttons
- **Applying Liquid Glass effects** to custom views using `glassEffect(_:in:)`, `GlassEffectContainer`, or `GlassButtonStyle`
- **Setting up dark theme** with `preferredColorScheme(.dark)` and custom color schemes
- **Building status dot indicators** using `Circle` overlays on avatar images
- **Styling sidebar lists** with `SidebarListStyle`, hidden separators, and transparent backgrounds

## Key Concepts

### Liquid Glass (iOS 26 / macOS 26)

Liquid Glass is a dynamic material that combines optical glass properties with fluidity. It blurs content behind it, reflects surrounding color and light, and reacts to touch/pointer interactions in real time. Standard SwiftUI components adopt Liquid Glass automatically when built with the latest SDK.

Key types:
- **`Glass`** - Defines the Liquid Glass material configuration. Variants: `.regular`, `.clear`, `.identity`
- **`glassEffect(_:in:)`** - Applies Liquid Glass to a view with a shape (default: `Capsule`)
- **`GlassEffectContainer`** - Combines multiple glass shapes for morphing and performance optimization
- **`GlassButtonStyle`** - Button style with glass border artwork
- **`backgroundExtensionEffect()`** - Extends content under sidebars/inspectors with mirrored blur

### NavigationSplitView

The primary container for sidebar-based navigation. Presents views in two or three columns where selections in leading columns control presentations in subsequent columns. Supports programmatic column visibility control and compact column preference.

### Sidebar List Style

`SidebarListStyle` (or `.listStyle(.sidebar)`) provides the standard sidebar appearance with disclosure indicators for collapsible sections. Use `Section` with `isExpanded` bindings for collapsible groups.

### Hierarchical Data

- **`OutlineGroup`** - Renders tree-structured data with disclosure controls from a collection and children key path
- **`DisclosureGroup`** - Manual expand/collapse control with a label and content
- **`List(_:children:rowContent:)`** - Built-in hierarchical list from tree data

## Quick Reference

### 1. Two-Column NavigationSplitView with Sidebar

```swift
@State private var selectedItem: Item.ID?

var body: some View {
    NavigationSplitView {
        List(items, selection: $selectedItem) { item in
            Label(item.name, systemImage: item.icon)
        }
        .listStyle(.sidebar)
        .navigationTitle("Workspaces")
    } detail: {
        DetailView(itemID: selectedItem)
    }
}
```

### 2. Applying Liquid Glass Effect

```swift
// Basic glass effect (capsule shape by default)
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()

// Custom shape with tint and interactivity
Text("Interactive")
    .padding()
    .glassEffect(.regular.tint(.orange).interactive(),
                  in: .rect(cornerRadius: 16.0))
```

### 3. GlassEffectContainer for Morphing

```swift
@State private var isExpanded = false
@Namespace private var namespace

GlassEffectContainer(spacing: 40.0) {
    HStack(spacing: 40.0) {
        Image(systemName: "scribble.variable")
            .frame(width: 80, height: 80)
            .font(.system(size: 36))
            .glassEffect()
            .glassEffectID("pencil", in: namespace)

        if isExpanded {
            Image(systemName: "eraser.fill")
                .frame(width: 80, height: 80)
                .font(.system(size: 36))
                .glassEffect()
                .glassEffectID("eraser", in: namespace)
        }
    }
}
```

### 4. Hierarchical Workspace Tree with OutlineGroup

```swift
struct Workspace: Hashable, Identifiable {
    var id: Self { self }
    var name: String
    var children: [Workspace]? = nil
}

OutlineGroup(workspaces, children: \.children) { item in
    Label(item.name, systemImage: item.children != nil
          ? "folder" : "doc")
}
```

### 5. Collapsible Sections with DisclosureGroup

```swift
@State private var isExpanded = true

DisclosureGroup("Items", isExpanded: $isExpanded) {
    Toggle("Toggle 1", isOn: $toggleStates.oneIsOn)
    Toggle("Toggle 2", isOn: $toggleStates.twoIsOn)
    DisclosureGroup("Sub-items") {
        Text("Sub-item 1")
    }
}
```

### 6. Badge Notifications on List Rows

```swift
List {
    Text("Recents")
        .badge(
            Text("\(recentItems.count)")
                .monospacedDigit()
                .foregroundColor(.red)
                .bold()
        )
    Text("Favorites")
}
```

### 7. Dark Theme with Transparent Sidebar Background

```swift
NavigationSplitView {
    List { /* sidebar content */ }
        .listStyle(.sidebar)
        .scrollContentBackground(.hidden)
        .background(.ultraThinMaterial)
} detail: {
    DetailView()
}
.preferredColorScheme(.dark)
```

### 8. Pinned Bottom Bar in Sidebar

```swift
TabView {
    Tab("Home", systemImage: "house") { HomeView() }
    Tab("Alerts", systemImage: "bell") { AlertsView() }
}
.tabViewStyle(.sidebarAdaptable)
.tabViewSidebarBottomBar {
    AccountButton()
}
```

### 9. Search Bar with Keyboard Shortcut (⌘K)

```swift
@State private var searchText = ""
@FocusState private var isSearchFocused: Bool

NavigationSplitView {
    List { /* content */ }
        .searchable(text: $searchText, prompt: "Search...")
} detail: {
    DetailView()
}
```

### 10. Status Dot Indicator on Avatar

```swift
Image(systemName: "person.circle.fill")
    .font(.title)
    .foregroundStyle(.white)
    .overlay(alignment: .bottomTrailing) {
        Circle()
            .fill(.green)
            .frame(width: 10, height: 10)
    }
```

### 11. Background Extension Under Sidebar

```swift
NavigationSplitView {
    // sidebar content
} detail: {
    ZStack {
        BannerView()
            .backgroundExtensionEffect()
    }
}
```

### 12. Glass Button Style

```swift
Button("Toggle") {
    withAnimation { isExpanded.toggle() }
}
.buttonStyle(.glass)
```

## Reference Files

This skill includes 11 reference files in `references/`, organized by component category. All sourced from official Apple Developer Documentation via sosumi.ai extraction.

| File | Pages | Coverage |
|------|-------|----------|
| **`sidebar_structure.md`** | 8 | `NavigationSplitView`, `NavigationSplitViewStyle`, `List`, `listStyle`, `listRowSeparator`, `tabViewSidebarBottomBar`, `SidebarListStyle`, `Section` |
| **`liquid_glass_effects.md`** | 11 | `Glass`, `glassEffect(_:in:)`, `GlassEffectContainer`, `GlassButtonStyle`, `glassEffectID`, `interactive(_:)`, `backgroundExtensionEffect()`, `ConcentricRectangle`, "Adopting Liquid Glass" guide, "Applying Liquid Glass to custom views" guide |
| **`hierarchy_and_trees.md`** | 2 | `OutlineGroup`, `DisclosureGroup` |
| **`dark_theme_and_colors.md`** | 8 | `Color`, `preferredColorScheme`, `colorScheme`, `foregroundStyle`, `background(_:ignoresSafeAreaEdges:)`, `scrollContentBackground`, `shadow`, `environment` |
| **`badges_and_indicators.md`** | 4 | `Circle`, `Label`, `overlay(alignment:content:)`, `badge(_:)` |
| **`layout_and_spacing.md`** | 9 | `frame`, `Spacer`, `ZStack`, `VStack`, `HStack`, `Divider`, `padding`, `ToolbarSpacer`, `contentMargins` |
| **`navigation_and_toolbar.md`** | 4 | `Button`, `scrollIndicators`, `toolbar(content:)`, `navigationTitle` |
| **`search_and_shortcuts.md`** | 4 | `keyboardShortcut`, `FocusState`, `searchable`, `focused(_:)` |
| **`shapes_and_clipping.md`** | 3 | `clipShape`, `Capsule`, `RoundedRectangle` |
| **`typography_and_images.md`** | 4 | `Image`, `Font`, `font(_:)`, `Text` |
| **`interaction_and_feedback.md`** | 1 | `sensoryFeedback(_:trigger:)` |

## Working with This Skill

### Getting Started

1. **Start with `sidebar_structure.md`** to understand the `NavigationSplitView` layout and `SidebarListStyle`
2. **Read `liquid_glass_effects.md`** for the Liquid Glass API available in iOS 26 / macOS 26
3. **Review `hierarchy_and_trees.md`** for building collapsible workspace trees
4. **Check `dark_theme_and_colors.md`** for dark mode setup and material backgrounds

### Building the NeuralForge Sidebar Clone

Follow this component assembly order:

1. **Shell**: `NavigationSplitView` with `.preferredColorScheme(.dark)`
2. **Sidebar list**: `List` with `.listStyle(.sidebar)` and `.scrollContentBackground(.hidden)`
3. **Sections**: `Section` with `isExpanded` bindings or `DisclosureGroup` for workspace folders
4. **Tree items**: `OutlineGroup` for nested workspace hierarchy
5. **Badges**: `.badge()` on list rows for queue counts
6. **Search**: `.searchable()` modifier with `FocusState` for ⌘K activation
7. **Bottom bar**: `.tabViewSidebarBottomBar` for account/upgrade CTA
8. **Glass effects**: `glassEffect()` on custom controls, wrapped in `GlassEffectContainer`
9. **Status indicators**: `Circle` overlay on avatar images
10. **Haptic feedback**: `.sensoryFeedback(.selection, trigger:)` on interactive elements

### Platform Considerations

- **Liquid Glass APIs** (`Glass`, `glassEffect`, `GlassEffectContainer`, `GlassButtonStyle`, `ConcentricRectangle`, `backgroundExtensionEffect`) require **iOS 26.0+ / macOS 26.0+**
- **`tabViewSidebarBottomBar`** requires **iOS 18.0+ / macOS 15.0+**
- **`NavigationSplitView`** requires **iOS 16.0+ / macOS 13.0+**
- **`OutlineGroup` / `DisclosureGroup`** require **iOS 14.0+ / macOS 11.0+**
- **`searchable`** requires **iOS 15.0+ / macOS 12.0+**
- **`FocusState`** requires **iOS 15.0+ / macOS 12.0+**
- **`sensoryFeedback`** requires **iOS 17.0+ / macOS 14.0+**
- **`contentMargins`** requires **iOS 17.0+ / macOS 14.0+**
- **`ToolbarSpacer`** requires **iOS 26.0+ / macOS 26.0+**

### Performance Guidelines

From Apple's "Applying Liquid Glass to custom views" guide:

- **Use `GlassEffectContainer`** to combine multiple glass effects for better rendering performance
- **Limit the number of glass effects** onscreen simultaneously; overuse distracts from content
- **Apply `glassEffect` after** other appearance modifiers (it captures content for the container)
- **Use `backgroundExtensionEffect()` sparingly** - typically one instance per detail view
- **Control container spacing** to manage when glass shapes blend together (larger spacing = earlier blending)

### Adopting Liquid Glass Best Practices

From Apple's "Adopting Liquid Glass" technology overview:

- Standard SwiftUI components adopt Liquid Glass automatically when built with latest SDKs
- **Remove custom backgrounds** from navigation elements (tab bars, toolbars, split views) to avoid interfering with system glass effects
- **Test with accessibility settings** - translucency and morphing adapt to Reduce Transparency and Reduce Motion settings
- **Use standard button styles** (`.glass`, `.glassProminent`) instead of custom Liquid Glass on buttons
- **Use concentric shapes** (`ConcentricRectangle`) to match hardware corner curvature
- **Extend content under sidebars** with `backgroundExtensionEffect()` for edge-to-edge detail views

## Material Types Reference

| Material | Translucency | Use Case |
|----------|-------------|----------|
| `.ultraThinMaterial` | Most translucent | Subtle overlays |
| `.thinMaterial` | More translucent than opaque | Light overlays |
| `.regularMaterial` | Balanced | Standard backgrounds |
| `.thickMaterial` | More opaque than translucent | Prominent overlays |
| `.ultraThickMaterial` | Mostly opaque | Strong backgrounds |
| `.bar` | Matches system toolbar | Navigation bars |

## Glass Variants Reference

| Variant | Description |
|---------|-------------|
| `.regular` | Standard Liquid Glass material (default) |
| `.clear` | Clear variant of glass |
| `.identity` | No glass effect applied (passthrough) |

Modifiers on `Glass`:
- `.tint(_:)` - Add a tint color for prominence
- `.interactive()` - React to touch and pointer interactions (like glass buttons)

## Notes

- All reference documentation is extracted from official Apple Developer Documentation
- Liquid Glass APIs are new in iOS 26 / macOS 26 (WWDC 2025)
- The NeuralForge sidebar is a reference design - adapt the patterns to your specific app's needs
- When sidebars collapse on narrow devices (iPhone, Apple Watch), `NavigationSplitView` automatically stacks columns
- Section headers in lists now use title-style capitalization (no longer all-caps) in the latest SDK

## Updating

To refresh this skill with updated documentation:
1. Re-run the scraper with the same configuration
2. The skill will be rebuilt with the latest information
