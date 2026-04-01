# ConnectiCart — GCP SaaS Performance Assessment (Q1–Q6)

## Role
Systems Computing Engineer / Cloud Architect  
Platform: Google Cloud Platform (GCP)

## Scope
- Google Cloud Storage
- IAM (Least Privilege)
- Cloud Operations Suite
- SOP Maintenance
- Google Compute Engine (Templates)

---

## Q1 — Cloud Storage (Routine Data Management)
**Decision:** Upload via Google Cloud Console UI or standard CLI tool (gsutil).  
**Control Applied:** SOP-compliant data operation.

## Q2 — IAM / Least Privilege
**Decision:** Assign predefined custom role `gce-viewer-role` to the engineer’s user account.  
**Control Applied:** Least privilege, no primitive roles.

## Q3 — Cloud Monitoring Alert
**Decision:** Validate alert scope by reviewing correlated metrics (CPU, memory, error rate).  
**Control Applied:** Runbook-first-step validation.

## Q4 — Maintenance Window
**Decision:** Validate post-patch system health via monitoring dashboards.  
**Control Applied:** Post-change verification.

## Q5 — Error Investigation
**Decision:** Use Google Cloud Logging to filter service errors (last 30 minutes).  
**Control Applied:** Log-based incident triage.

## Q6 — GCE Provisioning
**Decision:** Create new VM from existing `batch-processor-template`.  
**Control Applied:** Template enforcement, configuration consistency.

---

## Evidence Characteristics
- Binary-graded answers
- SOP-aligned decisions
- Audit-ready documentation
