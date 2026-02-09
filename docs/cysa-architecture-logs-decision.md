# CySA+ — Architecture → Logs → Decision

## Operational Security Reference

### Purpose

This document consolidates a core CySA+ principle: **effective cybersecurity decisions emerge from the intersection of architecture awareness, log-based evidence, and structured analysis**. Tools change; this cognitive model does not.

---

## 1. Architecture as the Root of Security

Security outcomes are constrained by architectural decisions.
Network segmentation, control plane isolation, VPN design, and SDN policies define **where events can occur** and **what evidence can be generated**.

Key rule:

> If the architecture allows it, the incident will eventually happen.

---

## 2. Logs as Evidence, Not Noise

Logs are not stored for compliance alone. They exist to answer four invariant questions:

* **Who** acted?
* **What** occurred?
* **When** did it happen?
* **From where** and **with what result**?

Effective environments distinguish:

* Metadata logs (syslog, flow) for detection
* Contextual logs (firewall, IDS)
* Full evidence (PCAP) for confirmation

Time synchronization (NTP + UTC) is mandatory for correlation and forensic validity.

---

## 3. From Correlation to Decision

CySA+ analysis prioritizes:

1. Correlation before containment
2. Hypothesis before action
3. Evidence before escalation

Decisions fall into three categories:

* **Mitigate** (reduce likelihood or impact)
* **Contain** (limit spread)
* **Accept** (documented, risk-based)

Each decision must be **defensible, reproducible, and auditable**.

---

## 4. Feedback Loop

Every action changes the environment.
Every change must be:

* Documented
* Logged
* Validated

This closes the loop:
**Architecture → Logs → Decision → Change → New Architecture**

---

## Analyst Mindset (CySA+)

The analyst does not ask:

> “What tool detects this?”

The analyst asks:

> “Why did the system allow this, and how do I prove it?”

This mindset distinguishes responders from analysts.
