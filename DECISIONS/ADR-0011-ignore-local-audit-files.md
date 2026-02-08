# ADR-0011: Ignore Local Audit Scratch Files

## Status
Accepted

## Context
During CI hardening and certificate integrity validation, a local audit scratch file (README_Audit.md) caused non-deterministic working tree states and CI noise. The file is not a formal evidence artifact.

## Decision
Local audit scratch files must not be tracked in Git. Such files are removed from the index (if present) and listed in .gitignore.

## Consequences
- Deterministic CI/CD pipelines
- Reduced audit noise
- Clear separation between evidence and local analysis
- Improved supply-chain integrity

## References
- NIST SP 800-218 (SSDF)
- ISO/IEC 27001 A.8, A.12
- DevSecOps: Reproducible Builds
