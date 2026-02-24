---
description: Review a SwiftUI view for HIG compliance, pattern consistency, and Liquid Glass correctness
argument-hint: [file path or view name]
allowed-tools: Read, Glob, Grep
---

# Review UI: $ARGUMENTS

## Checklist

### HIG Compliance
- [ ] No glass effects on form elements
- [ ] Form buttons use `.buttonStyle(.plain)`
- [ ] Delete buttons: red icon only, no background
- [ ] Glass only on floating controls, toolbars, status pills

### Liquid Glass Correctness
- [ ] `GlassEffectContainer` used when multiple glass effects present
- [ ] Container spacing matches layout spacing
- [ ] No lagoonReveal on always-visible content
- [ ] Interactive glass only on tappable elements

### Pattern Consistency
- [ ] Uses `@Environment(AppState.self)` + `@Bindable var appState = appState`
- [ ] `#Preview` block present
- [ ] View extracted if > 100 lines
- [ ] `.scrollEdgeEffectStyle(.soft, for: .top)` on form ScrollViews

### Swift 6 Concurrency
- [ ] No `process.waitUntilExit()` (use terminationHandler)
- [ ] `static let` for VersionedSchema identifiers
- [ ] `@MainActor` on NSViewRepresentable Coordinators

### Accessibility
- [ ] Meaningful labels on interactive elements
- [ ] Dynamic Type support (no fixed font sizes without justification)
- [ ] Color not sole indicator of state

### Performance
- [ ] GeometryReader guarded with `> 0` AND `.isFinite`
- [ ] Limited glass effect count onscreen
- [ ] No unnecessary view recomputation

## Output

Report findings as: PASS / WARN / FAIL with file:line references.
