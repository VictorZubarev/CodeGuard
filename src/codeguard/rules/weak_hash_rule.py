import ast

from codeguard.models import Finding

WEAK_HASHES = {
    "md5",
    "sha1",
}

def check_weak_hash(node):
    if not isinstance(node, ast.Call):
        return None

    if not isinstance(node.func, ast.Attribute):
        return None

    if not isinstance(node.func.value, ast.Name):
        return None

    if node.func.value.id != "hashlib":
        return None

    if node.func.attr not in WEAK_HASHES:
        return None

    return Finding(
        rule="CG008",
        severity="MEDIUM",
        message="Use of weak cryptographic hash algorithm can be insecure.",
        line=node.lineno,
    )


