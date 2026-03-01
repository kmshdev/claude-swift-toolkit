---
name: swiftui-26-api
description: "Non-glass SwiftUI APIs from WWDC 2025 (iOS 26, macOS 26, visionOS 26). Covers @Animatable macro, TextEditor with AttributedString/AttributedTextSelection/AttributedTextFormattingDefinition, FindContext, WebView/WebPage, UIHostingSceneDelegate, ToolbarSpacer, Slider ticks, windowResizeAnchor, dragContainer, draggable(containerItemID:), scrollEdgeEffectStyle, tabBarMinimizeBehavior. Use when building rich text editors, embedding web content, bridging UIKit scenes to SwiftUI, or configuring scroll edge effects and tab bar minimization. DO NOT use for Liquid Glass design patterns (use apple-liquid-glass-design), general Swift or pre-iOS 26 SwiftUI (use swiftui-ui-patterns)."
---

# SwiftUI 26 API Reference

Non-glass SwiftUI APIs introduced at WWDC 2025 targeting **iOS 26, macOS 26, visionOS 26**. Synthesized from official Apple documentation (via sosumi.ai extractions).

> **For Liquid Glass APIs** (`glassEffect`, `GlassEffectContainer`, `backgroundExtensionEffect`, morph animations), load `apple-liquid-glass-design` skill instead.

---

## Quick Reference

### Animation

#### 1. @Animatable Macro

**iOS 13+ · macOS 10.15+ (Swift 5.9+ compiler required)**

Auto-synthesizes animatableData from the struct's numeric properties. Non-animatable properties must use @AnimatableIgnored.

```swift
@Animatable
struct CoolShape: Shape {
    var width: CGFloat
    var angle: Angle
    @AnimatableIgnored var isOpaque: Bool
    // animatableData synthesized from width + angle
}
```

### Text Editing

#### 2. AttributedString TextEditor with Selection

**iOS 26+ · macOS 26+**

Use `TextEditor` with an `AttributedString` binding and `AttributedTextSelection` to track the insertion point or selected range.

```swift
struct SuggestionTextEditor: View {
    @State var text: AttributedString = ""
    @State var selection = AttributedTextSelection()

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            SuggestionsView(substrings: getSubstrings(
                text: text, indices: selection.indices(in: text)))
        }
    }
}
```

#### 3. Formatting Definition

**iOS 26+ · macOS 26+**

Define an `AttributedTextFormattingDefinition` to restrict which formatting attributes are valid in a `TextEditor`.

```swift
struct MyTextFormattingDefinition: AttributedTextFormattingDefinition {
    var body: some AttributedTextFormattingDefinition<
        AttributeScopes.SwiftUIAttributes
    > {
        ValueConstraint(
            for: \.underlineStyle,
            values: [nil, .single],
            default: .single)
        MyAttributedTextValueConstraint()
        ContactsArePurple()
    }
}
```

### Web Content

#### 4. WebView with WebPage Controller

**iOS 26+ · macOS 26+ · visionOS 26+** (requires `import WebKit`)

Displays web content in a native SwiftUI view. Connect a WebPage controller for navigation, JavaScript, and title binding.

```swift
import WebKit

struct ContentView: View {
    @State private var page = WebPage()

    var body: some View {
        NavigationStack {
            WebView(page)
                .navigationTitle(page.title)
        }
    }
}
```

### UIKit Bridge

#### 5. UIHostingSceneDelegate

**iOS 26+ · iPadOS 26+ · tvOS 26+ · visionOS 26+**

Use `UIHostingSceneDelegate` to activate SwiftUI scenes from a UIKit app.

```swift
class HostingSceneDelegate: UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup(id: "swiftui-window") {
            ContentView()
        }
    }
}

// Activate from UIKit:
if let request = UISceneSessionActivationRequest(
    hostingDelegateClass: HostingSceneDelegate.self,
    id: "swiftui-window"
) {
    UIApplication.shared.activateSceneSession(for: request)
}
```

### Scroll & Tab Behavior

#### 6. Scroll Edge Effect

**iOS 26+ · macOS 26+**

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

#### 7. Tab Bar Minimization

**iOS 26+ · macOS 26+**

```swift
TabView {
    Tab("Numbers", systemImage: "number") {
        ScrollView {
            ForEach(0 ..< 50) { index in
                Text("\(index)").padding()
            }
        }
    }
}
.tabBarMinimizeBehavior(.onScrollDown)
```

### Toolbar & Layout

#### 8. Toolbar Spacer

**iOS 26+ · iPadOS 26+ · macOS 26+**

```swift
ContentView()
    .toolbar(id: "main-toolbar") {
        ToolbarItem(id: "tag") { TagButton() }
        ToolbarItem(id: "share") { ShareButton() }
        ToolbarSpacer(.fixed)
        ToolbarItem(id: "more") { MoreButton() }
    }
```

### macOS Only

#### 9. Window Resize Anchor — macOS 26

```swift
struct HeightResizingExample: View {
    @State private var height: CGFloat = 300

    var body: some View {
        Color.red
            .overlay { Text("Tap to toggle").foregroundStyle(.white) }
            .onTapGesture {
                withAnimation(.easeInOut) {
                    height = height == 300 ? 700 : 300
                }
            }
            .frame(width: 250, height: height)
            .windowResizeAnchor(.top)
    }
}
```

#### 10. Drag Container — macOS 26

```swift
VStack {
    ForEach(fruits) { fruit in
        FruitView(fruit)
            .draggable(containerItemID: fruit.name)
    }
}
.dragContainer(itemID: \Fruit.name) { ids in
    fruits(with: ids)
}
```

---

## Reading Paths

Clustered reference file sequences for common goals.

**A — Adopting Liquid Glass:**
Load `apple-liquid-glass-design` skill — it contains complete glass adoption paths.

**B — Building a Rich Text Editor:**
`text-editing.md` → `find-context.md`

**C — Embedding Web Content:**
`webkit.md` → `uikit-scene-bridge.md` (if UIKit host)

**D — Migrating an Existing App:**
Migration sections are embedded in each reference file: `webkit.md` (WKWebView → WebView), `uikit-scene-bridge.md` (UIHostingController → UIHostingSceneDelegate), `animatable-macro.md` (manual animatableData → @Animatable). For glass migration (.material → .glassEffect), see `apple-liquid-glass-design`.

**E — macOS-Specific Features:**
`macos-drag-and-windows.md` → `toolbar-and-slider.md`

**F — Custom Shape Animation:**
`animatable-macro.md` → `apple-liquid-glass-design` (if animating glass shapes)

---

## Common Gotchas

1. **`WebPage` is `@MainActor`** — all interactions must happen on the main actor
2. **One `WebPage` per `WebView`** — only one `WebPage` can bind to a single `WebView` at a time
3. **Drag container APIs are macOS 26 only** — `dragContainer` and `draggable(containerItemID:)` are not available on iOS
4. **`@Animatable` availability is broad** — the macro works back to iOS 13, but requires Swift 5.9+ compiler
5. **`FindContext` uses environment** — access via `@Environment(\.findContext)`, returns optional
6. **`TextEditor` selection requires `AttributedString`** — `AttributedTextSelection` binding doesn't work with plain `String`

---

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `WebView` type not found | Missing framework import | Add `import WebKit` — WebView/WebPage are in WebKit, not SwiftUI |
| `@Animatable` compilation error | Compiler too old | Requires Swift 5.9+ (Xcode 15+), even though protocol availability is iOS 13+ |
| `scrollEdgeEffectStyle` has no visible effect | Applied to wrong container | Only works on `ScrollView`, not `List` |
| `UIHostingSceneDelegate` callbacks not firing | Missing scene declaration | Ensure `static var rootScene` is implemented and `UISceneConfiguration.delegateClass` is set |
| `FindContext` is nil at runtime | Not accessing via environment | Use `@Environment(\.findContext) var findContext` — returns optional |
| `WebPage.title` is always nil | Not stored as @State | Declare as `@State private var page = WebPage()` |
| `windowResizeAnchor` ignored during shrink | Missing resizability setting | Set `.windowResizability(.contentSize)` on the Scene |
| `AttributedTextSelection.indices` returns empty | Selection bound to String | `TextEditor` must use `$attributedString` binding, not `$string` |
| `dragContainer` compile error on iOS | macOS 26 only | Guard with `#if os(macOS)` |

---

## Reference Files

| File | Read when... |
|------|-------------|
| `references/animatable-macro.md` | using `@Animatable` macro to synthesize animatableData |
| `references/text-editing.md` | building `TextEditor` with `AttributedString`, selection, or formatting definitions |
| `references/find-context.md` | implementing find/replace via `FindContext` |
| `references/webkit.md` | embedding web content with `WebView` or `WebPage` |
| `references/uikit-scene-bridge.md` | bridging UIKit scene lifecycle to SwiftUI via `UIHostingSceneDelegate` |
| `references/macos-drag-and-windows.md` | adding `dragContainer`/`draggable` or `windowResizeAnchor` (macOS 26 only) |
| `references/scroll-and-tabs.md` | configuring `scrollEdgeEffectStyle` or `tabBarMinimizeBehavior` |
| `references/toolbar-and-slider.md` | adding `ToolbarSpacer` or `Slider` tick marks |

## Cross-References

- `apple-liquid-glass-design` — All Liquid Glass APIs (glassEffect, GlassEffectContainer, backgroundExtensionEffect, morph animations)
- `swiftui-input-api` — Pre-iOS 26 TextEditor, text fields, pickers
- `swift-app-lifecycle` — Scene phase management, app entry points
- `swiftui-effects-api` — Pre-iOS 26 blur, shadow, opacity effects
