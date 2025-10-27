# Centaur Template

A comprehensive multi-language development template for GitHub Codespaces featuring Python, Rust, comprehensive testing strategies, CI/CD workflows, and auto-generated documentation.

## Features

### Multi-Language Support
- **Python 3.12+** with `uv` for fast dependency management
- **Rust (edition 2024)** with WASM support
- Independent project structures that can coexist or be used separately

### Comprehensive Testing
- **Unit Tests**: Fast, isolated tests for individual functions
- **Integration Tests**: Cross-component testing
- **Fuzzing**:
  - Python: Hypothesis (property-based testing)
  - Rust: cargo-fuzz (libFuzzer) + honggfuzz

### CI/CD Pipeline (3 Levels)
- **Basic**: Linting and formatting checks
- **Intermediate**: Testing with code coverage reporting
- **Advanced**: Matrix testing, dependency caching, artifact builds, scheduled fuzzing

### Documentation
- **MkDocs** with Material theme
- **Auto-generated API docs**:
  - Python: mkdocstrings
  - Rust: cargo doc integration
- **GitHub Pages** deployment

### Code Quality
- Pre-commit hooks for automatic formatting
- Strict linting (ruff for Python, clippy for Rust)
- Type checking (mypy)

## Quick Start

### Option 1: GitHub Codespaces (Recommended)

1. Click **"Use this template"** to create your own repository
2. Click **"Code"** → **"Codespaces"** → **"Create codespace on main"**
3. Wait 3-5 minutes for environment setup
4. Everything is pre-installed and ready!

### Option 2: Local Development Container

1. Clone your repository
2. Open in VS Code
3. Install "Dev Containers" extension
4. Click "Reopen in Container"
5. Wait for container to build

### Option 3: Manual Setup

See [Development → Getting Started](docs/development/getting-started.md) for manual installation instructions.

## Project Structure

```
centaur_template/
├── .devcontainer/           # Codespaces configuration
│   ├── devcontainer.json   # Container settings
│   └── setup.sh            # Auto-install script
├── .github/
│   └── workflows/          # CI/CD pipelines
│       ├── python-ci.yml   # Python testing & coverage
│       ├── rust-ci.yml     # Rust testing & coverage
│       └── docs.yml        # Documentation deployment
├── docs/                   # MkDocs documentation
│   ├── index.md
│   ├── development/
│   ├── api/
│   └── testing/
├── python/                 # Python project
│   ├── src/
│   │   └── centaur_example/
│   ├── tests/
│   │   ├── unit/          # Fast, isolated tests
│   │   ├── integration/   # Cross-component tests
│   │   └── fuzzing/       # Hypothesis + atheris
│   ├── pyproject.toml
│   └── .python-version
├── rust/                   # Rust project
│   ├── src/
│   │   ├── lib.rs
│   │   ├── calculator.rs
│   │   └── text_utils.rs
│   ├── tests/             # Integration tests
│   ├── fuzz/              # cargo-fuzz targets
│   └── Cargo.toml
├── scripts/                # Utility scripts
├── Summary/                # Daily development notes
├── .pre-commit-config.yaml # Pre-commit hooks
├── mkdocs.yml             # Documentation config
├── Claude.md              # Claude Code guidance
└── README.md              # This file
```

## Using This Template

### For Python Projects

```bash
cd python

# Install dependencies
uv sync --all-extras

# Run tests
uv run pytest                        # All tests
uv run pytest tests/unit/           # Unit tests only
uv run pytest --cov                 # With coverage

# Linting and formatting
uv run ruff check src tests
uv run black src tests
uv run mypy src

# Run fuzzing
uv run pytest tests/fuzzing/ -v
```

### For Rust Projects

```bash
cd rust

# Build and test
cargo build
cargo test                          # All tests
cargo test --lib                    # Unit tests only
cargo test --test '*'               # Integration tests

# Linting and formatting
cargo fmt
cargo clippy -- -D warnings

# Build for WASM
wasm-pack build --target web

# Run fuzzing
cargo +nightly fuzz run fuzz_calculator
```

### Documentation

```bash
# Serve docs locally
mkdocs serve

# Visit http://localhost:8000

# Build docs
mkdocs build

# Build with strict mode (recommended for production)
mkdocs build --strict

# Docs are auto-deployed to GitHub Pages on push to main
```

**Note**: The template builds without `--strict` mode to allow example code with documentation warnings. Once you've replaced the example code with your own, enable strict mode in `.github/workflows/docs.yml` for better documentation quality checks.

## Customizing for Your Project

### 1. Remove Example Code

**Python:**
```bash
rm -rf python/src/centaur_example
rm -rf python/tests/unit/test_*.py
rm -rf python/tests/integration/test_*.py
rm -rf python/tests/fuzzing/test_hypothesis_*.py
```

**Rust:**
```bash
rm rust/src/calculator.rs
rm rust/src/text_utils.rs
rm rust/tests/integration_test.rs
```

### 2. Update Project Metadata

**Python** (`python/pyproject.toml`):
```toml
[project]
name = "your-project-name"
description = "Your project description"
authors = [{ name = "Your Name", email = "your.email@example.com" }]
```

**Rust** (`rust/Cargo.toml`):
```toml
[package]
name = "your-project-name"
description = "Your project description"
authors = ["Your Name <your.email@example.com>"]
```

### 3. Update Documentation

- Edit `mkdocs.yml` to reflect your project structure
- Update `docs/index.md` with your project overview
- Modify API documentation paths in `docs/api/`

### 4. Enable Strict Mode for Documentation

Once you've replaced the example code, enable strict mode for better documentation quality:

In `.github/workflows/docs.yml`, change:
```yaml
run: mkdocs build
```

To:
```yaml
run: mkdocs build --strict
```

This will fail the build on documentation warnings, ensuring high-quality docs.

### 5. Configure Repository Settings

1. **Enable GitHub Pages**:
   - Settings → Pages → Source: GitHub Actions

2. **Add Codecov Token** (optional for coverage reporting):
   - Get token from codecov.io
   - Add as repository secret: `CODECOV_TOKEN`

3. **Update Repository URLs**:
   - In `mkdocs.yml`: Update `repo_url`
   - In workflow files: Update any hardcoded URLs

## Development Workflow

### Daily Summary Pattern

```bash
# Create daily summary file
date=$(date +%Y%m%d)
touch Summary/summary${date}.md
```

Update throughout the day with:
- Work completed
- Issues discovered
- Good practices learned
- Commit with your changes

### Pre-commit Hooks

```bash
# Install hooks (first time)
pre-commit install

# Run manually
pre-commit run --all-files
```

Hooks automatically run on commit and will:
- Format code (black, rustfmt)
- Lint code (ruff, clippy)
- Check for common issues
- Block commits if unfixable issues found

### Committing Changes

Hooks run automatically. If they modify files:
1. Review the changes
2. Stage the modifications
3. Commit again

### CI/CD Workflows

- **On Push/PR**: Linting + testing + coverage
- **On Push to Main**: + Build artifacts + deploy docs
- **Scheduled/Manual**: Fuzzing tests

## Testing Philosophy

### Python

- **Unit Tests**: Test individual functions with edge cases
- **Integration Tests**: Test components working together
- **Property-Based (Hypothesis)**: Automatically generate test cases

### Rust

- **Unit Tests**: In `#[cfg(test)]` modules within source files
- **Integration Tests**: In `tests/` directory
- **Property-Based (proptest)**: Generate test inputs
- **Fuzzing**: cargo-fuzz + honggfuzz for security

## Documentation

Full documentation is available at: `https://yourusername.github.io/centaur_template/`

Or run locally:
```bash
mkdocs serve
```

### Key Documentation Pages

- **Getting Started**: Setup and daily workflow
- **Python Setup**: Python-specific configuration
- **Rust Setup**: Rust-specific configuration
- **Testing Strategy**: Comprehensive testing guide
- **CI/CD**: GitHub Actions workflows
- **API Reference**: Auto-generated API docs

## Contributing

See [Claude.md](Claude.md) for development guidelines and best practices when working with Claude Code.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

Built for use with [Claude Code](https://claude.ai/code) in GitHub Codespaces.
