# v1.6 Skill Enrichment — Merge swiftui-expert-skill + swiftui-ui-patterns & Concurrency Update

## Context

Two external skills from [Dimillian/Skills](https://github.com/Dimillian/Skills) contain substantial content that fills gaps in the claude-swift-toolkit:

- **`swiftui-ui-patterns`** — 25 reference files covering app architecture, navigation routing, sheet routing, theming, haptics, deep links, macOS menu bar, loading states, and more. Sourced from IceCubesApp (production Mastodon client).
- **`swift-concurrency-expert`** — 3 reference files covering Swift 6.2 "approachable concurrency", `@concurrent`, main-actor-by-default, isolated conformances, and SwiftUI off-main-thread APIs.

### Analysis Results

- **swiftui-ui-patterns**: 11 topics with zero plugin coverage, 12 with partial overlap, 2 fully covered (skip)
- **swift-concurrency-expert**: 5 critical gaps in our concurrency coverage (Swift 6.2 semantics)
- **swiftui-view-refactor**: Already in plugin since v1.4

### Decision

Full cherry-pick of all content. Merge `swiftui-expert-skill` + `swiftui-ui-patterns` into a single `swiftui-ui-patterns` skill. Cherry-pick concurrency into existing `swift-concurrency`. Cherry-pick macOS content into `macos-development`.

---

## Work Streams

### Stream 1: Create `swiftui-ui-patterns` (Replace `swiftui-expert-skill`)

**New skill:** `skills/swiftui-ui-patterns/`
**Replaces:** `skills/swiftui-expert-skill/`
**Lifecycle position:** Phase 3 (Implement) + Phase 5 (Review checklist)

#### SKILL.md Design

Follow `writing-skills` guidelines:
- Frontmatter: name + description (< 1024 chars)
- Description starts with "Use when..."
- Graphviz decision flowchart for "which reference to load?"
- Quick reference table mapping UI need → reference file
- Review checklist section (preserved from swiftui-expert-skill)
- Cross-references to related skills

#### Reference Files — Merged (7 files)

Each merges content from both source skills, de-duplicated:

| New File | Expert Source | Dimillian Source | Merge Notes |
|----------|-------------|------------------|-------------|
| `references/sheets-and-routing.md` | `sheet-navigation-patterns.md` (leaf API: `.sheet(item:)`, dismiss) | `sheets.md` (SheetDestination enum, `withSheetDestinations`, group-id) | Expert's API → "Leaf Patterns" section; Dimillian's → "App-Level Routing" section |
| `references/navigation.md` | `sheet-navigation-patterns.md` (nav section: `navigationDestination`, `NavigationPath`) | `navigationstack.md` (RouterPath `@Observable`, TabRouter, `withAppRouter()`) | Expert's type-safe destinations → "Foundation"; Dimillian's router → "Scalable Architecture" |
| `references/lists.md` | `list-patterns.md` (ForEach identity, pull-to-refresh, AnyView avoidance) | `list.md` (scroll-to-top, tab re-tap, dense feeds, settings-style) | Expert's correctness → "Rules"; Dimillian's UX → "Patterns" |
| `references/scroll-patterns.md` | `scroll-patterns.md` (ScrollViewReader, paging, position tracking, parallax) | `scrollview.md` (chat anchor, horizontal chips, safeAreaInset) | Expert's technical depth + Dimillian's UX patterns |
| `references/animation-transitions.md` | `animation-transitions.md` (matchedGeometryEffect, withAnimation) | `matched-transitions.md` (iOS 26+ matchedTransitionSource + navigationTransition(.zoom)) | Expert's base + new iOS 26 hero transition section |
| `references/image-and-media.md` | `image-optimization.md` (AsyncImage, downsampling, loading) | `media.md` (QuickLook viewer, openWindow vs sheet) | Expert's performance → "Image Loading"; Dimillian's → "Media Viewer Architecture" |
| `references/forms-and-input.md` | (form guidance in checklist) | `form.md` (themed modal, scrollContentBackground, auto-focus) | Combined form patterns |

#### Reference Files — New (14 files)

Copied from Dimillian, adapted for plugin conventions:

| File | Content | Notes |
|------|---------|-------|
| `references/app-wiring.md` | Root shell: AppTab + TabRouter + dependency graph + SwiftData wiring | Largest unique piece |
| `references/tabview.md` | AppTab enum, TabSection, .tabPlacement, compose-tab interception | iOS 26+ `.tabPlacement(.pinned)` |
| `references/overlay-toast.md` | ToastCenter, auto-dismiss, transition composition | Rename from `overlay.md` for clarity |
| `references/input-toolbar.md` | Bottom-anchored composer, .safeAreaInset, .scrollDismissesKeyboard | Chat/messaging pattern |
| `references/top-bar.md` | iOS 26+ safeAreaBar(edge: .top), Material fallback | Version-gated with `if #available` |
| `references/theming.md` | @Observable Theme class, semantic colors, environment injection | Full implementation pattern |
| `references/haptics.md` | HapticManager, enum-driven types, user preference gating | Self-contained pattern |
| `references/deeplinks.md` | RouterPath.handle(url:), OpenURLAction, .onOpenURL | Couples with navigation.md |
| `references/title-menus.md` | ToolbarTitleMenu, principal title/subtitle VStack | Small but unique |
| `references/searchable.md` | .searchable + .searchScopes, debounced async search, .task(id:) | Fills gap in swiftui-input-api |
| `references/loading-placeholders.md` | .redacted(reason: .placeholder), ContentUnavailableView, 3-state pattern | Production staple |
| `references/lightweight-clients.md` | Closure-based client struct, @Observable store + DI | Networking architecture |
| `references/split-views.md` | Manual HStack split, isSecondaryColumn env flag, NavigationSplitView trade-offs | macOS/iPad pattern |
| `references/grids.md` | LazyVGrid adaptive/fixed, media gallery, GeometryReader square cells | Layout patterns |

#### Reference Files — Kept from Expert (1 file)

| File | Content |
|------|---------|
| `references/modern-apis.md` | API deprecation table, modern replacements |

#### Files NOT Copied (3)

- `controls.md` → fully covered by `swiftui-input-api`
- `focus.md` → fully covered by `swiftui-input-api`
- `components-index.md` → replaced by Quick Reference table in SKILL.md

#### Total: 22 reference files

#### Rename References Across Plugin

All occurrences of `swiftui-expert-skill` renamed to `swiftui-ui-patterns`:
- `CLAUDE.md` (Phase 3, Phase 5, taxonomy)
- `README.md` (lifecycle table, skill table)
- `agents/ui-developer.md`
- `agents/macos-architect.md`
- `agents/swift-reviewer.md`
- `commands/feature-dev.md`
- `commands/implement-component.md`
- `skills/app-development-workflow/SKILL.md`
- `skills/autonomous-ui-workflow/SKILL.md`
- `skills/swift-concurrency/SKILL.md` (cross-ref)
- `skills/swiftui-input-api/SKILL.md` (cross-ref)
- `skills/swiftui-26-api/SKILL.md` (cross-ref)
- Ciphyr hookify rule

---

### Stream 2: Enhance `swift-concurrency` (Cherry-Pick)

**Target:** `skills/swift-concurrency/`

#### SKILL.md Changes

Add new section "## Swift 6.2 Approachable Concurrency" between "Migration from GCD" and existing review content:
- Main-actor-by-default module mode (opt-in, recommended for app targets)
- Async functions stay on caller's actor by default
- `@concurrent` attribute as modern replacement for `Task.detached` for pure background work
- Extend "Common Warnings and Fixes" table with isolated conformance fix
- Add project triage step to review checklist: check build settings before diagnosing

#### New Reference Files

| File | Source | Content |
|------|--------|---------|
| `references/swift-6-2-changes.md` | `swift-6-2-concurrency.md` + `approachable-concurrency.md` (merged) | PhotoProcessor progression, isolated conformances, main-actor-by-default, `@concurrent`, keyword cheat sheet |
| `references/swiftui-concurrency.md` | `swiftui-concurrency-tour-wwdc.md` | SwiftUI off-main-thread APIs (Shape, Layout, visualEffect, onGeometryChange), Sendable closure requirements, value-copy capture patterns |

---

### Stream 3: Enhance `macos-development` (Cherry-Pick)

**Target:** `skills/macos-development/SKILL.md`

Add references or sections for:
- `menu-bar.md` → CommandMenu, CommandGroup, FocusedValue for macOS menu bar
- `macos-settings.md` → Settings scene, tabbed SettingsView, @AppStorage, OpenSettingsAction

These are macOS-specific patterns that belong in the macOS architecture skill, not in the UI patterns skill.

---

### Stream 4: Cross-Reference Wiring

After all content is in place, add cross-references:

| From Skill | To Skill | Reference |
|-----------|----------|-----------|
| `swift-app-lifecycle` | `swiftui-ui-patterns` | App wiring, deep links |
| `swift-networking` | `swiftui-ui-patterns` | Lightweight clients pattern |
| `swiftui-input-api` | `swiftui-ui-patterns` | Searchable async, forms |
| `apple-liquid-glass-design` | `swiftui-ui-patterns` | Top bar safeAreaBar, overlay patterns |
| `swiftui-ui-patterns` | `swift-concurrency` | SwiftUI concurrency patterns |
| `swiftui-ui-patterns` | `swift-app-lifecycle` | Scene structure, deep links |

---

### Stream 5: Delete Old Skill

Delete `skills/swiftui-expert-skill/` entirely after all content is merged and references renamed.

---

## Execution Order

1. **Stream 2** — Concurrency cherry-pick (independent, can be committed separately)
2. **Stream 1** — Create `swiftui-ui-patterns` skill (main work)
3. **Stream 5** — Delete `swiftui-expert-skill`
4. **Stream 3** — macOS development cherry-pick
5. **Stream 4** — Cross-reference wiring
6. **Verification** — grep for stale `swiftui-expert-skill` references, validate all reading paths resolve

## Verification Checklist

- [ ] `grep -r "swiftui-expert-skill" .` returns zero hits (fully renamed)
- [ ] `swiftui-ui-patterns/SKILL.md` has graphviz flowchart and quick reference table
- [ ] Review checklist from old skill preserved in new skill
- [ ] `swift-concurrency/SKILL.md` has Swift 6.2 section with `@concurrent`
- [ ] `swift-concurrency/references/swift-6-2-changes.md` exists
- [ ] `swift-concurrency/references/swiftui-concurrency.md` exists
- [ ] `macos-development/SKILL.md` references menu-bar and settings patterns
- [ ] All cross-references wired
- [ ] Ciphyr hookify rule updated
- [ ] Plugin count: 26 skills (one replaced, not added)
- [ ] Commit and push

## Risk Assessment

- **Breaking change**: Renaming `swiftui-expert-skill` → `swiftui-ui-patterns` breaks any external project that references the old name. Mitigated by the rename being within our plugin only.
- **Skill size**: 22 reference files is large. The SKILL.md must have a clear routing table so agents don't need to read all files. The components-index pattern from Dimillian helps here.
- **Quality**: Dimillian's content uses IceCubesApp-specific types. These need to be generalized or commented as "adapt to your project."
