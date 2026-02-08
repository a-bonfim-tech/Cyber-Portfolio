# Evidence — Commit Signing Baseline (SSH) — 2026-02-08

## Scope
Establish audit-ready evidence that commits in this repository are:
- cryptographically signed (SSH/ED25519),
- attributable to a GitHub-verified email address,
- locally verifiable with an allowed signers file.

## Repository / Branch
- Repository: a-bonfim-tech/Cyber-Portfolio
- Branch: feature/evidence-gcp-connecticart-q1-q6

## Verified Commit (reference)
- Commit SHA: be72cc24b5e478a071133298c866ac07ff4f55fb
- Author/Committer email: a.bonfim.tech@cloud-comunity.de
- Signature method: SSH (ED25519)
- Signing key fingerprint: SHA256:frrOk4/ex/f8wxPR9DXwOIAHM6fBl5DULeIWQL5fHyk

## Local verification commands (evidence)
### Identity attribution
```bash
git show -s --format='%H%nAuthor: %an <%ae>%nCommitter: %cn <%ce>' HEAD


```

### Signature verification
```bash
commit 03ebc99bde57f06905b19a8423c1f77d19624fd5
Good "git" signature for a.bonfim.tech@cloud-comunity.de with ED25519 key SHA256:frrOk4/ex/f8wxPR9DXwOIAHM6fBl5DULeIWQL5fHyk
Author: a-bonfim-tech <a.bonfim.tech@cloud-comunity.de>
Date:   Sun Feb 8 16:19:10 2026 +0100

    docs(evidence): add SSH signing verification baseline notes (2026-02-08)

diff --git a/governance/evidence/commit-signing-ssh-baseline-2026-02-08.md b/governance/evidence/commit-signing-ssh-baseline-2026-02-08.md
new file mode 100644
index 0000000..f321cda
--- /dev/null
+++ b/governance/evidence/commit-signing-ssh-baseline-2026-02-08.md
@@ -0,0 +1,23 @@
+# Evidence — Commit Signing Baseline (SSH) — 2026-02-08
+
+## Scope
+Establish audit-ready evidence that commits in this repository are:
+- cryptographically signed (SSH/ED25519),
+- attributable to a GitHub-verified email address,
+- locally verifiable with an allowed signers file.
+
+## Repository / Branch
+- Repository: a-bonfim-tech/Cyber-Portfolio
+- Branch: docs/add-certificates-badge-readme
+
+## Verified Commit (reference)
+- Commit SHA: be72cc24b5e478a071133298c866ac07ff4f55fb
+- Author/Committer email: a.bonfim.tech@cloud-comunity.de
+- Signature method: SSH (ED25519)
+- Signing key fingerprint: SHA256:frrOk4/ex/f8wxPR9DXwOIAHM6fBl5DULeIWQL5fHyk
+
+## Local verification commands (evidence)
+### Identity attribution
+```bash
+git show -s --format='%H%nAuthor: %an <%ae>%nCommitter: %cn <%ce>' HEAD
+
```

### Config provenance
```bash
file:/Users/andreluizvieirabonfim/.gitconfig	ssh
file:/Users/andreluizvieirabonfim/.gitconfig	/Users/andreluizvieirabonfim/.ssh/id_ed25519.pub
file:/Users/andreluizvieirabonfim/.gitconfig	/Users/andreluizvieirabonfim/.ssh/allowed_signers
```

