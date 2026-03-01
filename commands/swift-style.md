---
description: Check and fix Swift style, conventions, and modern API usage
allowed-tools: Bash(swiftlint *), Bash(swift-format *), Bash(which *), Read, Grep, Glob
---

# Swift Style Check

## Steps

### 1. Detect Available Linters
- Check for SwiftLint: `which swiftlint` or look for `.swiftlint.yml` in the project root
- Check for swift-format: `which swift-format` or look for `.swift-format` config
- Check `Package.swift` or `Brewfile` for linter dependencies
- If neither is installed → skip to step 3 (manual checks)

### 2. Run Linters (if available)
**SwiftLint:**
- Run `swiftlint lint --reporter json` for machine-readable output
- Categorize violations by severity: error (must fix) vs warning (should fix)
- Auto-fix safe violations: `swiftlint lint --fix` (handles spacing, trailing whitespace, etc.)

**swift-format:**
- Run `swift-format lint -r .` for recursive check
- Auto-fix: `swift-format format -i -r .` (in-place formatting)

Report remaining violations grouped by rule with file:line references.

### 3. Manual Style Checks (always run)
Load `swiftui-ui-patterns` modern API checklist and check for:

**Modern API Usage:**
- [ ] `foregroundStyle()` instead of `foregroundColor()`
- [ ] `clipShape(.rect(cornerRadius:))` instead of `cornerRadius()`
- [ ] `Tab` API instead of `tabItem()`
- [ ] `Button` instead of `onTapGesture()` (unless need location/count)
- [ ] `NavigationStack` instead of `NavigationView`
- [ ] Two-parameter `onChange(of:)` variant

**Swift Conventions:**
- [ ] `@State` and `@StateObject` are `private`
- [ ] No force-unwraps outside of tests and `fatalError` guards
- [ ] Prefer static member lookup (`.blue` vs `Color.blue`)
- [ ] Imports sorted alphabetically
- [ ] No unused imports

**Naming:**
- [ ] Types are `UpperCamelCase`, properties/methods are `lowerCamelCase`
- [ ] Boolean properties read as assertions (`isEnabled`, `hasContent`, `shouldReload`)
- [ ] Protocol names describe capability (`Identifiable`, `Codable`) not type

### 4. Report
- Group findings by severity: errors → warnings → suggestions
- Show file:line for each finding
- Note which fixes were auto-applied vs which require manual attention
