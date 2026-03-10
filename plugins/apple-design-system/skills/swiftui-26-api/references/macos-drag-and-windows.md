# macOS Drag-and-Drop and Window APIs
macOS 26-only APIs for container-based drag and drop (dragContainer, draggable) and window resize anchoring (windowResizeAnchor).

## Table of Contents
- [dragContainer(for:itemID:in:\_:)](#dragcontainerforitemidini_)
- [draggable(containerItemID:containerNamespace:)](#draggablecontaineritemidcontainernamespace)
- [windowResizeAnchor(\_:)](#windowresizeanchor_)

## dragContainer(for:itemID:in:_:)

**URL:** https://sosumi.ai/documentation/SwiftUI/View/dragContainer(for:itemID:in:_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion

**Navigation:** [SwiftUI](/documentation/SwiftUI) › [View](/documentation/SwiftUI/View)

**Available on:** macOS 26.0+

A type of the dragged items.

A closure that provides an item's identifier.

A namespace that identifies the drag container.

A closure which is called when a drag operation begins. As an argument, the closure receives either the identifiers of all the selected items, if the dragged item is a part of selection or only the identifier of the dragged item, if it is not part of the selection. Using the passed identifiers, put together the payload to drag, and return from the closure. Return an empty `Collection` to disable the drag.

A view that can be activated as the source of a drag and drop operation, beginning with user gesture input.

In an example below, an app presents a view with `Fruit` values. `Fruit` does not conform to `Identifiable` but uses its name as its identifier.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func dragContainer<ItemID, Item, Data>(for itemType: Item.Type = Item.self, itemID: KeyPath<Item, ItemID>, in namespace: Namespace.ID? = nil, _ payload: @escaping (Array<ItemID>) -> Data) -> some View where ItemID : Hashable, ItemID : Sendable, Item : Transferable, Item == Data.Element, Data : Collection
```

Example 2 (swift):
```swift
   @State private var fruits: [Fruit]
   @State private var selection: [String]

   var body: some View {
       VStack {
           ForEach(fruits) { fruit in
               FruitView(fruit)
                   .draggable(containerItemID: fruit.name)
           }
       }
       .dragContainer(itemID: \Fruit.name) { ids in
          fruits(with: ids)
       }
   }

   func fruits(with ids: [String]) -> [Fruit] { ... }

   struct Fruit: Transferable {
       var name: String
       ...
   }
```

---

## draggable(containerItemID:containerNamespace:)

**URL:** https://sosumi.ai/documentation/SwiftUI/View/draggable(containerItemID:containerNamespace:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion

**Navigation:** [SwiftUI](/documentation/SwiftUI) › [View](/documentation/SwiftUI/View)

**Available on:** macOS 26.0+

An identifier of the associated drag payload.

**containerNamespace**

A namespace of the associated drag container.

A view that activates this view as the source of a drag and drop operation, beginning with user gesture input.

This modifier marks the view as a draggable element of an enclosing `dragContainer(*:containerNamespace:*:)`. Since this modifier does not require to provide the payload, only its identifier, it works lazily (the framework asks to provide the actual dragged items only when drag starts; also, the framework doesn't have to render a view in order to access its payload).

Applying the `draggable(containerItemID:containerNamespace:)` modifier to a view inside a drag container adds the appropriate gestures for drag and drop to this view. SwiftUI generates a default drag preview for drag.

Below, each `FruitView` is assigned an identifier: a code of a fruit it represents. When dragging begins, the `dragContainer` closure is called with the codes of the selected fruit, or, if a user drags a view that is not selected, the closure receives the identifier of that view as a parameter.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
nonisolated func draggable<ItemID>(containerItemID: ItemID, containerNamespace: Namespace.ID? = nil) -> some View where ItemID : Hashable, ItemID : Sendable
```

Example 2 (swift):
```swift
   var fruits: [Fruit]
   var selectedFruitCodes: [UUID]

   var body: some View {
       VStack {
           ForEach(fruits) { fruit in
               .draggable(containerItemID: fruit.code)
       }
       .dragContainer { codes in
           fruits(with: codes)
       }
       .dragContainerSelection(selectedFruitCodes)
   }

   func fruits(with codes: [UUID]) -> [Fruit] { ... }

   struct Fruit: Transferable {
       var code: UUID
       ...
   }
```

---

## windowResizeAnchor(_:)

**URL:** https://sosumi.ai/documentation/SwiftUI/View/windowResizeAnchor(_:)?.md

**Contents:**
- Parameters
- Return Value
- Discussion

**Navigation:** [SwiftUI](/documentation/SwiftUI) › [View](/documentation/SwiftUI/View)

**Available on:** macOS 26.0+

The window point fixed under programmatic size changes caused by the content size of the window changing. Defaults to a system defined value when `nil`.

A view whose scene resizes on `anchor`.

In SwiftUI life cycle apps, this modifier can be used to control how a window anchors when animating: drive window animations by changing the size of a view in a way that causes the window size to change. Note that if the window size is decreasing and an animation is desired, it is often necessary to (temporarily, if desired) set the [windowResizability(*:)](/documentation/swiftui/scene/windowresizability(*:)) to [content Size](/documentation/swiftui/windowresizability/contentsize).

The default anchor varies by scene type and is used when `anchor` is nil. Generally, it resolves to the `.topLeading` corner.

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

### Common UnitPoint Anchors

| Anchor | Effect |
|--------|--------|
| `.top` | Window grows/shrinks downward from top edge |
| `.center` | Window resizes symmetrically around center |
| `.topLeading` | Default — window anchors at top-left corner |
| `.bottom` | Window grows upward from bottom edge |

**Examples:**

Example 1 (swift):
```swift
nonisolated func windowResizeAnchor(_ anchor: UnitPoint?) -> some View
```

Example 2 (swift):
```swift
struct Scratchpad: App {
    var body: some Scene {
        WindowGroup {
            HeightResizingExample()
        }
        .windowResizability(.contentSize)
    }
}

struct HeightResizingExample: View {
    @State private var height: CGFloat = 300

    var body: some View {
        ZStack(alignment: .topLeading) {
            Color.red
                .overlay {
                    Text("Tap to toggle")
                        .foregroundStyle(.white)
                }
        }
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

---

## Anti-Patterns

| Don't | What Happens | Do Instead |
|-------|-------------|-----------|
| Use `dragContainer` on iOS target | Compile error — API is macOS 26 only | Guard with `#if os(macOS)` or use platform-conditional views |
| `windowResizeAnchor(.top)` without `.windowResizability(.contentSize)` | Shrink animations don't work — anchor is ignored | Set `.windowResizability(.contentSize)` on the Scene |

## Reading Paths

**Path E — macOS Features (this file is step 1):**
Start here → Next: `toolbar-and-slider.md` → For glass effects, load `apple-liquid-glass-design`
