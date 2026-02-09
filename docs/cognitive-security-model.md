# Cognitive Security Model

### Architecture → Logs → Decision (CySA+ Reference)

## Purpose

This document consolidates the core analytical model underlying the CompTIA CySA+ curriculum: **security as a closed cognitive loop**, not a collection of tools.

---

## 1. Architecture as the First Security Control

System, infrastructure, and network architecture define:

* Trust boundaries
* Attack surface
* Control placement
* Visibility points

Poor architecture does not fail silently — it **fails observably**, through logs.

---

## 2. Logs as Objective Evidence

Logs are not artifacts; they are **evidence streams**:

* Host logs explain *local behavior*
* Network logs explain *flow and interaction*
* Control plane logs explain *decision logic*

Without logs:

* No investigation
* No correlation
* No audit
* No defensible decision

---

## 3. From Events to Decisions

Raw logs have no value until:

1. Ingested
2. Normalized
3. Enriched
4. Correlated

Only then can an analyst:

* Identify root cause
* Measure impact
* Recommend architectural change

---

## 4. Controls Are Architectural Choices

Security controls map directly to architecture:

* Technical → implemented in systems
* Operational → enforced by roles
* Managerial → defined by policy and cadence
* Physical → enforce real-world boundaries

Controls do not exist independently of design.

---

## 5. Analyst Mindset (CySA+ Core)

A CySA+ analyst does not ask:

> “What alert fired?”

They ask:

> “Why did this architecture allow this event to occur, and how do we redesign it?”

---

## Conclusion

Security maturity is achieved when:

* Architecture guides visibility
* Logs provide evidence
* Decisions reshape the environment

This feedback loop is the foundation of detection, response, and prevention at scale.
