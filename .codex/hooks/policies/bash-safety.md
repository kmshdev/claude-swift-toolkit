---
name: codex-bash-safety
enabled: true
event: bash
action: block
tool_matcher: Bash
conditions:
  - field: command
    operator: regex_match
    pattern: "(?:^|[;&|]\s*)(?:(?:sudo\s+)?(?:/bin/)?rm\s+-[A-Za-z]*(?:rf|fr)[A-Za-z]*\b|git\s+reset\s+--hard\b|git\s+checkout\s+--\b|git\s+clean\s+-[A-Za-z]*f[A-Za-z]*d[A-Za-z]*)"
---

This repo blocks destructive shell commands. Use recoverable alternatives such as
`trash`, `git restore`, or a scoped non-destructive command.
