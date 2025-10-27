# Getting Started

This guide will help you set up the development environment and start working with the Centaur template.

## Prerequisites

### Option 1: GitHub Codespaces (Recommended)

No installation required! Just open the repository in Codespaces and everything will be set up automatically.

### Option 2: Local Development

Install the following tools:

- **Docker** or **Podman** (for dev containers)
- **VS Code** with Dev Containers extension
- OR manually install: Python 3.12+, Rust, uv, cargo-fuzz, honggfuzz

## Setup Steps

### Using Codespaces

1. Click **Code** → **Codespaces** → **Create codespace on main**
2. Wait for the devcontainer to build (3-5 minutes first time)
3. Everything is pre-installed and ready!

### Using Local Dev Container

1. Clone the repository
2. Open in VS Code
3. Click "Reopen in Container" when prompted
4. Wait for container to build

### Manual Setup

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install fuzzing tools
cargo install cargo-fuzz honggfuzz

# Install Python tools
pip install pre-commit mkdocs mkdocs-material mkdocstrings[python]
```

## Project Setup

### Python Project

```bash
cd python

# Install dependencies
uv sync --all-extras

# Verify installation
uv run pytest --version
uv run python --version
```

### Rust Project

```bash
cd rust

# Build project
cargo build

# Verify installation
cargo --version
rustc --version
```

## Daily Workflow

### 1. Create Daily Summary

```bash
# Create a new summary file
date=$(date +%Y%m%d)
touch Summary/summary${date}.md
```

Update this file throughout the day with progress, issues, and learnings.

### 2. Work on Features

Follow the 6-stage development workflow:

1. **Problem Analysis**: Define input/output with examples
2. **Signature & Purpose**: Write function signature and docstring
3. **Examples**: Create test cases
4. **Template**: Outline function structure
5. **Implementation**: Fill in the logic
6. **Testing**: Run and verify tests

### 3. Run Tests Frequently

=== "Python"
    ```bash
    # Run all tests
    uv run pytest

    # Run with coverage
    uv run pytest --cov

    # Run specific test file
    uv run pytest tests/unit/test_calculator.py -v
    ```

=== "Rust"
    ```bash
    # Run all tests
    cargo test

    # Run with output
    cargo test -- --nocapture

    # Run specific test
    cargo test test_add
    ```

### 4. Format and Lint

Pre-commit hooks will run automatically, but you can run manually:

=== "Python"
    ```bash
    uv run black src tests
    uv run ruff check --fix src tests
    uv run mypy src
    ```

=== "Rust"
    ```bash
    cargo fmt
    cargo clippy -- -D warnings
    ```

### 5. Commit Changes

```bash
git add .
git commit -m "Descriptive commit message

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

Pre-commit hooks will run and may modify files. Review changes and commit again if needed.

### 6. Update Documentation

```bash
# Update Claude.md with new patterns/practices
# Update summary file with progress

# Serve docs locally to preview
mkdocs serve
```

## IDE Setup

### VS Code Extensions

The devcontainer automatically installs:

- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- Ruff (charliermarsh.ruff)
- Rust Analyzer (rust-lang.rust-analyzer)
- Better TOML (tamasfe.even-better-toml)

### Settings

Python interpreter: `.venv/bin/python` (automatically detected)

Rust analyzer: Configured with clippy checks

## Troubleshooting

### Python virtual environment not found

```bash
cd python
uv sync
```

### Rust tools not installed

```bash
cargo install cargo-fuzz honggfuzz wasm-pack
```

### Pre-commit hooks failing

```bash
pre-commit install
pre-commit run --all-files
```

### Devcontainer rebuild needed

Press `F1` → "Dev Containers: Rebuild Container"

## Next Steps

- [Python Setup Guide](python-setup.md)
- [Rust Setup Guide](rust-setup.md)
- [Testing Strategy](testing.md)
