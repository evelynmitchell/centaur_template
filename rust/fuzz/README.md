# Fuzzing with cargo-fuzz

## Setup

First time setup:

```bash
# Install cargo-fuzz (nightly required)
rustup install nightly
cargo install cargo-fuzz

# Initialize fuzzing (if not already done)
cargo fuzz init
```

## Running Fuzz Tests

```bash
# List available fuzz targets
cargo +nightly fuzz list

# Run a fuzz target
cargo +nightly fuzz run fuzz_calculator

# Run with a time limit (e.g., 60 seconds)
cargo +nightly fuzz run fuzz_calculator -- -max_total_time=60

# Run with address sanitizer
cargo +nightly fuzz run fuzz_calculator -- -sanitizer=address
```

## Fuzz Targets

### fuzz_calculator

Tests calculator operations with random inputs to find:
- Integer overflow issues
- Division by zero handling
- Unexpected panics

### fuzz_text_utils

Tests text processing with random strings to find:
- Unicode handling issues
- Empty string edge cases
- Memory safety issues

## Corpus

The `corpus/` directory contains test cases that trigger different code paths.
Good test cases are automatically saved here.

## Artifacts

When a crash or failure is found, it's saved in `artifacts/` for debugging.

To reproduce a crash:

```bash
cargo +nightly fuzz run fuzz_calculator artifacts/fuzz_calculator/crash-xxx
```
