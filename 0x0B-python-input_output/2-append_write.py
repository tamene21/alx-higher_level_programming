#!/usr/bin/python3
"""
A module to append a string at the end of the file.
"""


def append_write(filename="", text=""):
    """
    Apends text to filename

    Args:
    - filename: name of the file
    - text: text to append

    Return: the number of characters added
    """

    with open(filename, 'a') as f:
        return f.write(text)
