---
description: Run comprehensive code review with parallel Swift-specific and general quality agents
argument-hint: [file paths or "all"]
allowed-tools: Read, Grep, Glob, Task, Bash(git diff *)
---

# Code Review: $ARGUMENTS

## Workflow

1. **Identify scope:**
   - If `$ARGUMENTS` specifies files → review those files
   - If `$ARGUMENTS` is "all" or empty → identify changed files via `git diff main`
   - If no git context → review all Swift files in the project

2. **Dispatch two review agents in parallel:**
   - `swift-reviewer` agent — Swift 6 concurrency, Liquid Glass, deprecated APIs, accessibility, performance
   - `code-reviewer` agent — plan adherence, code organization, error handling, test coverage (code-analyzer protocol)

3. **Merge findings:**
   - Deduplicate overlapping issues (both reviewers often catch the same root cause)
   - Unify severity: CRITICAL → MAJOR → MINOR → SUGGESTION
   - Preserve file:line references from both reviewers

4. **Grade the review:**
   - Count FAIL sections from code-analyzer output
   - Count CRITICAL findings from swift-reviewer
   - **A-:** 0 FAIL, 0 CRITICAL → meets Phase 5 exit criterion
   - **B:** 0 FAIL, 1-2 CRITICAL → fix CRITICALs, re-review
   - **C:** 1+ FAIL → fix FAILs and CRITICALs, re-review
   - Report grade and whether it meets the Phase 5 exit criterion

5. **Present unified report** grouped by severity with actionable fixes

## Rules

- ALWAYS dispatch both agents — do not skip one for speed
- ALWAYS produce a grade — the grade drives the review-fix loop in Phase 5
- Findings from both agents with the same root cause count as ONE finding
- If zero issues found → Grade A, report "Clean review"
