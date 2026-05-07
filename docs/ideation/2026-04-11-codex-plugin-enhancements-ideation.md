---
date: 2026-04-11
topic: codex-plugin-enhancements
focus: next scope for codex plugin enhancements
---

# Ideation: Codex Plugin Enhancements

## Codebase Context

### Repo-grounded context
- The repository now ships four Codex lifecycle plugins through `.codex-plugin/plugin.json` manifests and a repo marketplace at `.agents/plugins/marketplace.json`.
- `apple-app-builder` and `apple-app-quality` bundle plugin-local `.mcp.json` files that launch the official Xcode MCP bridge via `xcrun mcpbridge`.
- The active Codex contract is split across `README.md`, `AGENTS.md`, `.agents/plugins/marketplace.json`, four plugin manifests, and marketplace-exposed skill trees.
- The repo has a local validator at `scripts/validate-codex-support.py`, but no CI automation in `.github/` yet.
- Metadata coverage is intentionally partial but uneven: some entrypoint skills have `agents/openai.yaml`, while many marketplace-exposed skills do not.
- The largest exposed tree is `plugins/apple-design-system/skills`, which serves both as local authoring/reference material and as a packaged plugin surface.

### Official Codex guidance shaping this refinement
- OpenAI’s skills docs say Codex starts from skill metadata, uses `description` for implicit matching, and requires descriptions with clear scope and boundaries. Optional `agents/openai.yaml` can configure UI metadata, invocation policy, and tool dependencies; `allow_implicit_invocation: false` disables implicit matching for a skill while preserving explicit `$skill` use. ([OpenAI Skills docs](https://developers.openai.com/codex/skills))
- The same docs say to keep each skill focused on one job, prefer instructions over scripts unless deterministic behavior is needed, and test prompts against the skill description to confirm the right trigger behavior. ([OpenAI Skills docs](https://developers.openai.com/codex/skills))
- OpenAI’s plugin docs say plugins are the installable distribution unit, while local skills are best for repo-scoped authoring. They also emphasize repo marketplaces, `./`-prefixed relative paths, and install-surface metadata in plugin manifests. ([OpenAI Build Plugins docs](https://developers.openai.com/codex/plugins/build))

## Ranked Ideas

### 1. Define and enforce an entrypoint-vs-reference skill model
**Description:** Introduce an explicit Codex taxonomy for marketplace-exposed skills: entrypoint skills, follow-on workflow skills, and reference-only skills. Give entrypoints strong `agents/openai.yaml` metadata, set `allow_implicit_invocation: false` on reference-heavy skills that should only be used explicitly, and tighten `description` text so implicit matching has clear boundaries.
**Rationale:** This is the strongest match to the official skills guidance. Right now the repo exposes broad skill trees, but Codex decides implicit use from metadata and descriptions. Without a formal model, broad reference skills can overmatch and weaker descriptions can steal traffic from narrower entrypoints.
**Downsides:** Requires policy work before code changes. Some currently exposed skills may need metadata, description rewrites, or packaging changes.
**Confidence:** 95%
**Complexity:** Medium
**Status:** Unexplored

### 2. Split local authoring trees from distributed plugin surfaces
**Description:** Keep the current broad skill trees for repo-local authoring, but package narrower curated plugin surfaces for Codex distribution. In practice, that likely means adding wrapper skill roots or smaller packaged subtrees so the installable plugin surface maps to intentional user journeys rather than whole authoring libraries.
**Rationale:** The official plugin docs draw a line between local skill authoring and plugin distribution. The current repo blurs that line most strongly in `apple-design-system`, where a broad shared `skills/` tree is both the authoring area and the packaged surface.
**Downsides:** This is structural work. It may require moving files, adding wrapper entrypoints, and revisiting how the design-system plugin is assembled.
**Confidence:** 92%
**Complexity:** High
**Status:** Unexplored

### 3. Turn the validator into a contract checker and put it in CI
**Description:** Extend `scripts/validate-codex-support.py` from syntax/unsafe-reference validation into a repo contract checker, then run it in GitHub Actions on every PR. The validator should understand the entrypoint/reference model, check YAML validity, enforce marketplace/manifests/path rules, and protect against host-language regressions.
**Rationale:** The repo already has a validator, which is the right primitive. The missing piece is turning that local guardrail into an always-on contract and aligning its checks with official plugin and skills expectations.
**Downsides:** Requires deciding which checks are hard failures versus advisory. Overly aggressive rules could slow iteration if the surface model is not defined first.
**Confidence:** 94%
**Complexity:** Medium
**Status:** Unexplored

### 4. Formalize tool dependency metadata and Xcode MCP readiness checks
**Description:** Standardize `dependencies.tools` coverage for every Codex skill that assumes Xcode MCP, and add a small readiness/doctor path that verifies Xcode is installed, running, and reachable through the bundled bridge before users hit build/test workflows.
**Rationale:** The official skills metadata model explicitly supports tool dependencies. The repo already uses that for some builder/quality entrypoints, so the next leverage is consistency plus a lightweight operator check for the most failure-prone runtime dependency.
**Downsides:** Needs discipline to avoid becoming a large setup framework. The readiness path should diagnose, not own full environment management.
**Confidence:** 86%
**Complexity:** Medium
**Status:** Unexplored

### 5. Generate the live Codex surface inventory from manifests
**Description:** Add a small generator that derives a single active-surface inventory from `.agents/plugins/marketplace.json`, plugin manifests, `.mcp.json`, and designated entrypoint metadata. Use that generated output to support `README.md`, `AGENTS.md`, and reviewer tooling so the live Codex contract stops drifting across hand-maintained docs.
**Rationale:** Recent cleanup work has repeatedly targeted drift between the live install surface and the surrounding docs. That is a sign the repo needs one generated source for “what Codex actually sees.”
**Downsides:** Easy to overengineer. The generator should stay declarative and derived from the existing contract files, not become a second configuration layer.
**Confidence:** 89%
**Complexity:** Medium
**Status:** Unexplored

## Rejection Summary

| # | Idea | Reason Rejected |
|---|------|-----------------|
| 1 | Add more screenshots, icons, and marketplace polish | Helpful later, but official docs place higher leverage on manifest truth and skill metadata quality first. |
| 2 | Create a second Codex-only README | Adds another duplicate narrative and increases drift risk rather than reducing it. |
| 3 | Blanket-add `openai.yaml` to every skill | Too mechanical; official metadata is optional and should reflect intended invocation and dependencies, not cargo-cult coverage. |
| 4 | Keep the current broad packaged trees and just rewrite descriptions | Too weak; the main gap is structural exposure plus invocation policy, not only wording. |
| 5 | Build a custom installer around the marketplace | Not grounded in current pain; the repo already has the official local marketplace model. |
| 6 | Add more MCP servers beyond Xcode | Not justified by current plugin goals or official guidance. |
| 7 | Focus next on Claude-first command/agent cleanup | Outside the requested Codex enhancement scope. |

## Session Log
- 2026-04-11: Initial ideation — generated a broad next-scope list grounded in the merged Codex plugin migration; 6 survivors remained after filtering.
- 2026-04-11: Refined ideation against official Codex plugin and skills guidance — raised the bar on install-surface truth, implicit invocation boundaries, and plugin-vs-local-skill separation; 5 survivors remained.
