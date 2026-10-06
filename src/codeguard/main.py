import argparse
from collections import Counter

from codeguard.scanner import scan_path_with_stats

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
            findings, files_scanned = scan_path_with_stats(args.path)
        except FileNotFoundError as error:
            print(f"Error: {error}")
            return

        print("CodeGuard Security Report")
        print()

        if not findings:
            print("No security findings.")
            print()
            print("Summary:")
            print(f"Files scanned: {files_scanned}")
            print("Findings: 0")
            return

        for finding in findings:
            print(
                f"[{finding.severity}] "
                f"{finding.rule} — "
                f"{finding.message}"
            )
            print(f"File: {finding.file}")
            print(f"Line: {finding.line}")
            print(f"CWE: {finding.metadata.cwe}")
            print(
                f"Recommendation: "
                f"{finding.metadata.recommendation}"
            )
            print()

        severity_counts = Counter(
            finding.severity
            for finding in findings
        )

        print("Summary:")
        print(f"Files scanned: {files_scanned}")
        print(f"Findings: {len(findings)}")

        for severity, count in severity_counts.items():
            print(f"{severity}: {count}")

if __name__ == "__main__":
    main()