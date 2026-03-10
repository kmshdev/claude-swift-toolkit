# Form Patterns

## Settings-Style Form

```swift
Form {
    Section("General") {
        NavigationLink("Display") { DisplaySettingsView() }
        NavigationLink("Haptics") { HapticsSettingsView() }
    }
    Section("Account") {
        Button("Edit profile") { /* open sheet */ }
            .buttonStyle(.plain)
    }
    .listRowBackground(theme.primaryBackgroundColor)
}
.navigationTitle("Settings")
.navigationBarTitleDisplayMode(.inline)
.scrollContentBackground(.hidden)
.background(theme.secondaryBackgroundColor)
```

## Modal Form with Validation

```swift
@MainActor
struct AddServerView: View {
    @Environment(\.dismiss) private var dismiss
    @State private var server = ""
    @State private var isValid = false
    @FocusState private var isServerFieldFocused: Bool

    var body: some View {
        NavigationStack {
            Form {
                TextField("Server URL", text: $server)
                    .keyboardType(.URL)
                    .textInputAutocapitalization(.never)
                    .autocorrectionDisabled()
                    .focused($isServerFieldFocused)

                Button("Add") {
                    guard isValid else { return }
                    dismiss()
                }
                .disabled(!isValid)
            }
            .formStyle(.grouped)
            .navigationTitle("Add Server")
            .navigationBarTitleDisplayMode(.inline)
            .scrollContentBackground(.hidden)
            .scrollDismissesKeyboard(.immediately)
            .toolbar { CancelToolbarItem() }
            .onAppear { isServerFieldFocused = true }
        }
    }
}
```

## Rules

- Prefer `Form` over custom stacks for settings and data entry screens
- Group related controls in `Section` blocks
- Use `.formStyle(.grouped)` for grouped styling
- Use `.scrollContentBackground(.hidden)` + custom background for theming
- Use `@FocusState` for keyboard focus management
- Auto-focus the primary field with `.onAppear { isFocused = true }`
- Wrap in `NavigationStack` only when presented standalone (sheet/root)
- Don't mix background strategies — pick default or custom, not both
