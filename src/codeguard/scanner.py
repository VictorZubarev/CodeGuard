import ast

from codeguard.rules.eval_rule import check_eval
from codeguard.rules.os_system_rule import check_os_system

def scan_file(file_path):
    findings = []

    with open(file_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    tree = ast.parse(source_code, filename=file_path)

    for node in ast.walk(tree):
        finding = check_eval(node)

        if finding is not None:
            findings.append(finding)

        finding = check_os_system(node)

        if finding is not None:
            findings.append(finding)
    return findings