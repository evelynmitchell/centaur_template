# Fuzzing Guide

Fuzzing is an automated testing technique that feeds random or mutated inputs to your code to find bugs, crashes, and security vulnerabilities.

## Why Fuzz?

Fuzzing helps find:
- Edge cases you didn't think to test
- Integer overflows and underflows
- Memory safety issues
- Infinite loops or hangs
- Assertion failures
- Security vulnerabilities

## Python Fuzzing

### Hypothesis (Property-Based Testing)

Hypothesis generates test inputs automatically to verify properties of your code. This template uses Hypothesis as the primary fuzzing tool for Python.

#### Setup

Already included in dev dependencies:
```toml
[project.optional-dependencies]
dev = [
    "hypothesis>=6.92.0",
]
```

#### Writing Tests

```python
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_add_commutative(a: int, b: int) -> None:
    """Addition should be commutative: a + b = b + a"""
    assert add(a, b) == add(b, a)
```

#### Strategies

Common strategies for input generation:

```python
import hypothesis.strategies as st

# Basic types
st.integers()                    # Any integer
st.integers(min_value=0)        # Non-negative
st.floats()                      # Any float
st.text()                        # Any string
st.booleans()                    # True/False

# Collections
st.lists(st.integers())         # Lists of integers
st.lists(st.text(), min_size=1) # Non-empty lists

# Custom types
st.builds(MyClass)              # Instances of MyClass
```

#### Running

```bash
# Run all hypothesis tests
uv run pytest tests/fuzzing/test_hypothesis_*.py -v

# With more examples
uv run pytest tests/fuzzing/ --hypothesis-seed=42

# CI profile (more thorough)
uv run pytest tests/fuzzing/ --hypothesis-profile=ci
```

#### Configuration

In `pyproject.toml`:
```toml
[tool.pytest.ini_options]
addopts = [
    "--hypothesis-show-statistics",
]
```

## Rust Fuzzing

### cargo-fuzz (libFuzzer)

cargo-fuzz provides structure-aware fuzzing backed by LLVM's libFuzzer.

#### Setup

```bash
# Install cargo-fuzz
cargo install cargo-fuzz

# Initialize (if not already done)
cd rust
cargo fuzz init
```

#### Writing Fuzz Targets

Create `fuzz/fuzz_targets/fuzz_calculator.rs`:

```rust
#![no_main]
use libfuzzer_sys::fuzz_target;
use centaur_example::calculator::{add, divide};

fuzz_target!(|data: &[u8]| {
    if data.len() < 8 {
        return;
    }

    let a = i32::from_le_bytes([data[0], data[1], data[2], data[3]]);
    let b = i32::from_le_bytes([data[4], data[5], data[6], data[7]]);

    let _ = add(a, b);

    if b != 0 {
        match divide(a, b) {
            Ok(_) => {},
            Err(_) => panic!("divide should succeed for non-zero"),
        }
    }
});
```

#### Running

```bash
# List targets
cargo fuzz list

# Run target
cargo +nightly fuzz run fuzz_calculator

# Run for specific time (seconds)
cargo +nightly fuzz run fuzz_calculator -- -max_total_time=60

# Run with memory limit
cargo +nightly fuzz run fuzz_calculator -- -rss_limit_mb=2048

# Use specific corpus
cargo +nightly fuzz run fuzz_calculator corpus/
```

#### Sanitizers

```bash
# Address Sanitizer (memory errors)
cargo +nightly fuzz run fuzz_calculator -- -sanitizer=address

# Undefined Behavior Sanitizer
cargo +nightly fuzz run fuzz_calculator -- -sanitizer=undefined
```

### honggfuzz

Alternative fuzzer with different fuzzing strategies.

#### Setup

```bash
cargo install honggfuzz
```

#### Running

```bash
# Run honggfuzz
cargo hfuzz run hfuzz_target

# With coverage
HFUZZ_RUN_ARGS="--coverage" cargo hfuzz run hfuzz_target
```

### proptest (Property-Based Testing)

Similar to Hypothesis but for Rust.

#### Setup

In `Cargo.toml`:
```toml
[dev-dependencies]
proptest = "1.4"
```

#### Writing Tests

```rust
use proptest::prelude::*;

proptest! {
    #[test]
    fn test_add_commutative(a: i32, b: i32) {
        assert_eq!(add(a, b), add(b, a));
    }

    #[test]
    fn test_divide_reciprocal(a in 1..1000i32, b in 1..1000i32) {
        let result = divide(a, b).unwrap();
        assert_eq!(result, a / b);
    }
}
```

## CI/CD Integration

### GitHub Actions

Fuzzing runs on a schedule or manual trigger:

```yaml
# Runs fuzzing for limited time
- name: Run fuzzing
  run: |
    timeout 60 cargo +nightly fuzz run fuzz_target || true
```

### Continuous Fuzzing

For production projects:

1. **OSS-Fuzz**: Free for open-source projects
2. **ClusterFuzz**: Google's fuzzing infrastructure
3. **Self-hosted**: Run fuzzing on dedicated machines

## Corpus Management

### Saving Interesting Inputs

Both fuzzers automatically save inputs that increase coverage:

```
fuzz/corpus/fuzz_target/
├── artifact1
├── artifact2
└── ...
```

### Using Corpus

```bash
# cargo-fuzz
cargo fuzz run target corpus/

# atheris
python fuzz_script.py corpus/
```

### Minimizing Corpus

```bash
# cargo-fuzz
cargo fuzz cmin target

# Reduces corpus to minimal set covering all coverage
```

## Debugging Crashes

### Reproducing Crashes

When a crash is found, artifacts are saved:

```bash
# cargo-fuzz
cargo fuzz run target fuzz/artifacts/target/crash-xxx

# atheris
python fuzz_script.py < artifacts/crash-xxx
```

### Debugging

```bash
# Run with debugger
cargo fuzz run --debug target artifacts/crash-xxx

# Get stack trace
RUST_BACKTRACE=1 cargo fuzz run target artifacts/crash-xxx
```

## Best Practices

1. **Start small**: Begin with simple fuzz targets
2. **Use seeds**: Provide example inputs in corpus/
3. **Run overnight**: Fuzzing finds more bugs with more time
4. **Check coverage**: Ensure fuzzer reaches all code paths
5. **Fix crashes**: Don't ignore fuzzer findings
6. **Minimize repros**: Make crash reproducers as small as possible
7. **Continuous fuzzing**: Run regularly, not just once

## Interpreting Results

### Coverage

```bash
# cargo-fuzz coverage report
cargo fuzz coverage target

# Generate HTML report
cargo cov -- show target/...
```

### Statistics

Fuzzers show:
- **exec/s**: Executions per second (faster = better)
- **coverage**: Code paths explored
- **crashes**: Bugs found
- **hangs**: Infinite loops detected

## Fuzzing Checklist

- [ ] Write fuzz targets for critical code
- [ ] Provide seed corpus with valid inputs
- [ ] Run locally before CI
- [ ] Check coverage reports
- [ ] Reproduce and fix any crashes found
- [ ] Add regression tests for crashes
- [ ] Run fuzzing in CI on schedule
- [ ] Consider continuous fuzzing for production

## Next Steps

- [Unit Tests](unit-tests.md)
- [Integration Tests](integration-tests.md)
- [CI/CD Configuration](../cicd/github-actions.md)
