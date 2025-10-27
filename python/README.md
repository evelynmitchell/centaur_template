# Python Project

This is the Python component of the Centaur template.

## Quick Start

```bash
# Install dependencies
uv sync --all-extras

# Run tests
uv run pytest

# Run specific test types
uv run pytest tests/unit/              # Unit tests only
uv run pytest tests/integration/       # Integration tests only

# Run fuzzing tests (limited time)
uv run pytest tests/fuzzing/ -v

# Run linting
uv run ruff check src tests
uv run black --check src tests
uv run mypy src

# Format code
uv run black src tests
uv run ruff check --fix src tests
```

## Project Structure

```
python/
├── src/
│   └── centaur_example/     # Main package
│       ├── __init__.py
│       ├── calculator.py    # Example module
│       └── text_utils.py    # Another example
├── tests/
│   ├── unit/               # Fast, isolated tests
│   ├── integration/        # Tests with dependencies
│   └── fuzzing/           # Property-based and fuzz tests
├── pyproject.toml         # Project configuration
└── .python-version        # Python version specification
```

## Testing Strategy

### Unit Tests
Fast, isolated tests for individual functions and classes.

### Integration Tests
Tests that verify components work together correctly.

### Fuzzing Tests
- **Hypothesis**: Property-based testing for logic validation
- **Atheris**: Coverage-guided fuzzing for security testing

## Removing Example Code

To use this template for your own project:

1. Delete example modules: `src/centaur_example/{calculator,text_utils}.py`
2. Delete example tests: `tests/**/{test_calculator,test_text_utils,test_fuzz_*}.py`
3. Update `pyproject.toml` with your project name and dependencies
4. Keep the directory structure and configuration
