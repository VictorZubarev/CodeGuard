import ast

from codeguard.models import Finding

SECRET_KEYWORDS = {
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

IGNORED_SECRET_VALUES = {
    "",
    "password",
    "secret",
    "changeme",
    "your_password",
    "your_api_key",
    "your_token",
}

def _looks_like_secret_name(name):
    normalized_name = name.lower()

    if normalized_name in SECRET_KEYWORDS:
        return True

    parts = normalized_name.split("_")

    return any(
        part in {"password", "passwd", "secret", "token"}
        for part in parts
    )

def check_hardcoded_secret(node):
    if not isinstance(node, ast.Assign):
        return None

    if not isinstance(node.value, ast.Constant):
        return None

    if not isinstance(node.value.value, str):
        return None

    secret_value = node.value.value.strip()

    if secret_value.lower() in IGNORED_SECRET_VALUES:
        return None

    for target in node.targets:
        if not isinstance(target, ast.Name):
            continue

        if not _looks_like_secret_name(target.id):
            continue

        return Finding(
            rule="CG005",
            severity="HIGH",
            message="Possible hardcoded secret detected.",
            line=node.lineno,
        )

    return None