from dataclasses import dataclass

@dataclass (frozen=True)
class RuleMetadata:
    rule_id: str
    name: str
    severity: str
    description: str
    cwe: str
    recommendation: str
RULE_METADATA = {
    "CG001": RuleMetadata(
        rule_id="CG001",
        name="Use of eval()",
        severity="CRITICAL",
        description="Detects use of eval(), which can execute arbitrary Python code.",
        cwe="CWE-95",
        recommendation="Avoid eval() and use safer alternatives for parsing or evaluating data.",
    ),
    "CG002": RuleMetadata(
        rule_id="CG002",
        name="Use of os.system()",
        severity="HIGH",
        description="Detects use of os.system(), which can execute operating system commands.",
        cwe="CWE-78",
        recommendation="Use safer process execution APIs and avoid constructing commands from untrusted input.",
    ),
    "CG003": RuleMetadata(
        rule_id="CG003",
        name="subprocess with shell=True",
        severity="HIGH",
        description="Detects subprocess calls using shell=True, which can enable command injection.",
        cwe="CWE-78",
        recommendation="Avoid shell=True when possible and pass command arguments as a list.",
    ),
    "CG004": RuleMetadata(
        rule_id="CG004",
        name="Use of exec()",
        severity="CRITICAL",
        description="Detects use of exec(), which can execute arbitrary Python code.",
        cwe="CWE-95",
        recommendation="Avoid exec() and use safer alternatives.",
    ),
    "CG005": RuleMetadata(
        rule_id="CG005",
        name="Hardcoded secret",
        severity="HIGH",
        description="Detects possible hardcoded secrets stored directly in source code.",
        cwe="CWE-798",
        recommendation="Store secrets in environment variables or a dedicated secret management system.",
    ),
    "CG006": RuleMetadata(
        rule_id="CG006",
        name="Unsafe pickle deserialization",
        severity="HIGH",
        description="Detects pickle.load() and pickle.loads(), which can execute arbitrary code when processing untrusted data.",
        cwe="CWE-502",
        recommendation="Avoid deserializing untrusted data with pickle and use a safer serialization format.",
    ),
    "CG007": RuleMetadata(
        rule_id="CG007",
        name="Unsafe YAML loading",
        severity="HIGH",
        description="Detects yaml.load(), which can be unsafe when processing untrusted data.",
        cwe="CWE-502",
        recommendation="Use yaml.safe_load() when loading untrusted YAML data.",
    ),
    "CG008": RuleMetadata(
        rule_id="CG008",
        name="Weak cryptographic hash",
        severity="MEDIUM",
        description="Detects use of MD5 or SHA-1 cryptographic hash algorithms.",
        cwe="CWE-328",
        recommendation="Use a stronger hash algorithm such as SHA-256 when appropriate.",
    ),
}