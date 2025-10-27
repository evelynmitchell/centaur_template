#!/bin/bash
set -e

echo "========================================="
echo "Setting up Centaur development environment"
echo "========================================="

# Install uv for Python dependency management
echo "Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.cargo/bin:$PATH"

# Install Rust tools for fuzzing
echo "Installing Rust fuzzing tools..."
cargo install cargo-fuzz
cargo install honggfuzz

# Install wasm-pack for WebAssembly
echo "Installing wasm-pack..."
cargo install wasm-pack

# Install Python development tools
echo "Installing Python tools..."
pip install --user pre-commit mkdocs mkdocs-material mkdocstrings[python]

# Install Claude Code (if not already present)
if ! command -v claude &> /dev/null; then
    echo "Installing Claude Code..."
    curl -fsSL https://claude.ai/install.sh | bash
fi

# Create cache directory for better performance
mkdir -p ~/.cache/pip ~/.cache/cargo

echo "========================================="
echo "Setup complete! Environment ready."
echo "========================================="
echo ""
echo "Quick start:"
echo "  Python: cd python && uv sync"
echo "  Rust:   cd rust && cargo build"
echo "  Docs:   mkdocs serve"
echo ""
