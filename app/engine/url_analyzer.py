"""Safe URL inspection. No URL is requested, crawled, or opened."""
import re
from urllib.parse import urlparse
from .config import SUSPICIOUS_TLDS, FREE_HOSTS

URL_RE = re.compile(r"https?://[^\s<>\"']+")

def extract_urls(text: str) -> list[str]:
    return URL_RE.findall(text or "")

def analyze_url(url: str) -> dict:
    raw = url.rstrip(".,;:!?)]}")
    parsed = urlparse(raw)
    host = (parsed.hostname or "").lower()
    reasons = []
    score = 0

    if parsed.scheme != "https":
        score += 8
        reasons.append("URL does not use HTTPS.")
    if "@" in parsed.netloc:
        score += 15
        reasons.append("URL contains '@', which can obscure the actual destination.")
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host):
        score += 18
        reasons.append("URL uses an IP address instead of a normal domain.")
    if host in FREE_HOSTS:
        score += 12
        reasons.append(f"URL uses a common link-shortening service ({host}).")
    if any(host.endswith(tld) for tld in SUSPICIOUS_TLDS):
        score += 10
        reasons.append("Domain uses a TLD commonly seen in suspicious samples.")
    if host.count(".") >= 3:
        score += 6
        reasons.append("Domain has many subdomain levels; verify the registered domain.")
    if len(raw) > 120:
        score += 5
        reasons.append("Unusually long URL; inspect the destination carefully.")
    if any(x in host for x in ("login", "verify", "secure", "account", "update")):
        score += 8
        reasons.append("Domain contains a security/account-themed keyword.")

    return {"url": raw, "host": host, "score": min(score, 30), "reasons": reasons}

def analyze_urls(text: str) -> dict:
    urls = extract_urls(text)
    details = [analyze_url(u) for u in urls]
    return {
        "urls": urls,
        "details": details,
        "score": min(sum(d["score"] for d in details), 35),
        "reasons": [r for d in details for r in d["reasons"]][:10],
    }
