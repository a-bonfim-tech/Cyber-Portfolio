# ConnectiCart (GCP) — Performance Assessment (Q1–Q6) — Evidence

## Context
Role: Systems Computing Engineer / Cloud Architect for SaaS running fully on Google Cloud Platform (GCP).
Scope: Cloud Storage (GCS), IAM, troubleshooting, SOP maintenance, Observability (Cloud Ops Suite), GCE templates.

## Answers (Binary-graded selections)

### Q1 — Cloud Storage (routine data management)
**Selected:** Use the Google Cloud Console UI or the standard CLI tool to upload the file to the specified Cloud Storage bucket.  
**Rationale:** Standard supported method for object upload to GCS; aligns with routine SOP operations.

### Q2 — IAM Least Privilege
**Selected:** Add the engineer’s user account as a principal and grant the pre-defined custom role `gce-viewer-role` at the project IAM policy.  
**Rationale:** Least privilege; view-only access; avoids primitive overly-broad roles.

### Q3 — Cloud Monitoring alert: high latency
**Selected:** Quickly validate the alert and understand scope by checking related metrics (CPU, memory, error rates).  
**Rationale:** First runbook step: confirm signal, correlate metrics, assess blast radius before remediation.

### Q4 — Weekly maintenance window: security patches
**Selected:** Validate system health after maintenance by checking key indicators on monitoring dashboards.  
**Rationale:** Post-change verification is mandatory in SOP to ensure reliability after patching.

### Q5 — Recurring issue: photo upload errors
**Selected:** Google Cloud Logging to search/filter aggregated logs for `user-profile-service` (last 30 minutes).  
**Rationale:** Logs are the authoritative source for error messages and service events; filtering by time + service is standard.

### Q6 — Provision new backend VM using an existing template
**Selected:** Create a new instance directly from the existing `batch-processor-template` (as required by SOP).  
**Rationale:** Prevents config drift; enforces standardization, auditability, and repeatability.

## Operational controls included in this evidence
- Written record of selections + rationale (this document)
- Cryptographic hash recorded separately
- Version control history (git commits)
