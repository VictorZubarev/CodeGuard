# CodeGuard — Current Project State

## Project

CodeGuard is an open-source security analyzer for Python code.

The long-term goal is to analyze source code and dependencies,
detect security vulnerabilities, explain findings, and help developers
fix security problems.

CodeGuard is intended to become a real long-term open-source project,
not a temporary portfolio project.

## Current Stage

Security Analyzer MVP — `v0.1.0` released.

The first public MVP release has been published on GitHub.

The core analyzer, CLI, tests, CI, documentation, and project licensing
are in place.

## Completed

### Project Foundation

- GitHub repository created
- Git repository initialized
- GitHub remote configured
- README created and updated for the MVP release
- PROJECT_PLAN.md created
- ROADMAP.md created
- CHANGELOG.md created and updated for `v0.1.0`
- .gitignore created
- pyproject.toml created
- Python 3.14 development environment configured
- Virtual environment created
- Editable package installation configured
- Apache License 2.0 added

### CodeGuard Architecture

- Python package structure created under `src/codeguard`
- Security rules separated into individual modules
- Central `RULES` registry created
- AST-based source-code analysis implemented
- Scan statistics are collected during scanning

### Security Rules

- `CG001` — unsafe `eval()` usage
- `CG002` — `os.system()` usage
- `CG003` — `subprocess` with `shell=True`
- `CG004` — unsafe `exec()` usage
- `CG005` — possible hardcoded secrets

### Testing

- pytest configured and working
- Tests for all five security rules created
- Positive and negative test coverage for security rules
- Safe subprocess usage has negative tests
- Directory scanning has automated test coverage
- CLI error handling has automated test coverage
- Invalid Python syntax during directory scanning has automated test coverage
- `subprocess` security detection has positive and negative test coverage
- Tests cover `shell=True`, `shell=False`, and missing `shell` arguments
- Tests cover multiple supported `subprocess` functions
- Hardcoded secret detection has positive and negative test coverage
- Current test suite contains 27 tests
- Current test suite passes: 27/27

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
- report a clear error when the specified path does not exist
- report the number of scanned files
- report the total number of findings
- report findings grouped by severity
- display a report when no security findings are detected

### Directory Scanning

Directory scanning is implemented.

CodeGuard automatically skips:

- `.git`
- `.venv`
- `__pycache__`
- `build`
- `dist`

This prevents the analyzer from scanning its own virtual environment
and build/cache files.

When scanning a directory, CodeGuard continues analyzing other Python files
if an individual file contains invalid Python syntax.

### Continuous Integration

GitHub Actions CI is configured.

The CI workflow:

- runs on pushes;
- runs on pull requests;
- installs the project;
- installs pytest;
- runs the test suite.

### Documentation

The project currently includes:

- README.md
- PROJECT_STATE.md
- PROJECT_PLAN.md
- ROADMAP.md
- CHANGELOG.md
- LICENSE

The README contains installation instructions,
usage examples, supported security rules, development instructions,
and project direction.

## Current Task

Prepare the CodeGuard MVP for the first public release.

The immediate release-preparation tasks are:

1. keep project documentation consistent with the current implementation;
2. review the roadmap and development plan;
3. verify the complete test suite;
4. verify the CLI behavior;
5. review the README and examples;
6. verify the repository is clean;
7. create the `v0.1.0` Git tag;
8. prepare the GitHub release;
9. make the repository public when the MVP is ready.

## Next Planned Security Rules

Potential next rules include:

- unsafe deserialization
- dangerous YAML usage
- SQL injection patterns
- improved command-injection detection
- additional hardcoded credential patterns

Rules should be added together with tests and documented in the changelog
when appropriate.

## Long-Term Direction

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

## Research Direction

A long-term research direction is the security analysis of
AI-generated Python code, including:

- vulnerability detection
- false-positive reduction
- false-negative analysis
- automated remediation
- security benchmarking
- comparison of different detection approaches

Potential future research may lead to technical publications.

## Development Principle

Every significant feature should have:

- a clear technical purpose;
- tests;
- documentation where appropriate;
- a traceable Git history.

Important development decisions, features, releases, research work,
and real-world usage should be preserved in the project history.

## Repository Status

The GitHub repository is public.

The first public MVP release, `v0.1.0`, has been created and published.

The repository, GitHub release, Git tag, source code, tests,
documentation, and Git history are the primary record of the project.

## Recovery Instructions

If the development chat is lost, use this file as the current project state.

The source code in the GitHub repository is the source of truth.

To continue development in a new chat, provide the GitHub repository
and ask the assistant to read:

- PROJECT_STATE.md
- PROJECT_PLAN.md
- ROADMAP.md
- CHANGELOG.md

Then continue from the `Current Task` section above.