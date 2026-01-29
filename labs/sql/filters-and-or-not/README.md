# SQL Investigation Lab — Filters with AND, OR, and NOT (employees + log_in_attempts)

## Context
You are a security professional in a large organization. Part of your job is to investigate security issues to help keep systems secure. You identified potential security concerns involving employee machines and login attempts.

This lab examines organizational data in two tables:
- `employees`
- `log_in_attempts`

Goal: Use SQL filters (`WHERE` + `AND/OR/NOT`) to retrieve specific record sets and investigate suspicious activity.

> Evidence note: This portfolio artifact can be completed with or without revisiting the lab. If you revisit the lab, add screenshots as evidence.

---

## Scope and Constraints
- **Scope**: Read-only investigation using SQL queries.
- **Data types**: Includes strings (e.g., `country`, `department`, `office`) and time/date fields (e.g., `login_time`, `login_date`).
- **Assumptions**:
  - `success` is stored as a boolean-like value in MySQL (commonly `1` for TRUE, `0` for FALSE).
  - The organization’s business hours end at `18:00:00` for this scenario.
  - Country field may include values like `MEX` and `MEXICO`.

---

## Objectives
1. Identify failed login attempts after business hours.
2. Retrieve login attempts for a suspicious date and the previous day.
3. Identify login attempts not originating from Mexico (accounting for `MEX` and `MEXICO`).
4. Support operational follow-ups with employee roster filtering.

---

## Method (Audit-Ready)
For each task:
1. Run the SQL query exactly as written.
2. Capture output evidence (screenshot or exported result).
3. Record findings and next-step actions.
4. Store evidence artifacts with timestamps.

---

## Queries and Results

### Task 1 — Failed logins after business hours (AND)
**Purpose**: Identify failed login attempts occurring after `18:00:00`.

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00:00'
  AND success = 0;
