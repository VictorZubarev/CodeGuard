import ast
from pathlib import Path

from codeguard.rules import RULES

EXCLUDED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
}

def scan_file(file_path):
    findings = []

    with open(file_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    tree = ast.parse(source_code, filename=file_path)

    for node in ast.walk(tree):
        for rule in RULES:
            finding = rule(node)

            if finding is not None:
                finding["file"] = str(file_path)
                findings.append(finding)

    return findings

def scan_path(path):
    path = Path(path)

    if path.is_file():
        return scan_file(path)

    if path.is_dir():
        findings = []

        for file_path in path.rglob("*.py"):
            if any(
                excluded_directory in file_path.parts
                for excluded_directory in EXCLUDED_DIRECTORIES
            ):
                continue

            try:
                findings.extend(scan_file(file_path))
            except SyntaxError:
                continue

        return findings

    raise FileNotFoundError(f"Path not found: {path}")


