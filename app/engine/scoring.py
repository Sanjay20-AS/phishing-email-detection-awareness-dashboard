"""Combine independent signals into a 0-100 explainable risk score."""
from .config import RISK_LABELS

def classify(score: int) -> str:
    for low, high, label in RISK_LABELS:
        if low <= score <= high:
            return label
    return "HIGH RISK / LIKELY PHISHING"

def calculate_risk(content, urls, sender) -> dict:
    raw = content["score"] + urls["score"] + sender["score"]
    # A small bonus makes multiple independent signals matter more.
    signal_count = sum(bool(x["reasons"]) for x in (content, urls, sender))
    bonus = min(8, max(0, signal_count - 1) * 3)
    score = min(100, raw + bonus)
    reasons = content["reasons"] + urls["reasons"] + sender["reasons"]
    if not reasons:
        reasons = ["No strong phishing indicators were detected by the current rules."]
    return {
        "score": score,
        "classification": classify(score),
        "reasons": reasons,
        "components": {
            "content": content["score"],
            "urls": urls["score"],
            "sender": sender["score"],
            "multi_signal_bonus": bonus,
        },
    }
