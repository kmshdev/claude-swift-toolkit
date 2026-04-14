---
name: codex-bash-post-review
enabled: true
event: bash
action: warn
tool_matcher: Bash
conditions:
  - field: command
    operator: regex_match
    pattern: "(generate_codex_parity_contract\.py|validate-codex-support\.py|xcrun\s+mcpbridge)"
  - field: tool_response_text
    operator: regex_match
    pattern: "(?s)(traceback|\berror\b|\bfailed\b|not found|no such file|stale or invalid)"
---

The Bash result indicates the Codex runtime or Xcode bridge is not ready. Read
the full command output, fix the reported issue, and do not treat this workflow
as healthy until the command passes.
