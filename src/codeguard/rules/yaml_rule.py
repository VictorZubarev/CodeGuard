import ast

from codeguard.models import Finding

def check_yaml_load(node):
    if not isinstance(node, ast.Call):
        return None

    if not isinstance(node.func, ast.Attribute):
        return None

    if not isinstance(node.func.value, ast.Name):
        return None

    if node.func.value.id != "yaml":
        return None

    if node.func.attr != "load":
        return None

    return Finding(
        rule="CG007",
        severity="HIGH",
        message="Use of yaml.load() can be unsafe when processing untrusted data.",
        line=node.lineno,
    )


