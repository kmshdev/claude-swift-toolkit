---
name: autonomous-ui-workflow
description: Use when building or modifying SwiftUI views autonomously - orchestrates the full UI development loop from spec through research, design, implementation, build verification, and visual validation using Xcode MCP and documentation skills
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "jq -r '.tool_input.file_path // empty' | xargs -I{} sh -c 'case \"{}\" in *.swift) which swiftlint >/dev/null 2>&1 && swiftlint lint --fix --path \"{}\" --quiet 2>/dev/null || true ;; esac'"
          async: true
          timeout: 30
  Stop:
    - hooks:
        - type: prompt
          prompt: "Check if the SwiftUI view implementation is complete. Verify: 1) A build was attempted 2) The user's requirements were addressed 3) No obvious errors remain. Context: $ARGUMENTS. Respond {\"ok\": true} if complete, or {\"ok\": false, \"reason\": \"what remains\"} if not."
          timeout: 30
---

## Project Context

- Xcode schemes: !`xcodebuild -list -json 2>/dev/null | jq -r '.project.schemes[]' 2>/dev/null || echo "no schemes found"`
- Recent build errors: !`xcodebuild -list 2>&1 | grep -i error | head -5 || echo "none"`

# Autonomous UI Development Workflow

## Lifecycle Position

Phases 2-4 (Design → Implement → Build). The inner UI development loop. After build is green, proceed to Phase 5 — load `swiftui-view-refactor` and `code-analyzer` for review.

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
| Glass effects, floating controls | `apple-liquid-glass-design` |
| Icons, SF Symbols | `swiftui-iconography-api` |
| Background materials, shapes | `swiftui-material-api` |
| Text fields, pickers, forms | `swiftui-input-api` |
| Font choices, text styling | `swiftui-typography-api` |
| Colors, gradients, tint | `swiftui-colors-api` |
| Blur, shadow, opacity | `swiftui-effects-api` |
| Sheets, popovers, alerts | `swiftui-presentation-api` |
| Local data storage, offline cache | `swift-actor-persistence` |

Also load project skills: `swiftui-components`, `macos-app-design`, `apple-liquid-glass-design`

## Phase 3: Design

Before writing code:
1. Read existing similar views in the project's Views directory for patterns
2. Decide view hierarchy and component breakdown
3. Plan state: `@State` for local, shared state via project's pattern; if data must survive app restart, load `swift-actor-persistence`
4. Plan design system usage: check CLAUDE.md for project-specific design rules
5. Document the design before implementing

## Phase 4: Implement

Follow project conventions (check CLAUDE.md and existing code):
- Use the project's state management pattern
- `#Preview` block at bottom
- Extract views > 100 lines
- Follow project-specific coding standards

## Phase 5: Build

```bash
xcodebuild -project *.xcodeproj -scheme <SchemeName> -destination 'platform=macOS' build
```

Or via Xcode MCP: `BuildProject`

If build fails → read errors → fix → rebuild. Do NOT claim success without build evidence.

## Phase 6: Preview

Use Xcode MCP `RenderPreview` to capture the view. Read the PNG to verify:
- Content is visible (not blank — watch for lagoonReveal)
- Layout matches intent
- Colors and typography are correct

## Phase 7: Validate

Check against project rules (see CLAUDE.md for project-specific guidelines):
- [ ] Follows project design system conventions
- [ ] Meets accessibility requirements
- [ ] Consistent with existing views
- [ ] No force unwrapping without justification
- [ ] GeometryReader guarded with `> 0` AND `.isFinite`

## Phase 8: Iterate

If validation fails → fix → rebuild → re-preview. One view at a time.
