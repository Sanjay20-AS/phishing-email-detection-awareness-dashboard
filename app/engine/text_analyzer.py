"""Analyze email text using explainable defensive heuristics."""
import re
from collections import Counter
from .config import URGENCY_TERMS, MANIPULATION_TERMS, CREDENTIAL_TERMS

def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").lower()).strip()

def find_terms(text: str, terms: set[str]) -> list[str]:
    low = normalize(text)
    return sorted({term for term in terms if term in low})

def analyze_content(subject: str, body: str) -> dict:
    combined = f"{subject or ''}\n{body or ''}"
    low = normalize(combined)
    urgency = find_terms(combined, URGENCY_TERMS)
    manipulation = find_terms(combined, MANIPULATION_TERMS)
    credentials = find_terms(combined, CREDENTIAL_TERMS)
    exclamations = combined.count("!")
    caps_words = re.findall(r"\b[A-Z]{4,}\b", combined)
    suspicious_phrases = urgency + manipulation + credentials

    score = 0
    reasons = []
    if urgency:
        score += min(18, 6 + 3 * len(urgency))
        reasons.append(f"Urgency language detected: {', '.join(urgency[:5])}")
    if manipulation:
        score += min(18, 5 + 4 * len(manipulation))
        reasons.append(f"Manipulation/social-engineering language detected: {', '.join(manipulation[:5])}")
    if credentials:
        score += min(20, 5 + 3 * len(credentials))
        reasons.append(f"Credential-related language detected: {', '.join(credentials[:5])}")
    if exclamations >= 3:
        score += 5
        reasons.append("Heavy use of exclamation marks increases pressure/tone risk.")
    if len(caps_words) >= 3:
        score += 4
        reasons.append("Multiple all-caps words may indicate pressure or alarmist wording.")
    if re.search(r"dear (customer|user|member|employee)", low):
        score += 2
        reasons.append("Generic greeting detected; verify whether the sender normally addresses you this way.")

    return {
        "score": min(score, 40),
        "urgency_terms": urgency,
        "manipulation_terms": manipulation,
        "credential_terms": credentials,
        "suspicious_phrases": suspicious_phrases,
        "exclamation_count": exclamations,
        "all_caps_word_count": len(caps_words),
        "reasons": reasons,
    }
