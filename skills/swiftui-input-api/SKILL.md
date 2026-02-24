---
name: swiftui-input-api
description: This skill should be used when the user asks to "add TextField", "implement text input", "create pickers/sliders", "handle keyboard shortcuts", "use onKeyPress", or needs SwiftUI user input API reference. Provides TextField, SecureField, TextEditor, form controls, keyboard shortcuts, and key press handling patterns.
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
