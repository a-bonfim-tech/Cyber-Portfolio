# Detection and Prevention Controls – Ransomware Healthcare Clinic

This document outlines detection mechanisms and preventive security controls recommended to reduce the risk of ransomware attacks in healthcare environments.

---

## Detection Controls

### Email Security

* Phishing detection using secure email gateways.
* Attachment sandboxing to analyze malicious files.
* DMARC, DKIM, and SPF enforcement.

### Endpoint Detection and Response (EDR)

* Behavioral monitoring for ransomware activity.
* Detection of mass file encryption patterns.
* Automated isolation of compromised endpoints.

### SIEM Monitoring

* Correlation of suspicious email events with endpoint alerts.
* Alerts for abnormal file access and encryption activity.
* Monitoring failed login attempts following phishing campaigns.

---

## Preventive Controls

### User Awareness

* Mandatory phishing awareness training.
* Regular simulated phishing exercises.

### Access Control

* Principle of least privilege for all users.
* Multi-factor authentication for email and remote access.

### Backup Strategy

* Regular offline and immutable backups.
* Periodic restoration testing.

### Network Security

* Network segmentation to limit lateral movement.
* Restriction of macro-enabled attachments.

---

## Conclusion

Combining layered detection with preventive controls significantly reduces ransomware risk and improves organizational resilience.

