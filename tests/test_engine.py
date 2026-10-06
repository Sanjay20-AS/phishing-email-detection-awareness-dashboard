from app.engine.detector import analyze_email

def test_safe_sample_has_low_score():
    result = analyze_email(
        "library@example.test",
        "Book renewal successful",
        "Your library book renewal was completed successfully. No further action is required."
    )
    assert result["risk"]["score"] < 40

def test_urgent_credential_request_is_high():
    result = analyze_email(
        "security@example.test",
        "URGENT account verification",
        "Your account will be suspended. Verify your password immediately at https://secure-login.example.test/verify."
    )
    assert result["risk"]["score"] >= 40
    assert result["risk"]["classification"] in {"SUSPICIOUS", "HIGH RISK / LIKELY PHISHING"}

def test_url_analyzer_does_not_fetch():
    result = analyze_email(
        "support@example.test",
        "Check this",
        "Visit http://192.168.1.10/login or https://tinyurl.com/example"
    )
    assert len(result["url_analysis"]["urls"]) == 2
    assert result["url_analysis"]["score"] > 0
