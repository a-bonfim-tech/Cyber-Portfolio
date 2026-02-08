# Evidence — Commit Signing Baseline (SSH) — 2026-02-08

## Scope
Establish audit-ready evidence that commits in this repository are:
- cryptographically signed (SSH/ED25519),
- attributable to a GitHub-verified email address,
- locally verifiable with an allowed signers file.

## Repository / Branch
- Repository: a-bonfim-tech/Cyber-Portfolio
- Branch: docs/add-certificates-badge-readme

## Verified Commit (reference)
- Commit SHA: be72cc24b5e478a071133298c866ac07ff4f55fb
- Author/Committer email: a.bonfim.tech@cloud-comunity.de
- Signature method: SSH (ED25519)
- Signing key fingerprint: SHA256:frrOk4/ex/f8wxPR9DXwOIAHM6fBl5DULeIWQL5fHyk

## Local verification commands (evidence)
### Identity attribution
```bash
git show -s --format='%H%nAuthor: %an <%ae>%nCommitter: %cn <%ce>' HEAD

