from pathlib import Path

from codeguard.scanner import scan_file, scan_path

def test_detect_eval():
    findings = scan_file("tests/vulnerable_example.py")

    assert len(findings) == 1
    assert findings[0].rule == "CG001"
    assert findings[0].severity == "HIGH"
    assert findings[0].line == 3

def test_detect_os_system(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import os\n"
        "os.system('echo hello')\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG002"
    assert findings[0].severity == "HIGH"
    assert findings[0].line == 2

def test_detect_subprocess_shell_true(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.run('echo hello', shell=True)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG003"
    assert findings[0].severity == "HIGH"
    assert findings[0].line == 2

def test_safe_code(tmp_path):
    test_file = tmp_path / "safe.py"
    test_file.write_text(
        "print('hello')\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert findings == []

def test_safe_subprocess_without_shell(tmp_path):
    test_file = tmp_path / "safe.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.run(['echo', 'hello'])\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert findings == []

def test_directory_scanning(tmp_path):
    project_dir = tmp_path / "project"
    project_dir.mkdir()

    dangerous_file = project_dir / "dangerous.py"
    dangerous_file.write_text(
        "eval('1 + 1')\n",
        encoding="utf-8",
    )

    safe_file = project_dir / "safe.py"
    safe_file.write_text(
        "print('hello')\n",
        encoding="utf-8",
    )

    findings = scan_path(project_dir)

    assert len(findings) == 1
    assert findings[0].rule == "CG001"

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
    assert findings[0].rule == "CG002"

def test_directory_scanning_excludes_git(tmp_path):
    project_dir = tmp_path / "project"
    project_dir.mkdir()

    dangerous_file = project_dir / "dangerous.py"
    dangerous_file.write_text(
        "eval('1 + 1')\n",
        encoding="utf-8",
    )

    git_dir = project_dir / ".git"
    git_dir.mkdir()

    excluded_file = git_dir / "dangerous.py"
    excluded_file.write_text(
        "eval('1 + 1')\n",
        encoding="utf-8",
    )

    findings = scan_path(project_dir)

    assert len(findings) == 1
    assert findings[0].rule == "CG001"

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
    assert findings[0].rule == "CG002"

def test_detect_exec(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "exec('print(hello)')\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG004"
    assert findings[0].severity == "HIGH"
    assert findings[0].line == 1

def test_safe_exec_as_attribute(tmp_path):
    test_file = tmp_path / "safe.py"
    test_file.write_text(
        "obj.exec('hello')\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert findings == []

def test_detect_subprocess_popen_shell_true(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.Popen('echo hello', shell=True)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG003"

def test_detect_subprocess_call_shell_true(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.call('echo hello', shell=True)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG003"

def test_detect_subprocess_check_call_shell_true(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.check_call('echo hello', shell=True)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG003"

def test_detect_subprocess_check_output_shell_true(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.check_output('echo hello', shell=True)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG003"

def test_safe_subprocess_shell_false(tmp_path):
    test_file = tmp_path / "safe.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.run('echo hello', shell=False)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert findings == []

def test_safe_subprocess_without_shell_argument(tmp_path):
    test_file = tmp_path / "safe.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.run('echo hello')\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert findings == []

def test_detect_hardcoded_api_key():
    source = """
API_KEY = "secret-api-key"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert len(findings) == 1
    assert findings[0].rule == "CG005"
    assert findings[0].severity == "HIGH"

def test_detect_hardcoded_password():
    source = """
PASSWORD = "super-secret-password"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert len(findings) == 1
    assert findings[0].rule == "CG005"
    assert findings[0].severity == "HIGH"

def test_ignore_placeholder_password():
    source = """
PASSWORD = "password"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert findings == []

def test_ignore_empty_secret():
    source = """
API_KEY = ""
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert findings == []

def test_ignore_common_placeholder_secret():
    source = """
TOKEN = "changeme"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert findings == []

def test_detect_lowercase_api_key():
    source = """
api_key = "secret-api-key"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert len(findings) == 1
    assert findings[0].rule == "CG005"

def test_detect_token():
    source = """
token = "secret-token-value"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert len(findings) == 1
    assert findings[0].rule == "CG005"

def test_safe_variable_name():
    source = """
username = "admin"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert findings == []

def test_detect_pickle_loads(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import pickle\n"
        "data = pickle.loads(user_data)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG006"
    assert findings[0].severity == "HIGH"
    assert findings[0].line == 2

def test_detect_pickle_load(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import pickle\n"
        "data = pickle.load(file_object)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG006"
    assert findings[0].severity == "HIGH"
    assert findings[0].line == 2

def test_safe_non_pickle_load(tmp_path):
    test_file = tmp_path / "safe.py"
    test_file.write_text(
        "data = json.loads(user_data)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert findings == []   

def test_detect_yaml_load(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import yaml\n"
        "data = yaml.load(user_data)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG007"
    assert findings[0].severity == "HIGH"
    assert findings[0].line == 2

def test_safe_yaml_safe_load(tmp_path):
    test_file = tmp_path / "safe.py"
    test_file.write_text(
        "import yaml\n"
        "data = yaml.safe_load(user_data)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert findings == []

def test_safe_non_yaml_load(tmp_path):
    test_file = tmp_path / "safe.py"
    test_file.write_text(
        "data = json.load(file_object)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert findings == []

def test_detect_md5(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import hashlib\n"
        "digest = hashlib.md5(data)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG008"
    assert findings[0].severity == "MEDIUM"
    assert findings[0].line == 2

def test_detect_sha1(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import hashlib\n"
        "digest = hashlib.sha1(data)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0].rule == "CG008"
    assert findings[0].severity == "MEDIUM"
    assert findings[0].line == 2

def test_safe_sha256(tmp_path):
    test_file = tmp_path / "safe.py"
    test_file.write_text(
        "import hashlib\n"
        "digest = hashlib.sha256(data)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert findings == []






 