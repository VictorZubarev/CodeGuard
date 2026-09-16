import ast

def check_subprocess(node):
    if not isinstance(node, ast.Call):
        return None

    if not isinstance(node.func, ast.Attribute):
        return None

    if not isinstance(node.func.value, ast.Name):
        return None

    if node.func.value.id != "subprocess":
        return None

    if node.func.attr not in {"run", "Popen", "call", "check_call", "check_output"}:
        return None

    for keyword in node.keywords:
        if keyword.arg == "shell":
            if isinstance(keyword.value, ast.Constant) and keyword.value.value is True:
                return {
                    "rule": "CG003",
                    "severity": "HIGH",
                    "message": "Using subprocess with shell=True can allow command injection.",
                    "line": node.lineno,
                }

    return None





