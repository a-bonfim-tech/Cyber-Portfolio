# Compliance Control Mapping

This document maps architectural decisions (ADRs) to security and compliance frameworks.

## Frameworks
- NIST SP 800-218 (SSDF)
- ISO/IEC 27001:2022
- DevSecOps Best Practices

---

## ADR-0011 — Ignore Local Audit Scratch Files

**Decision**: Local audit scratch files are excluded from version control.

### Mapped Controls
- **NIST SP 800-218 (SSDF)**
  - PW.4 — Reproducible Builds
  - PS.3 — Protect Software Artifacts

- **ISO/IEC 27001:2022**
  - A.8.9 — Configuration Management
  - A.8.10 — Information Deletion
  - A.12.5 — Change Control

### DevSecOps Impact
- Deterministic CI/CD
- Reduced supply-chain noise
- Clear separation between evidence and local analysis

### Evidence
- DECISIONS/ADR-0011-ignore-local-audit-files.md
- .gitignore
