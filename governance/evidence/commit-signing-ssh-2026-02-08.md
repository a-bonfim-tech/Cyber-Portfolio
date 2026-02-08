# Evidence — SSH Commit Signing Baseline — 2026-02-08

## Goal
Record that commits are:
- signed via SSH (ED25519),
- attributed to a GitHub-verified email.

## Reference commit
- SHA: be72cc24b5e478a071133298c866ac07ff4f55fb
- Method: SSH signing (ED25519)
- GitHub signing key fingerprint: SHA256:frrOk4/ex/f8wxPR9DXwOIAHM6fBl5DULeIWQL5fHyk
- Author/Committer: a-bonfim.tech@cloud-comunity.de

## Local verification (workstation)
`gpg.ssh.allowedSignersFile` is a local Git requirement to verify SSH signatures on the workstation.
Example: ~/.ssh/allowed_signers

## Evidence commands
git show --show-signature -1
git show -s --format='%H%nAuthor: %an <%ae>%nCommitter: %cn <%ce>' HEAD
