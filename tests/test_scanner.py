import ast
from pathlib import Path

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

def test_ignore_subprocess_shell_false(tmp_path):
    test_file = tmp_path / "safe.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.run('echo hello', shell=False)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert findings == []

def test_ignore_subprocess_without_shell(tmp_path):
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
def test_detect_exec(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "exec('print(hello)')\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG004"
    assert findings[0]["severity"] == "HIGH"
    assert findings[0]["line"] == 1

def test_detect_subprocess_popen_shell_true(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.Popen('echo hello', shell=True)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG003"
    assert findings[0]["severity"] == "HIGH"
    assert findings[0]["line"] == 2

def test_detect_subprocess_call_shell_true(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.call('echo hello', shell=True)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG003"
    assert findings[0]["severity"] == "HIGH"
    assert findings[0]["line"] == 2

def test_detect_subprocess_check_output_shell_true(tmp_path):
    test_file = tmp_path / "dangerous.py"
    test_file.write_text(
        "import subprocess\n"
        "subprocess.check_output('echo hello', shell=True)\n",
        encoding="utf-8",
    )

    findings = scan_file(str(test_file))

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG003"
    assert findings[0]["severity"] == "HIGH"
    assert findings[0]["line"] == 2

def test_ignore_os_system_on_other_object():
    source = """
class Example:
    def system(self, command):
        pass

obj = Example()
obj.system("ls")
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert findings == []

def test_ignore_eval_on_other_object():
    source = """
class Example:
    def eval(self, value):
        return value

obj = Example()
obj.eval("test")
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert findings == []

def test_ignore_exec_on_other_object():
    source = """
class Example:
    def exec(self, value):
        return value

obj = Example()
obj.exec("test")
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert findings == []        \

def test_ignore_other_object_run_shell_true():
    source = """
class Example:
    def run(self, command, shell=False):
        pass

obj = Example()
obj.run("ls", shell=True)
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert findings == []

def test_detect_hardcoded_api_key():
    source = """
API_KEY = "secret-api-key"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG005"
    assert findings[0]["severity"] == "HIGH"

def test_detect_hardcoded_password():
    source = """
PASSWORD = "super-secret-password"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG005"
    assert findings[0]["severity"] == "HIGH"

def test_ignore_normal_string_variable():
    source = """
message = "hello"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert findings == []

def test_ignore_username_variable():
    source = """
username = "admin"
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
    assert findings[0]["rule"] == "CG005"

def test_detect_token():
    source = """
token = "secret-token-value"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert len(findings) == 1
    assert findings[0]["rule"] == "CG005"

def test_ignore_empty_password():
    source = """
PASSWORD = ""
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert findings == []

def test_ignore_generic_password_value():
    source = """
PASSWORD = "password"
"""

    file_path = Path("test.py")
    file_path.write_text(source, encoding="utf-8")

    findings = scan_file(file_path)

    assert findings == []







