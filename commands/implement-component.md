---
description: Implement a SwiftUI component from a spec — creates files, builds, validates
argument-hint: <spec or description>
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Implement Component: $ARGUMENTS

## Workflow

1. **Read the spec** — understand what to build (from /design-ui output or direct description)
2. **Read existing patterns** — check similar views in the project's Views directory for consistency
3. **Implement:**
   - Create/modify Swift files in appropriate Views subdirectory
   - Use the project's state management pattern (check existing files)
   - Include `#Preview` block
   - Follow project coding standards (check CLAUDE.md for conventions)
4. **Build:**
   ```bash
   xcodebuild -project *.xcodeproj -scheme <SchemeName> -destination 'platform=macOS' build
   ```
   (The toolkit auto-detects the .xcodeproj file in the working directory)
5. **Validate:** Check build output for success. If errors, fix and rebuild.
6. **Report:** List created/modified files and build status.

## Rules

- NO glass on form elements (HIG violation)
- NO lagoonReveal on always-visible content
- ONE view at a time for multi-view changes
- Build MUST succeed before claiming completion
- Include `#Preview` in every new view file
