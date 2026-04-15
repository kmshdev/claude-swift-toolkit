---
date: 2026-04-15
topic: xcode-mcpbridge-integration
focus: Apple's official Xcode MCP bridge (xcrun mcpbridge) — scope and impact on toolkit architecture
---

# Ideation: Apple Official Xcode MCP Bridge Integration

## Codebase Context

**Toolkit state:** 5 plugins, 49 skills, 10 agents across a 6-phase Apple app development lifecycle (Scaffold > Architecture > Design > Implement > Build > Review > Test).

**Current Xcode MCP integration:** Tightly coupled to the community `xcodebuildmcp` server. 40+ tool references hard-coded as `mcp__xcodebuildmcp__*` across 9 skills. Hardened crash-recovery patterns (BuildFix loop max 5 iterations, TestFix loop with `notRun` = crash detection, `pkill -f "xctest"` recovery). Zero awareness of Apple's official `xcrun mcpbridge`.

**Apple's official bridge (Xcode 26.3):** 20 native MCP tools via `xcrun mcpbridge`. Overlaps ~80% of community server tools (XcodeRead, BuildProject, RunAllTests, RenderPreview). Two exclusive tools: `DocumentationSearch` (Squirrel MLX semantic search of all Apple docs + WWDC transcripts) and `ExecuteSnippet` (Swift REPL). Requires Xcode running with project open. Permission dialog per-agent.

**Key tension:** Community server has 67 tools (UI automation, debugging, logging, scaffolding, daemon management). Apple has 20 tools (core ops + 2 exclusives). Neither is a superset of the other.

**Past learnings:** 40-minute MCP lockup from SwiftData test crash shaped all current patterns. `notRun` = crash (NOT "still running"). BuildFix loop max 5 iterations. Review gate between build and test is mandatory.

## Ranked Ideas

### 1. Compatibility Test Suite (`/verify-xcode-server`)
**Description:** Diagnostic skill that probes both MCP servers' actual tool surface with representative inputs. Produces structured report: available tools, missing tools, response schema differences, crash-recovery compatibility. Mandatory test categories: file ops, build/test cycle, preview rendering, crash scenarios (does `pkill -f "xctest"` work through Apple's bridge?).
**Rationale:** Every migration decision depends on empirical data. The "80% overlap" claim needs tool-by-tool verification. Evidence-based migration > speculative migration.
**Downsides:** Requires both servers installed. Maintenance cost as servers evolve.
**Confidence:** 85%
**Complexity:** Medium
**Status:** Unexplored

### 2. Bridge-Exclusive Feature Skills (`apple-docs-search` + `swift-snippet`)
**Description:** Two additive skills wrapping Apple-exclusive tools. `apple-docs-search` — semantic search across Apple docs + WWDC transcripts via on-device MLX. `swift-snippet` — Swift REPL without project context. No existing files modified.
**Rationale:** Zero risk, immediate value. Creates foundation for idea #5. Users get Apple's most compelling exclusive capabilities through the toolkit's skill system.
**Downsides:** Only available with Apple's bridge. Creates two-tier experience. Needs graceful fallback.
**Confidence:** 90%
**Complexity:** Low
**Status:** Unexplored

### 3. Dual `allowed-tools` + Convention-Over-Configuration
**Description:** Mechanical changes across 49 skills: (a) add Apple bridge tool glob alongside community glob in `allowed-tools`, (b) strip server prefixes from all skill body text so instructions say "call BuildProject" not `mcp__xcodebuildmcp__BuildProject`. Reduces coupling from 40+ refs per skill to 1 line per skill.
**Rationale:** Minimum viable coexistence. Smallest diff, immediate dual-server support. Future server changes become a mechanical `allowed-tools` edit.
**Downsides:** Need to verify Apple's bridge tool prefix. Dual-glob may over-permission. Doesn't solve routing.
**Confidence:** 85%
**Complexity:** Low
**Status:** Unexplored

### 4. CLAUDE.md / AGENTS.md as Cross-Vendor Standard
**Description:** Apple recommends AGENTS.md/CLAUDE.md for project context. Evolve `/revise-claude-md` to produce Apple-compatible context (Build System, Testing, Documentation sections) that works with Xcode's built-in Claude Agent, Codex, AND external tools.
**Rationale:** Toolkit is already ahead. Apple endorsing this format makes CLAUDE.md a cross-vendor standard. Low effort, strategic positioning.
**Downsides:** Apple's format may diverge. Minor monitoring needed.
**Confidence:** 80%
**Complexity:** Low
**Status:** Unexplored

### 5. Snippet-Validated Architecture Decisions
**Description:** During Phase 1, when architect agents propose patterns, use `ExecuteSnippet` (via `swift-snippet` skill) to compile minimal proof-of-concept against target SDK. Validates patterns compile before committing to plans.
**Rationale:** The 40-minute SwiftData crash was an architectural pattern that compiled but crashed at runtime. Compile-time validation in Phase 1 front-loads failures with zero cost. Literally impossible workflow before `ExecuteSnippet`.
**Downsides:** ExecuteSnippet may not support all SDK imports. Adds latency. Some patterns only fail at runtime.
**Confidence:** 75%
**Complexity:** Medium (depends on #2)
**Status:** Unexplored

## Rejection Summary

| # | Idea | Reason Rejected |
|---|------|-----------------|
| 1 | Unified Tool Abstraction Layer | Premature abstraction; need data first |
| 2 | Capability Trait System | Over-engineered for solo-dev toolkit |
| 3 | Thin Wrapper Tool Layer (Proxy) | Adds runtime infrastructure for uncertain benefit |
| 4 | MCP Server Adapter Plugin | 6th plugin for indirection before coexistence is proven |
| 5 | Skill Preprocessor / Template Expansion | Build step in static-file system; complexity-to-value too high |
| 6 | Tool Name Rewriting Hook | Fragile; tools may have different response schemas |
| 7 | Kill the Build Phase | Too aggressive; Apple's bridge is RC 2, crash-recovery is battle-tested |
| 8 | Post-Community-Server World | Speculation about Apple's roadmap; not actionable |
| 9 | Multi-IDE Plugin Kit | Out of scope; toolkit is explicitly Apple-only |
| 10 | Agent Permission Handshake | Over-designed; Apple's permission is a simple one-time dialog |
| 11 | Collaborative Agent Topology | Conceptually interesting but not technically actionable |
| 12 | Snippet Playground for Learning | Tangential; toolkit builds apps, not tutorials |
| 13 | Interactive Migration Assistant | Too niche; one-time event, not recurring |
| 14 | Documentation-Driven Test Generation | Apple docs too general for useful parameterized tests |
| 15 | Server-Agnostic Glob (`mcp__*__ToolName`) | Undocumented Claude Code behavior; can't build on unverified |
| 16 | Inline Provider Annotations | Documentation-only value; compatibility test more actionable |
| 17 | Runtime Server Detection (dupl.) | Duplicates auto-detection hook with less grounding |
| 18 | Provider Profile Presets (dupl.) | Duplicates server profile configs with less specificity |
| 19 | Dual-Server Composition (dupl.) | Duplicates dual-bridge architecture |
| 20 | Strip File-Op Substitution Table | 55% confidence; entirely dependent on #1 data |
| 21 | WWDC Session-Grounded Code Review | Marginal over #2; noisy results risk |
| 22 | Sandbox-Aware Crash Recovery | Folded into #1 as mandatory test category |
| 23 | Performance Router | Speculative; uncertain performance difference |
| 24 | Session Handoff Between Servers | Too complex; session models likely incompatible |
| 25 | Preview-Driven Dev Loop | RenderPreview reliability unproven; image analysis is research-level |
| 26 | Capability Alias Map (dupl.) | Duplicates convention-over-config |
| 27 | Allowed-Tools Server-Agnostic (dupl.) | Risky bet on undocumented glob behavior |

## Session Log
- 2026-04-15: Initial ideation — 38 candidates generated across 4 frames (migration, capabilities, abstraction, assumption-breaking), 8 survived first pass, refined to 5 survivors on stricter second pass
