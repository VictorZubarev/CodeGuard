import ast

def scan_file(file_path):
    findings = []

    with open(file_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    tree = ast.parse(source_code, filename=file_path)

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "eval":
                findings.append(
                    {
                        "rule": "CG001",
                        "severity": "HIGH",
                        "message": "Use of eval() can execute arbitrary Python code.",
                        "line": node.lineno,
                    }
                )

    return findings