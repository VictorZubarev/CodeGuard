from dataclasses import dataclass

@dataclass
class Finding:
    rule: str
    severity: str
    message: str
    line: int
    file: str | None = None