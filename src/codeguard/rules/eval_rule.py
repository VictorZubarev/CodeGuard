import ast

def check_eval(node):
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id == "eval":
            return {
                "rule": "CG001",
                "severity": "HIGH",
                "message": "Use of eval() can execute arbitrary Python code.",
                "line": node.lineno,
            }

    return None



