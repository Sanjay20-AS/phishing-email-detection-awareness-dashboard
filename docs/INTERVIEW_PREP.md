# Interview & Viva Preparation

## 1. What did you build?
I built a defensive phishing-email detection and awareness dashboard. It analyzes email content, sender patterns and URL characteristics, then produces an explainable risk score and classification.

## 2. Why did you use rule-based detection?
Rules are transparent and easy to explain. In security, explainability is useful because an analyst should understand why a message was flagged.

## 3. Does an indicator prove phishing?
No. An indicator is a signal, not proof. The system combines multiple signals and recommends independent verification.

## 4. Does the application open URLs?
No. It only parses the URL string. This prevents accidental interaction with potentially unsafe destinations.

## 5. Why SQLite?
SQLite is lightweight, free and sufficient for a local student project. It demonstrates persistence without requiring an external database server.

## 6. Why add machine learning?
The ML module demonstrates feature extraction and classification while keeping the rule engine as the primary explainable detector.

## 7. Why TF-IDF?
TF-IDF converts text into numerical features based on word importance. It is simple, fast and appropriate for a baseline text-classification experiment.

## 8. What would you use in production?
A production system would combine authenticated mail telemetry, SPF/DKIM/DMARC results, reputation data, threat intelligence, attachment analysis, sandboxing, calibrated ML, SIEM/SOAR integration and strong access controls.

## 9. What security principles did you follow?
Least functionality, local processing, no credential collection, no URL fetching, synthetic data, input validation and clear defensive boundaries.

## 10. What is the biggest limitation?
The synthetic dataset and heuristic rules are not representative of enterprise-scale email traffic. A production detector needs rigorous evaluation on a large authorized dataset with precision, recall, F1, false-positive and false-negative analysis.
