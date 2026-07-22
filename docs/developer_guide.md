# UMICODE Developer Guide

## 1. Introduction

Welcome to the UMICODE developer guide.

This document explains how the UMICODE project is organised, how development is carried out, and the practical steps needed to contribute new code. It is intended both as a reference for the original developers and as a guide for future collaborators.

UMICODE is a research software project. As such, scientific reasoning is considered as important as the code itself. Wherever possible, biological decisions are documented alongside software design decisions.

---

# 2. Development Philosophy

UMICODE is developed using a simple principle:

> **Biology drives the software, not the other way around.**

Every new feature begins with the biological problem that needs to be solved. That problem is translated into software objects, validated with automated tests, documented, and only then extended into algorithms.

The typical development workflow is:

```text
Biological question
        ↓
Design discussion
        ↓
Software specification
        ↓
Implementation
        ↓
Automated tests
        ↓
Documentation
        ↓
Git commit
```

This approach keeps the software closely aligned with the experimental assay while maintaining a clean, maintainable codebase.

---

# 3. Repository Structure

Current project layout:

```text
UMICODE
│
├── README.md
├── CHANGELOG.md
├── LICENCE
├── pyproject.toml
│
├── config/
│   └── default.yaml
│
├── docs/
│   ├── vision.md
│   ├── specification.md
│   └── developer_guide.md
│
├── src/
│   └── umicode/
│       ├── config.py
│       ├── exceptions.py
│       ├── models.py
│       ├── validators.py
│       └── anchor_design.py
│
└── tests/
```

Each module has a single responsibility.

- **config.py** loads configuration.
- **models.py** represents biological objects.
- **validators.py** checks those objects.
- Future modules will contain the design and decoding algorithms.

---

# 4. Development Workflow

The recommended workflow for every new feature is:

1. Discuss the biological problem.
2. Decide how it should be represented computationally.
3. Implement the smallest useful version.
4. Write automated tests.
5. Ensure all tests pass.
6. Commit a coherent piece of work.
7. Update documentation where appropriate.

Large changes should be built from a series of small, tested commits.

---

# 5. Terminal Commands

## Where am I?

```bash
pwd
```

Displays the current working directory.

---

## List files

```bash
ls
```

or

```bash
ls -la
```

The `-la` option also shows hidden files such as `.git` and `.venv`.

---

## Change directory

```bash
cd folder_name
```

Go up one level:

```bash
cd ..
```

---

## Activate the Python virtual environment

```bash
source .venv/bin/activate
```

The prompt should begin with:

```text
(.venv)
```

Deactivate with:

```bash
deactivate
```

---

## Check which Python is being used

```bash
which python
```

The result should point inside the project's `.venv`.

---

## Install the current package

```bash
pip install .
```

At present this project uses a standard installation rather than an editable install. Whenever a new module is added, reinstall the package before running the tests.

Current workflow:

```text
Edit code
      ↓
pip install .
      ↓
pytest
```

---

## Run all tests

```bash
pytest
```

Example:

```text
8 passed
```

Run a single test file:

```bash
pytest tests/test_models.py
```

---

# 6. Git Workflow

Check repository status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Describe the change"
```

Upload to GitHub:

```bash
git push
```

Download updates:

```bash
git pull
```

Commits should represent one logical change wherever possible.

---

# 7. Testing Philosophy

Every important module should have a corresponding test.

For example:

```text
models.py
        ↓
test_models.py
```

Tests are expected to pass before committing changes.

Testing is intended to provide confidence when new features are added rather than merely increasing code coverage.

---

# 8. Project Architecture

The software mirrors the experimental workflow.

```text
Configuration
        │
        ▼
Load configuration
        │
        ▼
Create biological objects
        │
        ▼
Validate objects
        │
        ▼
Design anchors
        │
        ▼
Generate candidate UMIs
        │
        ▼
Filter candidate UMIs
        │
        ▼
Construct left/right codebooks
        │
        ▼
Simulate sequencing
        │
        ▼
Decode UMIs
        │
        ▼
Integrate VDJ sequence information
        │
        ▼
Final molecular assignment
```

The intention is that every software component has a direct biological interpretation.

---

# 9. Coding Principles

The following principles guide development:

- Prefer clarity over cleverness.
- Keep functions small and focused.
- Document *why* decisions were made, not only *what* the code does.
- Separate configuration from implementation.
- Separate biological concepts from algorithms.
- Build incrementally.
- Write tests early.
- Keep commits small and meaningful.

---

# 10. Troubleshooting

Common problems include:

**`ModuleNotFoundError`**

If a new module has been added:

```bash
pip install .
```

before running `pytest`.

---

**Tests fail**

Run:

```bash
pytest
```

Read the first error carefully before making changes.

---

**Unsure what changed**

Run:

```bash
git status
```

This is often the quickest way to understand the current state of the repository.

---

# 11. Roadmap

The planned architecture is:

```text
Configuration
      ↓
Models
      ↓
Validation
      ↓
Anchor design
      ↓
UMI generation
      ↓
UMI filtering
      ↓
Codebook optimisation
      ↓
Sequencing simulation
      ↓
Probabilistic decoding
      ↓
Integration with VDJ evidence
      ↓
MRD analysis
```

The current implementation represents the project foundation. Future work will progressively replace placeholder components with biologically informed algorithms.

---

# 12. Closing Remarks

UMICODE is intended to be both a research platform and a practical tool for molecular assay development. The goal is not simply to produce working software, but to capture the biological reasoning behind assay design in a form that is transparent, reproducible and extensible.

As the project evolves, this guide should evolve alongside it.