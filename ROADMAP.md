# CodeGuard Roadmap

## Phase 1 — Foundation

- [x] Create GitHub repository
- [x] Make the repository public
- [x] Initialize Git
- [x] Create initial README
- [x] Create project plan
- [x] Create project structure
- [x] Set up Python development environment
- [x] Configure editable package installation
- [x] Add automated tests
- [x] Add Apache License 2.0
- [x] Add GitHub Actions CI

## Phase 2 — Security Analyzer MVP

- [x] Implement Python source-code scanning
- [x] Detect unsafe `eval()` usage (`CG001`)
- [x] Detect `os.system()` usage (`CG002`)
- [x] Detect `subprocess` with `shell=True` (`CG003`)
- [x] Detect unsafe `exec()` usage (`CG004`)
- [x] Detect potential hardcoded secrets (`CG005`)
- [x] Add severity levels
- [x] Add security reports
- [x] Add recursive directory scanning
- [x] Skip virtual environments and build/cache directories
- [x] Handle invalid Python syntax during directory scanning
- [x] Add scan statistics
- [x] Add CLI error handling
- [x] Add positive and negative security-rule tests
- [x] Reach 27 passing automated tests
- [x] Prepare MVP documentation
- [x] Create `v0.1.0` Git tag
- [x] Publish the `v0.1.0` GitHub release
- [x] Publish the repository

## Phase 3 — Detection Quality and Rule Expansion

- [x] Add unsafe deserialization detection (`CG006`)
- [x] Add dangerous YAML loading detection (`CG007`)
- [x] Add weak cryptographic hash detection (`CG008`)
- [x] Introduce rule metadata with descriptions, CWE identifiers, and recommendations
- [x] Classify `eval()` and `exec()` findings as `CRITICAL`
- [x] Improve hardcoded credential detection for compound variable names and placeholder values
- [x] Add regression tests for all rule severity assignments
- [x] Add CLI severity filtering with `--severity`
- [x] Reach 42 passing automated tests
- [ ] Improve command-injection detection
- [ ] Investigate SQL injection patterns
- [ ] Reduce false positives
- [ ] Investigate false negatives
- [ ] Improve analyzer architecture
- [ ] Improve reporting
- [ ] Add machine-readable JSON output
- [ ] Investigate dependency analysis
- [ ] Investigate data-flow analysis
- [ ] Investigate taint analysis

## Phase 4 — Developer Integrations

- [ ] GitHub integration
- [ ] GitHub Action improvements
- [ ] CI/CD integrations
- [ ] SARIF reporting
- [ ] Documentation website
- [ ] Investigate VS Code integration

## Phase 5 — Security Research

- [ ] Build a reproducible security benchmark
- [ ] Collect AI-generated Python code samples
- [ ] Define security evaluation methodology
- [ ] Measure detection accuracy
- [ ] Study false positives and false negatives
- [ ] Investigate automated remediation
- [ ] Compare different detection approaches
- [ ] Document reproducible research results
- [ ] Prepare research publication

## Phase 6 — Long-term Ecosystem

- [ ] Expand the open-source contributor community
- [ ] Improve developer experience
- [ ] Add advanced security analysis capabilities
- [ ] Develop additional integrations
- [ ] Evaluate professional and enterprise-oriented features

## Roadmap Principle

The roadmap is intentionally incremental.

New capabilities should be added only when the core analyzer,
test coverage, documentation, and maintainability are sufficiently mature.

Significant roadmap items should result in traceable code changes,
tests, documentation, and Git history.