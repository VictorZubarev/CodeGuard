# Changelog

All notable changes to CodeGuard will be documented here.

## Unreleased

### Added

- Added `CG004` to detect unsafe `exec()` usage.
- Added automated CLI error-handling test.
- Added directory-scanning test coverage.
- Added handling for Python files with invalid syntax during directory scanning.

### Improved

- CLI now reports a clear error when the specified path does not exist.
- Directory scanning continues when an individual Python file contains invalid syntax.

### Testing

- Expanded the test suite to 9 tests.
- Added positive and negative test coverage for security rules and scanning behavior.