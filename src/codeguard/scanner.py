import ast

from codeguard.rules import RULES

def scan_file(file_path):
    findings = []

    with open(file_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    tree = ast.parse(source_code, filename=file_path)

    for node in ast.walk(tree):
        for rule in RULES:
            finding = rule(node)

            if finding is not None:
                findings.append(finding)

    return findings