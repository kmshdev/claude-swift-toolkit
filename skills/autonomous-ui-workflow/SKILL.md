---
name: autonomous-ui-workflow
description: Use when building or modifying SwiftUI views autonomously - orchestrates the full UI development loop from spec through research, design, implementation, build verification, and visual validation using Xcode MCP and documentation skills
---

# Autonomous UI Development Workflow

## The Loop

```
Spec → Research → Design → Implement → Build → Preview → Validate → Iterate
```

## Phase 1: Spec

Gather requirements from user input (description, screenshot, Figma URL, or existing view reference). Identify:
- What the component does
- Where it fits in the view hierarchy
- Required interactions (tap, drag, keyboard)
- Data dependencies (AppState properties, bindings)

## Phase 2: Research

Load documentation skills based on what the UI needs:

| Need | Skill to Load |
|------|---------------|
| Glass effects, floating controls | `swiftui-liquid-glass-api` |
| Icons, SF Symbols | `swiftui-iconography-api` |
| Background materials, shapes | `swiftui-material-api` |
| Text fields, pickers, forms | `swiftui-input-api` |
| Font choices, text styling | `swiftui-typography-api` |
| Colors, gradients, tint | `swiftui-colors-api` |
| Blur, shadow, opacity | `swiftui-effects-api` |
| Sheets, popovers, alerts | `swiftui-presentation-api` |

Also load project skills: `swiftui-components`, `macos-app-design`, `apple-liquid-glass-design`

## Phase 3: Design

Before writing code:
1. Read existing similar views in `Kulpt/Views/` for patterns
2. Decide view hierarchy and component breakdown
3. Plan state: `@State` for local, `@Environment(AppState.self)` for shared
4. Plan Liquid Glass: ONLY on floating controls, toolbars, status pills (see CLAUDE.md rules)
5. Document the design before implementing

## Phase 4: Implement

Follow Kulpt conventions:
- `@Environment(AppState.self)` + `@Bindable var appState = appState`
- `#Preview` block at bottom
- Extract views > 100 lines
- `.scrollEdgeEffectStyle(.soft, for: .top)` on form ScrollViews
- NO glass on form elements (HIG violation)

## Phase 5: Build

```bash
xcodebuild -project Kulpt.xcodeproj -scheme Kulpt -destination 'platform=macOS' build
```

Or via Xcode MCP: `BuildProject`

If build fails → read errors → fix → rebuild. Do NOT claim success without build evidence.

## Phase 6: Preview

Use Xcode MCP `RenderPreview` to capture the view. Read the PNG to verify:
- Content is visible (not blank — watch for lagoonReveal)
- Layout matches intent
- Colors and typography are correct

## Phase 7: Validate

Check against CLAUDE.md rules:
- [ ] No wholesale glass styles on forms
- [ ] No lagoonReveal on always-visible content
- [ ] Form buttons use `.buttonStyle(.plain)`
- [ ] Delete buttons: red icon only
- [ ] GeometryReader guarded with `> 0` AND `.isFinite`

## Phase 8: Iterate

If validation fails → fix → rebuild → re-preview. One view at a time.
