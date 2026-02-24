---
name: neuralforge-chat-sidebar
description: Use when building a SwiftUI AI chat/discussion sidebar panel with user and assistant message bubbles, avatar-aligned conversations, streaming 'thinking...' indicators, generated work item links, and a bottom message input bar. Covers ScrollView with anchored scrolling, message bubble views, markdown rendering in chat, typing indicators, real-time streaming text, contextual work item generation cards, and dark-themed inspector-panel chat layouts with Liquid Glass effects for macOS Tahoe and iOS 26.
---

# Neuralforge Chat Sidebar

A comprehensive SwiftUI reference for building AI-powered chat sidebar panels. Covers the full stack of components needed: inspector panel layout, message bubbles, scroll anchoring, streaming/typing indicators, text input bars, avatar identity, Liquid Glass effects, and generated work item cards.

## Source Information

All documentation is sourced from **Apple's official SwiftUI documentation** (extracted via sosumi.ai). This is a single-source skill — all patterns and API references trace back to Apple's developer documentation for iOS 26 / macOS Tahoe (26).

**Source confidence:** Medium. The extraction is automated from official docs, so API signatures are authoritative, but some contextual details may be abbreviated. When in doubt, cross-reference with Apple's developer documentation directly.

## When to Use This Skill

Use this skill when:

- Building a **chat sidebar panel** in SwiftUI (inspector-style or NavigationSplitView trailing column)
- Implementing **message bubbles** with user/assistant alignment, rounded corners, and foreground styling
- Adding **scroll-to-bottom anchoring** for chat message lists that auto-scroll on new messages
- Creating **streaming text indicators** (typing dots, "thinking..." animations, phase-based animations)
- Building a **text input bar** pinned to the bottom of a chat view with submit handling and keyboard shortcuts
- Styling chat UI with **Liquid Glass effects** (macOS Tahoe / iOS 26)
- Displaying **avatar images** (Circle clips, AsyncImage for remote avatars, overlay badges)
- Creating **generated work item cards** with buttons, labels, badges, and tint colors
- Implementing **dark mode theming** with `preferredColorScheme` and adaptive colors
- Wiring up **focus management** for chat input fields using `@FocusState`
- Adding **haptic feedback** on message send with `sensoryFeedback`
- Implementing **context menus** on message bubbles for copy/delete actions

Do **not** use this skill for:

- Non-SwiftUI chat implementations (UIKit, AppKit directly)
- Server-side chat logic, networking, or WebSocket management
- General SwiftUI tutorials unrelated to chat/sidebar patterns
- Navigation patterns beyond inspector/split-view sidebar placement

## Key Concepts

| Concept | SwiftUI Components | Reference File |
|---|---|---|
| Inspector panel layout | `NavigationSplitView`, `.inspector()`, `.safeAreaInset()`, `.safeAreaBar()` | `inspector_panel.md` |
| Message bubble shape | `RoundedRectangle`, `Capsule`, `.clipShape()`, `.background(_:in:)` | `message_bubble.md` |
| Message list scrolling | `ScrollView`, `.defaultScrollAnchor(.bottom)`, `ScrollViewReader` | `scrolling_and_anchoring.md` |
| Streaming/typing animation | `ProgressView`, `.phaseAnimator()`, `.contentTransition()`, `TimelineView` | `streaming_and_typing.md` |
| Text input bar | `TextField`, `.onSubmit()`, `@FocusState`, `.submitLabel()`, `.keyboardShortcut()` | `text_input.md` |
| Avatar display | `Circle`, `AsyncImage`, `Image`, `.overlay()`, `.clipShape(Circle())` | `avatar_and_identity.md` |
| Color and theming | `Color`, `.preferredColorScheme()`, `.foregroundStyle()` | `color_and_theming.md` |
| Liquid Glass effects | `.glassEffect()`, `GlassEffectContainer`, `GlassButtonStyle`, `.scrollEdgeEffectStyle()` | `liquid_glass.md` |
| Generated item cards | `Button`, `Label`, `.badge()`, `.tint()`, `.buttonStyle()`, `GlassButtonStyle` | `generated_items.md` |
| Layout primitives | `VStack`, `HStack`, `ZStack`, `LazyVStack`, `Spacer`, `Divider` | `message_list_layout.md` |
| Interactions | `.sensoryFeedback()`, `.onHover()`, `.disabled()`, `.onTapGesture()`, `.contextMenu()` | `button_and_interaction.md` |
| Sizing | `.frame(minWidth:idealWidth:maxWidth:...)` | `other.md` |

## Quick Reference

### 1. Chat Message List with Bottom Anchoring

Auto-scroll to the latest message. From official docs: `defaultScrollAnchor` controls which part of content is visible initially.

```swift
ScrollView {
    LazyVStack(alignment: .leading, spacing: 12) {
        ForEach(messages) { message in
            MessageBubbleView(message: message)
        }
    }
}
.defaultScrollAnchor(.bottom)
```

### 2. Programmatic Scroll-to-Bottom

Use `ScrollViewReader` to scroll on new message arrival. **Important:** only call `scrollTo` from actions (`onChange`, gesture handlers), never during view building.

```swift
@Namespace var bottomID

ScrollViewReader { proxy in
    ScrollView {
        LazyVStack {
            ForEach(messages) { msg in
                MessageBubbleView(message: msg)
            }
            Color.clear.frame(height: 1).id(bottomID)
        }
    }
    .onChange(of: messages.count) {
        withAnimation {
            proxy.scrollTo(bottomID)
        }
    }
}
```

### 3. Message Bubble with Rounded Background

User bubble trailing, assistant bubble leading:

```swift
HStack {
    if message.isUser { Spacer() }

    Text(message.content)
        .padding(12)
        .foregroundStyle(message.isUser ? .white : .primary)
        .background(
            message.isUser ? Color.blue : Color(.systemGray5),
            in: RoundedRectangle(cornerRadius: 16)
        )

    if !message.isUser { Spacer() }
}
.padding(.horizontal)
```

### 4. Avatar with Circle Clip and Status Badge

From official docs: apply `.resizable()` to the `Image` inside the content closure, not `AsyncImage` itself.

```swift
AsyncImage(url: avatarURL) { image in
    image.resizable()
} placeholder: {
    Circle()
        .fill(Color.gray.opacity(0.3))
}
.frame(width: 36, height: 36)
.clipShape(Circle())
.overlay(alignment: .bottomTrailing) {
    Circle()
        .fill(.green)
        .frame(width: 10, height: 10)
}
```

### 5. Streaming Typing Indicator (Phase Animation)

Animated dots using `phaseAnimator` (iOS 17+):

```swift
HStack(spacing: 4) {
    ForEach(0..<3, id: \.self) { index in
        Circle()
            .frame(width: 8, height: 8)
            .foregroundStyle(.secondary)
            .phaseAnimator([false, true]) { content, phase in
                content.opacity(phase ? 1 : 0.3)
            } animation: { _ in
                .easeInOut(duration: 0.6)
                    .delay(Double(index) * 0.2)
            }
    }
}
```

### 6. Bottom Text Input Bar (safeAreaInset)

Pin an input bar to the bottom of the chat. Use `.submitScope()` on nested fields to prevent submission propagation.

```swift
ScrollView {
    // message list
}
.safeAreaInset(edge: .bottom) {
    HStack {
        TextField("Message...", text: $messageText, axis: .vertical)
            .lineLimit(1...4)
            .textFieldStyle(.roundedBorder)
            .focused($isInputFocused)
            .onSubmit { sendMessage() }
            .submitLabel(.send)

        Button("Send", systemImage: "arrow.up.circle.fill") {
            sendMessage()
        }
        .disabled(messageText.isEmpty)
        .keyboardShortcut(.return, modifiers: .command)
    }
    .padding()
}
```

### 7. Bottom Input Bar with Scroll Edge Effect (iOS 26+)

Use `.safeAreaBar` instead of `.safeAreaInset` on iOS 26+ to get automatic scroll edge effects that maintain legibility:

```swift
ScrollView {
    // message list
}
.safeAreaBar(edge: .bottom) {
    InputBarView()
}
```

### 8. Inspector-Style Sidebar Panel

Present the chat as a trailing inspector column. Adapts to sheet on compact size classes.

```swift
MyEditorView()
    .inspector(isPresented: $showChat) {
        ChatView()
            .inspectorColumnWidth(min: 280, ideal: 320, max: 400)
    }
```

### 9. Liquid Glass Button (iOS 26+ / macOS Tahoe)

Use standard `.glass` button style instead of custom Liquid Glass effects on buttons:

```swift
Button("Generate Task", systemImage: "sparkles") {
    generateWorkItem()
}
.buttonStyle(.glass)
```

### 10. Liquid Glass on Custom View

Wrap multiple glass effects in `GlassEffectContainer` for performance and morphing:

```swift
GlassEffectContainer {
    HStack {
        Label("AI Response", systemImage: "brain")
            .padding()
            .glassEffect()
    }
}
```

### 11. Glass Effect Identity for Transitions

Use `glassEffectID` with a namespace to animate glass shapes between states:

```swift
@Namespace var glassNS

GlassEffectContainer {
    if isExpanded {
        ExpandedView()
            .glassEffect()
            .glassEffectID("panel", in: glassNS)
    } else {
        CompactView()
            .glassEffect()
            .glassEffectID("panel", in: glassNS)
    }
}
```

### 12. Scroll Edge Effect (Liquid Glass)

Maintain legibility when content scrolls beneath a bar:

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

### 13. Generated Work Item Card

```swift
Button {
    openWorkItem(item)
} label: {
    Label(item.title, systemImage: "checkmark.circle")
}
.buttonStyle(.bordered)
.tint(.blue)
.badge(item.commentCount)
```

### 14. Async Streaming Response with Content Transition

Use `.task` for async streaming. `.contentTransition(.interpolate)` smoothly animates text changes:

```swift
Text(streamedText)
    .task {
        do {
            for try await chunk in responseStream {
                streamedText += chunk
            }
        } catch {
            streamedText = "Failed to load response."
        }
    }
    .contentTransition(.interpolate)
    .animation(.easeInOut, value: streamedText)
```

### 15. Focus Management for Chat Input

From official docs: use `@FocusState` with an enum for multi-field focus, or with `Bool` for single-field:

```swift
enum ChatField: Hashable {
    case messageInput
}

@FocusState private var focusedField: ChatField?

TextField("Message...", text: $text)
    .focused($focusedField, equals: .messageInput)

// Programmatically focus:
focusedField = .messageInput
```

### 16. Context Menu on Message Bubble

```swift
Text(message.content)
    .padding()
    .contextMenu {
        Button {
            copyToClipboard(message.content)
        } label: {
            Label("Copy", systemImage: "doc.on.doc")
        }
        Button(role: .destructive) {
            deleteMessage(message)
        } label: {
            Label("Delete", systemImage: "trash")
        }
    }
```

### 17. Haptic Feedback on Message Send

```swift
Button("Send") { sendMessage() }
    .sensoryFeedback(.selection, trigger: messageCount)
```

### 18. Dark Mode Toggle

```swift
.preferredColorScheme(isDarkMode ? .dark : nil)
```

## Architecture Pattern

A typical chat sidebar view hierarchy:

```
NavigationSplitView / .inspector()
  +-- ChatView
        +-- ScrollView + .defaultScrollAnchor(.bottom)
        |     +-- LazyVStack
        |           +-- ForEach(messages)
        |                 +-- MessageBubbleView
        |                       +-- HStack (avatar + bubble)
        |                       +-- Text/Markdown content
        |                       +-- .background(in: RoundedRectangle)
        |           +-- TypingIndicatorView (conditional)
        |                 +-- phaseAnimator / ProgressView
        +-- .safeAreaInset(edge: .bottom)  // or .safeAreaBar on iOS 26+
              +-- InputBarView
                    +-- TextField + .onSubmit + @FocusState
                    +-- Button("Send") + .keyboardShortcut
```

## Reference Files

Detailed API documentation lives in `references/`. Read these when you need parameter-level detail or all available initializers.

| File | Pages | Source | What It Covers |
|---|---|---|---|
| `scrolling_and_anchoring.md` | 4 | Apple docs (medium) | `ScrollView`, `defaultScrollAnchor`, `ScrollViewReader`, `scrollTargetBehavior` — chat scroll position management including paging and view-aligned behaviors |
| `message_bubble.md` | 16 | Apple docs (medium) | `Text`, `TextField`, `TextEditor`, `RoundedRectangle`, `Capsule`, `foregroundStyle`, `background(_:in:)`, `clipShape`, `shadow`, `font`, `lineLimit`, `padding`, `contextMenu`, `textSelection`, `backgroundExtensionEffect` — the largest reference covering all text rendering and bubble styling |
| `message_list_layout.md` | 6 | Apple docs (medium) | `VStack`, `HStack`, `ZStack`, `LazyVStack`, `Spacer`, `Divider` — core layout containers for message lists |
| `streaming_and_typing.md` | 11 | Apple docs (medium) | `ProgressView`, `phaseAnimator`, `contentTransition`, `transition`, `animation`, `withAnimation`, `TimelineView`, `onChange`, `onReceive`, `task` — animation, streaming, and lifecycle patterns |
| `text_input.md` | 5 | Apple docs (medium) | `onSubmit`, `FocusState`, `focused`, `submitLabel`, `keyboardShortcut` — text input bar with focus management, keyboard handling, and submission scoping |
| `inspector_panel.md` | 7 | Apple docs (medium) | `NavigationSplitView`, `inspector`, `safeAreaInset`, `safeAreaBar`, `toolbar`, `ToolbarItem`, `navigationTitle` — panel/sidebar layout with column visibility and compact adaptation |
| `liquid_glass.md` | 5 | Apple docs (medium) | `glassEffect`, `GlassEffectContainer`, `glassEffectID`, `scrollEdgeEffectStyle`, Adopting Liquid Glass guide — comprehensive iOS 26 / macOS Tahoe design material |
| `avatar_and_identity.md` | 4 | Apple docs (medium) | `Circle`, `AsyncImage`, `Image`, `overlay` — avatar rendering with async loading, shape clipping, and phase-based image handling |
| `generated_items.md` | 7 | Apple docs (medium) | `Button`, `Label`, `GlassButtonStyle`, `badge`, `tint`, `buttonStyle`, `onTapGesture` — interactive work item cards with roles and styling |
| `color_and_theming.md` | 2 | Apple docs (medium) | `Color`, `preferredColorScheme` — dark/light mode, asset catalog colors, component-value colors, and platform-adaptive colors |
| `button_and_interaction.md` | 3 | Apple docs (medium) | `sensoryFeedback`, `onHover`, `disabled` — interaction polish, haptic feedback triggers, and hover states |
| `other.md` | 1 | Apple docs (medium) | `frame(minWidth:idealWidth:maxWidth:...)` — flexible sizing constraints for adaptive layouts |

## Working with This Skill

### Getting Started

1. Read this SKILL.md for patterns and quick reference examples
2. Start with `scrolling_and_anchoring.md` and `message_bubble.md` to build the core chat view
3. Add `text_input.md` patterns for the message input bar
4. Layer in `streaming_and_typing.md` for typing indicators

### Building the Chat Layout

1. Use `inspector_panel.md` for `.inspector()` or `NavigationSplitView` sidebar placement
2. Use `message_list_layout.md` for `LazyVStack` inside `ScrollView`
3. Apply `.defaultScrollAnchor(.bottom)` from `scrolling_and_anchoring.md`
4. Style bubbles using patterns from `message_bubble.md`
5. Add `.safeAreaInset(edge: .bottom)` for the input bar (or `.safeAreaBar` on iOS 26+)

### Applying Liquid Glass (macOS Tahoe / iOS 26)

1. Read `liquid_glass.md` for `glassEffect` and `GlassEffectContainer`
2. Use `.buttonStyle(.glass)` for action buttons — avoid custom Liquid Glass on buttons
3. Apply `.scrollEdgeEffectStyle()` for content scrolling under bars
4. Wrap multiple glass effects in `GlassEffectContainer` for performance and morphing
5. Use `glassEffectID` with `@Namespace` for animated glass transitions
6. Follow Apple guidance: limit glass to important functional elements, don't overuse

### Adding Polish

- **Haptic feedback**: `sensoryFeedback` from `button_and_interaction.md`
- **Context menus**: `contextMenu` from `message_bubble.md`
- **Keyboard shortcuts**: `keyboardShortcut` from `text_input.md`
- **Hover effects**: `onHover` from `button_and_interaction.md`
- **Text selection**: `textSelection(.enabled)` from `message_bubble.md`
- **Shadows on bubbles**: `shadow(color:radius:x:y:)` from `message_bubble.md`

### Navigating Reference Files

- **Start broad**: Use the Quick Reference above for common patterns
- **Go deep**: Open the specific reference file when you need exact API signatures, all initializer variants, or conformances
- **Largest reference**: `message_bubble.md` (16 pages) covers the most ground — text, shapes, styling, and interaction
- **Newest APIs**: `liquid_glass.md` covers iOS 26+ only APIs; check platform availability before using

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using `VStack` instead of `LazyVStack` for long message lists | Use `LazyVStack` inside `ScrollView` — only renders visible items for performance |
| Forgetting `.defaultScrollAnchor(.bottom)` | Chat lists should start scrolled to the bottom; add this modifier to `ScrollView` |
| Applying `.resizable()` directly to `AsyncImage` | Apply it to the `Image` inside the `content` closure, not the `AsyncImage` itself |
| Overusing Liquid Glass on many custom elements | Apple guidance: limit glass effects to important functional elements; use `GlassEffectContainer` to combine them |
| Hard-coding button layout metrics | Use standard `buttonStyle(.glass)` or `.bordered` — they adapt to platform automatically |
| Using `ScrollViewReader.scrollTo` during view building | Only call `scrollTo` from actions (gesture handlers, `onChange`, etc.), never during content builder execution |
| Not using `submitScope()` on nested text fields | Use `.submitScope()` to prevent inner field submissions from propagating to outer `onSubmit` handlers |
| Using `.animation(_:)` without a `value:` parameter | Prefer `.animation(_:value:)` to scope animations to specific state changes |
| Using `safeAreaInset` where `safeAreaBar` is better (iOS 26+) | `safeAreaBar` extends scroll edge effects automatically; prefer it for bars with content scrolling beneath |
| Multiple views binding `@FocusState` to the same value | Each focus binding should use a unique enum case; reusing values causes ambiguity and runtime warnings |
| Not wrapping glass effects in `GlassEffectContainer` | Multiple standalone `glassEffect()` calls hurt performance; wrap them in a container for optimized rendering |

## Platform Availability Notes

| Feature | Minimum Platform |
|---|---|
| `glassEffect`, `GlassButtonStyle`, `GlassEffectContainer` | iOS 26.0+, macOS 26.0+ |
| `safeAreaBar`, `scrollEdgeEffectStyle` | iOS 26.0+, macOS 26.0+ |
| `backgroundExtensionEffect` | iOS 26.0+, macOS 26.0+ |
| `glassEffectID` | iOS 26.0+, macOS 26.0+ |
| `inspector(isPresented:)` | iOS 17.0+, macOS 14.0+ |
| `defaultScrollAnchor` | iOS 17.0+, macOS 14.0+ |
| `phaseAnimator` | iOS 17.0+, macOS 14.0+ |
| `scrollTargetBehavior` | iOS 17.0+, macOS 14.0+ |
| `sensoryFeedback` | iOS 17.0+, macOS 14.0+ |
| `contentTransition` | iOS 16.0+, macOS 13.0+ |
| `NavigationSplitView` | iOS 16.0+, macOS 13.0+ |
| `FocusState` | iOS 15.0+, macOS 12.0+ |
| `AsyncImage` | iOS 15.0+, macOS 12.0+ |
| `task(priority:_:)` | iOS 15.0+, macOS 12.0+ |
| `safeAreaInset` | iOS 15.0+, macOS 12.0+ |
| `onSubmit` | iOS 15.0+, macOS 12.0+ |
| `ScrollView`, `TextField`, `Text`, `Button` | iOS 13.0+, macOS 10.15+ |

## Liquid Glass Adoption Guide

Key principles from Apple's official "Adopting Liquid Glass" documentation:

1. **Standard components adopt automatically.** Build with the latest SDK and standard SwiftUI controls pick up Liquid Glass appearance.
2. **Remove custom backgrounds.** Custom backgrounds in controls and navigation elements can overlay or interfere with Liquid Glass effects.
3. **Limit custom glass usage.** Apply `glassEffect` sparingly to the most important functional elements. Overuse distracts from content.
4. **Combine with GlassEffectContainer.** Multiple glass effects should be wrapped in a container for rendering performance and morphing animations.
5. **Test accessibility settings.** Liquid Glass adapts to reduced transparency and motion settings. Ensure custom elements degrade gracefully.
6. **Use scroll edge effects.** Apply `.scrollEdgeEffectStyle` or `.safeAreaBar` so content remains legible when scrolling beneath bars.
7. **Prefer built-in button styles.** Use `.buttonStyle(.glass)` or `GlassProminentButtonStyle` rather than manually applying glass to custom buttons.

## Notes

- All documentation is extracted from Apple's official SwiftUI docs via sosumi.ai
- Code examples use proper `swift` language annotations
- Reference files preserve original API signatures, conformances, and related links
- Liquid Glass APIs require building against the latest iOS 26 / macOS Tahoe SDK
- When reference docs mention deprecated APIs (e.g., `onChange(of:perform:)`), prefer the newer overloads documented in the same reference file
