"""Main orchestration layer for the phishing detector."""
from .text_analyzer import analyze_content
from .url_analyzer import analyze_urls
from .sender_analyzer import analyze_sender
from .scoring import calculate_risk

def analyze_email(sender: str, subject: str, body: str) -> dict:
    content = analyze_content(subject, body)
    urls = analyze_urls(f"{subject}\n{body}")
    sender_result = analyze_sender(sender)
    risk = calculate_risk(content, urls, sender_result)
    return {
        "sender": sender,
        "subject": subject,
        "body": body,
        "content_analysis": content,
        "url_analysis": urls,
        "sender_analysis": sender_result,
        "risk": risk,
    }
