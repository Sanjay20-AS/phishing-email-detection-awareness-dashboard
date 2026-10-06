"""Parse safe .eml samples locally. No network access is performed."""
from email import policy
from email.parser import BytesParser

def parse_eml(raw_bytes: bytes) -> dict:
    msg = BytesParser(policy=policy.default).parsebytes(raw_bytes)
    sender = msg.get("From", "")
    subject = msg.get("Subject", "")
    body_parts = []

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    body_parts.append(part.get_content())
                except Exception:
                    pass
    else:
        try:
            body_parts.append(msg.get_content())
        except Exception:
            pass

    return {"sender": sender, "subject": subject, "body": "\n".join(body_parts).strip()}
