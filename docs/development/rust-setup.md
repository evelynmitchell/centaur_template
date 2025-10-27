# Rust Setup Guide

This guide covers Rust-specific setup and development in the Centaur template.

## Prerequisites

- Rust 1.85 or higher (edition 2024)
- cargo (comes with Rust)
- Optional: wasm-pack for WebAssembly builds

## Installation

### In Codespaces (Automatic)

Everything is pre-installed. Just run:

```bash
cd rust
cargo build
```

### Local Setup

```bash
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"

# Install fuzzing tools
cargo install cargo-fuzz
cargo install honggfuzz

# Install wasm-pack (optional)
cargo install wasm-pack
```

## Project Structure

```
rust/
├── src/
│   ├── lib.rs              # Library root
│   ├── calculator.rs       # Example module
│   └── text_utils.rs       # Example module
├── tests/
│   └── integration_test.rs # Integration tests
├── fuzz/
│   ├── Cargo.toml
│   └── fuzz_targets/       # Fuzzing targets
├── benches/                # Benchmarks
├── Cargo.toml             # Project config
└── README.md
```

## Development Workflow

### Building

```bash
# Debug build
cargo build

# Release build (optimized)
cargo build --release

# Check without building
cargo check

# Check all targets
cargo check --all-targets
```

### Running Tests

```bash
# All tests
cargo test

# With output
cargo test -- --nocapture

# Unit tests only (in src/)
cargo test --lib

# Integration tests only (in tests/)
cargo test --test '*'

# Specific test
cargo test test_add

# With detailed output
cargo test -- --show-output
```

### Code Quality

```bash
# Formatting
cargo fmt

# Check formatting
cargo fmt --check

# Linting
cargo clippy

# Strict linting
cargo clippy -- -D warnings

# Documentation
cargo doc --no-deps --open
```

## Testing

### Unit Tests

Located in `#[cfg(test)]` modules within source files.

**Example**:
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

**Best practices**:
- Place tests in same file as code
- Use descriptive names: `test_<function>_<scenario>`
- Test edge cases and error conditions
- Use `assert_eq!`, `assert!`, `assert_ne!`

### Integration Tests

Located in `tests/` directory as separate crates.

**Example**:
```rust
use centaur_example::{add, multiply};

#[test]
fn test_chain_operations() {
    let result = add(5, 3);
    let result = multiply(result, 2);
    assert_eq!(result, 16);
}
```

### Property-Based Testing

Use `proptest` for property-based testing:

```toml
[dev-dependencies]
proptest = "1.4"
```

```rust
use proptest::prelude::*;

proptest! {
    #[test]
    fn test_add_commutative(a: i32, b: i32) {
        assert_eq!(add(a, b), add(b, a));
    }
}
```

### Fuzzing

#### cargo-fuzz (libFuzzer)

```bash
# List fuzz targets
cargo +nightly fuzz list

# Run fuzz target
cargo +nightly fuzz run fuzz_calculator

# Run for specific time
cargo +nightly fuzz run fuzz_calculator -- -max_total_time=60

# Run with specific sanitizer
cargo +nightly fuzz run fuzz_calculator -- -sanitizer=address
```

**Fuzz target example**:
```rust
#![no_main]
use libfuzzer_sys::fuzz_target;

fuzz_target!(|data: &[u8]| {
    if data.len() >= 8 {
        let a = i32::from_le_bytes([data[0], data[1], data[2], data[3]]);
        let b = i32::from_le_bytes([data[4], data[5], data[6], data[7]]);
        let _ = add(a, b);
    }
});
```

## WebAssembly

Build for WebAssembly to run in browsers or with Python.

### Building

```bash
# For web
wasm-pack build --target web

# For Node.js
wasm-pack build --target nodejs

# For bundlers (webpack, etc.)
wasm-pack build --target bundler
```

### Using in JavaScript

```javascript
import init, { add } from './pkg/centaur_example.js';

await init();
const result = add(5, 3);  // 8
```

### Required in Cargo.toml

```toml
[lib]
crate-type = ["cdylib", "rlib"]

[target.'cfg(target_arch = "wasm32")'.dependencies]
wasm-bindgen = "0.2"
```

## Configuration

### Cargo.toml

Key sections:

```toml
[package]
name = "your-project-name"
version = "0.1.0"
edition = "2024"
rust-version = "1.85"

[dependencies]
# Runtime dependencies

[dev-dependencies]
# Test-only dependencies
criterion = "0.5"      # Benchmarking
proptest = "1.4"       # Property testing

[profile.release]
opt-level = 3
lto = true
```

## Benchmarking

Use Criterion for benchmarks:

```rust
use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn benchmark_add(c: &mut Criterion) {
    c.bench_function("add", |b| b.iter(|| {
        add(black_box(5), black_box(3))
    }));
}

criterion_group!(benches, benchmark_add);
criterion_main!(benches);
```

Run with:
```bash
cargo bench
```

## Common Issues

### Compilation errors

```bash
# Clean and rebuild
cargo clean
cargo build
```

### Test failures

```bash
# Run with detailed output
cargo test -- --show-output

# Run specific test
cargo test test_name -- --exact
```

### Clippy warnings

```bash
# Fix automatically when possible
cargo clippy --fix
```

## IDE Integration

### VS Code

Extensions installed in devcontainer:
- rust-analyzer (rust-lang.rust-analyzer)
- Better TOML (tamasfe.even-better-toml)
- CodeLLDB (vadimcn.vscode-lldb) for debugging

### RustRover / IntelliJ

1. Install Rust plugin
2. Open `rust/` directory
3. Project should auto-configure

## Naming Conventions

Rust enforces naming via compiler warnings:

- **Functions/variables**: `snake_case`
- **Types/traits**: `PascalCase`
- **Constants**: `SCREAMING_SNAKE_CASE`
- **Lifetimes**: `'a`, `'b`, etc.

## Next Steps

- [Testing Strategy](../testing/integration-tests.md)
- [Python Setup](python-setup.md)
- [Fuzzing Guide](../testing/fuzzing.md)
