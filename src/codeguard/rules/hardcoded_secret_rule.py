import ast
SECRET_NAMES = {
    "api_key",
    "apikey",
    "secret",
    "secret_key",
    "password",
    "passwd",
    "token",
    "access_token",
    "auth_token",
}
def check_hardcoded_secret(node):
    if not isinstance(node, ast.Assign):
        return None
    if not isinstance(node.value, ast.Constant):
        return None
    if not isinstance(node.value.value, str):
        return None
    for target in node.targets:
        if not isinstance(target, ast.Name):
            continue
        if target.id.lower() not in SECRET_NAMES:
            continue
        return {
            "rule": "CG005",
            "severity": "HIGH",
            "message": "Possible hardcoded secret detected.",
            "line": node.lineno,
        }
    return None