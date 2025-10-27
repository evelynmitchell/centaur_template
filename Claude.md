# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Important Notes

**For Claude**: If you notice you've forgotten key details about this project (like using `uv` instead of `pip`, multi-language structure, or commit message specificity), re-read this entire file to refresh context.

**For User**: If you notice Claude has forgotten key workflow details after context compression, ask it to re-read this file.

**Codespaces**: This template is designed for GitHub Codespaces. The devcontainer automatically installs all required tools on startup.

## Repository Overview

This is a **multi-language project template** for GitHub Codespaces with comprehensive testing and CI/CD.

**Languages**: Python (3.12+) and Rust (edition 2024), independent but coexisting

**Testing**: Unit tests, integration tests, and fuzzing (Hypothesis for Python, cargo-fuzz/honggfuzz for Rust)

**CI/CD**: GitHub Actions with three levels (basic linting → intermediate testing+coverage → advanced fuzzing+artifacts)

**Documentation**: MkDocs with auto-generated API docs (mkdocstrings for Python, cargo doc for Rust)

Working notes are collected under `Summary/` with daily summary files.

## Repository Structure

```
centaur_template/
├── .devcontainer/          # Codespaces setup (auto-installs tools)
├── .github/workflows/      # CI/CD pipelines
│   ├── python-ci.yml      # Python lint/test/coverage/fuzz
│   ├── rust-ci.yml        # Rust lint/test/coverage/fuzz/WASM
│   └── docs.yml           # Documentation deployment
├── docs/                  # MkDocs documentation
├── python/                # Python project (independent)
│   ├── src/centaur_example/
│   └── tests/{unit,integration,fuzzing}/
├── rust/                  # Rust project (independent)
│   ├── src/
│   ├── tests/
│   └── fuzz/
├── scripts/               # Utility scripts
├── Summary/               # Daily development notes
├── .pre-commit-config.yaml
└── mkdocs.yml
```



## Development Workflow

This repository follows a structured 6-stage programming workflow inspired by design recipe methodology (documented in `Process` file):

1. **Problem Analysis to Data Definitions**: Identify input/output data representation with examples
2. **Signature, Purpose Statement, Header**: Define function signature and stub
3. **Functional Examples**: Create manual examples that will become tests
4. **Function Template**: Translate data definitions into function outline
5. **Function Definition**: Fill in the template
6. **Testing**: Run tests to verify correctness

Time tracking: The workflow uses git commit timestamps to track time spent at each stage.

## Python Development

This project uses **uv** for Python version and dependency management.

### What is uv?

`uv` is a fast, Rust-based Python package manager that:
- Resolves dependencies 10-100x faster than pip
- Automatically manages virtual environments
- Handles Python version management
- Creates lock files for reproducible builds
- Fully compatible with standard `pyproject.toml` format

### Installation

Install uv (one-time setup):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or on macOS with Homebrew:
```bash
brew install uv
```

### Common Commands

**Install dependencies:**
```bash
uv sync
```
This creates a virtual environment and installs all dependencies from `pyproject.toml`.

**Install with dev dependencies:**
```bash
uv sync --all-extras
```

**Run a Python script:**
```bash
uv run scripts/test_yfinance_api.py
```
Automatically uses the project's virtual environment.

**Run a Python module:**
```bash
uv run python -m pytest
```

**Add a new dependency:**
```bash
uv add package-name
```

**Add a dev dependency:**
```bash
uv add --dev package-name
```

**Update dependencies:**
```bash
uv lock --upgrade
uv sync
```

**Run Python REPL with project environment:**
```bash
uv run python
```

### Project Dependencies

**Dev dependencies** (installed with `--all-extras`):
- `pytest>=8.0.0` - Testing framework
- `pytest-cov>=4.1.0` - Coverage plugin
- `pytest-asyncio>=0.23.0` - Async test support
- `black>=24.0.0` - Code formatter
- `ruff>=0.1.0` - Fast Python linter
- `mypy>=1.8.0` - Type checker
- `hypothesis>=6.92.0` - Property-based testing

Add your project dependencies to `pyproject.toml` under `[project.dependencies]`.

### Python Version

This project requires **Python 3.12 or higher**.

The `.python-version` file specifies the exact version. `uv` will automatically use the correct Python version when running commands.

### Virtual Environment

`uv` automatically creates and manages a virtual environment in `.venv/`.

You don't need to manually activate it - `uv run` handles this automatically.

### IDE Setup

**VS Code**: Install the Python extension. It should automatically detect the `.venv/` environment created by uv.

**PyCharm**: Set the Python interpreter to `.venv/bin/python`.

## Rust Development

This project includes Rust code compiled to WebAssembly (WASM).

### Installation

**Install Rust toolchain:**
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source "$HOME/.cargo/env"
```

**Install wasm-pack:**
```bash
cargo install wasm-pack
```

### Naming Conventions

Rust enforces naming conventions via the compiler:

- **Functions and variables**: Use `snake_case`
  - ✅ `test_add_positive_negative`
  - ❌ `test_add_positiveNegT`
- **Types and traits**: Use `PascalCase`
- **Constants**: Use `SCREAMING_SNAKE_CASE`

The compiler will emit warnings if these conventions are violated.

### Common Commands

**Run tests:**
```bash
cargo test
```

**Build WASM for web:**
```bash
wasm-pack build --target web
```

**Check code without building:**
```bash
cargo check
```

**Format code:**
```bash
cargo fmt
```

**Lint code:**
```bash
cargo clippy
```

### Testing in Rust

- Place tests in a `#[cfg(test)]` module within `src/lib.rs`
- Use `#[test]` attribute for test functions
- Follow snake_case naming: `test_<function>_<scenario>`
- Use `assert_eq!`, `assert!`, `assert_ne!` macros
- Test edge cases: empty inputs, zeros, boundary values, negative numbers

Example:
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add_positive_positive() {
        assert_eq!(add(5, 3), 8);
    }
}
```

### WASM-Specific Notes

- Use `#[wasm_bindgen]` to export functions to JavaScript
- The `wasm-pack build --target web` command generates:
  - `pkg/*.wasm` - The compiled WebAssembly binary
  - `pkg/*.js` - JavaScript bindings
  - `pkg/*.d.ts` - TypeScript definitions
- Build artifacts (`target/` and `pkg/`) should be gitignored

## Common Patterns

### Workflow

Create a Summaryyyymmdd.md file for every new workday, and update it with progress regularly. Add it to the commit after updating and then do the commit.

Use the summary to track work done, issues discovered, and good practices learned.

Update Claude.md when you have learned a new good practice.

### Testing Philosophy

- Write comprehensive tests covering edge cases (empty arrays, zeros, boundary conditions)
- Test naming: `test_<feature>_<case><expected_result>` (e.g., `test_array_oneT` for True result)
- Use combinatorial testing: test sign combinations (+/+, +/-, -/-, -/+) and value ranges (low/low, low/high, high/low, high/high)

### Code Quality Standards

Common errors to avoid:
- Use `False/True` not `FALSE/TRUE` (Python booleans)
- Watch for edge case "thinkos" - assumptions about cases that aren't needed
- Always use version control with meaningful commits

**Python Import Ordering** (critical for ruff/isort):
- Imports are sorted **alphabetically by module name** within each group
- Groups: (1) standard library, (2) third-party, (3) local imports
- Blank line separates each group
- **The syntax (`import` vs `from`) doesn't matter** - only the module name matters
- Example:
  ```python
  # Correct (alphabetical by module name)
  from hypothesis import given, strategies as st
  import pytest

  from centaur_example.calculator import add

  # Wrong (not alphabetical)
  import pytest
  from hypothesis import given, strategies as st
  ```

### CI/CD with GitHub Actions

This repository uses GitHub Actions with **three levels of CI/CD**:

**Level 1 - Basic** (runs on every push/PR):
- Linting: ruff, black, mypy for Python; rustfmt, clippy for Rust
- Fast feedback on code quality

**Level 2 - Intermediate** (runs on every push/PR):
- All linting checks
- Unit and integration tests
- Code coverage reporting (Codecov integration)
- Matrix testing across Python 3.12/3.13 and Rust stable/beta

**Level 3 - Advanced** (runs on schedule or manual trigger):
- Fuzzing tests (Hypothesis, cargo-fuzz)
- Build artifacts (Python wheels, Rust binaries, WASM)
- Multi-platform builds (Linux, macOS, Windows for Rust)
- Documentation deployment to GitHub Pages

**Workflows**:
- `.github/workflows/python-ci.yml` - Python pipeline
- `.github/workflows/rust-ci.yml` - Rust pipeline
- `.github/workflows/docs.yml` - Documentation deployment


### Pre-commit Hooks

This repository uses pre-commit hooks to enforce code quality before commits:

**Initial setup** (one-time):
```bash
pip install pre-commit
pre-commit install
```

**What runs automatically on commit**:
- **Python**: black (formatter), ruff (linter), mypy (type checker)
- **Rust**: rustfmt (formatter), clippy (linter)
- **General**: trailing whitespace, YAML/TOML/JSON checks, large file detection
- **Security**: bandit for Python security issues
- **Docs**: mdformat for markdown files

If hooks fail, they will:
1. Auto-fix formatting issues where possible
2. Block the commit if there are unfixable issues
3. Allow you to review changes and re-attempt the commit

**Manual execution** (optional):
```bash
# Run on all files
pre-commit run --all-files

# Run on staged files only
pre-commit run
```

The pre-commit hooks serve as the first line of defense, with GitHub Actions as a backup for any changes that bypass local hooks.

## Template-Specific Guidance

### This is a Template Repository

**IMPORTANT**: This is a template meant to be copied and customized. Users will:

1. Click "Use this template" on GitHub to create their own repository
2. Remove the example code (`centaur_example` package)
3. Add their own code following the established structure
4. Customize configuration files with their project details

### Example Code

The template includes example code demonstrating best practices:

**Python** (`python/src/centaur_example/`):
- `calculator.py` - Basic arithmetic with error handling
- `text_utils.py` - String manipulation utilities

**Rust** (`rust/src/`):
- `calculator.rs` - Arithmetic with Result types
- `text_utils.rs` - String operations

**Tests** demonstrate all three testing levels:
- Unit tests with edge cases and parametrized tests
- Integration tests combining multiple modules
- Fuzzing tests (property-based and coverage-guided)

### Multi-Language Coordination

**Python and Rust are independent** - each can be used alone or together:

- **Python-only projects**: Keep `python/` directory, remove `rust/`
- **Rust-only projects**: Keep `rust/` directory, remove `python/`
- **Both**: Rust can compile to WASM for use in Python (via PyO3) or web

### Testing Strategy

**Test Directory Structure**:
```
tests/
├── unit/          # Fast, isolated tests (run always)
├── integration/   # Cross-component tests (run in CI)
└── fuzzing/       # Property-based and fuzz tests (run scheduled)
```

**Rust follows different conventions**:
- Unit tests: In `#[cfg(test)]` modules within source files
- Integration tests: Separate `tests/` directory
- Fuzzing: Separate `fuzz/` crate

### Fuzzing Setup

**Python Fuzzing**:
- Hypothesis: Write property-based tests in `tests/fuzzing/test_hypothesis_*.py`
- Run with pytest: `uv run pytest tests/fuzzing/ -v`

**Rust Fuzzing**:
```bash
# Initialize fuzzing (first time)
cd rust
cargo fuzz init

# Add fuzz targets in rust/fuzz/fuzz_targets/
# Run with: cargo +nightly fuzz run <target_name>
```

### Documentation

**MkDocs Structure**:
- `docs/index.md` - Landing page with quick start
- `docs/development/` - Setup and workflow guides
- `docs/api/` - Auto-generated API reference
- `docs/testing/` - Testing strategy and examples

**API Documentation**:
- Python: Docstrings automatically extracted by mkdocstrings
- Rust: Generated by `cargo doc`, copied to site during build

**Deployment**: Docs auto-deploy to GitHub Pages on push to main

**Strict Mode**: Template builds docs without `--strict` to allow example code warnings. Users should enable `--strict` after replacing example code by editing `.github/workflows/docs.yml`.

### Removing Example Code

**Python**:
```bash
rm -rf python/src/centaur_example
rm python/tests/unit/test_*.py
rm python/tests/integration/test_*.py
rm python/tests/fuzzing/test_hypothesis_*.py
```

**Rust**:
```bash
rm rust/src/{calculator,text_utils}.rs
rm rust/tests/integration_test.rs
# Edit rust/src/lib.rs to remove module declarations
```

**Keep**:
- Directory structure
- Configuration files (pyproject.toml, Cargo.toml)
- CI/CD workflows
- Pre-commit hooks
- Documentation structure

### Common Template Customizations

1. **Update project names** in:
   - `python/pyproject.toml` → `[project] name`
   - `rust/Cargo.toml` → `[package] name`
   - `mkdocs.yml` → `site_name`, `repo_url`

2. **Update author info** in:
   - `pyproject.toml` and `Cargo.toml` → authors field
   - `LICENSE` file

3. **Configure GitHub Pages**:
   - Repo Settings → Pages → Source: GitHub Actions

4. **Add Codecov token** (optional):
   - Get from codecov.io
   - Add as repo secret: `CODECOV_TOKEN`

5. **Adjust language focus**:
   - Remove workflows you do not need
   - Update `.devcontainer/setup.sh` to skip unused tools
   - Update `docs/` structure

6. **Enable documentation strict mode**:
   - After removing example code, edit `.github/workflows/docs.yml`
   - Change `mkdocs build` to `mkdocs build --strict` (2 places)
   - This ensures documentation quality by failing on warnings

### Working with the Template

When helping users with this template:

1. **Identify their focus**: Python-only, Rust-only, or both?
2. **Respect the structure**: Tests go in designated directories
3. **Maintain CI/CD**: Keep workflows updated as project evolves
4. **Document changes**: Update docs/ when adding features
5. **Update summaries**: Remind users to maintain Summary/ files

### Version Information

- **Python**: 3.12+ required, uses `uv` for dependency management
- **Rust**: Edition 2024, rust-version 1.85+
- **CI/CD**: GitHub Actions with three-level strategy
- **Docs**: MkDocs with Material theme, mkdocstrings plugin
