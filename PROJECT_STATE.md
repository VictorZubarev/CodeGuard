# CodeGuard — Current Project State

## Project

CodeGuard is an open-source security analyzer for Python code.

The long-term goal is to analyze source code and dependencies,
detect security vulnerabilities, explain findings, and help developers
fix security problems.

CodeGuard is intended to become a real long-term open-source project,
not a temporary portfolio project.

## Current Stage

Security Analyzer — `v0.2.0` released.

The first public MVP release, `v0.1.0`, has been published on GitHub.

The current development version includes eight security rules,
rule metadata, severity filtering, automated tests, CI, and updated
project documentation.

The `v0.2.0` release has been published on GitHub.

## Completed

### Project Foundation

- GitHub repository created and made public
- Git repository initialized
- GitHub remote configured
- README.md created and maintained
- PROJECT_PLAN.md created
- ROADMAP.md created and maintained
- CHANGELOG.md created and maintained
- PROJECT_STATE.md created and maintained
- .gitignore created
- pyproject.toml created
- Python 3.14 development environment configured
- Editable package installation configured
- Apache License 2.0 added
- GitHub Actions CI configured
- `v0.1.0` Git tag created
- `v0.1.0` GitHub release published

### CodeGuard Architecture

- Python package structure created under `src/codeguard`
- Security rules separated into individual modules
- Central `RULES` registry created
- AST-based source-code analysis implemented
- Scan statistics collected during scanning
- Rule metadata defined with IDs, names, severity levels,
  descriptions, CWE identifiers, and recommendations

### Security Rules

- `CG001` — unsafe `eval()` usage (`CRITICAL`)
- `CG002` — `os.system()` usage (`HIGH`)
- `CG003` — `subprocess` with `shell=True` (`HIGH`)
- `CG004` — unsafe `exec()` usage (`CRITICAL`)
- `CG005` — possible hardcoded secret (`HIGH`)
- `CG006` — potentially unsafe pickle deserialization (`HIGH`)
- `CG007` — potentially unsafe `yaml.load()` usage (`HIGH`)
- `CG008` — weak cryptographic hash algorithms, including MD5 and SHA-1 (`MEDIUM`)

These rules detect potentially dangerous code patterns.
A finding does not automatically prove that a vulnerability is exploitable.

### Testing

- pytest configured and working
- Positive and negative test coverage for security rules
- Safe subprocess usage has negative tests
- Directory scanning has automated test coverage
- CLI error handling has automated test coverage
- Invalid Python syntax during directory scanning has automated test coverage
- `subprocess` detection covers `shell=True`, `shell=False`,
  missing `shell` arguments, and multiple supported functions
- Hardcoded secret detection has positive and negative test coverage
- Pickle deserialization detection has positive and negative test coverage
- YAML loading detection has positive and negative test coverage
- Weak hash detection has positive and negative test coverage
- Severity assignments have regression test coverage
- CLI severity filtering has test coverage
- Current test suite contains 43 tests
- Latest reported test run passed: 43/43

### CLI

CodeGuard can be launched with:

    py -3.14 -m codeguard.main scan <path>

The CLI can:

- scan individual Python files
- scan directories recursively
- display security findings
- show rule IDs and severity levels
- show finding messages, file paths, and line numbers
- display CWE identifiers and remediation recommendations
- report a clear error when the specified path does not exist
- report the number of scanned files
- report the total number of findings
- report findings grouped by severity
- display a report when no security findings are detected
- filter findings using `--severity`

The severity filter specifies a minimum level.
For example, `--severity HIGH` includes `HIGH` and `CRITICAL` findings.

### Directory Scanning

Directory scanning is implemented.

CodeGuard automatically skips:

- `.git`
- `.venv`
- `__pycache__`
- `build`
- `dist`

When scanning a directory, CodeGuard continues analyzing other Python files
if an individual file contains invalid Python syntax.

### Continuous Integration

GitHub Actions CI is configured.

The CI workflow:

- runs on pushes
- runs on pull requests
- installs the project
- installs pytest
- runs the test suite

### Documentation

The project includes:

- README.md
- PROJECT_STATE.md
- PROJECT_PLAN.md
- ROADMAP.md
- CHANGELOG.md
- LICENSE

The documentation is being updated to reflect the current implementation
and the planned `v0.2.0` release.

## Current Task

The `v0.2.0` release has been published.

The next task is to plan and implement `v0.3.0`, focusing on meaningful
security-analysis improvements, appropriate tests, and documentation.
## Next Planned Improvements

Potential areas for future work include:

- improved command-injection detection
- SQL injection detection research
- reduction of false positives
- investigation of false negatives
- JSON and SARIF reporting
- improved analyzer architecture
- dependency security analysis
- data-flow analysis
- taint analysis

New rules should include appropriate tests and documentation.

## Long-Term Direction

CodeGuard may gradually develop into a developer-focused security platform with:

- source-code analysis
- dependency security analysis
- data-flow and taint analysis
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

A long-term research direction is security analysis of AI-generated Python code, including:

- vulnerability detection
- false-positive reduction
- false-negative analysis
- automated remediation
- reproducible security benchmarking
- comparison of different detection approaches

Any future research claims should be supported by reproducible methods
and verifiable results.

## Development Principle

Every significant feature should have:

- a clear technical purpose
- appropriate automated tests
- documentation where appropriate
- a traceable Git history

Important development decisions, features, releases, research work,
and real-world usage should be recorded in the project history.

## Repository Status

The GitHub repository is public.

The first public MVP release, `v0.1.0`, has been created and published.

The `v0.2.0` release remains in development.

The repository, source code, tests, documentation, Git history,
Git tags, and GitHub releases are the primary record of the project.

## Recovery Instructions

If the development chat is lost, use this file as the current project state.

The source code in the GitHub repository is the source of truth.

To continue development in a new chat, provide the GitHub repository
and review:

- PROJECT_STATE.md
- PROJECT_PLAN.md
- ROADMAP.md
- CHANGELOG.md

Then continue from the `Current Task` section above.
