# CodeGuard — Project Plan

## Purpose

CodeGuard is an open-source security analyzer for Python code.

The project aims to help developers detect, understand, and fix
security vulnerabilities in source code and dependencies.

CodeGuard is being developed as a long-term open-source security tool.

## Current Objective

Prepare and release the first stable MVP as `v0.1.0`.

The MVP should provide:

- AST-based Python source-code analysis;
- multiple security rules;
- positive and negative test coverage;
- recursive directory scanning;
- safe handling of invalid Python files;
- a usable command-line interface;
- scan statistics;
- automated CI testing;
- clear documentation;
- an open-source license.

## Development Priorities

### 1. Security Analysis

Continue expanding the security rule set.

Potential areas include:

- unsafe deserialization;
- dangerous YAML usage;
- SQL injection patterns;
- improved command-injection detection;
- additional hardcoded credential patterns.

Every new rule should include:

- a clear security purpose;
- positive test cases;
- negative test cases;
- an appropriate severity;
- documentation where appropriate.

### 2. Detection Quality

Improve the accuracy of CodeGuard by investigating:

- false positives;
- false negatives;
- safe coding patterns;
- limitations of AST-based detection;
- increasingly complex Python code patterns.

### 3. Analyzer Architecture

Gradually improve the internal architecture to support:

- additional rules;
- reusable analysis components;
- structured findings;
- more advanced code analysis;
- future data-flow and taint analysis.

### 4. CLI

Continue improving the command-line interface with:

- clearer reports;
- useful error handling;
- additional output formats;
- configurable scanning options;
- machine-readable output in the future.

### 5. Testing and Quality

Maintain automated testing as the project grows.

Future testing should include:

- broader rule coverage;
- regression tests;
- false-positive cases;
- false-negative cases;
- integration tests;
- CLI tests;
- performance testing where appropriate.

### 6. Developer Integrations

After the core analyzer becomes sufficiently mature, investigate:

- GitHub integration;
- CI/CD integration;
- GitHub Action;
- SARIF reporting;
- possible VS Code integration.

### 7. Dependency Security

A future development area is security analysis of Python dependencies.

Potential capabilities include:

- dependency discovery;
- known-vulnerability detection;
- dependency risk reporting;
- integration with existing vulnerability databases.

## Research Direction

A long-term research direction is the security analysis of
AI-generated Python code.

Potential research areas include:

- vulnerability detection;
- false-positive and false-negative analysis;
- automated remediation;
- security benchmarking;
- comparison of different detection approaches;
- evaluation of security weaknesses in AI-generated code.

Research work should be based on reproducible experiments,
documented methodology, and measurable results.

Potential future research may lead to technical publications.

## Release Strategy

The project will use versioned releases.

The first public MVP release is planned as:

- Version: `0.1.0`
- Focus: core Python security analysis and CLI
- Distribution: GitHub repository
- License: Apache License 2.0

Future releases should contain meaningful, tested improvements.

## Development Principle

Every significant feature should:

- have a clear technical purpose;
- include appropriate tests;
- be documented where necessary;
- be traceable through Git history.

The project should prioritize real technical progress,
reproducibility, and maintainability over artificial metrics.

## Long-term Vision

The long-term goal is to develop CodeGuard into a useful
developer-focused security platform capable of analyzing source code,
dependencies, and increasingly complex security patterns.

Advanced capabilities such as data-flow analysis, remediation,
integrations, and AI-generated code security research should be added
gradually as the core analyzer matures.