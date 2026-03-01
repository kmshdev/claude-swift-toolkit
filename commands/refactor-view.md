---
description: Analyze and refactor a SwiftUI view for clarity and performance
argument-hint: <source-file>
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Refactor View: $ARGUMENTS

## Steps

### 1. Analyze Complexity
- Read the target view file completely
- Measure: line count, nesting depth, number of `@State`/`@Binding` properties
- Count subviews and computed properties in `body`
- Flag views over 100 lines or with nesting > 4 levels deep

### 2. Load Skills
- Load `swiftui-view-refactor` skill for view ordering rules and MV patterns
- Load `swiftui-ui-patterns` review checklist for performance and composition checks
- Check the project's CLAUDE.md for any project-specific view conventions

### 3. Apply Review Checklist
Run through these checks (from `swiftui-ui-patterns`):
- [ ] `@State` and `@StateObject` properties are `private`
- [ ] Using `@Observable` instead of `ObservableObject` for new view models
- [ ] No passed values declared as `@State`
- [ ] Using modifiers instead of conditionals for state changes
- [ ] `body` is simple and pure (no side effects or complex logic)
- [ ] Action handlers reference methods, not inline logic
- [ ] Using `.task` instead of `.onAppear { Task { } }`
- [ ] No `AnyView` usage
- [ ] ForEach uses stable identity (not `.indices` for dynamic content)

### 4. Refactor
Apply changes in this order (from `swiftui-view-refactor` skill):
1. **Reorder properties:** `@Environment` → `@State` → `let`/`var` → computed → `body` → subviews → methods
2. **Extract subviews:** Any distinct visual section > 30 lines becomes a separate `@ViewBuilder` or extracted view
3. **Simplify state:** Remove unnecessary `@State` wrappers, convert `@StateObject` → `@State` with `@Observable`
4. **Fix modifier order:** Layout modifiers before style modifiers before interaction modifiers
5. **Eliminate redundancy:** Remove dead code, unused properties, duplicate modifiers

### 5. Verify
- Build the project to confirm no compilation errors after refactoring
- Check that view behavior is unchanged (no accidentally removed modifiers or bindings)
- Report what was changed and why
