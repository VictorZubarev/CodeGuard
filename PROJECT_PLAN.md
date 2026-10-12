# CodeGuard — Project Plan

## Purpose

CodeGuard is an open-source security analyzer for Python code.

The project aims to help developers detect, understand, and fix
security vulnerabilities in source code and, in the future, dependencies.

CodeGuard is being developed as a long-term open-source security tool.

The project prioritizes real technical progress, reproducible results,
maintainability, and useful security analysis over artificial metrics.

## Current Objective

Complete and release `v0.2.0`.

The first public MVP release, `v0.1.0`, has already been published.

The current development version includes:

- AST-based Python source-code analysis;
- eight security rules (`CG001`–`CG008`);
- structured rule metadata;
- severity levels;
- severity filtering in the CLI;
- recursive directory scanning;
- handling of invalid Python syntax during directory scanning;
- scan statistics and security recommendations;
- automated tests;
- GitHub Actions CI;
- project documentation;
- Apache License 2.0.

The `v0.2.0` release must not be considered complete until
the implementation, tests, documentation, package metadata,
and release artifacts have been verified.

## Development Priorities

### 1. Security Analysis

Continue expanding and improving the security rule set.

Current rules cover:

- unsafe `eval()` usage;
- `os.system()` usage;
- `subprocess` calls with `shell=True`;
- unsafe `exec()` usage;
- possible hardcoded secrets;
- potentially unsafe pickle deserialization;
- potentially unsafe YAML loading;
- weak cryptographic hash algorithms.

Potential future areas include:

- SQL injection patterns;
- improved command-injection detection;
- additional hardcoded credential patterns;
- additional unsafe deserialization patterns;
- other common Python security weaknesses.

Every new rule should include:

- a clear security purpose;
- an appropriate rule identifier;
- a justified severity level;
- positive test cases;
- negative test cases;
- regression tests where appropriate;
- relevant CWE references when justified;
- remediation guidance;
- documentation where appropriate.

Findings should describe potentially dangerous patterns accurately.
A detected pattern does not automatically prove exploitability.

### 2. Detection Quality

Improve the accuracy and reliability of CodeGuard by investigating:

- false positives;
- false negatives;
- safe coding patterns;
- limitations of AST-based detection;
- complex Python syntax and code patterns;
- rule overlap and inconsistent findings.

Changes intended to improve detection quality should be supported
by reproducible tests and clearly documented behavior.

### 3. Analyzer Architecture

Gradually improve the internal architecture to support:

- maintainable rule registration;
- reusable analysis components;
- consistent finding metadata;
- reliable severity handling;
- more advanced code analysis;
- future data-flow and taint analysis.

Architectural changes should reduce complexity and improve maintainability
rather than introduce abstractions without a clear purpose.

### 4. CLI and Reporting

Continue improving the command-line interface with:

- clear and consistent reports;
- useful error handling;
- configurable scanning options;
- severity filtering;
- machine-readable JSON output;
- SARIF reporting in a future release.

Output formats should be tested and documented.

### 5. Testing and Quality

Maintain automated testing as the project grows.

Testing should cover:

- positive and negative rule cases;
- safe coding patterns;
- false-positive regression cases;
- edge cases;
- severity assignments;
- CLI behavior;
- directory scanning;
- malformed or unsupported input;
- integration behavior;
- performance where appropriate.

The test suite should run through the established development workflow
and GitHub Actions CI.

### 6. Developer Integrations

After the core analyzer becomes sufficiently mature, investigate:

- GitHub integration;
- CI/CD integration;
- a dedicated GitHub Action;
- SARIF reporting;
- possible VS Code integration;
- a documentation website.

Integrations should provide practical value and have their own tests
and documentation where appropriate.

### 7. Dependency Security

A future development area is security analysis of Python dependencies.

Potential capabilities include:

- dependency discovery;
- parsing dependency manifests and lockfiles;
- identifying known vulnerable dependency versions;
- dependency risk reporting;
- integration with vulnerability databases;
- clear handling of advisory data and version constraints.

Dependency analysis should be developed as a distinct capability
with its own requirements, tests, and limitations.

## Research Direction

A long-term research direction is security analysis of AI-generated
Python code.

Potential research areas include:

- vulnerability detection;
- false-positive and false-negative analysis;
- automated remediation;
- reproducible security benchmarking;
- comparison of different detection approaches;
- evaluation of security weaknesses in AI-generated code.

Research work should use a documented methodology, reproducible
experiments, measurable outcomes, and clearly stated limitations.

Research claims and publications must be supported by actual results.

## Release Strategy

CodeGuard uses versioned releases.

### Released

- `v0.1.0` — initial public MVP release.

### In Development

- `v0.2.0` — security-rule expansion, rule metadata, severity
  classification, CLI severity filtering, regression coverage,
  and documentation improvements.

A release should be published only after:

- the implementation has been reviewed;
- automated tests pass;
- CLI behavior has been verified;
- package metadata is consistent with the intended version;
- documentation matches the implementation;
- Git changes have been reviewed;
- release notes accurately describe the changes.

Future releases should contain meaningful, tested improvements.

## Development Workflow

For significant changes:

1. Define the problem and expected behavior.
2. Implement the smallest maintainable solution.
3. Add or update automated tests.
4. Run the complete test suite.
5. Review the Git diff and check formatting.
6. Update documentation where necessary.
7. Commit and push verified changes.
8. Record significant decisions and release information.

The GitHub repository and Git history are the primary record
of the project's development.

## Development Principle

Every significant feature should:

- have a clear technical purpose;
- include appropriate tests;
- be documented where necessary;
- be traceable through Git history;
- have known limitations recorded when relevant.

The project should prioritize real technical progress,
reproducibility, and maintainability over artificial metrics.

## Long-term Vision

The long-term goal is to develop CodeGuard into a useful
developer-focused security platform capable of analyzing source code,
dependencies, and increasingly complex security patterns.

Advanced capabilities such as data-flow analysis, taint analysis,
remediation, integrations, and AI-generated code security research
should be added gradually as the core analyzer matures.