# ADR-0002 — GCP Operational Decisions for ConnectiCart SaaS

## Status
Accepted

## Context
The ConnectiCart SaaS platform runs entirely on Google Cloud Platform.
Operational decisions must follow:
- Least privilege (IAM)
- SOP-driven operations
- Observability-first troubleshooting
- Infrastructure standardization

## Decision
Adopt and document the following operational standards:
1. Cloud Storage uploads via Console or gsutil only
2. IAM access via predefined/custom roles (no primitive roles)
3. Incident triage starting with Cloud Monitoring dashboards
4. Error investigation via Cloud Logging
5. Post-maintenance validation using monitoring indicators
6. Compute Engine provisioning strictly via instance templates

## Consequences
- Reduced configuration drift
- Improved auditability
- Faster incident response
- Reproducible infrastructure

## Evidence
- Assessment Q1–Q6: `EVIDENCE/GCP/ASSESSMENTS/connecticart-saas`
- GCP Evidence README: `EVIDENCE/GCP/README.md`
