# Changelog

All notable changes to CodeGuard will be documented here.

## Unreleased

### Added

- Added `CG004` to detect unsafe `exec()` usage.
- Added `CG005` to detect possible hardcoded secrets.
- Added automated CLI error-handling test.
- Added directory-scanning test coverage.
- Added handling for Python files with invalid syntax during directory scanning.

### Improved

- CLI now reports a clear error when the specified path does not exist.
- Directory scanning continues when an individual Python file contains invalid syntax.

### Testing

- Expanded the test suite to 14 tests.
- Added positive and negative test coverage for security rules and scanning behavior.
- Added additional test coverage for `subprocess` command execution patterns, including `Popen()`, `call()`, and `check_output()` with `shell=True`.
- Added negative test coverage for `subprocess` usage with `shell=False` and without the `shell` argument.
- Added positive and negative test coverage for hardcoded secret detection.