---
description: Design a SwiftUI component from a description — researches docs, plans architecture, outputs spec
argument-hint: <component description>
allowed-tools: Read, Glob, Grep
---

# Design UI Component: $ARGUMENTS

## Workflow

1. **Parse the request** — identify what UI component is needed
2. **Research existing patterns** — read similar views in `Kulpt/Views/` for consistency
3. **Load documentation** — use relevant swiftui-*-api skills for API reference
4. **Design the component:**
   - View hierarchy breakdown
   - State management plan (@State vs @Environment)
   - Liquid Glass decisions (where to apply, where NOT to)
   - SwiftUI APIs to use (with code snippets from documentation skills)
5. **Output a structured spec** with:
   - Files to create/modify
   - View hierarchy diagram
   - State flow
   - Key modifiers and patterns
   - Glass effect placement (following CLAUDE.md rules)

## Rules

- Reference existing Kulpt views for pattern consistency
- Follow CLAUDE.md critical rules for glass usage
- No glass on form elements
- Plan `#Preview` blocks
- Consider accessibility
