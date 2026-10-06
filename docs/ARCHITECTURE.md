# Architecture Notes

## Layers

**Presentation:** `app/main.py`  
Streamlit pages, forms, results and charts.

**Application:** `app/engine/detector.py`  
Coordinates the analysis pipeline.

**Detection:**  
- `text_analyzer.py`
- `url_analyzer.py`
- `sender_analyzer.py`
- `scoring.py`

**Parsing:** `eml_parser.py`  
Local parsing of safe `.eml` samples.

**Persistence:** `database.py`  
SQLite storage.

**ML:** `ml_model.py`  
Optional local baseline.

## Data flow

```text
Input
  |
  +--> Sender Analyzer ----+
  |                         |
  +--> Content Analyzer ---+--> Risk Engine --> Classification
  |                         |                       |
  +--> URL Analyzer -------+                       +--> Explanation
                                                    |
                                                    +--> SQLite
                                                    |
                                                    +--> Dashboard
```

## Threat-model assumptions

The application assumes an analyst/user may paste untrusted text. The design therefore avoids executing message content and never fetches URLs. File parsing is limited to text content from `.txt` and `.eml` samples.

## Production gap

A real email-security platform would need stronger isolation, file scanning, authentication, authorization, centralized logging, monitoring, secret management, rate limiting, secure deployment and comprehensive evaluation.
