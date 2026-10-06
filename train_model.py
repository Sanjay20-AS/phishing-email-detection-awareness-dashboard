import csv
from app.ml_model import train

rows = []
with open("data/synthetic_emails.csv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        rows.append({"text": f'{r["subject"]}\n{r["body"]}', "label": r["label"]})

model = train(rows)
print("Model trained and saved to models/phishing_text_model.joblib")
