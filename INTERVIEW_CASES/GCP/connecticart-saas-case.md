# Interview Case — ConnectiCart SaaS (GCP)

## Context
SaaS running fully on Google Cloud Platform.
Role: Systems Computing Engineer / Cloud Architect.

## Challenge
Ensure secure operations, observability, and standardized infrastructure
while handling routine changes and incident signals.

## Actions Taken
- Managed public assets via Cloud Storage using Console/gsutil
- Enforced IAM least privilege with predefined roles
- Investigated latency via Cloud Monitoring dashboards
- Triaged recurring errors using Cloud Logging
- Applied security patches with post-maintenance validation
- Provisioned backend services using GCE instance templates

## Outcome
- Reduced configuration drift
- Faster incident triage
- Audit-ready operational trail

## Evidence
- `EVIDENCE/GCP/ASSESSMENTS/connecticart-saas`
- `DECISIONS/ADR-0002-gcp-connecticart-saas.md`
