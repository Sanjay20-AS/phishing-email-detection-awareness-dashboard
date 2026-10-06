"""Analyze sender metadata without contacting the sender domain."""
import re

FREE_EMAIL_DOMAINS = {"gmail.com", "outlook.com", "hotmail.com", "yahoo.com", "proton.me"}

def split_sender(sender: str):
    sender = (sender or "").strip()
    match = re.search(r"<([^>]+)>", sender)
    address = match.group(1) if match else sender
    if "@" not in address:
        return address, ""
    local, domain = address.rsplit("@", 1)
    return local.strip(), domain.lower().strip()

def analyze_sender(sender: str) -> dict:
    local, domain = split_sender(sender)
    reasons = []
    score = 0

    if not domain:
        return {"score": 12, "domain": "", "local_part": local, "reasons": ["Sender address is missing a valid domain."]}

    if domain in FREE_EMAIL_DOMAINS:
        score += 4
        reasons.append("Sender uses a free email provider; this is not malicious by itself, but verify business claims independently.")
    if any(x in local.lower() for x in ("admin", "support", "security", "billing", "verify")):
        score += 5
        reasons.append("Sender local-part uses a role/security keyword; verify the actual organization.")
    if re.search(r"[^a-zA-Z0-9._%+-]", local):
        score += 3
        reasons.append("Sender local-part contains unusual characters.")
    if len(local) > 35:
        score += 3
        reasons.append("Sender local-part is unusually long.")

    return {"score": min(score, 20), "domain": domain, "local_part": local, "reasons": reasons}
