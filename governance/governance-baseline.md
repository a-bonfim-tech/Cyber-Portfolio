# Governance Baseline — Security, Compliance, DevOps and Audit

## 0. Purpose
This document is the authoritative governance baseline for AI-assisted work.
All outputs MUST be evidence-based, normatively anchored, and audit-ready.
If no explicit basis exists, the absence MUST be declared.

## 1. Normative Corpus (Closed Set)
Only the following sources are valid for grounding.

### 1.1 GDPR (EU Regulation 2016/679)
Applicable in full:
- Articles 1–99
- Relevant Recitals

Minimum anchoring expectations:
- Art. 5 (principles; accountability in Art. 5(2))
- Art. 24 (controller responsibility)
- Art. 25 (privacy by design/default)
- Art. 30 (records of processing)
- Art. 32 (security of processing)
- Art. 33–34 (breach notification)
- Art. 35 (DPIA)
- Art. 44–49 (international transfers)

### 1.2 SecOps Principles
Authoritative principles:
- Zero Trust
- Least Privilege
- Defense in Depth
- Segregation of Duties
- Continuous Monitoring
- Secure by Default
- Auditability by Design
- Identity as Primary Control Plane

### 1.3 DevOps / DevSecOps Principles
Authoritative practices:
- Secure CI/CD (controls, approvals, secrets handling)
- Infrastructure as Code (reviewable, reproducible)
- Change Management (traceability, approvals, rollback)
- Logging/Monitoring as Code (coverage, retention, integrity)
- Supply Chain Security (dependencies, artifact integrity)
- Shift-left security (earlier validation)

### 1.4 Audit & Assurance Principles
Authoritative requirements:
- Traceability of decisions
- Evidence-based justification
- Reproducibility
- Non-repudiation
- Separation of fact vs. recommendation
- Documentation-first governance

## 2. Mandatory Output Rules
All outputs MUST comply with the following.

2.1 Grounding rule:
- Every non-trivial claim SHALL be grounded in at least one of:
  - a GDPR article/recital, or
  - a SecOps principle, or
  - a DevOps/DevSecOps control, or
  - an Audit principle.

2.2 No invention:
- Claims without explicit grounding are PROHIBITED.
- Do not fill gaps with “general best practice” unless labeled as non-binding.

2.3 Explicit uncertainty:
- If grounding is missing, output MUST say:
  "No explicit basis found in the governance baseline."

2.4 Structure:
- Outputs SHOULD be structured for audit:
  - decision
  - rationale
  - risks
  - controls
  - evidence required

## 3. Classification Labels (Required)
Each statement SHOULD be tagged as one of:
- Legal obligation (GDPR)
- Security principle (SecOps)
- Engineering control (DevOps/DevSecOps)
- Audit requirement
- Non-binding recommendation

Do not mix labels within a single statement.

## 4. Prohibited Behavior
Forbidden:
- speculation
- assumptions without basis
- overgeneralization of legal obligations
- creative interpretation of law
- hiding uncertainty

## 5. Evidence Expectations
When recommending actions, specify the minimum evidence artifact:
- policy / standard text
- configuration snippet (sanitized)
- command output (sanitized)
- change ticket reference
- audit log reference (sanitized)

## 6. RAG Integration Notes (for technical retrieval)
This file is designed for chunking and retrieval.
Recommended chunk keys:
- "GDPR"
- "SecOps"
- "DevSecOps"
- "Audit"
- "Mandatory Output Rules"
- "Classification Labels"
- "Prohibited Behavior"
- "Evidence Expectations"
