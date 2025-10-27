# Centaur Template

A comprehensive multi-language development template featuring:

- **Python** and **Rust** project structures
- Comprehensive testing (unit, integration, fuzzing)
- GitHub Actions CI/CD workflows
- API documentation generation
- Pre-commit hooks for code quality
- GitHub Codespaces ready

## Quick Start

### 1. Clone and Open in Codespaces

Click "Code" → "Codespaces" → "Create codespace on main"

The devcontainer will automatically install all required tools.

### 2. Set Up Python Project

```bash
cd python
uv sync --all-extras
uv run pytest
```

### 3. Set Up Rust Project

```bash
cd rust
cargo build
cargo test
```

### 4. View Documentation

```bash
mkdocs serve
```

Then open http://localhost:8000

## Features

### Multi-Language Support

- **Python 3.12+** with `uv` for fast dependency management
- **Rust** with fuzzing and WASM support

### Comprehensive Testing

=== "Python"
    - Unit tests with pytest
    - Property-based testing with Hypothesis

=== "Rust"
    - Unit and integration tests
    - Property-based testing with proptest
    - Fuzzing with cargo-fuzz and honggfuzz

### CI/CD Pipeline

- Automated linting and formatting checks
- Multi-level testing (unit → integration → fuzzing)
- Code coverage reporting
- Dependency caching for fast builds
- Documentation deployment to GitHub Pages

### Code Quality

- Pre-commit hooks for automatic formatting
- Strict linting rules (ruff, clippy)
- Type checking (mypy for Python)
- Comprehensive test coverage requirements

## Project Structure

```
centaur_template/
├── .devcontainer/          # Codespaces configuration
├── .github/workflows/      # CI/CD pipelines
├── docs/                   # MkDocs documentation
├── python/                 # Python project
│   ├── src/               # Source code
│   └── tests/             # Tests (unit/integration/fuzzing)
├── rust/                   # Rust project
│   ├── src/               # Source code
│   ├── tests/             # Integration tests
│   └── fuzz/              # Fuzzing targets
├── scripts/                # Utility scripts
├── Summary/                # Development notes
└── Claude.md              # Claude Code guidance
```

## Using This Template

### For a New Project

1. Click "Use this template" on GitHub
2. Clone your new repository
3. Open in Codespaces or local dev container
4. Remove example code (see language-specific READMEs)
5. Update project metadata in `pyproject.toml` and `Cargo.toml`
6. Start building!

### Customization

- Add/remove languages by editing `.devcontainer/setup.sh`
- Adjust CI/CD workflows in `.github/workflows/`
- Configure code quality rules in `pyproject.toml` and `Cargo.toml`
- Update documentation structure in `mkdocs.yml`

## Documentation Sections

- **Development**: Setup guides and workflows
- **API Reference**: Auto-generated API documentation
- **Testing**: Testing strategies and examples
- **CI/CD**: Pipeline configuration and usage

## Contributing

See [Development → Getting Started](development/getting-started.md) for contribution guidelines.

## License

MIT License - see LICENSE file for details.
