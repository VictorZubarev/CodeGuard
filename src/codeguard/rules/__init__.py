from codeguard.rules.eval_rule import check_eval
from codeguard.rules.os_system_rule import check_os_system

RULES = [
    check_eval,
    check_os_system,
]