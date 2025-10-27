# Python API Reference

This page contains auto-generated documentation for the Python codebase.

## Calculator Module

::: centaur_example.calculator
    options:
      show_source: true
      show_root_heading: true

## Text Utils Module

::: centaur_example.text_utils
    options:
      show_source: true
      show_root_heading: true

## Usage Examples

### Calculator

```python
from centaur_example.calculator import add, multiply, divide

# Basic arithmetic
result = add(5, 3)  # 8
result = multiply(4, 7)  # 28
result = divide(10, 2)  # 5.0
```

### Text Utilities

```python
from centaur_example.text_utils import reverse_string, count_words

# String manipulation
reversed_text = reverse_string("hello")  # "olleh"
word_count = count_words("hello world")  # 2
```

## Removing Example Code

When starting your own project, remove these example modules and add your own:

1. Delete `python/src/centaur_example/{calculator,text_utils}.py`
2. Create your own modules in `python/src/your_package_name/`
3. Update this documentation page to reference your modules
4. Update `mkdocs.yml` to point to your package
