# Control Mapping (Policy-as-Code)

## CTRL-LOCAL-001 — Forbid audit scratch files in repo/workspace
**Risk**: leakage of local artifacts / ambiguous provenance / audit noise  
**Policy**: audit scratch files MUST NOT be tracked and MUST NOT exist in CI workspace  
**Enforcement**:
- GitHub Actions: `Certificates Integrity CI`
- Script: `.github/scripts/guardrail_no_audit_scratch.sh`
- Trigger: `push`, `pull_request`
**Evidence**:
- CI run logs: step `Guardrail — forbid audit scratch files`
- Repository state: `.gitignore` contains `README_Audit.md`
