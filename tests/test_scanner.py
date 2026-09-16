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

def test_detect_subprocess_shell_true(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.run('echo hello', shell=True)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG003"
    assert findings[0]["severity"] == "HIGH"
    assert findings[0]["line"] == 2

def test_ignore_safe_subprocess(tmp_path):
    test_file = tmp_path / "safe.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.run(['echo', 'hello'])\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert findings == []



