# 🔐 Cyber-Portfolio — Cloud & Security Case Studies

Welcome to my **Cybersecurity Portfolio**, focused on:

- **Cloud Security (Google Cloud Platform)**
- **API Security & IAM Troubleshooting**
- **Log Analysis & Observability**
- **Hands-on Labs integrated with GitHub & LinkedIn**

This repository is built to be **recruiter-friendly** and **technically auditável**, with case studies that show:

- Real command-line workflows  
- API request/response structures  
- Security reasoning (threat modeling, data handling, IAM)  
- Clear English documentation + PT-BR summary  

---

## 🌟 Featured Case Study

### Vision Base64 Security Lab — AI Portraits (GCP Vision API)

End-to-end workflow for securely handling AI-generated self-portraits using:

- Base64 encoding
- Google Cloud Vision API
- OAuth2 Application Default Credentials (ADC)
- 403 PERMISSION_DENIED / SERVICE_DISABLED analysis

📂 Project folder: `projects/vision-base64-security-lab/`  
🌐 HTML summary: `projects/vision-base64-security-lab/index.html`

---

## 🧠 Focus Areas

- Cloud Security (GCP) — IAM, APIs, quotas, service enablement  
- API Security — tokens, permissions, structured JSON flows  
- Observability — error logging, response analysis  
- Documentation — clear, bilingual, portfolio-ready  

---

## 👤 About Me

**André Luiz Vieira Bonfim**  
Junior Cybersecurity (Training) · Berlin, Germany  

Languages: **Portuguese, German, English**  
Focus: **Cloud Security, API Security, Governance & Hands-on Learning**

---

## 🇧🇷 Resumo rápido em PT-BR

Este repositório reúne estudos de caso práticos em:

- Segurança em nuvem (Google Cloud)  
- Segurança de APIs e IAM  
- Análise de erros e logs  
- Documentação clara voltada para portfólio internacional  

---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>André Bonfim – Cybersecurity Portfolio</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      margin: 0;
      padding: 32px 16px;
      background: #020617;
      color: #e5e7eb;
      display: flex;
      justify-content: center;
    }
    main {
      width: 100%;
      max-width: 960px;
    }
    h1 { font-size: 2rem; margin-bottom: 6px; }
    h2 { margin-top: 28px; font-size: 1.4rem; }
    h3 { margin-top: 18px; font-size: 1.1rem; }
    p  { color: #9ca3af; line-height: 1.6; }
    a  { color: #60a5fa; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .tagline { color: #9ca3af; margin-bottom: 20px; }
    .section {
      margin-top: 18px;
      padding: 16px 18px;
      border-radius: 12px;
      background: #020819;
      border: 1px solid #111827;
    }
    ul { color: #9ca3af; }
  </style>
</head>
<body>
  <main>
    <h1>André Bonfim – Cybersecurity Portfolio</h1>
    <p class="tagline">
      Junior Cybersecurity (Training) · Berlin · Cloud Security · API Security · Hands-on Labs
    </p>

    <div class="section">
      <h2>🌟 Featured Project</h2>
      <h3>Vision Base64 Security Lab — AI Portraits (GCP Vision API)</h3>
      <p>
        End-to-end workflow for securely handling AI-generated self-portraits using Base64 encoding,
        Google Cloud Vision API and OAuth2 (Application Default Credentials), with a strong focus on
        cloud security and real-world error analysis (403 PERMISSION_DENIED / SERVICE_DISABLED).
      </p>
      <p>
        <strong>Skills:</strong> Vision API, Base64, OAuth2 (ADC), Cloud Security, STRIDE Threat Modeling,
        Bash, JSON, API Troubleshooting
      </p>
      <p>
        <a href="projects/vision-base64-security-lab/index.html">🔗 Open case study</a>
      </p>
    </div>

    <div class="section">
      <h2>📚 Focus Areas</h2>
      <ul>
        <li>Google Cloud Platform · IAM · APIs · Quotas</li>
        <li>API Security & Authentication (OAuth2, tokens)</li>
        <li>Log analysis, error handling and observability</li>
        <li>Bilingual documentation for global teams</li>
      </ul>
    </div>

    <div class="section">
      <h2>🌐 Contact</h2>
      <p>
        LinkedIn:
        <a href="https://www.linkedin.com/in/a-bonfim-tech/" target="_blank">
          linkedin.com/in/a-bonfim-tech
        </a><br />
        GitHub:
        <a href="https://github.com/a-bonfim-tech" target="_blank">
          github.com/a-bonfim-tech
        </a>
      </p>
    </div>
  </main>
</body>
</html>

---

<svg width="260" height="40" viewBox="0 0 260 40" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0f172a"/>
      <stop offset="1" stop-color="#1d4ed8"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" rx="8" ry="8" width="259" height="39"
        fill="url(#bg)" stroke="#1e293b" stroke-width="1"/>
  <circle cx="18" cy="20" r="6" fill="#22c55e"/>
  <circle cx="18" cy="20" r="9" fill="none" stroke="rgba(34,197,94,0.4)" stroke-width="2"/>
  <text x="34" y="24" fill="#e5e7eb"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
        font-size="13">
    Vision Base64 Security Lab
  </text>
</svg>

---

# 🔍 Vision Base64 Security Lab — AI Portraits Case Study

<p align="left">
  <img src="../../assets/vision-base64-security-lab-badge.svg" width="260" alt="Vision Base64 Security Lab Badge" />
</p>

<p align="left">
  <img src="https://img.shields.io/badge/Cloud-Google%20Cloud-blue?logo=googlecloud&logoColor=white" />
  <img src="https://img.shields.io/badge/API-Vision%20API-orange?logo=googlecloud&logoColor=white" />
  <img src="https://img.shields.io/badge/Security-Cloud%20IAM-red?logo=googlecloud&logoColor=white" />
  <img src="https://img.shields.io/badge/Workflow-Base64-lightgrey" />
  <img src="https://img.shields.io/badge/Language-Bash-green?logo=gnu-bash&logoColor=white" />
</p>

> 🇬🇧 English first — scroll down for 🇧🇷 PT-BR.

---

## 1. Executive Overview (EN)

This directory contains an **authorial, security-focused case study** inspired by the Google Cloud Skills Boost lab:

> Detect Labels, Faces, and Landmarks in Images with the Cloud Vision API (GSP037)

Key differences:

- Uses **three AI-generated self-portraits** (kept local for privacy).
- Converts them into **Base64** for Vision API requests.
- Builds **manual JSON requests** for `LABEL_DETECTION` and `FACE_DETECTION`.
- Uses OAuth2 Application Default Credentials (ADC) for authentication.
- Captures and documents **403 PERMISSION_DENIED / SERVICE_DISABLED** errors due to quota/project configuration.
- Structures everything as a **portfolio-grade, auditable Cloud Security lab**.

Even under quota restrictions, the **workflow and reasoning are technically correct** and reflect realistic constraints.

---

## 2. Directory Layout

```text
projects/vision-base64-security-lab/
├── README.md
├── index.html
├── images/
│   └── README-images.md
├── requests/
│   ├── request-andre1.json
│   ├── request-andre2.json
│   └── request-andre3.json
├── responses/
│   ├── response-andre1-error.json
│   ├── response-andre2-error.json
│   └── response-andre3-error.json
└── scripts/
    └── generate_requests_example.sh
```

---

## 3. Architecture Overview

```text
AI Portraits (local, private)
        ↓
 Base64 Encoding (local)
        ↓
 Vision API JSON Requests
        ↓
 OAuth2 Access Token (ADC)
        ↓
 Vision API (LABEL + FACE)
        ↓
 403 Error Responses logged in /responses
```

---

## 4. Skills Demonstrated

### Cloud & Infrastructure

- Google Cloud IAM and service enablement  
- Vision API (`LABEL_DETECTION` + `FACE_DETECTION`)  
- OAuth2 Application Default Credentials (ADC)  
- Quota project troubleshooting and error analysis  

### Security Engineering

- Secure handling of AI-generated portrait data (**no raw images in Git**)  
- Clear separation between images, requests, responses and scripts  
- Threat modeling using the **STRIDE** framework  
- Minimal exposure of credentials and sensitive material  

### DevOps / Automation

- Bash scripting for request generation  
- Reproducible JSON-based workflows  
- Structured logging of error responses in `/responses`  

---

## 5. Threat Modeling (STRIDE)

| Threat                 | Mitigation                                                                 |
|------------------------|----------------------------------------------------------------------------|
| Spoofing               | Only OAuth2 tokens from `gcloud` are used; no API keys.                    |
| Tampering              | JSON requests generated from controlled files and scripts.                 |
| Repudiation            | Error responses stored in `/responses` as an audit trail.                  |
| Information Disclosure | No biometric images or raw tokens committed; placeholders only.            |
| Denial of Service      | 403 failures captured and documented, tied to quota / ADC configuration.  |
| Elevation of Privilege | No service accounts or long-lived secrets are exposed.                     |

---

## 6. Hands-on Flow (EN)

### 6.1 Project layout (Cloud Shell)

```bash
mkdir -p ~/vision-base64-security-lab/{images,requests,responses,scripts}
cd ~/vision-base64-security-lab
```

### 6.2 Image handling (local)

```bash
cd images
base64 -w 0 andre1.png > andre1.base64
base64 -w 0 andre2.png > andre2.base64
base64 -w 0 andre3.png > andre3.base64
```

### 6.3 Authentication & ADC

```bash
gcloud auth application-default login
PROJECT_ID=$(gcloud config get-value project)
gcloud auth application-default set-quota-project "$PROJECT_ID"
ACCESS_TOKEN=$(gcloud auth application-default print-access-token)
```

### 6.4 API call example

```bash
curl -s -X POST \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json; charset=utf-8" \
  https://vision.googleapis.com/v1/images:annotate \
  --data-binary @requests/request-andre1.json \
  > responses/response-andre1-error.json
```

---

## 7. Summary for Hiring Managers

This case demonstrates:

- Ability to design and document a **secure, auditable cloud workflow**.  
- Comfort with **ADC, IAM and API errors** instead of just “happy path” demos.  
- Careful handling of **sensitive/biometric-like data** in public repos.  
- Bilingual, clear documentation aligned with international teams.  

---

## 🇧🇷 Versão resumida em PT-BR

Este estudo de caso mostra:

- Uso da Vision API com imagens geradas por IA e Base64.  
- Autenticação via ADC e análise de erros 403.  
- Separação clara entre dados sensíveis (mantidos locais) e artefatos públicos.  
- Documentação em inglês e português, voltada para portfólio profissional.  

---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Vision Base64 Security Lab – Case Study</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      margin: 0;
      padding: 32px 16px;
      background: #020617;
      color: #e5e7eb;
      display: flex;
      justify-content: center;
    }
    main {
      width: 100%;
      max-width: 900px;
    }
    h1 { font-size: 1.9rem; margin-bottom: 8px; }
    h2 { margin-top: 24px; font-size: 1.3rem; }
    p  { color: #9ca3af; line-height: 1.6; }
    pre {
      background: #020819;
      border-radius: 10px;
      border: 1px solid #111827;
      padding: 10px 12px;
      overflow-x: auto;
      font-size: 0.85rem;
    }
    ul { color: #9ca3af; }
    a  { color: #60a5fa; text-decoration: none; }
    a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <main>
    <h1>Vision Base64 Security Lab — AI Portraits Case Study</h1>
    <p>
      This page summarizes the security-focused workflow implemented using Google Cloud Vision API,
      Base64-encoded AI portraits, and OAuth2 Application Default Credentials.
    </p>

    <h2>Architecture</h2>
    <pre>AI Portraits (local only)
      ↓
Base64 Encoding
      ↓
Vision API JSON Requests
      ↓
OAuth2 Access Token (ADC)
      ↓
Vision API (LABEL + FACE)
      ↓
403 Error Responses logged in /responses
    </pre>

    <h2>Key Security Principles</h2>
    <ul>
      <li>No raw biometric images stored in this repository.</li>
      <li>Only Base64 placeholders and JSON requests are committed.</li>
      <li>403 error responses are preserved as evidence of real-world ADC/quota issues.</li>
    </ul>

    <h2>Full Documentation</h2>
    <p>See the complete Markdown version in <code>README.md</code> in this folder.</p>
  </main>
</body>
</html>

---

# Images — Vision Base64 Security Lab

This folder is used for **local-only** AI-generated portraits (`andre1.png`, `andre2.png`, `andre3.png`).

The raw images are **not** committed to the public repository to avoid publishing biometric-like content.

They are converted to Base64 locally and referenced through placeholders in the JSON requests.

---

{
  "requests": [
    {
      "image": {
        "content": "BASE64_PLACEHOLDER_ANDRE1"
      },
      "features": [
        { "type": "LABEL_DETECTION", "maxResults": 5 },
        { "type": "FACE_DETECTION", "maxResults": 3 }
      ]
    }
  ]
}

---

{
  "requests": [
    {
      "image": {
        "content": "BASE64_PLACEHOLDER_ANDRE2"
      },
      "features": [
        { "type": "LABEL_DETECTION", "maxResults": 5 },
        { "type": "FACE_DETECTION", "maxResults": 3 }
      ]
    }
  ]
}

---

{
  "requests": [
    {
      "image": {
        "content": "BASE64_PLACEHOLDER_ANDRE3"
      },
      "features": [
        { "type": "LABEL_DETECTION", "maxResults": 5 },
        { "type": "FACE_DETECTION", "maxResults": 3 }
      ]
    }
  ]
}

---

{
  "error": {
    "code": 403,
    "status": "PERMISSION_DENIED",
    "message": "Quota project missing in Application Default Credentials for Vision API.",
    "details": [
      {
        "reason": "SERVICE_DISABLED",
        "service": "vision.googleapis.com"
      }
    ]
  }
}

---

{
  "error": {
    "code": 403,
    "status": "PERMISSION_DENIED",
    "message": "Vision API cannot be called because the ADC quota project is not configured.",
    "details": [
      {
        "reason": "SERVICE_DISABLED",
        "service": "vision.googleapis.com"
      }
    ]
  }
}

---

{
  "error": {
    "code": 403,
    "status": "PERMISSION_DENIED",
    "message": "The ADC used does not have an associated quota project.",
    "details": [
      {
        "reason": "SERVICE_DISABLED",
        "service": "vision.googleapis.com"
      }
    ]
  }
}

---

#!/usr/bin/env bash
set -e

echo "Example script – demonstrates how Base64 assets would be converted into Vision API requests."
echo "Real Base64 content is kept local for privacy."

for i in 1 2 3; do
  echo "Simulating generation of request-andre${i}.json..."
done
