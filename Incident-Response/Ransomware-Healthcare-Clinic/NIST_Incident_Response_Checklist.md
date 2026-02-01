# NIST Incident Response Checklist

**Case: Ransomware – Healthcare Clinic**

This checklist is aligned with the NIST SP 800-61r2 Incident Response Lifecycle and documents the actions applicable to this ransomware incident affecting a healthcare organization.

---

## 1. Preparation

* Incident Response Plan documented and accessible
* Roles and responsibilities defined (IR lead, IT, legal, communications)
* Staff security awareness training in place (phishing awareness)
* Backup strategy defined (offline and immutable backups)
* Logging and monitoring enabled on endpoints and servers

---

## 2. Detection and Analysis

* Multiple employees reported inability to access files
* Ransom note observed on affected systems
* Initial indicators identified:

  * Encrypted medical records
  * Suspicious email attachments
  * Malware execution on endpoints
* Incident classified as **Ransomware (High Severity)**
* Potential impact to patient data and business continuity identified

---

## 3. Containment

* Affected systems powered down or isolated from the network
* Network segmentation enforced to prevent lateral movement
* Email gateway rules reviewed to block similar phishing attempts
* Credentials potentially exposed flagged for reset

---

## 4. Eradication

* Malware identified and removed from affected endpoints
* Phishing email artifacts collected for analysis
* Vulnerable systems patched
* Malicious persistence mechanisms removed

---

## 5. Recovery

* Systems restored from clean, verified backups (if available)
* File integrity validated
* Systems monitored closely for reinfection
* Gradual return to normal operations

---

## 6. Post-Incident Activity

* Incident documented in the Incident Handler’s Journal
* Root cause analysis completed
* Lessons learned session conducted
* Security controls updated (email filtering, endpoint protection)
* Regulatory and legal reporting requirements reviewed (HIPAA con

