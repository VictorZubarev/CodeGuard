import ast

from codeguard.models import Finding

def check_os_system(node):
    if isinstance(node, ast.Call):
        if (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "os"
            and node.func.attr == "system"
        ):
            return Finding(
                rule="CG002",
                severity="HIGH",
                message="Use of os.system() can execute operating system commands.",
                line=node.lineno,
            )

    return None


