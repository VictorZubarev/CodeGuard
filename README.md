# CodeGuard

Open-source security analyzer for Python code.

CodeGuard uses AST-based static analysis to detect potentially dangerous
patterns in Python source code and report security findings with
rule IDs, severity levels, file paths, and line numbers.

## Status

Early development — Security Analyzer MVP.

Current version: `0.1.0`

## Goal

CodeGuard aims to detect security vulnerabilities in Python source code,
help developers understand security findings, and eventually provide
useful guidance for fixing them.

The project is being developed as a long-term open-source security tool.

## Current Features

CodeGuard currently provides AST-based static analysis for Python code.

### Security Rules

| Rule | Description | Severity |
|---|---|---|
| CG001 | Unsafe `eval()` usage | HIGH |
| CG002 | `os.system()` usage | HIGH |
| CG003 | `subprocess` with `shell=True` | HIGH |
| CG004 | Unsafe `exec()` usage | HIGH |
| CG005 | Possible hardcoded secret | HIGH |

### Scanning

CodeGuard can:

- scan individual Python files;
- scan directories recursively;
- automatically skip `.git`, `.venv`, `__pycache__`, `build`, and `dist`;
- continue directory scanning when an individual Python file has invalid syntax;
- report the rule ID, severity, message, file, and line number;
- report the number of scanned files;
- report the total number of findings;
- group findings by severity.

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

Example output:

    CodeGuard Security Report

    [HIGH] CG001 — Use of eval() can execute arbitrary Python code.
    File: tests\vulnerable_example.py
    Line: 3

    Summary:
    Files scanned: 1
    Findings: 1
    HIGH: 1

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

The current test suite contains 27 tests covering security rules,
safe cases, directory scanning, CLI behavior, and invalid Python syntax.

## Continuous Integration

CodeGuard uses GitHub Actions to automatically run the test suite
on pushes and pull requests.

## Project Direction

CodeGuard is planned to gradually expand toward:

- additional Python security rules;
- improved false-positive reduction;
- dependency security analysis;
- data-flow and taint analysis;
- remediation suggestions;
- GitHub integration;
- CI/CD integration;
- GitHub Action;
- SARIF reporting;
- documentation website;
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

The project source code and Git history are the primary record of development.

## License

CodeGuard is licensed under the Apache License 2.0.