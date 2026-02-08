# ADR-0002 — Standardize SSH Commit Signing (ED25519)

- Status: Accepted
- Date: 2026-02-08
- Decision Owner: a-bonfim-tech
- Scope: This repository

## Context
Repository governance requires auditability and integrity of change history. Commit signing is required to provide cryptographic provenance for authored changes.

Two mechanisms exist in practice:
- GPG signing (key management + email verification constraints)
- SSH signing (ED25519) supported by Git and verifiable by GitHub when the signing key is registered

## Decision
Adopt SSH commit signing (ED25519) as the default commit-signing standard for this repository.

Baseline requirements:
- Git configured with `gpg.format=ssh`
- `commit.gpgsign=true`
- Signing public key registered in GitHub as a **Signing key**
- Commit author/committer email is a **verified** email in GitHub

Local verification requirement:
- `gpg.ssh.allowedSignersFile` configured for workstation verification (e.g., `~/.ssh/allowed_signers`)

## Consequences
### Positive
- Consistent Verified status on GitHub when email + signing key are correctly registered
- Simplified key management relative to GPG for day-to-day operations
- Strong audit trail aligned with governance objectives

### Negative / Trade-offs
- Local verification depends on workstation configuration (`allowedSignersFile`)
- Parallel GPG keys may remain in GitHub account settings and can create visual noise (non-blocking)

## Evidence
- governance/evidence/commit-signing-ssh-2026-02-08.md
