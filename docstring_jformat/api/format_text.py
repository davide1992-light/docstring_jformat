import warnings


def __format_multiline_text(text: str, width: int, justify: bool) -> list[str]:
    """Formats the input text into lines of specified width with optional justification.

    Args:
        text (str): The input text to be formatted.
        width (int): The maximum width of each line.
        justify (bool): If  True,  the  lines  will  be fully justified (evenly spaced);
            otherwise, left-justified.

    Returns:
        list[str]: A  list  of  strings where each string represents a formatted line of
            text.
    """
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length == 0 and len(word) >= width:
            lines.append(word)
            continue
        if current_length + len(word) + len(current_line) > width:
            # Distribute spaces evenly in the current line
            if justify:
                for i in range(width - current_length):
                    current_line[i % (len(current_line) - 1 or 1)] += " "
                lines.append("".join(current_line))
            else:
                lines.append(" ".join(current_line).ljust(width))
            current_line = []
            current_length = 0

        current_line.append(word)
        current_length += len(word)

    lines.append(" ".join(current_line).ljust(width))

    return lines


def format_text_with_prefix(
    text: str, prefix: str, line_length: int, justify: bool
) -> list[str]:
    """Formats text into lines of specified length and adds a prefix to each line.

    Args:
        text (str): The input text to be formatted.
        prefix (str): A string to be added at the beginning of each line.
        line_length (int): The total length of each line, including the prefix.
        justify (bool): If   True,   the  lines  will  be  fully  justified;  otherwise,
            left-justified.

    Returns:
        list[str]: A list of formatted lines, each prefixed with the given prefix.

    Raises:
        Warning: If  the  prefix  length  makes  the  remaining line width too small for
            proper formatting a warning is issued and the unformatted text is returned.
    """
    if len(text.strip()) == 0:
        return []
    width = line_length - len(prefix)
    if width < 10:
        warnings.warn("Prefix too big: returning text without formatting")
        return text
    justified_lines = __format_multiline_text(text, width, justify)
    return [prefix + line for line in justified_lines]
