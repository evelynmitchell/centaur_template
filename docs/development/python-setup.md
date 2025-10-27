# Python Setup Guide

This guide covers Python-specific setup and development in the Centaur template.

## Prerequisites

- Python 3.12 or higher
- `uv` package manager (installed automatically in devcontainer)

## Installation

### In Codespaces (Automatic)

Everything is pre-installed. Just run:

```bash
cd python
uv sync --all-extras
```

### Local Setup

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Navigate to Python project
cd python

# Install dependencies
uv sync --all-extras
```

## Project Structure

```
python/
├── src/
│   └── centaur_example/      # Main package
│       ├── __init__.py
│       ├── calculator.py
│       └── text_utils.py
├── tests/
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── fuzzing/              # Fuzzing tests
├── pyproject.toml           # Project config
├── .python-version          # Python version
└── README.md
```

## Development Workflow

### Running Tests

```bash
# All tests
uv run pytest

# With coverage
uv run pytest --cov --cov-report=html

# Specific test types
uv run pytest tests/unit/ -v
uv run pytest tests/integration/ -v
uv run pytest tests/fuzzing/ -v

# Specific test file
uv run pytest tests/unit/test_calculator.py -v

# Specific test function
uv run pytest tests/unit/test_calculator.py::test_add_positive_positive -v
```

### Code Quality

```bash
# Linting
uv run ruff check src tests

# Auto-fix linting issues
uv run ruff check --fix src tests

# Formatting
uv run black src tests

# Check formatting only
uv run black --check src tests

# Type checking
uv run mypy src
```

### Adding Dependencies

```bash
# Add runtime dependency
uv add requests

# Add development dependency
uv add --dev pytest-benchmark

# Remove dependency
uv remove package-name

# Update all dependencies
uv lock --upgrade
uv sync
```

## Testing

### Unit Tests

Located in `tests/unit/`, these test individual functions in isolation.

**Example**:
```python
def test_add_positive_positive() -> None:
    """Test adding two positive numbers."""
    assert add(5, 3) == 8
```

**Best practices**:
- Test one function per test file
- Test edge cases: zero, negative, empty, boundary values
- Use descriptive test names: `test_<function>_<scenario>`
- Use parametrized tests for multiple similar cases

### Integration Tests

Located in `tests/integration/`, these test components working together.

**Example**:
```python
def test_chain_operations() -> None:
    """Test chaining multiple operations."""
    result = add(5, 3)
    result = multiply(result, 2)
    assert result == 16
```

### Property-Based Testing (Hypothesis)

Tests properties that should always hold true.

**Example**:
```python
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_add_commutative(a: int, b: int) -> None:
    """Test that addition is commutative."""
    assert add(a, b) == add(b, a)
```

### Fuzzing (atheris)

Coverage-guided fuzzing for security testing.

**Example**:
```python
import atheris

def test_calculator(data: bytes) -> None:
    fdp = atheris.FuzzedDataProvider(data)
    a = fdp.ConsumeFloat()
    b = fdp.ConsumeFloat()
    _ = add(a, b)
```

## Configuration

### pyproject.toml

Key sections:

```toml
[project]
name = "your-project-name"
version = "0.1.0"
dependencies = [
    # Your runtime dependencies
]

[project.optional-dependencies]
dev = [
    # Development dependencies
]

[tool.pytest.ini_options]
# Pytest configuration

[tool.ruff]
# Ruff linter configuration

[tool.black]
# Black formatter configuration

[tool.mypy]
# Type checking configuration
```

### .python-version

Specifies Python version. `uv` uses this automatically.

## Common Issues

### Virtual environment not found

```bash
cd python
uv sync
```

### Import errors in tests

Ensure you're using `uv run`:
```bash
uv run pytest
```

### Type checking errors

```bash
# Run type checker
uv run mypy src

# Add type stubs for third-party libraries
uv add --dev types-requests
```

## IDE Integration

### VS Code

Extensions are automatically installed in devcontainer:
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- Ruff (charliermarsh.ruff)

The `.venv` should be automatically detected as the Python interpreter.

### PyCharm

1. Open the `python/` directory
2. Settings → Project → Python Interpreter
3. Add Interpreter → Existing → `python/.venv/bin/python`

## Next Steps

- [Testing Strategy](../testing/unit-tests.md)
- [Rust Setup](rust-setup.md)
- [CI/CD](../cicd/github-actions.md)
