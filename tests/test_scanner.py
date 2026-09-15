from codeguard.scanner import scan_file

def test_detect_eval():
    findings = scan_file("tests/vulnerable_example.py")

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG001"
    assert findings[0]["severity"] == "HIGH"
    assert findings[0]["line"] == 3