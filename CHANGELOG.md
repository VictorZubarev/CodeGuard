# Changelog

All notable changes to CodeGuard will be documented here.

## [0.2.0] - 2026-10-13

### Added

- Added `CG006` to detect potentially unsafe `pickle.load()` and `pickle.loads()` usage.
- Added `CG007` to detect potentially unsafe `yaml.load()` usage.
- Added `CG008` to detect weak cryptographic hash algorithms, including MD5 and SHA-1.
- Added rule metadata containing rule IDs, names, severity levels, descriptions, CWE identifiers, and recommendations.
- Added `--severity` CLI option to filter findings by minimum severity level.

### Improved

- Introduced `CRITICAL`, `HIGH`, and `MEDIUM` severity levels.
- Classified unsafe `eval()` and `exec()` usage as `CRITICAL`.
- Improved hardcoded secret detection.
- Expanded regression tests for security rules and CLI behavior.

### Testing

- Expanded the test suite to 43 tests.
- Added coverage for pickle deserialization, YAML loading, and weak cryptographic hashes.
- Added regression coverage for severity assignments and CLI severity filtering.

## [0.1.0] - Initial MVP Release

### Added

- Added `CG001` to detect unsafe `eval()` usage.
- Added `CG002` to detect `os.system()` usage.
- Added `CG003` to detect `subprocess` usage with `shell=True`.
- Added `CG004` to detect unsafe `exec()` usage.
- Added `CG005` to detect possible hardcoded secrets.
- Added recursive directory scanning.
- Added scan statistics to the CLI report.
- Added CLI error handling for missing paths.
- Added handling for Python files with invalid syntax during directory scanning.
- Added GitHub Actions CI for automated testing.
- Added Apache License 2.0.

### Improved

- Directory scanning automatically skips `.git`, `.venv`, `__pycache__`, `build`, and `dist`.
- CLI reports rule ID, severity, message, file, and line number.
- CLI reports the number of scanned files and findings.
- CLI displays a clear report when no security findings are detected.

### Testing

- Expanded the test suite to 27 tests.
- Added positive and negative test coverage for all security rules.
- Added directory-scanning test coverage.
- Added CLI error-handling test coverage.
- Added invalid Python syntax test coverage.
- Added positive and negative test coverage for `subprocess` command execution patterns.
- Added test coverage for `shell=True`, `shell=False`, and missing `shell` arguments.
- Added test coverage for multiple supported `subprocess` functions.
- Added positive and negative test coverage for hardcoded secret detection.
