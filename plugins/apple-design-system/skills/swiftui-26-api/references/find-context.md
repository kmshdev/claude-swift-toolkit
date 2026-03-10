# FindContext API
Environment-based find navigator context for custom text views. Access via @Environment(\.findContext). Not specific to TextEditor — works with any view implementing text search.

## FindContext

**URL:** https://sosumi.ai/documentation/SwiftUI/FindContext?.md

**Contents:**
- Overview
- Conforms To
- Instance Properties
- Searching for text in a view

**Navigation:** [SwiftUI](/documentation/SwiftUI)

**Available on:** iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+

Views which support text editing can use this information to implement a a find navigator that is controlled using the modifiers used for controlling the find navigator throughout the rest of SwiftUI.

For example, the following shows a minimal find navigator implementation driven by the find context which falls back to local state if no `isPresented` binding is provided:

*Extracted by [sosumi.ai](https://sosumi.ai) - Making Apple docs AI-readable.* *This is unofficial content. All documentation belongs to Apple Inc.*

**Examples:**

Example 1 (swift):
```swift
struct FindContext
```

Example 2 (swift):
```swift
struct FindNavigatorDrivenTextInput: View {
    @State var text: String = ""
    @State var showFindNavigator = false
    @Environment(\.findContext) var findContext
    var body: some View {
        MyTextInputView(text: $text)
            .overlay(alignment: .topTrailing) {
                if let context = findContext &&
                    context.isPresented?.wrappedValue ?? showFindNavigator
                {
                    HStack {
                        FindInputView(text: text)
                        if context.allowedOperations == .findAndReplace {
                            ReplaceInputView(text: $text)
                        }
                        Button("Close") {
                            context.isPresented?.wrappedValue = false
                            showFindNavigator = false
                        }
                    }
                } else {
                    Button("Show Find Navigator") {
                        context.isPresented?.wrappedValue = true
                        showFindNavigator = true
                    }
                }
            }
    }
}
```

---

## Anti-Pattern

| Don't | What Happens | Do Instead |
|-------|-------------|-----------|
| Force-unwrap `FindContext` from environment | `@Environment(\.findContext)` returns optional — force-unwrap crashes if no find context provided | `if let context = findContext { ... }` |

## Reading Paths

**Path B — Rich Text Editor (this file is step 2):**
← From `text-editing.md` → this file
