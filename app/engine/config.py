"""Central configuration for the defensive phishing detector."""

RISK_LABELS = [
    (0, 19, "SAFE"),
    (20, 39, "LOW RISK"),
    (40, 69, "SUSPICIOUS"),
    (70, 100, "HIGH RISK / LIKELY PHISHING"),
]

URGENCY_TERMS = {
    "urgent", "immediately", "act now", "within 24 hours", "final warning",
    "account suspended", "verify now", "last chance", "expires today",
    "respond immediately", "action required", "failure to comply"
}

MANIPULATION_TERMS = {
    "secret", "confidential", "do not tell", "keep this private",
    "gift card", "wire transfer", "payment required", "send money",
    "confirm your password", "share your otp", "security code"
}

CREDENTIAL_TERMS = {
    "password", "passcode", "otp", "one-time password", "login",
    "sign in", "verify your account", "credentials", "security code"
}

SUSPICIOUS_TLDS = {".zip", ".mov", ".click", ".top", ".xyz", ".gq", ".tk"}
FREE_HOSTS = {"bit.ly", "tinyurl.com", "t.co", "is.gd", "cutt.ly"}
