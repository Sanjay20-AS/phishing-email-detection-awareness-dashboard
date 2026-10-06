# 🛡️ Phishing Email Detection & Awareness Dashboard

A beginner-friendly, defensive cybersecurity project for detecting phishing indicators in synthetic email samples and explaining why a message may be risky.

## What it demonstrates

- Phishing and social-engineering fundamentals
- Email content analysis
- URL risk indicators **without visiting URLs**
- Sender-pattern analysis
- Explainable rule-based scoring
- Optional TF-IDF + Logistic Regression baseline
- SQLite analysis history
- Security analytics dashboard
- Phishing-awareness education
- Safe `.txt` / `.eml` parsing
- Unit testing
- GitHub-ready documentation

## Safety scope

This project is intentionally defensive.

It does **not**:
- send emails
- open/crawl submitted URLs
- collect credentials
- create credential-harvesting pages
- attack real systems
- perform domain impersonation
- use real victim data

Use synthetic samples and reserved/example domains such as `example.test`.

## Architecture

```text
                     ┌──────────────────────────┐
                     │      Streamlit UI        │
                     │ Analyze / Dashboard /    │
                     │ Awareness / About        │
                     └────────────┬─────────────┘
                                  │
                         ┌────────▼────────┐
                         │ Detection Engine│
                         └────────┬────────┘
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
       Content Analyzer      URL Analyzer       Sender Analyzer
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  ▼
                         Explainable Scoring
                                  │
                         ┌────────▼────────┐
                         │ Classification  │
                         └────────┬────────┘
                                  ▼
                       SQLite + Analytics
                                  │
                                  ▼
                           Awareness Tips

Optional:
Synthetic Dataset → TF-IDF → Logistic Regression → Local model
```

## Risk bands

| Score | Classification |
|---:|---|
| 0–19 | SAFE |
| 20–39 | LOW RISK |
| 40–69 | SUSPICIOUS |
| 70–100 | HIGH RISK / LIKELY PHISHING |

The score is an educational heuristic, not a production email gateway verdict.

## Project structure

```text
phishing-email-detection-awareness-dashboard/
├── app/
│   ├── engine/
│   │   ├── config.py
│   │   ├── text_analyzer.py
│   │   ├── url_analyzer.py
│   │   ├── sender_analyzer.py
│   │   ├── scoring.py
│   │   ├── eml_parser.py
│   │   └── detector.py
│   ├── database.py
│   ├── ml_model.py
│   └── main.py
├── data/synthetic_emails.csv
├── models/
├── tests/
├── docs/
├── screenshots/
├── train_model.py
├── requirements.txt
└── README.md
```

## Run locally

### 1. Create a virtual environment

Windows PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app/main.py
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Start the dashboard

```powershell
python -m streamlit run app/main.py
```

Open the local address shown by Streamlit.

### 4. Run tests

```powershell
python -m pytest -q
```

### 5. Optional ML baseline

```powershell
python train_model.py
```

The model is saved locally under `models/`. It is ignored by Git by default because generated model artifacts can be large.

## How detection works

### Content analysis
Looks for:
- urgency
- account suspension threats
- credential requests
- OTP/password language
- payment/gift-card manipulation
- alarmist formatting

### URL analysis
Looks at the URL string only:
- HTTP instead of HTTPS
- IP-address destinations
- `@` in URL authority
- link shorteners
- suspicious TLDs
- excessive subdomains
- very long URLs
- security-themed domain words

### Sender analysis
Looks at:
- missing/invalid domain
- free-mail provider use
- role/security keywords
- unusual characters
- unusually long local-parts

None of these indicators proves that a message is malicious. The engine combines signals and explains them.

## GitHub strategy

Recommended repository name:

`phishing-email-detection-awareness-dashboard`

Suggested commits:

1. `chore: initialize project structure`
2. `feat: add synthetic phishing dataset`
3. `feat: implement content and sender analyzers`
4. `feat: add safe URL analyzer`
5. `feat: add explainable risk scoring`
6. `feat: add SQLite history`
7. `feat: build Streamlit dashboard`
8. `feat: add awareness center`
9. `test: add detection engine tests`
10. `docs: add project report and screenshots`

Never commit:
- real emails
- credentials
- `.env`
- API keys
- private company data
- database files containing sensitive data

## LinkedIn / portfolio positioning

Example project bullet:

> Built a defensive phishing-email detection and awareness dashboard using Python, Streamlit and SQLite, combining explainable content, sender and URL heuristics with risk scoring, analysis history, security analytics and an optional TF-IDF/Logistic Regression baseline.

## Limitations

This is a student/portfolio system, not a replacement for Microsoft Defender, Proofpoint, Mimecast, secure email gateways, SIEM/SOAR, sandboxing, SPF/DKIM/DMARC validation, threat-intelligence feeds, or enterprise mail telemetry.

Future improvements:
- SPF/DKIM/DMARC header parsing from authorized samples
- attachment metadata analysis
- better IDN/homograph detection
- calibrated ML evaluation
- precision/recall/F1 reporting
- SHAP/LIME explanations
- SIEM export
- role-based access
- secure deployment
- larger authorized datasets
