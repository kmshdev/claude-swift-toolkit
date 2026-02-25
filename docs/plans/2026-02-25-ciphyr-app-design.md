# Ciphyr — macOS Secrets Vault App Design

**Date:** 2026-02-25
**Purpose:** Real-world test of the claude-swift-toolkit agent swarm workflow by converting a SwiftUI Playground into a full macOS app.

## Brand

**Name:** Ciphyr
**Tagline:** Your secrets, beautifully guarded.
**Positioning:** For developers who manage API keys and tokens, Ciphyr is a native macOS secrets vault with Liquid Glass design and local-first encryption.

## Architecture

- **App type:** Single-window macOS utility + menu bar presence
- **Target:** macOS 26+ (Liquid Glass native)
- **State:** `@Observable @MainActor` throughout
- **Navigation:** `NavigationSplitView` (sidebar categories → secret list → detail)

### Scene Structure

```swift
@main struct CiphyrApp: App {
    var body: some Scene {
        WindowGroup { ContentView() }
            .defaultSize(width: 900, height: 700)
        Settings { SettingsView() }
        MenuBarExtra("Ciphyr", systemImage: "lock.shield.fill") { MenuBarView() }
    }
}
```

### Models

- `Secret`: id (UUID), name, value (encrypted string), category, notes, createdAt, lastAccessed
- `Category`: enum — apiKeys, tokens, passwords, certificates, other
- `VaultManager`: @Observable — CRUD, search, filtering, encryption/decryption

### Playground Component Mapping

| Playground Component | Ciphyr Feature |
|---------------------|----------------|
| GlassStatusCard | Vault lock status in toolbar |
| GlassToggleSwitch | Auto-lock toggle |
| ThemeSelector | Vault profile switcher (Personal/Work/Shared) |
| DecryptedText | Secret value reveal animation |
| TypewriterText | Secret metadata display |
| AnimationCardsScrollView | Secret cards in horizontal browse mode |
| GlassAnimationCard | Individual secret card with glass background |
| BeveledBorder | Active state indicators on selected items |

## File Structure

```
Ciphyr/
├── CiphyrApp.swift
├── Models/
│   ├── Secret.swift
│   ├── Category.swift
│   └── VaultManager.swift
├── Views/
│   ├── ContentView.swift
│   ├── Toolbar/
│   │   ├── ToolbarView.swift
│   │   ├── GlassStatusCard.swift
│   │   ├── GlassToggleSwitch.swift
│   │   └── ThemeSelector.swift
│   ├── Sidebar/
│   │   └── CategorySidebar.swift
│   ├── SecretList/
│   │   ├── SecretListView.swift
│   │   └── SecretRowView.swift
│   └── Detail/
│       ├── SecretDetailView.swift
│       ├── DecryptedText.swift
│       └── TypewriterText.swift
├── Components/
│   ├── ConcentricRingsIcon.swift
│   ├── GlassAnimationCard.swift
│   └── HighlightedCarouselCard.swift
├── DesignSystem/
│   ├── DesignSystem.swift
│   ├── Theme.swift
│   └── BeveledBorder.swift
├── MenuBar/
│   └── MenuBarView.swift
└── Settings/
    └── SettingsView.swift
```

## Implementation Phases

### Phase 1: Scaffold (create project + design system)
1. Create Xcode project targeting macOS 26
2. Extract DesignSystem, Theme, BeveledBorder from playground
3. Set up @main App struct with 3 scenes
4. Create Secret and Category models
5. Create VaultManager with in-memory store

### Phase 2: Migrate components (playground → app)
6. Move GlassStatusCard, GlassToggleSwitch, ThemeSelector, ConcentricRingsIcon
7. Move TypewriterText, DecryptedText, HighlightedCarouselCard
8. Move GlassAnimationCard, AnimationCardsScrollView
9. Adapt components to use @Bindable and real data sources

### Phase 3: Build app shell
10. ContentView with NavigationSplitView
11. CategorySidebar with filtering
12. SecretListView with glass card rows
13. SecretDetailView with DecryptedText reveal
14. ToolbarView integrating migrated toolbar components

### Phase 4: Wire features
15. Add/edit secret sheets
16. Copy-to-clipboard with auto-clear
17. Search filtering
18. MenuBarView quick access
19. SettingsView (auto-lock, theme)

### Phase 5: Build & review
20. Build and fix compilation
21. Run swift-reviewer + code-reviewer swarm
22. Fix review findings
