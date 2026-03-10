#!/bin/bash
INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

if [ "$TOOL" = "Bash" ]; then
  # Block pod install in SPM projects
  if echo "$COMMAND" | grep -q "pod install"; then
    echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"This project uses Swift Package Manager, not CocoaPods. Use Package.swift for dependencies."}}'
    exit 0
  fi

  # Block rm on xcodeproj
  if echo "$COMMAND" | grep -qE "rm.*\.xcodeproj"; then
    echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Do not delete .xcodeproj files. Use Xcode to manage project structure."}}'
    exit 0
  fi

  # Block rm -rf on source directories
  if echo "$COMMAND" | grep -qE "rm\s+-[^[:space:]]*r[^[:space:]]*f.*/(Sources|src|App|Models|Views|ViewModels)"; then
    echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Blocked: cannot recursively delete source directories."}}'
    exit 0
  fi
fi

exit 0
