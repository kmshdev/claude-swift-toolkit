---
date: 2026-04-12
topic: codex-plugin-parity
focus: new possibilities and bringing the codex plugin closer to claude code plugin
---

# Ideation: Codex Plugin Parity and New Capabilities

## Codebase Context

### Repo-grounded context
- The repository still presents a Claude-first full surface in `/Users/kmsh/Developer/claude-swift-toolkit/README.md` and `/Users/kmsh/Developer/claude-swift-toolkit/CLAUDE.md`, while Codex currently ships only the four lifecycle plugins through `/Users/kmsh/Developer/claude-swift-toolkit/.agents/plugins/marketplace.json` and the plugin-local `.codex-plugin/plugin.json` manifests.
- `hookify` remains outside the live Codex surface today even though it is the clearest host-parity gap: Claude has commands, agents, and hooks for policy-style workflows, while Codex currently exposes none of that through the repo.
- The repo does not currently have a project-scoped `/Users/kmsh/Developer/claude-swift-toolkit/.codex/` runtime layer, so it is not using repo-local Codex hooks or custom agents yet.
- Official Codex-facing metadata coverage is still uneven. Several packaged skills in `plugins/apple-design-system/skills`, plus `swift-networking`, `swift-localization`, `swift-concurrency`, and `audit-context-building`, still lack `agents/openai.yaml`.
- The current Codex contract still spans multiple files: `/Users/kmsh/Developer/claude-swift-toolkit/AGENTS.md`, `/Users/kmsh/Developer/claude-swift-toolkit/README.md`, `/Users/kmsh/Developer/claude-swift-toolkit/.agents/plugins/marketplace.json`, plugin manifests, and the validator.
- There is no `docs/solutions/` knowledge base yet, so there is no institutional learnings layer to compound parity decisions.

### Official Codex capabilities that change the parity ceiling
- Codex skills use `description` and optional `agents/openai.yaml` metadata for invocation, UI metadata, and tool dependencies. That means Codex can approximate command-style entrypoints through curated skills, but only if the metadata is deliberate. ([OpenAI Skills docs](https://developers.openai.com/codex/skills))
- Codex itself does have native slash-command surfaces in the app and CLI, and enabled skills appear in the slash-command list. The real gap is not "Codex has no commands"; it is that Codex does not use Claude plugin command manifests as the distribution primitive. ([OpenAI Codex app commands docs](https://developers.openai.com/codex/app/commands), [OpenAI Codex CLI slash commands docs](https://developers.openai.com/codex/cli/slash-commands))
- Codex plugins are the installable distribution unit for skills and app integrations. The plugin docs emphasize packaging skills, apps, and MCP config, not Claude-style slash-command manifests. This means parity has to be outcome-level rather than syntax-level. ([OpenAI Build Plugins docs](https://developers.openai.com/codex/plugins/build))
- Codex now supports hooks officially, but through repo/user `hooks.json` config, not through the existing Claude hook model. Hooks are experimental, gated behind `codex_hooks = true`, currently disabled on Windows, and current interception is partial and Bash-heavy. ([OpenAI Hooks docs](https://developers.openai.com/codex/hooks))
- Codex also supports project-scoped custom agents under `.codex/agents/`, but they are repo/runtime config rather than plugin-packaged distribution primitives. That opens a parity path for high-value agent behaviors, but not as a straight copy of Claude plugin agents. ([OpenAI Subagents docs](https://developers.openai.com/codex/subagents))

## Ranked Ideas

### 1. Re-architect the toolkit around a host-neutral lifecycle core with a Codex-native operating layer
**Description:** Combine the strongest parts of the previous runtime-layer, command-parity, and host-adapter ideas into one program. Extract shared lifecycle knowledge into host-neutral core content, then build a repo-scoped `/Users/kmsh/Developer/claude-swift-toolkit/.codex/` operating layer that expresses Codex-native runtime behavior such as hooks, custom agents, and skill-backed workflow entrypoints. Back that layer with a generated parity contract so plugin manifests, marketplace entries, docs, validation, and runtime config all describe the same supported surface.
**Rationale:** This is the first idea that is structurally strong enough. The repo does not just need more Codex packaging. It needs a clean separation between shared lifecycle knowledge and host-specific delivery, plus a Codex-native runtime layer that takes advantage of modern Codex features without copying Claude plugin semantics. This single direction fixes the content architecture, the user-facing workflow mapping, and the truth-maintenance problem together.
**Downsides:** This is a program, not a cleanup. It touches content layout, plugin packaging, runtime config, validation, and documentation. If phased badly, it can produce a long period of churn or an overbuilt contract layer.
**Confidence:** 96%
**Complexity:** High
**Status:** Unexplored

### 2. Rebuild `hookify` as a host-neutral policy engine with Claude and Codex targets
**Description:** Split `hookify` into a shared rule model plus host adapters. Keep the current Claude runtime as one target, and add a Codex target that emits or drives repo-local `.codex/hooks.json` plus the supporting hook scripts Codex expects.
**Rationale:** This is the biggest new possibility unlocked by the official Codex hooks release. It addresses the sharpest feature gap between the Claude plugin and the Codex plugin while reusing a surface the repo already owns and understands.
**Downsides:** Codex hook coverage is still materially weaker than Claude's current model. Full behavioral parity is not realistic yet because Codex hook interception is experimental, Windows is disabled, and current tool interception is partial.
**Confidence:** 94%
**Complexity:** High
**Status:** Unexplored

### 3. Add a formal parity matrix and CI gate for host claims
**Description:** Track every meaningful surface by capability and host: skills, MCP, hooks, custom agents, commands, and docs claims. Enforce that matrix in CI so the repo can distinguish `shared`, `Claude-only`, `Codex-only`, and `experimental Codex` instead of leaving the status implicit.
**Rationale:** The repo is already close enough to dual-host that misleading phrasing is now a product defect. A parity matrix would stop accidental overclaiming and make it easier to stage future Codex parity work without breaking trust.
**Downsides:** This creates guardrails rather than new user value on its own. It is strongest when paired with one of the capability-building ideas above.
**Confidence:** 91%
**Complexity:** Medium
**Status:** Unexplored

### 4. Ship a Codex readiness and policy pack for hooks and Xcode workflows
**Description:** Add a small readiness layer that checks Codex hook prerequisites, feature-flag state, OS limitations, Xcode MCP bridge availability, and supported repo surfaces before users hit a broken workflow. Bundle that with a small set of starter guardrail policies for build, review, and testing flows.
**Rationale:** New capability without operability is noise. If the repo adopts hooks or repo-scoped agents, users need a deterministic way to understand what is supported in their environment before trusting the toolkit.
**Downsides:** This can bloat into a setup framework if the scope is not held tightly. It should remain diagnostic and enablement-focused.
**Confidence:** 84%
**Complexity:** Medium
**Status:** Unexplored

## Rejection Summary

| # | Idea | Reason Rejected |
|---|------|-----------------|
| 1 | Publish `hookify` as a fifth Codex plugin immediately | Too early; the current implementation is still Claude-specific and the official Codex hook model is materially different. |
| 2 | Mirror every Claude slash command one-for-one in Codex docs | Too literal; official Codex has native slash commands already, so the repo should map workflows onto Codex primitives instead of imitating Claude manifests. |
| 3 | Port every Claude agent directly into `.codex/agents/` right now | Too broad before the repo defines shared core content and a host-claim matrix. |
| 4 | Keep the old runtime-layer, command-parity, and host-adapter ideas as separate top-level bets | Weaker than the merged program; they overlap heavily and are stronger as one architectural direction. |
| 5 | Blanket-add `agents/openai.yaml` to every skill | Too mechanical; metadata should reflect intended invocation behavior, not cargo-cult completeness. |
| 6 | Create a second standalone Codex README | Adds another drift surface without solving contract truth. |
| 7 | Build a custom hook daemon or installer | Not justified by the current problem; Codex already has an official repo-scoped hook mechanism. |
| 8 | Focus next on marketplace polish and branding | Lower leverage than closing the capability and truth gap first. |
| 9 | Keep Codex lifecycle-only and ignore hooks/subagents | No longer defensible now that official Codex capabilities have expanded. |

## Session Log
- 2026-04-12: Fresh ideation focused on Codex-vs-Claude parity after the Codex hooks release; generated 18 candidates, kept 7 survivors.
- 2026-04-12: Raised the bar after reviewing the official Codex app and CLI command docs; corrected the baseline that Codex lacks commands, merged the `.codex/` runtime-layer idea into a stronger parity-contract proposal, and cut the weaker standalone variant.
- 2026-04-12: Combined the strongest overlapping directions into one lead program: host-neutral lifecycle core plus Codex-native operating layer plus generated parity contract.
