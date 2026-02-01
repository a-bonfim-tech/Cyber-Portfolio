# MITRE ATT&CK Mapping – Ransomware Healthcare Clinic

This document maps the ransomware incident affecting a small healthcare clinic to the MITRE ATT&CK framework. The mapping reflects observed behaviors based on incident reports and initial analysis.

---

## Tactic: Initial Access (TA0001)

**Technique: Phishing – Spearphishing Attachment (T1566.001)**
Attackers gained initial access by sending targeted phishing emails containing a malicious attachment. Once opened by employees, the attachment executed malware on endpoint systems.

---

## Tactic: Execution (TA0002)

**Technique: User Execution – Malicious File (T1204.002)**
The malware required user interaction to execute. Employees unknowingly launched the malicious attachment, enabling the ransomware payload to run.

---

## Tactic: Persistence (TA0003)

**Technique: Not Determined**
At this stage of the investigation, no confirmed persistence mechanisms have been identified. Further forensic analysis is required.

---

## Tactic: Privilege Escalation (TA0004)

**Technique: Not Determined**
There is insufficient information to confirm whether privilege escalation occurred prior to ransomware deployment.

---

## Tactic: Defense Evasion (TA0005)

**Technique: Obfuscated Files or Information (T1027)**
The ransomware payload was likely obfuscated to evade signature-based detection prior to execution.

---

## Tactic: Impact (TA0040)

**Technique: Data Encrypted for Impact (T1486)**
The ransomware encrypted critical organizational files, rendering systems unavailable and disrupting clinical operations. A ransom note was displayed demanding payment for decryption.

---

## Summary

The attack followed a common ransomware lifecycle beginning with phishing-based initial access, followed by user execution and culminating in data encryption for impact. Gaps in visibility remain regarding persistence, lateral movement, and privilege escalation, which should be addressed in subsequent investigation phases.

