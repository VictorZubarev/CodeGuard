from codeguard.rules.eval_rule import check_eval
from codeguard.rules.os_system_rule import check_os_system
from codeguard.rules.subprocess_rule import check_subprocess

RULES = [
    check_eval,
    check_os_system,
    check_subprocess,
]