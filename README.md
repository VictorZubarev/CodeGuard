# CodeGuard

Open-source security analyzer for Python code.

CodeGuard uses AST-based static analysis to detect potentially dangerous
patterns in Python source code and report security findings with
rule IDs, severity levels, file paths, line numbers, CWE identifiers,
and recommendations.

## Status

Early development — Security Analyzer MVP.

Python security analyzer for detecting common vulnerabilities in Python code.

Latest released version: 0.2.0

## Goal

CodeGuard aims to detect security vulnerabilities in Python source code,
help developers understand security findings, and provide practical
guidance for fixing them.

The project is being developed as a long-term open-source security tool.

## Current Features

CodeGuard currently provides AST-based static analysis for Python code.

### Security Rules

| Rule | Description | Severity | CWE |
|---|---|---|---|
| CG001 | Unsafe `eval()` usage | CRITICAL | CWE-95 |
| CG002 | `os.system()` usage | HIGH | CWE-78 |
| CG003 | `subprocess` with `shell=True` | HIGH | CWE-78 |
| CG004 | Unsafe `exec()` usage | CRITICAL | CWE-95 |
| CG005 | Possible hardcoded secret | HIGH | CWE-798 |
| CG006 | Potentially unsafe `pickle` deserialization | HIGH | CWE-502 |
| CG007 | Potentially unsafe `yaml.load()` usage | HIGH | CWE-502 |
| CG008 | Weak cryptographic hash algorithms, including MD5 and SHA-1 | MEDIUM | CWE-328 |

These rules identify potentially dangerous code patterns. A finding
does not automatically prove that a vulnerability is exploitable.

### Scanning

CodeGuard can:

- scan individual Python files;
- scan directories recursively;
- automatically skip `.git`, `.venv`, `__pycache__`, `build`, and `dist`;
- continue directory scanning when an individual Python file has invalid syntax;
- report rule IDs, severity levels, messages, file paths, and line numbers;
- include CWE identifiers and remediation recommendations;
- report the number of scanned files and findings;
- group findings by severity;
- filter findings by minimum severity.

## Installation

Clone the repository:

    git clone https://github.com/VictorZubarev/CodeGuard.git

Enter the project directory:

    cd CodeGuard

Install CodeGuard in editable mode:

    py -3.14 -m pip install -e .

## Usage

Scan a Python file:

    py -3.14 -m codeguard.main scan path/to/file.py

Scan a directory:

    py -3.14 -m codeguard.main scan path/to/project

### Filter by Severity

Show findings with severity `HIGH` or higher:

    py -3.14 -m codeguard.main scan path/to/project --severity HIGH

Show only `CRITICAL` findings:

    py -3.14 -m codeguard.main scan path/to/project --severity CRITICAL

Available severity levels, from lowest to highest:

- `LOW`
- `MEDIUM`
- `HIGH`
- `CRITICAL`

The `--severity` option sets a minimum severity. For example, `HIGH`
includes both `HIGH` and `CRITICAL` findings.

### Example Output

    CodeGuard Security Report

    [CRITICAL] CG001 — Use of eval() can execute arbitrary Python code.
    File: tests\vulnerable_example.py
    Line: 3
    CWE: CWE-95
    Recommendation: Avoid eval() and use safer alternatives for parsing or evaluating data.

    Summary:
    Files scanned: 1
    Findings: 1
    CRITICAL: 1

When no security findings are detected, CodeGuard reports:

    CodeGuard Security Report

    No security findings.

    Summary:
    Files scanned: 1
    Findings: 0

## Development

Install the project in editable mode:

    py -3.14 -m pip install -e .

Run the test suite:

    py -3.14 -m pytest

The current test suite contains 42 tests covering security rules,
safe cases, severity assignments, directory scanning, CLI behavior,
and invalid Python syntax.

## Continuous Integration

CodeGuard uses GitHub Actions to automatically run the test suite
on pushes and pull requests.

## Project Direction

CodeGuard is planned to gradually expand toward:

- additional Python security rules;
- improved false-positive reduction;
- data-flow and taint analysis;
- dependency security analysis;
- remediation suggestions;
- structured JSON and SARIF reporting;
- GitHub integration;
- CI/CD integration;
- a dedicated GitHub Action;
- a documentation website;
- possible VS Code integration.

A long-term research direction is security analysis of AI-generated
Python code, including vulnerability detection, false-positive and
false-negative analysis, automated remediation, and security benchmarking.

## Development Philosophy

CodeGuard is developed as a real long-term project.

Significant features should have:

- a clear technical purpose;
- automated tests;
- appropriate documentation;
- traceable Git history.

The project source code, tests, documentation, and Git history are
the primary record of development.

## License

CodeGuard is licensed under the Apache License 2.0.
