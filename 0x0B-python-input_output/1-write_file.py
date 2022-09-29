#!/usr/bin/python3
"""
Moudle-1 write a file and
and converts to a text file
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file
    and returns the number of characters.

    Args:
    -filename - the name of the text file
    -text - the type of text

    Returns:
    - the number of characters written
    """
    with open(filename, 'w') as f:
        return f.write(text)
