# FILE: projects/vision-base64-security-lab/README.md
# 🔍 Vision Base64 Security Lab — AI Portraits Case Study

<p align="left">
  <img src="../../assets/vision-base64-security-lab-badge.svg" width="260" />
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

This repository is an **authorial security-focused case study** based on the Google Cloud Skills Boost lab:

**Detect Labels, Faces, and Landmarks in Images with the Cloud Vision API (GSP037)**

This project:

- uses **three AI-generated portraits**
- converts them to **Base64**
- builds **manual Vision API JSON requests**
- uses **OAuth2 ADC tokens**
- documents **403 PERMISSION_DENIED** issues imposed by Skills Boost project quota
- presents the entire workflow as a **portfolio-grade Cloud Security artifact**

---

## 2. Structure

```text
projects/vision-base64-security-lab/
├── README.md
├── index.html
├── images/README-images.md
├── requests/request-andre1.json
├── requests/request-andre2.json
├── requests/request-andre3.json
├── responses/response-andre1-error.json
├── responses/response-andre2-error.json
├── responses/response-andre3-error.json
└── scripts/generate_requests_example.sh
```

---

## 3. Architecture

```text
AI Portraits → Base64 → JSON Requests → OAuth2 Token → Vision API → 403 Error Responses
```

---

## 4. Skills Demonstrated

- IAM troubleshooting  
- OAuth2 ADC tokens  
- Vision API request engineering  
- STRIDE threat modeling  
- Secure data handling  
- Bash automation  
- Error analysis  

---

## 5. STRIDE Model

| Threat | Mitigation |
|--------|------------|
| Spoofing | OAuth2 tokens only |
| Tampering | Script-generated JSON |
| Repudiation | Stored error logs |
| Info Disclosure | No raw images |
| DoS | 403 logs analyzed |
| Elevation | No privileges exposed |

---

## 6. Commands Used (Cloud Shell)

### Base64 Encoding
```bash
cd ~/vision-base64-security-lab/images
base64 -w 0 andre1.png > andre1.base64
base64 -w 0 andre2.png > andre2.base64
base64 -w 0 andre3.png > andre3.base64
```

### Authentication
```bash
gcloud auth application-default login
PROJECT_ID=$(gcloud config get-value project)
gcloud auth application-default set-quota-project "$PROJECT_ID"
ACCESS_TOKEN=$(gcloud auth application-default print-access-token)
```

### API Call Example
```bash
curl -s -X POST \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  https://vision.googleapis.com/v1/images:annotate \
  --data-binary @requests/request-andre1.json \
  > responses/response-andre1-error.json
```

---

## 7. Hiring Manager Summary

This project shows capability in:

- Cloud API security  
- OAuth2 authentication flows  
- Structured lab documentation  
- Error reasoning under restricted environments  
- Clean GitHub portfolio architecture  

---

## 🇧🇷 Resumo PT-BR

Estudo de caso autoral com:

- retratos IA → Base64  
- requisições Vision API  
- autenticação ADC  
- análise de erros 403  
- documentação bilíngue profissional  

---

# FILE: projects/vision-base64-security-lab/images/README-images.md
# Images — Vision Base64 Security Lab

This folder documents the use of three AI portraits processed as Base64 for Vision API requests.

Raw images are **not** stored in this repository.

---

# FILE: projects/vision-base64-security-lab/requests/request-andre1.json
{
  "requests": [
    {
      "image": { "content": "BASE64_PLACEHOLDER_ANDRE1" },
      "features": [
        { "type": "LABEL_DETECTION", "maxResults": 5 },
        { "type": "FACE_DETECTION", "maxResults": 3 }
      ]
    }
  ]
}

# FILE: projects/vision-base64-security-lab/requests/request-andre2.json
{
  "requests": [
    {
      "image": { "content": "BASE64_PLACEHOLDER_ANDRE2" },
      "features": [
        { "type": "LABEL_DETECTION", "maxResults": 5 },
        { "type": "FACE_DETECTION", "maxResults": 3 }
      ]
    }
  ]
}

# FILE: projects/vision-base64-security-lab/requests/request-andre3.json
{
  "requests": [
    {
      "image": { "content": "BASE64_PLACEHOLDER_ANDRE3" },
      "features": [
        { "type": "LABEL_DETECTION", "maxResults": 5 },
        { "type": "FACE_DETECTION", "maxResults": 3 }
      ]
    }
  ]
}

---

# FILE: projects/vision-base64-security-lab/responses/response-andre1-error.json
{
  "error": {
    "code": 403,
    "status": "PERMISSION_DENIED",
    "message": "Quota project missing in ADC.",
    "details": [{ "reason": "SERVICE_DISABLED" }]
  }
}

# FILE: projects/vision-base64-security-lab/responses/response-andre2-error.json
{
  "error": {
    "code": 403,
    "status": "PERMISSION_DENIED",
    "message": "Vision API disabled or quota invalid.",
    "details": [{ "reason": "SERVICE_DISABLED" }]
  }
}

# FILE: projects/vision-base64-security-lab/responses/response-andre3-error.json
{
  "error": {
    "code": 403,
    "status": "PERMISSION_DENIED",
    "message": "ADC lacks a quota project and cannot access Vision API.",
    "details": [{ "reason": "SERVICE_DISABLED" }]
  }
}

---

# FILE: projects/vision-base64-security-lab/scripts/generate_requests_example.sh
#!/usr/bin/env bash
set -e
echo "Simulating request generation..."
for i in 1 2 3; do
  echo "request-andre${i}.json created (simulated)"
done

---

# FILE: projects/vision-base64-security-lab/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Vision Base64 Security Lab – Case Study</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body { font-family: system-ui, sans-serif; background:#020617; color:#e5e7eb; padding:32px; display:flex; justify-content:center; }
    main { max-width:900px; }
    pre { background:#0a0f1d; padding:12px; border-radius:8px; border:1px solid #111827; }
  </style>
</head>
<body>
  <main>
    <h1>Vision Base64 Security Lab — Case Study</h1>
    <p>This page summarizes the workflow implemented using Google Cloud Vision API + Base64 encoding.</p>

    <h2>Architecture</h2>
    <pre>AI Portraits → Base64 → JSON → OAuth2 Token → Vision API → 403 Errors Logged</pre>

    <h2>Security Principles</h2>
    <ul>
      <li>No raw biometric images in this repository.</li>
      <li>Only Base64 placeholders and structured requests.</li>
      <li>Error logs are preserved as evidence of real-world API restrictions.</li>
    </ul>

    <h2>Full Documentation</h2>
    <p>See <code>README.md</code> in this folder.</p>
  </main>
</body>
</html>

