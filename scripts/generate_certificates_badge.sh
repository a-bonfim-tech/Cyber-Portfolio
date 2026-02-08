#!/usr/bin/env bash
set -euo pipefail

BASE="CERTIFICATES/2026"

COUNT=$(find "$BASE" -type f -name "certificate.pdf" | wc -l | tr -d ' ')
TAG="v2026-certificates-integrity"

mkdir -p public

cat > public/certificates-2026.json <<EOF
{
  "schemaVersion": 1,
  "label": "Certificates 2026",
  "message": "$COUNT verified",
  "color": "success",
  "namedLogo": "googlecloud",
  "links": {
    "self": "https://github.com/a-bonfim-tech/Cyber-Portfolio/tree/main/CERTIFICATES/2026",
    "tag": "https://github.com/a-bonfim-tech/Cyber-Portfolio/releases/tag/$TAG"
  }
}
EOF

echo "Generated badge JSON: $COUNT certificates"

