from app.engine.eml_parser import parse_eml

def test_parse_eml():
    raw = b"From: security@example.test\nSubject: Sample\n\nThis is a synthetic message."
    result = parse_eml(raw)
    assert result["sender"] == "security@example.test"
    assert result["subject"] == "Sample"
    assert "synthetic" in result["body"]
