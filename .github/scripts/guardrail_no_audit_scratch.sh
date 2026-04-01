#!/usr/bin/env bash
set -euo pipefail

# Regras explícitas
DENY_PATTERNS=(
  '^README_Audit\.md$'
  '^README_Audit\.md:'
)

# 1) Índice (tracked)
if git ls-files | grep -E "$(printf '%s|' "${DENY_PATTERNS[@]}" | sed 's/|$//')" >/dev/null; then
  echo "Guardrail failed: forbidden audit scratch file is tracked."
  exit 1
fi

# 2) Workspace (untracked)
if git status --porcelain=v1 | sed -n 's/^?? //p' \
  | grep -E "$(printf '%s|' "${DENY_PATTERNS[@]}" | sed 's/|$//')" >/dev/null; then
  echo "Guardrail failed: forbidden audit scratch file present in workspace."
  exit 1
fi

echo "Guardrail OK: no audit scratch files detected."
