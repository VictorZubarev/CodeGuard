from codeguard.scanner import scan_file

file_path = "tests/test_vulnerable.py"

findings = scan_file(file_path)

for finding in findings:
    print(f"[{finding['severity']}] {finding['rule']} — {finding['message']}")
    print(f"Line: {finding['line']}")




