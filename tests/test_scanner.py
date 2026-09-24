from codeguard.scanner import scan_file, scan_path

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

def test_directory_scanning_excludes_venv(tmp_path):
    project_dir = tmp_path / "project"
    project_dir.mkdir()

    dangerous_file = project_dir / "dangerous.py"
    dangerous_file.write_text(
        "import os\n"
        "os.system('echo hello')\n",
        encoding="utf-8",
    )

    venv_dir = project_dir / ".venv"
    venv_dir.mkdir()

    excluded_file = venv_dir / "dangerous.py"
    excluded_file.write_text(
        "import os\n"
        "os.system('echo hello')\n",
        encoding="utf-8",
    )

    findings = scan_path(project_dir)

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG002"
    assert findings[0]["file"] == str(dangerous_file)
def test_scan_file_invalid_syntax(tmp_path):
    test_file = tmp_path / "broken.py"
    test_file.write_text(
        "def broken(:\n"
        "    pass\n",
        encoding="utf-8",
    )

    try:
        scan_file(str(test_file))
    except SyntaxError:
        return

    assert False, "scan_file() should raise SyntaxError for invalid Python"
def test_directory_scanning_skips_invalid_python(tmp_path):
    project_dir = tmp_path / "project"
    project_dir.mkdir()

    dangerous_file = project_dir / "dangerous.py"
    dangerous_file.write_text(
        "import os\n"
        "os.system('echo hello')\n",
        encoding="utf-8",
    )

    broken_file = project_dir / "broken.py"
    broken_file.write_text(
        "def broken(:\n"
        "    pass\n",
        encoding="utf-8",
    )

    findings = scan_path(project_dir)

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG002"
    assert findings[0]["file"] == str(dangerous_file)



