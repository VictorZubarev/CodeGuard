# CodeGuard — Current Project State

## Project

CodeGuard is an open-source security analyzer for Python code.

The long-term goal is to analyze source code and dependencies,
detect security vulnerabilities, explain findings, and help developers
fix security problems.

CodeGuard is intended to become a real long-term open-source project,
not a temporary portfolio project.

## Current stage

Security analyzer MVP — early development.

## Completed

### Project foundation

- GitHub repository created
- Git repository initialized
- GitHub remote configured
- README created
- PROJECT_PLAN.md created
- ROADMAP.md created
- CHANGELOG.md created
- .gitignore created
- pyproject.toml created
- Python 3.14 development environment configured
- Virtual environment created
- Editable package installation configured

### CodeGuard architecture

- Python package structure created under `src/codeguard`
- Security rules separated into individual modules
- Central RULES registry created
- AST-based source-code analysis implemented

### Security rules

- CG001 — unsafe `eval()` usage
- CG002 — `os.system()` usage
- CG003 — `subprocess` with `shell=True`

### Testing

- pytest configured and working
- Tests for all current security rules created
- Safe subprocess usage has a negative test
- Current test suite passes

### CLI

CodeGuard can be launched with:

    py -3.14 -m codeguard.main scan <path>

The CLI can:

- scan individual Python files
- scan directories recursively
- display security findings
- show rule ID
- show severity
- show message
- show affected file
- show affected line

### Directory scanning

Directory scanning is implemented.

CodeGuard automatically skips:

- `.git`
- `.venv`
- `__pycache__`
- `build`
- `dist`

This prevents the analyzer from scanning its own virtual environment
and build/cache files.

## Current task

Continue improving the CodeGuard security analyzer.

The immediate development direction is:

1. verify directory scanning;
2. commit and push the directory-scanning changes;
3. improve CLI behavior;
4. add more security rules;
5. improve tests and reduce false positives.

## Next planned security rules

Potential next rules include:

- `exec()`
- hardcoded secrets
- unsafe deserialization
- dangerous YAML usage
- SQL injection patterns
- improved command-injection detection

Rules should be added together with tests and documented in the changelog
when appropriate.

## Long-term direction

CodeGuard is planned to gradually develop into a developer-focused
security platform with:

- source-code analysis
- dependency security analysis
- data-flow / taint analysis
- security findings with severity levels
- useful remediation suggestions
- verification of fixes
- GitHub integration
- CI/CD integration
- GitHub Action
- SARIF reporting
- documentation website
- possible VS Code integration
- research and benchmarking of AI-generated Python code

## Research direction

A long-term research direction is the security analysis of
AI-generated Python code, including:

- vulnerability detection
- false-positive reduction
- false-negative analysis
- automated remediation
- security benchmarking
- comparison of different detection approaches

Potential future research may lead to technical publications.

## Development principle

Every significant feature should have:

- a clear technical purpose;
- tests;
- documentation where appropriate;
- a traceable Git history.

Important development decisions, features, releases, research work,
and real-world usage should be preserved in the project history.

## Recovery instructions

If the development chat is lost, use this file as the current project state.

The source code in the GitHub repository is the source of truth.

To continue development in a new chat, provide the GitHub repository
and ask the assistant to read:

- PROJECT_STATE.md
- PROJECT_PLAN.md
- ROADMAP.md
- CHANGELOG.md

Then continue from the "Current task" section above.