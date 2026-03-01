---
name: swiftui-input-api
description: This skill should be used when the user asks to "add TextField", "implement text input", "create pickers/sliders", "handle keyboard shortcuts", "use onKeyPress", or needs SwiftUI user input API reference. Provides TextField, SecureField, TextEditor, form controls, keyboard shortcuts, and key press handling patterns.
---

# User Input API Reference

## Lifecycle Position

Phase 3 API Reference — load during implementation when building forms, text fields, or interactive controls. Dispatched from `autonomous-ui-workflow` Phase 2 research table.

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

## When to Use Which

| Need | Use |
|------|-----|
| Single-line text entry | `TextField("Placeholder", text: $value)` |
| Password/secret entry | `SecureField("Password", text: $password)` |
| Multi-line text editing | `TextEditor(text: $body)` or `TextField` with `.lineLimit(3...6)` (iOS 16+) |
| Email/URL/phone input | `TextField` with `.textContentType(.emailAddress)` and `.keyboardType(.emailAddress)` |
| Date/time selection | `DatePicker("Date", selection: $date)` |
| Color selection | `ColorPicker("Color", selection: $color)` |
| Numeric stepper | `Stepper("Count: \(count)", value: $count, in: 0...100)` |
| Form field navigation | `@FocusState` with `.focused($focus, equals: .field)` |
| Search filtering | `.searchable(text: $search)` on NavigationStack |

## Focus Management (Critical for forms)

```swift
enum Field: Hashable { case name, email, password }
@FocusState private var focus: Field?

TextField("Name", text: $name)
    .focused($focus, equals: .name)
    .onSubmit { focus = .email }
    .submitLabel(.next)

TextField("Email", text: $email)
    .focused($focus, equals: .email)
    .textContentType(.emailAddress)
    .onSubmit { focus = .password }
    .submitLabel(.next)

SecureField("Password", text: $password)
    .focused($focus, equals: .password)
    .onSubmit { submit() }
    .submitLabel(.done)
```

## macOS Form Conventions

- Use `Form` in `Settings` scene for preference windows
- Use `LabeledContent("Label") { control }` for aligned form rows
- Use `Toggle`, `Picker` with `.pickerStyle(.menu)` for macOS-native feel
- Keyboard shortcuts: `.keyboardShortcut("s", modifiers: .command)` on save buttons

## Common Mistakes

1. No `@FocusState` in forms — user can't Tab between fields on macOS or use Next on iOS keyboard
2. TextField without `.textContentType()` — misses AutoFill for emails, passwords, addresses
3. Using `onTapGesture` to dismiss keyboard instead of `.scrollDismissesKeyboard(.interactively)`
4. Missing `.submitLabel()` — iOS keyboard shows generic "return" instead of "Next"/"Done"/"Search"
5. `DatePicker` without `.datePickerStyle()` on macOS — defaults may not fit the layout

**Before (incorrect):**
```swift
// Form with no focus management:
TextField("Email", text: $email)
TextField("Password", text: $password)
// User must tap each field manually; Tab does nothing on macOS
```

**After (correct):**
```swift
enum Field: Hashable { case email, password }
@FocusState private var focus: Field?

TextField("Email", text: $email)
    .focused($focus, equals: .email)
    .textContentType(.emailAddress)
    .submitLabel(.next)
    .onSubmit { focus = .password }

SecureField("Password", text: $password)
    .focused($focus, equals: .password)
    .textContentType(.password)
    .submitLabel(.done)
    .onSubmit { login() }
```

**Before (incorrect):**
```swift
// Dismiss keyboard on tap — brittle, misses scroll gesture:
.onTapGesture { UIApplication.shared.sendAction(#selector(UIResponder.resignFirstResponder), ...) }
```

**After (correct):**
```swift
ScrollView {
    // form content
}
.scrollDismissesKeyboard(.interactively)
```

## Checklist

- [ ] All form fields have `@FocusState` for keyboard/Tab navigation
- [ ] Text fields have `.textContentType()` for AutoFill
- [ ] `.submitLabel()` set on all text fields in forms
- [ ] `.onSubmit` chains focus to next field (or submits on last field)
- [ ] macOS forms use `LabeledContent` for alignment
- [ ] `.searchable()` used instead of custom search TextField in navigation contexts

## Cross-References

- `swiftui-presentation-api` — sheets and alerts that contain forms
- `swiftui-typography-api` — text styles for form labels
- `swiftui-ui-patterns` — state management for form data (`@Observable` view model pattern)
- `swiftui-26-api` — iOS 26 rich text: `AttributedTextSelection`, `AttributedTextFormattingDefinition`, `FindContext`
