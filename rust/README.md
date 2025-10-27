# Rust Project

This is the Rust component of the Centaur template.

## Quick Start

```bash
# Build the project
cargo build

# Run tests
cargo test

# Run specific test types
cargo test --lib          # Unit tests (in src/)
cargo test --test '*'     # Integration tests (in tests/)

# Run benchmarks
cargo bench

# Run clippy (linting)
cargo clippy -- -D warnings

# Format code
cargo fmt

# Check without building
cargo check
```

## Fuzzing

### cargo-fuzz (libFuzzer)

```bash
# Initialize fuzzing (first time only)
cargo fuzz init

# List fuzz targets
cargo fuzz list

# Run a fuzz target
cargo fuzz run fuzz_target_1

# Run with sanitizers
cargo fuzz run fuzz_target_1 -- -sanitizer=address
```

### honggfuzz

```bash
# Run honggfuzz
cargo hfuzz run hfuzz_target_1

# View coverage
cargo hfuzz run-debug hfuzz_target_1
```

## WebAssembly

Build for WebAssembly:

```bash
# Build for web
wasm-pack build --target web

# Build for Node.js
wasm-pack build --target nodejs

# Build for bundlers
wasm-pack build --target bundler
```

## Project Structure

```
rust/
├── src/
│   ├── lib.rs              # Library root
│   ├── calculator.rs       # Example module
│   └── text_utils.rs       # Another example
├── tests/                  # Integration tests
│   └── integration_test.rs
├── benches/                # Benchmarks
│   └── benchmark.rs
├── fuzz/                   # Fuzzing targets (cargo-fuzz)
│   └── fuzz_targets/
└── hfuzz/                  # Honggfuzz targets
    └── src/
        └── main.rs
```

## Testing Strategy

### Unit Tests
- Located in `src/` files with `#[cfg(test)]` modules
- Fast, isolated tests for individual functions
- Run with `cargo test --lib`

### Integration Tests
- Located in `tests/` directory
- Test public API and component interactions
- Run with `cargo test --test '*'`

### Property-Based Testing
- Use `proptest` or `quickcheck` for property-based tests
- Automatically generates test cases

### Fuzzing
- **cargo-fuzz**: Coverage-guided fuzzing with libFuzzer
- **honggfuzz**: Feedback-driven fuzzing with coverage analysis
- Run continuously to find edge cases and security issues

## Code Quality

```bash
# Run all checks
cargo fmt --check    # Check formatting
cargo clippy        # Linting
cargo test          # All tests
cargo doc --no-deps # Generate docs
```

## Removing Example Code

To use this template for your own project:

1. Update `Cargo.toml` with your project name and dependencies
2. Delete example modules in `src/`
3. Delete example tests in `tests/`
4. Initialize fuzzing: `cargo fuzz init`
5. Keep the directory structure and configuration
