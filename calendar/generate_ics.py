#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import hashlib
from pathlib import Path

TZID = "Europe/Berlin"  # Apple Calendar uses floating local time when TZID header exists
START_DATE = datetime(2026, 2, 10, 9, 0, 0)  # Monday 2026-02-10 09:00 local
WORK_START_HHMM = (9, 0)

FOCUS_MIN = 25
BREAK_MIN = 5

@dataclass(frozen=True)
class DayPlan:
    code: str           # e.g., W1D1
    date: datetime      # local naive datetime at 09:00
    title: str          # summary base
    blocks_minutes: int # 240 for 4h, 180 for 3h, 240 for mock, etc.
    track: str          # "SECURITY+" or "CYSA+"
    tags: str           # description base

def dtstamp_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

def uid_deterministic(calendar_id: str, dtstart: datetime, summary: str) -> str:
    # Deterministic UID: sha256(calendar_id|dtstart|summary) -> first 32 hex
    seed = f"{calendar_id}|{dtstart.strftime('%Y%m%dT%H%M%S')}|{summary}".encode("utf-8")
    h = hashlib.sha256(seed).hexdigest()[:32]
    return f"{h}@a-bonfim-tech.local"

def vevent(calendar_id: str, dtstart: datetime, dtend: datetime, summary: str, description: str) -> str:
    uid = uid_deterministic(calendar_id, dtstart, summary)
    return "\n".join([
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{dtstamp_utc()}",
        f"DTSTART:{dtstart.strftime('%Y%m%dT%H%M%S')}",
        f"DTEND:{dtend.strftime('%Y%m%dT%H%M%S')}",
        f"SUMMARY:{summary}",
        f"DESCRIPTION:{description}",
        "END:VEVENT",
        ""
    ])

def build_pomodoros(calendar_id: str, day: DayPlan, out: list[str]) -> None:
    # We log focus + break as separate events.
    # To match total minutes exactly, we model as pairs:
    #   Focus (25) then Break (5) repeated N times where N = total/30 for 3h, 4h etc.
    total = day.blocks_minutes
    if total % (FOCUS_MIN + BREAK_MIN) != 0:
        raise ValueError(f"blocks_minutes must be multiple of 30. Got {total} for {day.code}")
    pairs = total // (FOCUS_MIN + BREAK_MIN)

    t = day.date.replace(hour=WORK_START_HHMM[0], minute=WORK_START_HHMM[1], second=0)
    for i in range(1, pairs + 1):
        # Focus
        focus_start = t
        focus_end = focus_start + timedelta(minutes=FOCUS_MIN)
        out.append(vevent(
            calendar_id,
            focus_start, focus_end,
            f"[{day.code}][P{i}] {day.title} (FOCUS)",
            f"Pomodoro {i}/{pairs} — {day.tags}"
        ))
        # Break
        break_start = focus_end
        break_end = break_start + timedelta(minutes=BREAK_MIN)
        out.append(vevent(
            calendar_id,
            break_start, break_end,
            f"[{day.code}][B{i}] BREAK",
            "Audit pause (logged)"
        ))
        t = break_end

def build_mock_block(calendar_id: str, day: DayPlan, out: list[str], minutes: int, label: str) -> None:
    t0 = day.date.replace(hour=WORK_START_HHMM[0], minute=WORK_START_HHMM[1], second=0)
    t1 = t0 + timedelta(minutes=minutes)
    out.append(vevent(
        calendar_id, t0, t1,
        f"[{day.code}] {label}",
        day.tags
    ))

def ics_header(prod: str) -> str:
    return "\n".join([
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "CALSCALE:GREGORIAN",
        f"PRODID:{prod}",
        f"X-WR-TIMEZONE:{TZID}",
        ""
    ])

def ics_footer() -> str:
    return "END:VCALENDAR\n"

def weekdays(start: datetime, count_days: int, only_weekdays=True) -> list[datetime]:
    dates = []
    d = start
    while len(dates) < count_days:
        if not only_weekdays or d.weekday() < 5:
            dates.append(d)
        d = d + timedelta(days=1)
    return dates

def main() -> None:
    # Dates: 4 weeks, Mon–Fri each = 20 days
    days = weekdays(START_DATE, 20, only_weekdays=True)

    # Map plan (EN) to days
    # Weeks: W1 (D1-5), W2 (D1-5), W3 (D1-5), W4 (D1-5)
    sec_days: list[DayPlan] = [
        DayPlan("W1D1", days[0],  "Security+ D1 — Attacks & Threats",             240, "SECURITY+", "Theory + Kali Lab + Evidence Commit"),
        DayPlan("W1D2", days[1],  "Security+ D1 — Vulnerabilities & MITRE",       240, "SECURITY+", "Threat analysis + Mapping + GitHub evidence"),
        DayPlan("W1D3", days[2],  "Security+ D2 — Secure Architecture",          240, "SECURITY+", "Zero Trust + GCP VPC + Diagram"),
        DayPlan("W1D4", days[3],  "Security+ D2 — IAM & Network Design",         240, "SECURITY+", "GCP IAM least privilege + evidence"),
        DayPlan("W1D5", days[4],  "Security+ — Practice Test + Review",          180, "SECURITY+", "Timed practice set + review + remediation"),

        DayPlan("W2D1", days[5],  "Security+ D3 — Security Operations",          240, "SECURITY+", "Logging + Monitoring + Triage + Evidence"),
        DayPlan("W2D2", days[6],  "Security+ D4 — Governance & Risk",            240, "SECURITY+", "Risk + Policy + GDPR/LGPD mapping"),
        DayPlan("W2D3", days[7],  "Security+ D5 — Cryptography & PKI",           240, "SECURITY+", "PKI + Certificates + Validation evidence"),
        DayPlan("W2D4", days[8],  "Security+ — Review & Weak Points",            240, "SECURITY+", "Gap closure + labs repeat + evidence"),
        DayPlan("W2D5", days[9],  "Security+ — Full Mock Exam + Post-mortem",    180, "SECURITY+", "90-minute timed exam + post-mortem + fixes"),
    ]

    cysa_days: list[DayPlan] = [
        DayPlan("W3D1", days[10], "CySA+ D1 — Threat & Vulnerability Mgmt",      240, "CYSA+",     "Scanning + Prioritization + Evidence"),
        DayPlan("W3D2", days[11], "CySA+ D1 — Vulnerability Assessment",         240, "CYSA+",     "Assessment + CVSS + reporting"),
        DayPlan("W3D3", days[12], "CySA+ D2 — Security Operations & Monitoring", 240, "CYSA+",     "SIEM + Detection + Logs"),
        DayPlan("W3D4", days[13], "CySA+ D2 — Incident Triage",                  240, "CYSA+",     "Triage playbooks + evidence handling"),
        DayPlan("W3D5", days[14], "CySA+ — Timed Practice Sets",                 180, "CYSA+",     "Timed practice + review + remediation"),

        DayPlan("W4D1", days[15], "CySA+ D3 — Incident Response",                240, "CYSA+",     "IR lifecycle + forensics basics"),
        DayPlan("W4D2", days[16], "CySA+ D3 — Threat Hunting",                   240, "CYSA+",     "Hypothesis-driven hunting + ATT&CK"),
        DayPlan("W4D3", days[17], "CySA+ D4 — Compliance & Reporting",           240, "CYSA+",     "Controls + reporting + evidence"),
        DayPlan("W4D4", days[18], "CySA+ — Review & Labs Consolidation",         240, "CYSA+",     "Close gaps + re-run key labs"),
        DayPlan("W4D5", days[19], "CySA+ — Full Mock Exam + Analysis",           240, "CYSA+",     "165-minute timed exam + analysis + fixes"),
    ]

    # Generate Security+ calendar (full expanded events)
    sec_out: list[str] = [ics_header("-//SecurityPlus Pomodoro Audit//EN")]
    for d in sec_days:
        # Mock day can be pomodoro-logged or single block. User asked pomodoros+breaks separated (ultra-auditável).
        # Keep everything as pomodoro+break pairs for full audit trail.
        build_pomodoros("securityplus", d, sec_out)
    sec_out.append(ics_footer())

    # Generate CySA+ calendar (full expanded events)
    cysa_out: list[str] = [ics_header("-//CySAPlus Pomodoro Audit//EN")]
    for d in cysa_days:
        build_pomodoros("cysa", d, cysa_out)
    cysa_out.append(ics_footer())

    out_dir = Path("ics")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "securityplus-pomodoro-4weeks.ics").write_text("\n".join(sec_out), encoding="utf-8")
    (out_dir / "cysa-pomodoro-4weeks.ics").write_text("\n".join(cysa_out), encoding="utf-8")

    print("OK: generated:")
    print(" - ics/securityplus-pomodoro-4weeks.ics")
    print(" - ics/cysa-pomodoro-4weeks.ics")

if __name__ == "__main__":
    main()
