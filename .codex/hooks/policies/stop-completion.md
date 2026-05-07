---
name: codex-stop-completion-gate
enabled: true
event: stop
action: block
conditions:
  - field: changed_targets
    operator: equals
    pattern: true
  - field: validation_failure
    operator: equals
    pattern: true
---

Canonical Codex files changed, but the parity contract or validator is not
passing. Regenerate the contract, fix the reported failure, rerun the checks,
and only stop once the Codex surface is truthful again.
