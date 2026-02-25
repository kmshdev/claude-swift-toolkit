---
description: Diagnose and fix build errors systematically
allowed-tools: mcp__xcodebuildmcp__*, Read, Write, Edit, Bash(swift *), Bash(xcodebuild *), Grep
---

# Fix Build Errors

## Steps

### 1. Get Fresh Errors
- Run a clean build to get the current error set (not stale cache errors)
- Use `mcp__xcodebuildmcp__build_project` or `xcodebuild build` with the same scheme/destination as `/build`
- Capture full build output

### 2. Categorize Errors
Read each error and classify:

**SPM / Package Resolution:**
- "package resolution failed", "dependency not found", "version solving failed"
- Fix: `swift package resolve`, clean derived data, check `Package.resolved` for conflicts
- Check minimum deployment target matches dependency requirements

**Swift Compiler:**
- Type mismatches, missing members, ambiguous references
- Fix: check API availability (`#available`), add missing imports, fix type signatures
- For deprecation warnings: load `swiftui-expert-skill` for modern API replacements

**Linker:**
- "undefined symbol", "framework not found", "library not found"
- Fix: verify framework is linked in Build Phases → Link Binary With Libraries
- Check framework search paths in Build Settings
- For SPM dependencies: ensure `.product()` is listed in target dependencies

**Code Signing:**
- "no provisioning profile", "code signing identity not found"
- Fix: verify team in Signing & Capabilities, check bundle ID matches profile
- For development: set "Automatically manage signing" in Xcode
- Check entitlements file matches capabilities

**Swift Concurrency (Swift 6):**
- "sending", "non-sendable", "actor-isolated", "data race"
- Fix: add `@MainActor`, conform to `Sendable`, use `@unchecked Sendable` (last resort)
- Load `swiftui-expert-skill` for concurrency patterns

### 3. Fix Errors
- Fix one category at a time, starting with the most upstream (SPM → compiler → linker → signing)
- SPM errors block everything else — resolve these first
- After each fix, rebuild to check if downstream errors resolve

### 4. Verify
- Run a full clean build after all fixes
- If build succeeds → report success
- If new errors appear → return to step 2 with the new error set
- Maximum 3 fix-rebuild cycles before stopping and reporting remaining issues to the user
