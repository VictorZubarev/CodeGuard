import ast

def check_os_system(node):
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Attribute):
            if (
                isinstance(node.func.value, ast.Name)
                and node.func.value.id == "os"
                and node.func.attr == "system"
            ):
                return {
                    "rule": "CG002",
                    "severity": "HIGH",
                    "message": "Use of os.system() can execute operating system commands.",
                    "line": node.lineno,
                }

    return None





