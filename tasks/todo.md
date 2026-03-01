# Add swiftui-26-api Skill (Trimmed)

## Context
Import the `swiftui-26-api` skill from `/Users/kmsh/Developer/skills-seeked/output/swiftui-26-api/`, stripping all glass-related content that duplicates `apple-liquid-glass-design`. Focus on the 8 unique API areas: WebView/WebPage, TextEditor rich text, @Animatable macro, FindContext, UIHostingSceneDelegate, dragContainer, Slider ticks, windowResizeAnchor.

## Tasks

### Phase 1: Copy and Trim Reference Files
- [ ] 1.1 Create `skills/swiftui-26-api/` directory and `references/` subdirectory
- [ ] 1.2 Copy and keep as-is: `text-editing.md`, `find-context.md`, `macos-drag-and-windows.md`, `scroll-and-tabs.md`, `toolbar-and-slider.md`
- [ ] 1.3 Copy `animatable-macro.md` — absorb the "manual animatableData → macro" migration from `migration-patterns.md` into it
- [ ] 1.4 Copy `webkit.md` — absorb the "WKWebView → WebView" migration from `migration-patterns.md` into it
- [ ] 1.5 Copy `uikit-scene-bridge.md` — absorb the "UIHostingController → UIHostingSceneDelegate" migration from `migration-patterns.md` into it
- [ ] 1.6 Merge non-glass anti-patterns from `anti-patterns.md` into relevant reference files (crash conditions → webkit.md, logic errors → text-editing.md/find-context.md/animatable-macro.md)
- [ ] 1.7 Do NOT copy: `glass-effects.md`, `migration-patterns.md` (dissolved), `anti-patterns.md` (dissolved)

### Phase 2: Rewrite SKILL.md
- [ ] 2.1 Strip glass Quick Reference section (examples 1-4, glass API table) — replace with redirect to `apple-liquid-glass-design`
- [ ] 2.2 Keep non-glass Quick Reference examples (5-12): @Animatable, TextEditor+selection, FormattingDefinition, WebView, UIHostingSceneDelegate, ToolbarSpacer, Slider ticks, windowResizeAnchor, dragContainer
- [ ] 2.3 Rewrite Reading Paths: Path A = redirect to `apple-liquid-glass-design`, Paths B-F = update file refs (remove glass-effects.md/anti-patterns.md/migration-patterns.md references, point to merged content)
- [ ] 2.4 Strip glass gotchas (items 3, 6), keep rest + renumber
- [ ] 2.5 Strip glass troubleshooting rows, keep non-glass rows
- [ ] 2.6 Update Reference Files table to list 8 files (not 11)
- [ ] 2.7 Update description frontmatter to exclude glass (already has "DO NOT use for Liquid Glass design patterns")

### Phase 3: Plugin Integration
- [ ] 3.1 Update `CLAUDE.md` — add `swiftui-26-api` to Phase 3 Implement skill list, update skill count (25 → 26), add to API Reference category in taxonomy table
- [ ] 3.2 Update `README.md` — add to Phase 3 table row, add to API Reference skill table
- [ ] 3.3 Update `plugin.json` — bump description skill count
- [ ] 3.4 Add cross-references: `apple-liquid-glass-design` → points to `swiftui-26-api` for non-glass iOS 26 APIs; `swiftui-input-api` → points here for rich text; `swift-app-lifecycle` → points here for UIHostingSceneDelegate
- [ ] 3.5 Update Ciphyr hookify rule — add `swiftui-26-api` row for "iOS 26 new APIs" intent

### Phase 4: Verify
- [ ] 4.1 Confirm no glass-effects.md, migration-patterns.md, or anti-patterns.md in final skill directory
- [ ] 4.2 Confirm SKILL.md has no `glassEffect` code examples (only redirect text)
- [ ] 4.3 Confirm all Reading Path file references resolve to actual files
- [ ] 4.4 `grep -r "swiftui-26-api" skills/ agents/ commands/` confirms cross-references exist
- [ ] 4.5 Commit and push
