---
name: swiftui-input-api
description: Use when implementing text fields, text editors, pickers, sliders, toggles, keyboard shortcuts, key press handlers, or form controls in SwiftUI - covers TextField, SecureField, TextEditor with AttributedString, autocorrection, and keyboard input handling
---

# User Input API Reference

## Text Input

```swift
TextField("Username", text: $username)
TextField(text: $username, prompt: Text("Required")) { Text("Username") }
SecureField("Password", text: $password)
TextEditor(text: $notes)
TextEditor(text: $attributedText, selection: $selection)  // rich text
```

## Text Modifiers

| Modifier | Purpose |
|----------|---------|
| `.autocorrectionDisabled()` | Disable autocorrect |
| `.keyboardType(_:)` | Keyboard type (iOS) |
| `.scrollDismissesKeyboard(_:)` | Dismiss on scroll |
| `.textInputAutocapitalization(_:)` | Auto-caps |
| `.textInputSuggestions { }` | Custom suggestions |
| `.textContentType(_:)` | Content type hints |
| `.textSelection(_:)` | Enable/disable selection |

## Controls

```swift
Picker("Choice", selection: $choice) { Text("A").tag(0) }.pickerStyle(.menu)
Slider(value: $volume, in: 0...100)
Stepper("Qty: \(count)", value: $count, in: 1...10)
Toggle("Feature", isOn: $isEnabled).toggleStyle(.switch)
```

## Keyboard Shortcuts

```swift
Button("Save") { save() }.keyboardShortcut("s", modifiers: .command)
Button("OK") { confirm() }.keyboardShortcut(.defaultAction)
```

## Key Press Handling

```swift
.onKeyPress(.return) { submit(); return .handled }
.onKeyPress(phases: .down) { keyPress in return .handled }
.onKeyPress(characters: .alphanumerics, phases: .down) { _ in .handled }
.onModifierKeysChanged(mask: .shift) { old, new in }
```
