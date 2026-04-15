---
title: "refactor: Align all 5 plugins with Claude Code v2.1+ plugin spec"
type: refactor
status: completed
date: 2026-04-15
---

# refactor: Align all 5 plugins with Claude Code v2.1+ plugin spec

## Overview

The validation audit on 2026-04-15 found 7 WARN-level spec deviations across all 5 plugins (0 FAIL). This plan addresses every finding — fixing agent frontmatter, cleaning manifests, migrating 22 deprecated commands to skills format, and documenting one intentional design choice.

## Problem Frame

Claude Code v2.1+ defines strict schemas for plugin manifests, agents, hooks, commands, and skills. While all 5 plugins load and function today (no FAIL issues), 7 categories of spec deviation create fragility risk — particularly W2 (malformed YAML in agent descriptions) which could break on any parser update, and W6 (deprecated commands/) which locks out features like `context: fork`, `paths:`, and `agent:` delegation.

## Requirements Trace

- R1. All agent `tools` fields use spec-compliant format (space-separated string or array)
- R2. All multi-line agent descriptions use YAML literal block scalar (`|`) to prevent parse failures
- R3. Non-spec frontmatter fields (`color`) removed from agents
- R4. Non-spec manifest fields (`categories`) removed from plugin.json files
- R5. All shell scripts use `#!/usr/bin/env zsh` per macOS spec + project convention
- R6. All 22 commands migrated from deprecated `commands/` to `skills/<name>/SKILL.md`
- R7. Hookify's universal matcher design documented as intentional
- R8. CLAUDE.md updated to reflect new skill/command counts post-migration

## Scope Boundaries

- No behavioral changes — all invocations (`/plugin:name`) must work identically after migration
- No content changes to skill/command markdown bodies
- No hook logic changes
- No new features added

## Context & Research

### Relevant Code and Patterns

- Existing skills follow `skills/<name>/SKILL.md` with YAML frontmatter (27 skills across 4 plugins)
- Agents using `description: |` already: `macos-architect`, `code-reviewer`, `swift-reviewer` — these are the pattern to follow
- Commands use same frontmatter fields as skills (`description`, `allowed-tools`, `argument-hint`, `disable-model-invocation`)
- `scaffold-project` (command) and `swift-project-scaffold` (skill) coexist in apple-app-architect — different names, no conflict

### Spec References

- Plugin manifest: `name` (required, kebab-case), `version`, `description`, `author`, `keywords` — `categories` not in spec
- Agent frontmatter: `name`, `description`, `model`, `tools` (string|array), `skills`, `isolation` — `color` not in spec
- Skills: `skills/<name>/SKILL.md` with frontmatter — replaces deprecated `commands/<name>.md`
- Hook scripts: `#!/usr/bin/env zsh` recommended for macOS

## Key Technical Decisions

- **Migrate commands to skills, not just rename**: The `skills/<name>/SKILL.md` format unlocks `context: fork`, `paths:`, `agent:`, and embedded hooks that flat `commands/*.md` cannot use. This future-proofs the toolkit even though current commands don't need these features yet.
- **Use space-separated string for `tools`**: Simpler than array format and matches the spec's primary example. All affected agents have 2-5 tools so readability is fine.
- **Remove `color` rather than keep it**: Non-spec fields add noise and could conflict with future spec additions. The field has no runtime effect today.
- **Document hookify universal matchers as intentional**: Hookify's Python rule engine dynamically evaluates `.local.md` files at runtime — it MUST receive all events to apply user-defined rules. Adding static matchers at `hooks.json` level would break the dynamic architecture.

## Open Questions

### Resolved During Planning

- **Q: Will migrating commands break `/plugin:name` invocations?** No — skills use the same namespace. `/hookify:list` works whether the source is `commands/list.md` or `skills/list/SKILL.md`.
- **Q: Does `skills/skills/SKILL.md` in hookify cause issues?** No — the directory name `skills` is valid. Invoked as `/hookify:skills` regardless of source format.
- **Q: Should `disable-model-invocation` carry over to skills?** Yes — it maps directly to the same field in skill frontmatter.

### Deferred to Implementation

- **Q: Should migrated skills gain new features like `context: fork` or `paths:`?** Out of scope for this refactor. Can be added incrementally per-skill later.

## Implementation Units

- [x] **Unit 1: Fix agent frontmatter compliance (W1 + W2 + W3)**

  **Goal:** Make all 10 agent definitions fully spec-compliant.

  **Requirements:** R1, R2, R3

  **Dependencies:** None

  **Files:**
  - Modify: `plugins/apple-app-architect/agents/code-architect.md`
  - Modify: `plugins/apple-app-architect/agents/code-explorer.md`
  - Modify: `plugins/apple-app-architect/agents/macos-architect.md`
  - Modify: `plugins/apple-app-builder/agents/ios-developer.md`
  - Modify: `plugins/apple-app-builder/agents/ui-developer.md`
  - Modify: `plugins/apple-app-quality/agents/code-reviewer.md`
  - Modify: `plugins/apple-app-quality/agents/swift-reviewer.md`
  - Modify: `plugins/hookify/agents/conversation-analyzer.md`
  - Modify: `plugins/hookify/agents/prompt-manager.md`
  - Modify: `plugins/hookify/agents/skill-manager.md`

  **Approach:**
  For each agent:
  1. If `tools` uses comma-separated format (`Glob, Grep, Read`), change to space-separated (`Glob Grep Read`)
  2. If `description` is a plain scalar with multi-line content (especially `<example>` blocks), convert to literal block scalar (`description: |`) and indent content by 2 spaces
  3. Remove `color: <value>` line if present
  4. Preserve all other frontmatter fields and markdown body unchanged

  **Patterns to follow:**
  - `plugins/apple-app-architect/agents/macos-architect.md` — already uses `description: |` correctly
  - `plugins/apple-app-quality/agents/code-reviewer.md` — already uses `description: |` and `tools: Read, Grep, Glob` (fix tools format only)

  **Test scenarios:**
  - Happy path: Load each modified agent via `claude --plugin-dir ./plugins/<plugin>` — agent appears in agent list with correct description
  - Edge case: Verify `<example>` blocks in descriptions render as part of the description, not as separate YAML keys
  - Error path: YAML parse — run `python3 -c "import yaml; yaml.safe_load(open('agents/X.md').read().split('---')[1])"` on each file to confirm valid YAML

  **Verification:**
  - All 10 agent files parse as valid YAML frontmatter
  - No `color` field in any agent
  - No comma-separated `tools` values
  - All multi-line descriptions use `|` block scalar

---

- [x] **Unit 2: Fix plugin manifests and shell shebang (W4 + W5)**

  **Goal:** Remove non-spec `categories` field from all manifests and fix shell shebang.

  **Requirements:** R4, R5

  **Dependencies:** None

  **Files:**
  - Modify: `plugins/apple-app-architect/.claude-plugin/plugin.json`
  - Modify: `plugins/apple-app-builder/.claude-plugin/plugin.json`
  - Modify: `plugins/apple-app-quality/.claude-plugin/plugin.json`
  - Modify: `plugins/apple-design-system/.claude-plugin/plugin.json`
  - Modify: `plugins/hookify/.claude-plugin/plugin.json`
  - Modify: `plugins/apple-app-builder/hooks/scripts/validate-swift-commands.sh`

  **Approach:**
  - Remove the `"categories": [...]` key-value pair from each `plugin.json`
  - Change line 1 of `validate-swift-commands.sh` from `#!/bin/bash` to `#!/usr/bin/env zsh`
  - Verify the script body is POSIX-compatible (it uses `if`, `echo`, `grep`, `jq` — all zsh-safe)

  **Patterns to follow:**
  - Hookify Python scripts already use `#!/usr/bin/env python3` — correct pattern

  **Test scenarios:**
  - Happy path: Each `plugin.json` parses as valid JSON with `jq .` and contains no `categories` key
  - Happy path: `validate-swift-commands.sh` executes correctly under zsh with mock JSON input piped to stdin
  - Edge case: Confirm `keywords` array is preserved (it IS in spec)

  **Verification:**
  - `jq 'has("categories")' plugin.json` returns `false` for all 5 manifests
  - `head -1 validate-swift-commands.sh` outputs `#!/usr/bin/env zsh`
  - All manifests still load via `claude --plugin-dir`

---

- [x] **Unit 3: Migrate apple-app-architect commands to skills (W6)**

  **Goal:** Convert 6 commands to skills format in apple-app-architect.

  **Requirements:** R6

  **Dependencies:** None (can run in parallel with Units 4-5)

  **Files:**
  - Delete: `plugins/apple-app-architect/commands/brainstorm.md`
  - Delete: `plugins/apple-app-architect/commands/execute-plan.md`
  - Delete: `plugins/apple-app-architect/commands/feature-dev.md`
  - Delete: `plugins/apple-app-architect/commands/revise-claude-md.md`
  - Delete: `plugins/apple-app-architect/commands/scaffold-project.md`
  - Delete: `plugins/apple-app-architect/commands/write-plan.md`
  - Create: `plugins/apple-app-architect/skills/brainstorm/SKILL.md`
  - Create: `plugins/apple-app-architect/skills/execute-plan/SKILL.md`
  - Create: `plugins/apple-app-architect/skills/feature-dev/SKILL.md`
  - Create: `plugins/apple-app-architect/skills/revise-claude-md/SKILL.md`
  - Create: `plugins/apple-app-architect/skills/scaffold-project/SKILL.md`
  - Create: `plugins/apple-app-architect/skills/write-plan/SKILL.md`
  - Delete: `plugins/apple-app-architect/commands/` (directory, after all files moved)

  **Approach:**
  For each command `commands/<name>.md`:
  1. Create directory `skills/<name>/`
  2. Copy content to `skills/<name>/SKILL.md`
  3. Frontmatter carries over as-is — `description`, `allowed-tools`, `argument-hint`, `disable-model-invocation` are all valid skill fields
  4. Add `user-invocable: true` only if the command was user-facing (all are, so this is the default — no change needed)
  5. Delete the original command file
  6. After all 6 are migrated, delete the empty `commands/` directory

  **Patterns to follow:**
  - Existing skills like `plugins/apple-app-architect/skills/app-development-workflow/SKILL.md`

  **Test scenarios:**
  - Happy path: `/apple-app-architect:brainstorm` invokes correctly from skills path
  - Happy path: `/apple-app-architect:scaffold-project MyApp` passes arguments correctly
  - Edge case: `disable-model-invocation: true` on brainstorm/execute-plan/write-plan prevents Claude from auto-invoking
  - Integration: `scaffold-project` skill coexists with `swift-project-scaffold` skill without name collision

  **Verification:**
  - `commands/` directory no longer exists in apple-app-architect
  - All 6 new skill directories contain valid `SKILL.md` with correct frontmatter
  - All 11 skills (5 existing + 6 migrated) appear in skill listing

---

- [x] **Unit 4: Migrate apple-app-builder + apple-app-quality + apple-design-system commands to skills (W6)**

  **Goal:** Convert 10 commands across 3 plugins to skills format.

  **Requirements:** R6

  **Dependencies:** None (can run in parallel with Units 3, 5)

  **Files:**
  - apple-app-builder: Delete 4 commands, create 4 skill directories
    - `build`, `fix-build`, `implement-component`, `run-app`
  - apple-app-quality: Delete 5 commands, create 5 skill directories
    - `refactor-view`, `review-ui`, `review`, `swift-style`, `test`
  - apple-design-system: Delete 1 command, create 1 skill directory
    - `design-ui`
  - Delete: `commands/` directory in each plugin after migration

  **Approach:**
  Same mechanical transformation as Unit 3. For each command:
  1. `mkdir skills/<name>/`
  2. Copy `commands/<name>.md` → `skills/<name>/SKILL.md`
  3. Delete original
  4. Delete empty `commands/` directory per plugin

  **Patterns to follow:**
  - Same as Unit 3

  **Test scenarios:**
  - Happy path: `/apple-app-builder:build` invokes from new skills path
  - Happy path: `/apple-app-quality:review all` passes arguments
  - Happy path: `/apple-design-system:design-ui Button component` works
  - Edge case: `allowed-tools` with MCP wildcards (`mcp__xcodebuildmcp__*`) carries over correctly

  **Verification:**
  - No `commands/` directory remains in any of the 3 plugins
  - All 10 new skill directories contain valid `SKILL.md`
  - Plugin skill counts: builder 10 (6+4), quality 9 (4+5), design-system 13 (12+1)

---

- [x] **Unit 5: Migrate hookify commands to skills (W6)**

  **Goal:** Convert 6 hookify commands to skills format.

  **Requirements:** R6

  **Dependencies:** None (can run in parallel with Units 3-4)

  **Files:**
  - Delete: `plugins/hookify/commands/configure.md`
  - Delete: `plugins/hookify/commands/help.md`
  - Delete: `plugins/hookify/commands/hookify.md`
  - Delete: `plugins/hookify/commands/list.md`
  - Delete: `plugins/hookify/commands/prompts.md`
  - Delete: `plugins/hookify/commands/skills.md`
  - Create: `plugins/hookify/skills/configure/SKILL.md`
  - Create: `plugins/hookify/skills/help/SKILL.md`
  - Create: `plugins/hookify/skills/hookify/SKILL.md`
  - Create: `plugins/hookify/skills/list/SKILL.md`
  - Create: `plugins/hookify/skills/prompts/SKILL.md`
  - Create: `plugins/hookify/skills/skills/SKILL.md`
  - Delete: `plugins/hookify/commands/`

  **Approach:**
  Same mechanical migration. Notable naming considerations:
  - `skills/hookify/SKILL.md` — skill named same as plugin. Valid, invoked as `/hookify:hookify`. No change from current behavior.
  - `skills/skills/SKILL.md` — directory named `skills` inside `skills/`. Structurally valid, invoked as `/hookify:skills`. No change from current behavior.

  **Patterns to follow:**
  - Same as Unit 3

  **Test scenarios:**
  - Happy path: `/hookify:hookify` creates rules from conversation analysis
  - Happy path: `/hookify:list` displays active rules
  - Happy path: `/hookify:configure` opens interactive config
  - Edge case: `skills/skills/SKILL.md` doesn't confuse the skill directory scanner
  - Edge case: `skills/hookify/SKILL.md` doesn't conflict with plugin name

  **Verification:**
  - No `commands/` directory remains in hookify
  - All 6 new skill directories contain valid `SKILL.md`
  - Hookify goes from 0 skills to 6 skills

---

- [x] **Unit 6: Document hookify matcher design + update CLAUDE.md (W7 + R8)**

  **Goal:** Document the hookify universal matcher as intentional and update CLAUDE.md to reflect post-migration component counts.

  **Requirements:** R7, R8

  **Dependencies:** Units 3, 4, 5 (need final skill counts)

  **Files:**
  - Modify: `CLAUDE.md`

  **Approach:**
  1. Add a note in the hookify section of CLAUDE.md explaining why hooks fire on all events (dynamic rule engine evaluates `.local.md` files at runtime — static matchers would break the architecture)
  2. Update the Skill Taxonomy table with new counts:
     - apple-app-architect: 5 → 11 skills, 6 → 0 commands
     - apple-app-builder: 6 → 10 skills, 4 → 0 commands
     - apple-app-quality: 4 → 9 skills, 5 → 0 commands
     - apple-design-system: 12 → 13 skills, 1 → 0 commands
     - hookify: 0 → 6 skills, 6 → 0 commands
  3. Remove or update the "Commands" column in the Phase Coverage table
  4. Update totals: 27 → 49 skills, 22 → 0 commands

  **Test expectation:** None — documentation-only change.

  **Verification:**
  - CLAUDE.md accurately reflects the post-migration plugin structure
  - Hookify matcher design is documented

## System-Wide Impact

- **Interaction graph:** Skill invocation paths change from `commands/<name>.md` → `skills/<name>/SKILL.md`. The `/plugin:name` interface is unchanged for users.
- **Error propagation:** No behavioral changes — if a skill fails to load, same error as a command failing to load.
- **State lifecycle risks:** None — purely structural file reorganization.
- **API surface parity:** All 22 command invocations must continue working post-migration.
- **Unchanged invariants:** Hook behavior, agent behavior, skill content, and plugin loading all remain identical. Only file locations change for commands.

## Risks & Dependencies

| Risk | Mitigation |
|------|------------|
| Skills scanner doesn't find migrated skills | Verify `skills/<name>/SKILL.md` pattern matches existing working skills |
| YAML description conversion introduces whitespace issues | Test each file with strict YAML parser after conversion |
| Hookify `skills/skills/` path confuses scanner | Test explicitly — if broken, rename to `skills/search-skills/` |
| CLAUDE.md counts become stale if plan is partially executed | Unit 6 depends on Units 3-5 completing first |

## Sources & References

- Validation audit: This conversation (2026-04-15)
- Claude Code v2.1+ Plugin Spec: Fetched via docs-researcher agent
- Existing working patterns: `macos-architect.md` (correct `description: |`), all 27 existing skills
