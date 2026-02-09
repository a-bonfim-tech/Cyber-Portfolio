# Security Controls, Architecture and Decision-Making

*(CySA+ Reference)*

## Purpose

This document consolidates the relationship between **architecture, logging, and decision-making** as a unified security model, aligned with CompTIA CySA+ objectives and operational cybersecurity practice.

## Security Control Categories

Security controls are grouped into four primary categories:

* **Technical**: Electronic and computing-based controls
  *(firewalls, IDS/IPS, antivirus, SIEM)*

* **Operational**: People and defined security roles
  *(CISO, SOC analysts, custodians, incident responders)*

* **Managerial**: Policies and decisions defined by management
  *(password rotation intervals, badge recertification, access reviews)*

* **Physical**: Tangible barriers and protections
  *(locks, gates, lighting, secured rooms)*

These categories are not tested as memorization items but as **recognition within scenarios**.

## Architecture → Logs → Decision Model

Security effectiveness depends on understanding:

1. **Architecture** – where events can occur
2. **Logs** – how events are recorded
3. **Correlation** – how meaning is extracted
4. **Decision** – how controls are applied or adjusted

Logs are evidence.
Architecture defines risk surface.
Decisions must be **defensible, traceable, and reproducible**.

## Operational Insight

* Changes without documentation create blind spots
* Logs validate both attacks and misconfigurations
* Control planes require stricter protection than data planes
* Honeypots are learning tools, not protective mechanisms

## Analyst Mindset

A CySA+ analyst does not ask only *“What happened?”*
They ask:

* Why did the architecture allow this?
* Which control failed or was absent?
* How can this decision be reproduced safely?

## Conclusion

Cybersecurity is a continuous feedback loop between **design, observation, and correction**.
Understanding this loop is foundational to detection, response, compliance, and audit readiness.
