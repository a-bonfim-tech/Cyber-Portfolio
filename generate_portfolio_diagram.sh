#!/bin/bash
# Script profissional para gerar PNG, PDF e README do diagrama CSIRT-SOC-DevSecOps

# Criar pasta se não existir
mkdir -p assets/diagrams

# Criar arquivo DOT final
cat << 'EOF' > assets/diagrams/csirt_soc_devsecops_portfolio.dot
digraph CSIRT_SOC_DevSecOps_Professional {
    rankdir=TB;
    node [shape=box, style=filled, fontname="Helvetica", fontsize=10, width=2.5, height=1.0];

    Exec [label="Executive Management\n(Stakeholders / Compliance)", color="#FFD700", style=filled, fontsize=12];
    SOCManager [label="SOC Manager\n(Performance, Audit)", color="#87CEFA", style=filled];
    L3Lead [label="SOC Lead L3\n(Advanced Detection, Forensics)", color="#87CEFA", style=filled];
    TechLead [label="Technical Lead\n(Containment, Eradication, Recovery)", color="#87CEFA", style=filled];
    IncidentCoordinator [label="Incident Coordinator\n(Cross-department Communication)", color="#32CD32", style=filled];
    L2Analyst [label="SOC Analyst L2\n(Deep Investigation)", color="#87CEFA", style=filled];
    SecurityAnalyst [label="CSIRT Security Analyst\n(Alert Triage, Investigation)", color="#32CD32", style=filled];
    L1Analyst [label="SOC Analyst L1\n(Monitoring, Escalation)", color="#87CEFA", style=filled];
    HR_IT_Legal [label="HR / Legal / IT / PR", color="#32CD32", style=filled];

    Exec -> SOCManager [label="Command", fontsize=10, penwidth=2];
    SOCManager -> L3Lead [label="Technical Control", fontsize=10, penwidth=2];
    SOCManager -> TechLead [label="Technical Control", fontsize=10, penwidth=2];
    SOCManager -> IncidentCoordinator [label="Coordination", fontsize=10, penwidth=2];
    L3Lead -> L2Analyst -> L1Analyst [label="Escalation", fontsize=10, penwidth=2];
    TechLead -> SecurityAnalyst [label="Incident Triage", fontsize=10, penwidth=2];
    IncidentCoordinator -> HR_IT_Legal [label="Communication", fontsize=10, penwidth=2];

    CI_CD [label="DevSecOps CI/CD Pipeline\n(Code, Build, Test, Deploy)", shape=ellipse, color="#FF8C00", style=filled, fontsize=10];
    CI_CD -> L1Analyst [label="Automated Alerts", fontsize=10, penwidth=2];
    CI_CD -> SecurityAnalyst [label="Automated Alerts", fontsize=10, penwidth=2];

    subgraph cluster_legend {
        label="Legend";
        fontsize=12;
        style=dashed;
        Legend1 [label="Yellow = Executive Management\nBlue = SOC\nGreen = CSIRT\nOrange = DevSecOps", shape=note, style=filled, color=white];
    }
}
EOF

# Gerar PNG e PDF
dot -Tpng assets/diagrams/csirt_soc_devsecops_portfolio.dot -o assets/diagrams/csirt_soc_devsecops_portfolio.png
dot -Tpdf assets/diagrams/csirt_soc_devsecops_portfolio.dot -o assets/diagrams/csirt_soc_devsecops_portfolio.pdf

# Criar README final
cat << 'EOF' > assets/diagrams/README_DIAGRAM_PORTFOLIO.md
# CSIRT + SOC + DevSecOps Diagram - Portfolio Professional Version

This PDF represents the complete hierarchical structure of a CSIRT and SOC integrated with a DevSecOps pipeline. It is optimized for portfolio presentation, with clear hierarchy, vivid colors, arrows, and a graphical legend.

- **Executive Management (Yellow):** Stakeholders / Compliance
- **SOC (Blue):** Analysts L1/L2, Lead L3, SOC Manager
- **CSIRT (Green):** Security Analysts, Incident Coordinator, HR/Legal/IT/PR collaboration
- **DevSecOps (Orange):** CI/CD pipeline,

