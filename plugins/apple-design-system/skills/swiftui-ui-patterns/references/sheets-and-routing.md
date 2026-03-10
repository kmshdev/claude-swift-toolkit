# Sheet Presentation & Routing Patterns

## Leaf-Level Patterns

### Item-Driven Sheets (Preferred)

Use `.sheet(item:)` instead of `.sheet(isPresented:)` for model-based content:

```swift
@State private var selectedItem: Item?

List(items) { item in
    Button(item.name) { selectedItem = item }
}
.sheet(item: $selectedItem) { item in
    ItemDetailSheet(item: item)
}
```

**Why:** Automatically handles presentation state, avoids optional unwrapping in sheet body.

### Sheets Own Their Actions

```swift
struct EditItemSheet: View {
    @Environment(\.dismiss) private var dismiss
    @Environment(DataStore.self) private var store

    let item: Item
    @State private var name: String
    @State private var isSaving = false

    init(item: Item) {
        self.item = item
        _name = State(initialValue: item.name)
    }

    var body: some View {
        NavigationStack {
            Form { TextField("Name", text: $name) }
            .navigationTitle("Edit Item")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button(isSaving ? "Saving..." : "Save") {
                        Task { await save() }
                    }
                    .disabled(isSaving || name.isEmpty)
                }
            }
        }
    }

    private func save() async {
        isSaving = true
        await store.updateItem(item, name: name)
        dismiss()
    }
}
```

### Other Presentation Modifiers

| Modifier | Use When |
|----------|---------|
| `.sheet(item:)` | Standard modal (draggable) |
| `.fullScreenCover(isPresented:)` | Immersive content, onboarding |
| `.popover(isPresented:)` | Contextual info on iPad/Mac |
| `.alert(title:isPresented:)` | Destructive confirmation |
| `.confirmationDialog(title:isPresented:)` | Multiple-choice actions |

## App-Level Sheet Routing

For apps with many modals, centralize sheet routing with an enum:

### SheetDestination Enum

```swift
enum SheetDestination: Identifiable, Hashable {
    case composer
    case editProfile
    case settings
    case report(itemID: String)

    var id: String {
        switch self {
        case .composer, .editProfile: return "editor"  // Mutually exclusive
        case .settings: return "settings"
        case .report: return "report"
        }
    }
}
```

### withSheetDestinations Modifier

```swift
extension View {
    func withSheetDestinations(sheet: Binding<SheetDestination?>) -> some View {
        sheet(item: sheet) { destination in
            Group {
                switch destination {
                case .composer: ComposerView()
                case .editProfile: EditProfileView()
                case .settings: SettingsView()
                case .report(let id): ReportView(itemID: id)
                }
            }
        }
    }
}
```

### Presenting from Any Child View

```swift
struct StatusRow: View {
    @Environment(RouterPath.self) private var router

    var body: some View {
        Button("Report") {
            router.presentedSheet = .report(itemID: "123")
        }
    }
}
```

### NavigationSheet Wrapper

For sheets that need internal push navigation:

```swift
struct NavigationSheet<Content: View>: View {
    var content: () -> Content

    var body: some View {
        NavigationStack {
            content()
                .toolbar { CloseToolbarItem() }
        }
    }
}
```

## Rules

- Prefer `sheet(item:)` over `sheet(isPresented:)` for model-driven sheets
- Sheets own their actions — no `onSave`/`onCancel` callback prop-drilling
- Group mutually exclusive sheets under the same `id`
- Don't store heavy state in `SheetDestination` — pass lightweight IDs
- Don't mix `sheet(isPresented:)` and `sheet(item:)` for the same concern
