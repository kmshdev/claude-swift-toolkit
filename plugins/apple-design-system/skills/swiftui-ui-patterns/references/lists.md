# List Patterns

## Correctness Rules

### ForEach Identity — Stable IDs Required

```swift
// Good — Identifiable
ForEach(users) { user in UserRow(user: user) }

// Good — keypath
ForEach(users, id: \.userId) { user in UserRow(user: user) }

// Wrong — indices create static content, can crash on removal
ForEach(users.indices, id: \.self) { index in UserRow(user: users[index]) }
```

### Constant View Count per Element

```swift
// Good
ForEach(items) { item in ItemRow(item: item) }

// Bad — variable view count breaks identity
ForEach(items) { item in
    if item.isSpecial {
        SpecialRow(item: item)
        DetailRow(item: item)
    } else {
        RegularRow(item: item)
    }
}
```

### No Inline Filtering

```swift
// Bad — unstable identity
ForEach(items.filter { $0.isEnabled }) { item in ItemRow(item: item) }

// Good — prefilter and cache
@State private var enabledItems: [Item] = []
ForEach(enabledItems) { item in ItemRow(item: item) }
.onChange(of: items) { _, new in enabledItems = new.filter(\.isEnabled) }
```

### No AnyView in Rows

Wrap in a unified row view instead of `AnyView`.

### Enumerated Sequences

```swift
// Must convert to array
ForEach(Array(items.enumerated()), id: \.offset) { index, item in
    Text("\(index): \(item)")
}
```

## UX Patterns

### Feed List with Scroll-to-Top

```swift
ScrollViewReader { proxy in
    List {
        ForEach(items) { item in
            TimelineRow(item: item)
                .id(item.id)
                .listRowInsets(.init(top: 12, leading: 16, bottom: 6, trailing: 16))
                .listRowSeparator(.hidden)
        }
    }
    .listStyle(.plain)
    .environment(\.defaultMinListRowHeight, 1)
    .onChange(of: selectedTabScrollToTop) { _, _ in
        withAnimation { proxy.scrollTo(topAnchorID, anchor: .top) }
    }
}
```

### Settings-Style List

```swift
List {
    Section("General") {
        NavigationLink("Display") { DisplaySettingsView() }
        NavigationLink("Haptics") { HapticsSettingsView() }
    }
    Section("Account") {
        Button("Sign Out", role: .destructive) {}
    }
}
.listStyle(.insetGrouped)
```

### Custom Styling

```swift
List(items) { item in
    ItemRow(item: item)
        .listRowInsets(EdgeInsets(top: 8, leading: 16, bottom: 8, trailing: 16))
        .listRowSeparator(.hidden)
}
.listStyle(.plain)
.scrollContentBackground(.hidden)
.background(Color.customBackground)
```

### Pull-to-Refresh

```swift
List(items) { item in ItemRow(item: item) }
.refreshable { await loadItems() }
```

## Rules

- Stable identity for ForEach (never `.indices` for dynamic content)
- Constant view count per ForEach element
- Prefilter collections before ForEach, don't inline `.filter`
- No `AnyView` in list rows
- Use `.contentShape(Rectangle())` for full-row tappability
- `.listStyle(.plain)` for feeds, `.insetGrouped` for settings
- `.refreshable` for pull-to-refresh
