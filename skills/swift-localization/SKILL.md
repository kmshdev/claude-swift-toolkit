---
name: swift-localization
description: Implement localization using modern String Catalogs and LocalizedStringResource. Use when adding user-facing text, handling plurals, formatting numbers/dates for locale, or preparing an app for international release.
---

# Swift Localization

## Lifecycle Position

Phase 3 (Implement). Load when adding user-facing text to ensure localization-readiness from the start.

## Modern API (Xcode 15+, iOS 16+)

### String(localized:)
```swift
// Basic localized string
let greeting = String(localized: "welcome_message")

// With default value and comment for translators
let greeting = String(localized: "welcome_message",
                      defaultValue: "Welcome back!",
                      comment: "Greeting shown on home screen after login")

// String interpolation (automatically handled)
let message = String(localized: "items_in_cart \(count) items")
```

### LocalizedStringResource
```swift
// For deferred localization (resolved later in the correct context)
struct Notification {
    let title: LocalizedStringResource
    let body: LocalizedStringResource
}

let notification = Notification(
    title: "new_message_title",
    body: "new_message_body \(senderName)"
)

// Resolve when displaying
Text(notification.title)
```

## String Catalogs (.xcstrings)

Xcode 15+ introduces String Catalogs — a visual editor replacing `.strings` and `.stringsdict` files.

### Setup
1. File → New → File → String Catalog
2. Name it `Localizable.xcstrings`
3. Xcode auto-extracts `Text()`, `String(localized:)`, and LocalizedStringKey usage
4. Add languages in Project → Info → Localizations
5. Translate directly in the String Catalog editor

### Benefits over .strings
- Visual editor with translation status indicators
- Automatic extraction of new strings on build
- Built-in plural support (no separate .stringsdict)
- Export/import for professional translation (XLIFF)
- Compile-time validation of string references

## Text Localization in SwiftUI

### Automatic Localization
```swift
// Text automatically localizes string literals
Text("Hello")  // Looks up "Hello" in String Catalog

// Explicit non-localized text
Text(verbatim: "Version 1.2.3")  // Never localized (version numbers, codes)

// Variable text is NOT automatically localized
let name = "John"
Text(name)           // NOT localized (String variable)
Text("Hello \(name)") // IS localized (string literal with interpolation)
```

### LocalizedStringKey
```swift
// Button, Label, Toggle etc. accept LocalizedStringKey
Button("Save") { save() }          // "Save" is looked up in catalog
Toggle("Enable notifications", isOn: $enabled)  // Localized

// Programmatic LocalizedStringKey
let key: LocalizedStringKey = "dynamic_key"
Text(key)
```

## Pluralization

### String Catalog Plural Rules
In the String Catalog editor, mark a string as "Varies by Plural" and provide variants:

| Category | English Example | Arabic Example |
|----------|----------------|----------------|
| `zero` | "No items" | (specific form) |
| `one` | "1 item" | (specific form) |
| `two` | — | (specific form) |
| `few` | — | (3-10) |
| `many` | — | (11-99) |
| `other` | "%lld items" | (100+) |

```swift
// In code — just use interpolation
Text("item_count \(items.count)")

// String Catalog handles the plural form automatically based on locale
// English: "1 item" / "5 items"
// Arabic: different forms for 0, 1, 2, 3-10, 11-99, 100+
```

### Legacy .stringsdict
```xml
<key>item_count</key>
<dict>
    <key>NSStringLocalizedFormatKey</key>
    <string>%#@count@</string>
    <key>count</key>
    <dict>
        <key>NSStringFormatSpecTypeKey</key>
        <string>NSStringPluralRuleType</string>
        <key>NSStringFormatValueTypeKey</key>
        <string>lld</string>
        <key>one</key>
        <string>%lld item</string>
        <key>other</key>
        <string>%lld items</string>
    </dict>
</dict>
```

## Number and Date Formatting

```swift
// Numbers — always locale-aware
Text(price, format: .currency(code: "USD"))     // "$1,234.56" or "1.234,56 $"
Text(count, format: .number)                      // "1,234" or "1.234"
Text(ratio, format: .percent)                     // "85%" or "85 %"

// Dates — always locale-aware
Text(date, format: .dateTime.day().month().year())  // "Jan 15, 2025" or "15 janv. 2025"
Text(date, format: .relative(presentation: .named)) // "yesterday" or "hier"

// Measurements
let distance = Measurement(value: 5, unit: UnitLength.kilometers)
Text(distance, format: .measurement(width: .abbreviated))  // "5 km" or "3.1 mi"
```

**Never use `String(format:)` for user-facing numbers/dates** — it ignores locale.

## RTL Layout Support

```swift
// SwiftUI handles RTL automatically when using:
// - .leading/.trailing instead of .left/.right
// - HStack (reverses in RTL)
// - padding(.leading) (becomes right in RTL)

// Explicit direction control (rare)
@Environment(\.layoutDirection) var layoutDirection

// Flip images for RTL
Image("arrow")
    .flipsForRightToLeftLayoutDirection(true)

// Force LTR for specific content (e.g., code, phone numbers)
Text("+1 (555) 123-4567")
    .environment(\.layoutDirection, .leftToRight)
```

## Asset Catalog Localization

- **Images:** Select image → Localize → provide per-locale variants (e.g., screenshots with localized UI)
- **Colors:** Named colors can have per-locale variants (rare but useful for culturally significant colors)
- **App Icon:** Same across locales (use Icon Composer for Liquid Glass)

## Common Mistakes

1. Hardcoded user-facing strings (`"Save"` instead of `String(localized:)`) — untranslatable
2. String concatenation for sentences (`"Hello " + name + "!"`) — word order varies by language. Use interpolation: `"greeting \(name)"`
3. `String(format:)` for numbers/dates — ignores user locale. Use `Text(value, format:)`
4. Assuming text length — German text is ~30% longer than English. Don't set fixed widths on labels
5. Using `.left`/`.right` instead of `.leading`/`.trailing` — breaks RTL layouts
6. `Text(variable)` expecting localization — only string literals are auto-localized. Use `Text(LocalizedStringKey(variable))` or `String(localized:)`

## Checklist

- [ ] No hardcoded user-facing strings — all use `String(localized:)` or `Text("literal")`
- [ ] Plurals handled via String Catalog plural variants (not conditional logic)
- [ ] Numbers and dates use `Text(value, format:)` not `String(format:)`
- [ ] All `.left`/`.right` replaced with `.leading`/`.trailing`
- [ ] Text containers allow for ~30% text expansion (no fixed widths on labels)
- [ ] RTL layout tested (change language in scheme settings)
- [ ] Non-localizable text uses `Text(verbatim:)` (version numbers, codes, identifiers)
- [ ] String Catalog has translator comments for ambiguous strings

## Cross-References

- `swiftui-typography-api` — Dynamic Type and text layout for localized text
- `swiftui-input-api` — localized form labels and placeholder text
- `swift-app-lifecycle` — app entry point where locale is determined
- `code-analyzer` — checks for hardcoded strings in review

## Templates

Reusable Swift files in `templates/` — copy and adapt:

- **`LocalizationManager.swift`** — `@MainActor @Observable` manager with runtime language switching, `EnvironmentKey` injection
- **`LocalizedStrings.swift`** — Type-safe `L10n` enum for compile-time checked localization keys
- **`LocalizedPreview.swift`** — SwiftUI preview helper for testing multiple locales
