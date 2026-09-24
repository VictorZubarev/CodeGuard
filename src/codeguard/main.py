import argparse

from codeguard.scanner import scan_path

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
        help="Python file or directory to scan.",
    )

    args = parser.parse_args()

    if args.command == "scan":
        try:
            findings = scan_path(args.path)
        except FileNotFoundError as error:
            print(f"Error: {error}")
            return

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
            print(f"File: {finding['file']}")
            print(f"Line: {finding['line']}")
            print()

if __name__ == "__main__":
    main()



