import argparse
import sys
from pathlib import Path

from .api.format_commented_lines import format_commented_lines
from .api.format_docstring import format_script_docstrings


def main():
    """Main entry point of the package."""
    parser = argparse.ArgumentParser(
        description="A script that accepts a path, an optional --justify flag, and an optional --line-length argument."
    )

    parser.add_argument("path", type=str, help="Path to the Python script (.py)")

    parser.add_argument(
        "--justify", action="store_true", help="Enable justification (default: False)"
    )

    parser.add_argument(
        "--line-length",
        type=int,
        default=88,
        help="Maximum line length for formatting (default: 88)",
    )

    args = parser.parse_args()

    path = Path(args.path)
    justify = args.justify
    line_length = args.line_length

    if not path.is_file() or not str(path).endswith(".py"):
        print(
            f"Error: The specified path '{str(path.absolute())}' does not exist or is not a valid Python file."
        )
        sys.exit(1)

    format_commented_lines(path, line_length)
    format_script_docstrings(path, line_length, justify)


if __name__ == "__main__":
    main()
