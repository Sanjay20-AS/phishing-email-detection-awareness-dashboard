# Project Report — Phishing Email Detection & Awareness Dashboard

## 1. Abstract

Phishing is a major social-engineering threat in which attackers use deceptive messages to influence recipients into revealing information, opening unsafe content, transferring money, or taking other harmful actions. This project presents a defensive Phishing Email Detection & Awareness Dashboard that analyzes synthetic email samples using explainable security heuristics.

The system examines email content, sender patterns and URL characteristics, combines the signals into a risk score, classifies the email into risk bands, explains the indicators and stores historical results for analytics. An optional local machine-learning baseline uses TF-IDF and Logistic Regression on a small synthetic dataset.

## 2. Problem statement

Users often receive emails that look urgent, official or familiar. A simple keyword check is not enough because phishing can combine multiple social-engineering techniques. A lightweight educational system can help demonstrate how different indicators contribute to a security decision.

## 3. Objectives

1. Detect common phishing indicators.
2. Analyze suspicious URLs without visiting them.
3. Identify social-engineering and urgency language.
4. Analyze sender patterns.
5. Produce an explainable risk score.
6. Store historical analyses.
7. Display security analytics.
8. Teach users how to respond safely.
9. Demonstrate optional machine learning.
10. Maintain a safe defensive scope.

## 4. Scope

### Included
- Synthetic email input
- Safe `.txt` and `.eml` parsing
- Content analysis
- Sender analysis
- URL string analysis
- Risk scoring
- Classification
- SQLite history
- Dashboard
- Awareness material
- Optional ML baseline
- Automated tests

### Excluded
- Sending phishing email
- Credential harvesting
- Real-user targeting
- URL crawling
- Exploitation
- Malware generation
- Unauthorized scanning

## 5. Modules

### Module 1 — Email Input
Accepts sender, subject, body and safe local sample files.

### Module 2 — Content Analyzer
Detects urgency, manipulation and credential-related terms.

### Module 3 — URL Analyzer
Extracts URLs and evaluates their textual properties without making network requests.

### Module 4 — Sender Analyzer
Examines sender structure and suspicious naming patterns.

### Module 5 — Risk Engine
Combines independent scores and produces a 0–100 risk score.

### Module 6 — Explanation Engine
Shows the indicators that contributed to the result.

### Module 7 — Database
Stores analysis history in SQLite.

### Module 8 — Dashboard
Displays counts, average score, classification distribution and score distribution.

### Module 9 — Awareness Center
Provides guidance on red flags, safe verification, MFA and incident response.

### Module 10 — Optional ML
Provides a simple local text-classification baseline.

## 6. Risk scoring

The current educational score is based on:

`Final Score = Content Score + URL Score + Sender Score + Multi-signal Bonus`

The score is capped at 100.

This is intentionally transparent so a student can explain each decision during a viva/interview.

## 7. Technologies

- Python
- Streamlit
- Pandas
- SQLite
- scikit-learn
- Plotly
- BeautifulSoup dependency reserved for future HTML parsing
- pytest
- Git/GitHub

## 8. Testing

Automated tests cover:
- safe message classification
- suspicious credential-request classification
- URL detection
- `.eml` parsing

Manual tests should also cover:
- empty input
- malformed sender
- multiple URLs
- long URL
- `.txt` upload
- `.eml` upload
- repeated dashboard analyses

## 9. Expected outcome

The application demonstrates an end-to-end defensive email-security workflow from sample ingestion to explainable risk scoring, historical analytics and user education.

## 10. Future enhancements

- Parse authorized `Authentication-Results`, SPF, DKIM and DMARC headers.
- Add attachment filename/type risk signals without opening files.
- Add evaluation metrics and train/validation/test splits.
- Compare rule-based and ML predictions.
- Add analyst notes and incident IDs.
- Add SIEM-compatible JSON export.
- Add secure multi-user deployment.

## 11. Conclusion

The project provides a safe and practical demonstration of phishing detection, security analytics, explainability and awareness. It is designed as a portfolio project rather than a production secure email gateway.
