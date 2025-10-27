# Template Notes

This file contains important information about using this template for your own project.

## Documentation Build Configuration

### Strict Mode

The template documentation builds **without** `--strict` mode to allow example code that may have documentation warnings. This is intentional for the template.

**When you use this template for your project:**

1. After removing example code and adding your own
2. Edit `.github/workflows/docs.yml`
3. Find both `mkdocs build` commands (build and link-check jobs)
4. Change them to: `mkdocs build --strict`

**Why enable strict mode?**

Strict mode (`--strict`) makes MkDocs fail the build on any warnings, including:
- Missing documentation references
- Broken internal links
- Invalid markdown syntax
- Docstring parsing errors

This ensures your documentation is always correct and complete.

### Example

**Template (current):**
```yaml
- name: Build MkDocs site
  run: mkdocs build
```

**Your Project (recommended):**
```yaml
- name: Build MkDocs site
  run: mkdocs build --strict
```

## Other Template Considerations

### Example Code

The template includes working example code in:
- `python/src/centaur_example/`
- `rust/src/{calculator,text_utils}.rs`

**Remove these** when starting your project. See main README for removal instructions.

### Pre-commit Hooks

Pre-commit hooks are configured but not installed by default. After cloning:

```bash
pre-commit install
```

### CI/CD Workflows

The workflows are configured to run on `main` branch. If you use a different default branch:
- Update branch names in `.github/workflows/*.yml`
- Update branch protection rules in GitHub settings

## Questions?

See [Claude.md](../Claude.md) for comprehensive development guidance.
