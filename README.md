# docstring_jformat

__Docstring-jformat__  is a Python tool designed to automatically format Python docstrings and comments according to the Google style guide. This tool provides the ability to format both docstrings and commented lines in a Python script while allowing users to customize formatting options, such as justification and line length.

## Features
- Automatically formats docstrings and inline comments in Python scripts.
- Supports Google-style docstring formatting.
- Optionally enables text justification for better readability.
- Handles multiple docstring structures, including function, class, and module docstrings.
- Identifies and preserves indentation levels based on Python syntax.

## Note

**This code is not production-ready.** It handles only some common cases and may fail to process more complex docstrings. Users should be cautious when using this tool on scripts with intricate or unusual docstring formats.

However, this covers 90% of my use cases, and I would suggest using it as a "first step" in formatting your docstrings.

## Installation

You can install **Docstring-jformat** directly from GitHub using `pip`:

```bash
pip install git+https://github.com/yourusername/Docstring-jformat.git
```

## Usage

__Docstring-jformat__ is designed to be used from the command line. It processes Python scripts, formatting both docstrings and comments based on the specified options.

```bash
docjformat <path-to-python-file> [--justify] [--line-length LENGTH]
```
- `<path-to-python-file>`: The path to the Python script you want to format.
- `--justify`: (Optional) Enable justification for docstrings and comments (default: __False__).
- `--line-length` *LENGTH*: (Optional) Specify the maximum line length for formatting (default: __88__).

### Example

```bash
docjformat myscript.py --justify --line-length 100
```
In this example, Docstring-jformat will:
- Justify docstrings and comments in myscript.py.
- Wrap lines to a maximum of 100 characters.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
