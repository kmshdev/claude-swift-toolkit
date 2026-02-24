---
name: neuralforge-main-content
description: Use this skill when building a SwiftUI issue/ticket detail view with title headers, status dependency links, rich description blocks, horizontal tag pill strips (Active, UX, owners, priority), work item card grids (2-column LazyVGrid), and status indicator badges. Covers LazyVGrid, card components, tag/chip views, priority indicators, date formatting, and dark-themed project management detail layouts with Liquid Glass effects for macOS Tahoe and iOS 26.
---

# Neuralforge Main Content Skill

Build SwiftUI project management detail views featuring title headers, status/dependency links, rich description blocks, horizontal tag pill strips, 2-column work item card grids, and status indicator badges. This skill covers layout containers (LazyVGrid, HStack, VStack, ZStack), card components with shadows and overlays, tag/chip pill views with Capsule backgrounds, typography and color theming, Liquid Glass effects for iOS 26 / macOS Tahoe, and dark-themed detail layouts.

**Source:** Official Apple SwiftUI documentation via sosumi.ai extraction.

## When to Use This Skill

This skill should be triggered when:

- **Building issue/ticket detail views** in SwiftUI with title, status, description, tags, and related work items
- **Creating 2-column card grids** using `LazyVGrid` with `GridItem(.flexible())` for work item displays
- **Implementing tag/pill strips** with horizontal `HStack` layouts using `Capsule` or `RoundedRectangle` backgrounds (e.g., "Active", "UX", "P1", owner badges)
- **Adding status indicator badges** with colored dots, priority markers, or state labels
- **Designing card components** with shadows, overlays, borders, and `GroupBox` containers
- **Applying Liquid Glass effects** to custom views using `.glassEffect()` and `GlassEffectContainer` (iOS 26+, macOS 26+)
- **Setting up dark-themed layouts** using `.preferredColorScheme(.dark)` with proper color and theming
- **Building scrollable detail views** with `ScrollView`, `LazyVStack`, and section-based content organization
- **Working with adaptive layouts** that respond to dynamic type or window size using `AnyLayout`, `ViewThatFits`, or custom `Layout` conformances
- **Creating navigation contexts** with toolbars, sections, and navigation titles for detail screens

## Key Concepts

### Layout Hierarchy for a Detail View

A typical Neuralforge-style detail view follows this structure:

```
NavigationStack / NavigationSplitView
  ScrollView
    VStack (main content)
      Text (title)                          -- .font(.title), .bold()
      HStack (status + dependency links)    -- tags, status badges
      Text / VStack (description block)     -- .font(.body), multiline
      HStack (tag pill strip)               -- Capsule backgrounds, scrollable
      LazyVGrid (work item cards)           -- 2-column GridItem(.flexible())
        ForEach (card views)                -- GroupBox / RoundedRectangle + shadow
```

### Grid Systems

- **`LazyVGrid`** - Vertically growing grid, items created lazily. Use for large scrollable card collections.
- **`LazyHGrid`** - Horizontally growing grid. Use for horizontally scrollable content.
- **`Grid` + `GridRow`** - Non-lazy, renders all at once. Better for small, precise 2D layouts with aligned columns.
- **`GridItem`** - Defines column/row sizing: `.fixed()`, `.flexible()`, `.adaptive()`.

### Tag/Pill Component Pattern

Tags use `Capsule` or `RoundedRectangle` as backgrounds with padding, wrapped in an `HStack` or `ScrollView(.horizontal)`.

### Card Component Pattern

Cards combine `RoundedRectangle` backgrounds, shadows, overlays, and optional `GroupBox` containers for visual grouping.

### Liquid Glass (iOS 26+ / macOS 26+)

The new Liquid Glass material provides translucent, dynamic glass effects for controls and navigation. Key APIs:
- `.glassEffect()` - Apply glass material to any view
- `GlassEffectContainer` - Combine multiple glass shapes for morphing and performance
- `GlassButtonStyle` / `.buttonStyle(.glass)` - Glass-styled buttons
- `.scrollEdgeEffectStyle(.hard, for: .all)` - Scroll edge effects under glass layers

## Quick Reference

### 2-Column LazyVGrid (Card Grid)

From official docs - the core pattern for work item card grids:

```swift
let columns = [GridItem(.flexible()), GridItem(.flexible())]

ScrollView {
    LazyVGrid(columns: columns) {
        ForEach(workItems) { item in
            WorkItemCard(item: item)
        }
    }
}
```

### Tag/Pill Strip with Capsule Background

From official docs - creating pill-shaped tag views:

```swift
HStack(spacing: 8) {
    ForEach(tags, id: \.self) { tag in
        Text(tag)
            .font(.caption)
            .padding(.horizontal, 12)
            .padding(.vertical, 6)
            .background(.teal, in: Capsule())
            .foregroundStyle(.white)
    }
}
```

### Card with Shadow and Overlay

From official docs - composing card components:

```swift
RoundedRectangle(cornerRadius: 12)
    .fill(Color(.systemBackground))
    .shadow(color: .gray.opacity(0.3), radius: 8, x: 0, y: 4)
    .overlay(alignment: .topTrailing) {
        Image(systemName: "star.fill")
            .foregroundStyle(.yellow)
            .padding(8)
    }
```

### Liquid Glass Effect

From official docs - applying glass material (iOS 26+):

```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()
```

### GlassEffectContainer for Multiple Glass Shapes

From official docs - combining glass shapes for performance:

```swift
GlassEffectContainer(spacing: 8) {
    ForEach(items) { item in
        ItemView(item: item)
            .glassEffect(.regular, in: RoundedRectangle(cornerRadius: 12))
    }
}
```

### Glass Button Style

From official docs - buttons with Liquid Glass (iOS 26+):

```swift
Button("Action", systemImage: "bolt.fill", action: performAction)
    .buttonStyle(.glass)
```

### Adaptive Layout with AnyLayout

From official docs - dynamically switching between HStack and VStack:

```swift
struct DynamicLayoutExample: View {
    @Environment(\.dynamicTypeSize) var dynamicTypeSize

    var body: some View {
        let layout = dynamicTypeSize <= .medium ?
            AnyLayout(HStackLayout()) : AnyLayout(VStackLayout())

        layout {
            Text("First label")
            Text("Second label")
        }
    }
}
```

### ViewThatFits for Responsive Content

From official docs - auto-selecting the best-fitting view:

```swift
ViewThatFits(in: .horizontal) {
    HStack {
        Text("\(progress.formatted(.percent))")
        ProgressView(value: progress).frame(width: 100)
    }
    ProgressView(value: progress).frame(width: 100)
    Text("\(progress.formatted(.percent))")
}
```

### Dark Theme with Color Scheme

From official docs - enforcing dark appearance:

```swift
MyDetailView()
    .preferredColorScheme(.dark)
```

### Scroll Edge Effect (iOS 26+)

From official docs - maintaining legibility under glass layers:

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

## Reference Files

This skill includes comprehensive documentation in `references/`, organized by UI concern:

| File | Description | Pages | Key APIs |
|------|-------------|-------|----------|
| **grid_and_layout.md** | Core layout containers and sizing | 13 | `LazyVGrid`, `LazyHGrid`, `Grid`, `GridItem`, `HStack`, `VStack`, `ZStack`, `LazyVStack`, `Spacer`, `Divider`, `fixedSize`, `layoutPriority`, `containerRelativeFrame` |
| **adaptive_layout.md** | Dynamic/responsive layout patterns | 3 | `AnyLayout`, `Layout` protocol, `ViewThatFits` |
| **tags_and_pills.md** | Tag strips, badges, and pill shapes | 6 | `badge(_:)`, `background(_:in:fillStyle:)`, `clipShape`, `Capsule`, `RoundedRectangle`, `padding` |
| **card_component.md** | Card composition and visual effects | 5 | `shadow`, `overlay`, `GroupBox`, `groupBoxStyle`, `border` |
| **liquid_glass.md** | Liquid Glass material system (iOS 26+) | 3 | `glassEffect(_:in:)`, `GlassEffectContainer`, Adopting Liquid Glass guide |
| **typography.md** | Text, fonts, and text-related controls | 10 | `Text`, `font(_:)`, `foregroundStyle`, `lineLimit`, `multilineTextAlignment`, `navigationTitle`, `contextMenu`, `GlassButtonStyle`, `textSelection` |
| **color_and_theming.md** | Color management and dark mode | 2 | `tint(_:)`, `preferredColorScheme(_:)` |
| **buttons_and_menus.md** | Interactive controls | 5 | `Button`, `buttonStyle(_:)`, `Menu`, `onTapGesture`, `onHover` |
| **icons_and_images.md** | Image display and SF Symbols | 3 | `Image`, `Label`, `symbolRenderingMode` |
| **navigation_context.md** | Navigation structure and sections | 2 | `toolbar(content:)`, `Section` |
| **scrolling.md** | Scroll views and scroll behavior | 3 | `ScrollView`, `scrollTargetBehavior`, `scrollEdgeEffectStyle` |
| **other.md** | Frame sizing constraints | 1 | `frame(minWidth:idealWidth:maxWidth:...)` |

All reference content is sourced from official Apple SwiftUI documentation (via sosumi.ai).

## Working with This Skill

### For Beginners

1. Start with **grid_and_layout.md** to understand `VStack`, `HStack`, `LazyVGrid`, and `Spacer` - these are the foundation of every detail view layout.
2. Read **typography.md** for `Text` and `font(_:)` basics.
3. Review **tags_and_pills.md** to learn how `Capsule` and `RoundedRectangle` backgrounds create pill-shaped tags.

### For Building the Detail View

1. Read **grid_and_layout.md** for `LazyVGrid` with `GridItem(.flexible())` to create the 2-column card grid.
2. Use **card_component.md** for shadow, overlay, and `GroupBox` patterns to compose card views.
3. Reference **tags_and_pills.md** for the horizontal tag pill strip with `background(_:in:Capsule())`.
4. Check **buttons_and_menus.md** for interactive elements like action buttons and context menus.
5. Use **navigation_context.md** for toolbar items and section organization.

### For iOS 26 / macOS Tahoe (Liquid Glass)

1. Read **liquid_glass.md** thoroughly - it covers `glassEffect(_:in:)`, `GlassEffectContainer`, and the full Adopting Liquid Glass guide.
2. Review the **Adopting Liquid Glass** section for best practices:
   - Use standard components to get automatic glass adoption
   - Avoid overusing glass effects - limit to the most important functional elements
   - Combine custom glass effects in a `GlassEffectContainer` for performance
   - Test with accessibility settings (reduce transparency, reduce motion)
3. Use `GlassButtonStyle` from **typography.md** for glass-styled buttons.
4. Apply **scrolling.md**'s `scrollEdgeEffectStyle` for scroll edge effects under glass layers.

### For Dark-Themed Layouts

1. Use **color_and_theming.md** for `preferredColorScheme(.dark)` and `tint(_:)`.
2. Reference **typography.md** for `Color` API including semantic colors (`.primary`, `.secondary`) and standard palette colors.
3. Use `foregroundStyle(.secondary)` for de-emphasized text in hierarchical layouts.

### For Responsive/Adaptive Layouts

1. Use **adaptive_layout.md** for `AnyLayout` (dynamic H/V stack switching) and `ViewThatFits` (auto-selecting best-fitting view).
2. Reference **grid_and_layout.md** for `containerRelativeFrame` to size views relative to their container.
3. Consider the `Layout` protocol for fully custom layout behavior.

## Common Patterns

### Badge/Status Indicator

```swift
HStack(spacing: 4) {
    Circle()
        .fill(.green)
        .frame(width: 8, height: 8)
    Text("Active")
        .font(.caption)
        .foregroundStyle(.secondary)
}
```

### Priority Pill

```swift
Text("P1")
    .font(.caption.bold())
    .padding(.horizontal, 8)
    .padding(.vertical, 4)
    .background(.red.opacity(0.2), in: Capsule())
    .foregroundStyle(.red)
```

### Tinted Action Buttons

From official docs:

```swift
HStack {
    Button {
        // Answer the call
    } label: {
        Label("Answer", systemImage: "phone")
    }
    .tint(.green)
    Button {
        // Decline the call
    } label: {
        Label("Decline", systemImage: "phone.down")
    }
    .tint(.red)
}
.buttonStyle(.borderedProminent)
```

### GroupBox Card

From official docs:

```swift
GroupBox(label: Label("End-User Agreement", systemImage: "building.columns")) {
    ScrollView(.vertical, showsIndicators: true) {
        Text(agreementText)
            .font(.footnote)
    }
    .frame(height: 100)
    Toggle(isOn: $userAgreed) {
        Text("I agree to the above terms")
    }
}
```

### Gradient Foreground Text

From official docs:

```swift
Text("Gradient Text")
    .font(.largeTitle)
    .foregroundStyle(
        .linearGradient(
            colors: [.yellow, .blue],
            startPoint: .top,
            endPoint: .bottom
        )
    )
```

### Context Menu on Detail Items

From official docs:

```swift
Text("Turtle Rock")
    .padding()
    .contextMenu {
        Button {
            // Add to favorites
        } label: {
            Label("Add to Favorites", systemImage: "heart")
        }
        Button {
            // Show in Maps
        } label: {
            Label("Show in Maps", systemImage: "mappin")
        }
    }
```

### Paging Scroll Behavior

From official docs:

```swift
ScrollView {
    LazyVStack(spacing: 0.0) {
        ForEach(items) { item in
            FullScreenItem(item)
        }
    }
}
.scrollTargetBehavior(.paging)
```

### View-Aligned Horizontal Scroll

From official docs:

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

## Performance Notes

- **Prefer `LazyVGrid`/`LazyHGrid`** over `Grid` for large scrollable collections. Lazy grids create views on demand.
- **Use `Grid` + `GridRow`** for small, static layouts where precise column alignment matters.
- **Combine glass effects** in a `GlassEffectContainer` to improve rendering performance when using multiple `glassEffect` modifiers.
- **Profile before switching** to lazy layouts - only use them if a `Grid` view performs poorly due to loading too many views at once.
- **Test with accessibility settings** when using Liquid Glass - reduce transparency and reduce motion settings modify glass effects.

## Notes

- This skill was generated from official Apple SwiftUI documentation extracted via sosumi.ai
- All reference files preserve the original structure, API details, and code examples from Apple's docs
- Liquid Glass APIs require iOS 26+ / macOS 26+ / tvOS 26+ / watchOS 26+
- Code examples include proper Swift language annotations for syntax highlighting
- All documentation content is unofficial - original documentation belongs to Apple Inc.
