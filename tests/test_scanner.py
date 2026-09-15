from codeguard.scanner import scan_file

def test_detect_eval():
    findings = scan_file("tests/vulnerable_example.py")

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG001"
    assert findings[0]["severity"] == "HIGH"
    assert findings[0]["line"] == 3

def test_detect_os_system(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import os\n"
        "os.system('echo hello')\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG002"
    assert findings[0]["severity"] == "HIGH"
    assert findings[0]["line"] == 2







