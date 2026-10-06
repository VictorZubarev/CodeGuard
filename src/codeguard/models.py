from dataclasses import dataclass

@dataclass
class Finding:
    rule: str
    severity: str
    message: str
    line: int
    file: str | None = None

    @property
    def metadata(self):
        from codeguard.rules.metadata import RULE_METADATA

        return RULE_METADATA[self.rule]



