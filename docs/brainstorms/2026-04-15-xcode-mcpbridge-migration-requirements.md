---
title: "Migrate from community xcodebuildmcp to Apple's official Xcode MCP bridge"
date: 2026-04-15
status: draft
origin: Brainstorm session — article synthesis + ideation doc + toolkit audit
---

# Migrate from community xcodebuildmcp to Apple's official Xcode MCP bridge

## Problem Frame

The toolkit is tightly coupled to the community `xcodebuildmcp` MCP server — 40+ hardcoded `mcp__xcodebuildmcp__*` tool references across 9 skills, 4 agents, and documentation. Apple shipped an official Xcode MCP bridge (`xcrun mcpbridge`) in Xcode 26.3 with 20 native tools covering ~80% of daily workflows plus two exclusive capabilities (DocumentationSearch, ExecuteSnippet). The community server (67 tools) remains the only source for debugging, UI automation, logging, and SwiftPM workflows.

**Why migrate now:** Apple's bridge is the official, supported path. Community servers can break on Xcode updates, have no SLA, and add a third-party dependency. Apple's bridge is zero-install (ships with Xcode), zero-config (`claude mcp add --transport stdio xcode -- xcrun mcpbridge`), and includes unique capabilities the community server will never have (on-device MLX documentation search, REPL).

**Why audit first:** The "80% overlap" claim is based on tool name matching, not empirical testing. The community server's crash-recovery patterns (BuildFix loop, TestFix loop, `notRun` detection) were hard-won through production incidents. We need to verify Apple's bridge handles these scenarios identically before migrating.

## Requirements

### R1. Compatibility Audit

Produce a structured `/verify-xcode-server` diagnostic skill that probes Apple's bridge with representative inputs across all tool categories. The audit must cover:

- **File operations:** XcodeRead/Write/Update/Glob/Grep/LS/MakeDir/RM/MV — do they behave identically to the community equivalents?
- **Build cycle:** BuildProject + GetBuildLog — does it return the same error structure as community `build_macos`/`build_sim`? Can the BuildFix loop work with it?
- **Test cycle:** RunAllTests/RunSomeTests/GetTestList — does `notRun` still indicate a crash? Does the TestFix loop work? Can we still `pkill -f "xctest"` to recover from hangs?
- **Preview:** RenderPreview — same image format and response schema?
- **Diagnostics:** XcodeListNavigatorIssues/XcodeRefreshCodeIssuesInFile — same structure?
- **Crash recovery:** Intentionally trigger a SwiftData parallel test crash and verify the recovery path works through Apple's bridge
- **Window management:** XcodeListWindows + tabIdentifier flow — verify it works with the toolkit's session patterns

**Success criteria:** Structured PASS/FAIL report per tool category with response schema diffs documented.

### R2. Gap Assessment

After the audit, produce a gap report identifying:

- **Covered:** Tools available in Apple's bridge that match community equivalents
- **Missing-but-unused:** Community tools with no Apple equivalent that the toolkit doesn't actively use (candidates for removal)
- **Missing-and-used:** Community tools with no Apple equivalent that the toolkit DOES use (migration blockers)
- **Apple-exclusive:** Tools only available in Apple's bridge (DocumentationSearch, ExecuteSnippet)

**Gate decision:** If "missing-and-used" is empty or has acceptable workarounds, proceed to R3. If blockers exist, scope narrows to additive-only (bridge-exclusive skills) plus partial migration of non-blocked tools.

### R3. Skill Migration

Rewrite all 9 skills that reference `mcp__xcodebuildmcp__*` to use Apple's bridge tools directly:

- Strip all `mcp__xcodebuildmcp__` prefixes from skill body text (instructions say "call BuildProject" not `mcp__xcodebuildmcp__BuildProject`)
- Update `allowed-tools` in frontmatter from `mcp__xcodebuildmcp__*` to Apple's bridge tool glob pattern
- Preserve crash-recovery patterns (BuildFix loop, TestFix loop) but adapt to Apple's response schemas if they differ
- Update the `xcodebuildmcp` skill to become the primary Apple bridge reference skill (rename to `xcode-tools` or similar)
- Decide fate of `xcodebuildmcp-cli` skill: keep as fallback for environments without Xcode running, or merge into main skill

**Affected skills (9):**
- `plugins/apple-app-builder/skills/xcodebuildmcp/SKILL.md` — full rewrite
- `plugins/apple-app-builder/skills/xcodebuildmcp-cli/SKILL.md` — evaluate: keep as CLI fallback or remove
- `plugins/apple-app-builder/skills/build-project/SKILL.md` — update allowed-tools + instructions
- `plugins/apple-app-builder/skills/run-app/SKILL.md` — update allowed-tools + instructions
- `plugins/apple-app-builder/skills/fix-build/SKILL.md` — update allowed-tools + instructions
- `plugins/apple-app-builder/skills/implement-component/SKILL.md` — update allowed-tools + instructions
- `plugins/apple-app-builder/skills/autonomous-ui-workflow/SKILL.md` — update build/test references
- `plugins/apple-app-quality/skills/test/SKILL.md` — update allowed-tools + instructions
- `plugins/apple-app-quality/skills/ios-testing/SKILL.md` — update allowed-tools

**Additional skills with indirect references (3):**
- `plugins/apple-app-architect/skills/app-development-workflow/SKILL.md` — update Phase 4 references
- `plugins/apple-app-architect/skills/scaffold-project/SKILL.md` — update allowed-tools
- `plugins/apple-app-architect/skills/swift-project-scaffold/SKILL.md` — update skill reference list

### R4. Bridge-Exclusive Feature Skills

Add skills for Apple-exclusive capabilities unavailable in the community server:

- **`apple-docs-search`** — Wraps `DocumentationSearch` for semantic search of Apple docs + WWDC transcripts. Integrates into Phase 1 (Architecture) and Phase 5 (Review) for documentation-grounded decisions.
- **`swift-snippet`** — Wraps `ExecuteSnippet` for Swift REPL execution. Integrates into Phase 1 for compile-time pattern validation (the ideation doc's "snippet-validated architecture decisions").

### R5. Agent and Documentation Cleanup

- Update agent skill reference lists in `macos-architect.md` and `swift-reviewer.md`
- Remove `xcodebuildmcp` keyword from `plugins/apple-app-builder/.claude-plugin/plugin.json`
- Update `CLAUDE.md` skill taxonomy with new skill names
- Update `README.md` lifecycle table
- Update `app-development-workflow` Phase 4 instructions
- Archive or delete the `xcodebuildmcp-cli` skill if audit confirms CLI fallback is unnecessary

### R6. MCP Server Configuration

- Document the setup: `claude mcp add --transport stdio xcode -- xcrun mcpbridge`
- Add prerequisite check to toolkit: Xcode running + MCP enabled in Xcode Settings > Intelligence
- Consider adding `.mcp.json` to `apple-app-builder` plugin for auto-configuration
- Document the `MCP_XCODE_PID` env var for multi-Xcode scenarios

## Scope Boundaries

- **In scope:** Full replacement of community xcodebuildmcp with Apple's official bridge, gated by audit results
- **In scope:** Adding bridge-exclusive feature skills (DocumentationSearch, ExecuteSnippet)
- **In scope:** Updating all affected skills, agents, documentation
- **Out of scope:** Supporting both servers simultaneously (dual-server mode rejected — full replacement intent)
- **Out of scope:** Recreating community-only capabilities (debugging, UI automation, logging) via alternative means
- **Out of scope:** Multi-IDE support (Cursor, VS Code) — toolkit is Claude Code-first

## Success Criteria

1. Zero `mcp__xcodebuildmcp__*` references remaining in the codebase after migration
2. All build/test/preview workflows pass through Apple's bridge with identical behavior
3. BuildFix and TestFix crash-recovery loops verified working through Apple's bridge
4. `DocumentationSearch` and `ExecuteSnippet` available as toolkit skills
5. Clean `claude mcp list` showing only `xcode` (Apple's bridge), no `xcodebuildmcp`

## Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Apple bridge response schemas differ from community | BuildFix/TestFix loops break | Audit (R1) catches this before migration |
| `notRun` crash detection doesn't work through Apple's bridge | Silent test failures | Mandatory crash-recovery test in audit |
| Apple bridge requires Xcode running (community can work headless) | CI/CD pipelines break | Keep `xcodebuildmcp-cli` as headless fallback or use `xcodebuild` CLI directly |
| Community server had per-platform build variants, Apple has generic `BuildProject` | Can't target specific simulator/device | Audit whether `BuildProject` accepts destination parameters |
| SwiftPM projects need `swift_package_*` tools, Apple has none | SPM-only projects can't build | Fall back to `swift build`/`swift test` CLI (already in `xcodebuildmcp-cli`) |

## Open Questions

### Resolve Before Planning

- **Q1:** What is Apple's bridge tool prefix in Claude Code? Is it `mcp__xcode__*` (from `claude mcp add ... xcode`)? This determines the `allowed-tools` glob pattern.
- **Q2:** Does `BuildProject` accept a destination parameter (simulator name, device ID)? Or does it always build for the scheme's default destination?
- **Q3:** Can `pkill -f "xctest"` recover from test hangs when tests were launched via Apple's bridge? (The bridge uses XPC to Xcode, which may handle process cleanup differently.)

### Defer to Implementation

- Exact response schema mapping between community and Apple tools
- Whether `ExecuteSnippet` supports importing project modules or only stdlib
- How `RenderPreview` handles previews that fail to compile

## Phased Delivery

### Phase A: Audit (R1 + R2)
Build `/verify-xcode-server`, run it, produce gap report. Gate decision.

### Phase B: Migration (R3 + R4)
Rewrite skills, add bridge-exclusive skills. Test all workflows.

### Phase C: Cleanup (R5 + R6)
Update agents, docs, plugin config. Remove all community server references.

## Sources

- Article: "Exploring AI Driven Coding: Using Xcode 26.3 MCP Tools" (2026)
- Ideation: `docs/ideation/2026-04-15-xcode-mcpbridge-integration-ideation.md`
- Toolkit audit: 9 skills, 4 agents, 40+ tool references mapped via codebase exploration
- Apple docs: Xcode > Settings > Intelligence > MCP toggle
- Known issue: Xcode 26.3 RC 1 `structuredContent` bug (fixed in RC 2)
