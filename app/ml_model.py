"""Optional local ML baseline using TF-IDF + Logistic Regression.

This model is deliberately a baseline for education. The application remains
fully functional with the explainable rule engine even if the model is absent.
"""
from pathlib import Path
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "phishing_text_model.joblib"

def train(rows):
    texts = [r["text"] for r in rows]
    labels = [r["label"] for r in rows]
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1,2), min_df=1, max_features=3000)),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    model.fit(texts, labels)
    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    return model

def load_model():
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)
    return None

def predict(text):
    model = load_model()
    if not model:
        return None
    pred = model.predict([text])[0]
    probs = model.predict_proba([text])[0]
    return {"label": pred, "confidence": float(max(probs))}
