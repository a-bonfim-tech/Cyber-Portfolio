#!/usr/bin/env bash
set -euo pipefail

BASE="CERTIFICATES/2026"

for pdf in "$BASE"/*/*/certificate.pdf; do
  dir="$(dirname "$pdf")"
  sha="$(shasum -a 256 "$pdf" | awk '{print $1}')"

  jq ". + {\"sha256\": \"$sha\"}" \
    "$dir/METADATA.json" > /tmp/meta.json

  mv /tmp/meta.json "$dir/METADATA.json"
  echo "OK: $dir"
done
