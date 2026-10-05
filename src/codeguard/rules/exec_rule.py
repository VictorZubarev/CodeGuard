import ast

from codeguard.models import Finding

def check_exec(node):
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id == "exec":
            return Finding(
                rule="CG004",
                severity="HIGH",
                message="Use of exec() can execute arbitrary Python code.",
                line=node.lineno,
            )

    return None