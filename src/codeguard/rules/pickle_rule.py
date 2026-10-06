import ast

from codeguard.models import Finding

PICKLE_FUNCTIONS = {
    "loads",
    "load",
}

def check_pickle(node):
    if not isinstance(node, ast.Call):
        return None

    if not isinstance(node.func, ast.Attribute):
        return None

    if not isinstance(node.func.value, ast.Name):
        return None

    if node.func.value.id != "pickle":
        return None

    if node.func.attr not in PICKLE_FUNCTIONS:
        return None

    return Finding(
        rule="CG006",
        severity="HIGH",
        message="Use of pickle.load() or pickle.loads() can execute arbitrary code when processing untrusted data.",
        line=node.lineno,
    )





