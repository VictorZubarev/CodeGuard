import argparse

from codeguard.scanner import scan_file

def main():
    parser = argparse.ArgumentParser(
        prog="codeguard",
        description="Security analyzer for Python code.",
    )

    parser.add_argument(
        "command",
        choices=["scan"],
        help="Command to execute.",
    )

    parser.add_argument(
        "path",
        help="Python file to scan.",
    )

    args = parser.parse_args()

    if args.command == "scan":
        findings = scan_file(args.path)

        if not findings:
            print("No security findings.")
            return

        print("CodeGuard Security Report")
        print()

        for finding in findings:
            print(
                f"[{finding['severity']}] "
                f"{finding['rule']} — "
                f"{finding['message']}"
            )
            print(f"Line: {finding['line']}")
            print()

if __name__ == "__main__":
    main()








