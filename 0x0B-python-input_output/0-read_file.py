#!/usr/bin/python3
"""
Module 0-read.
Reads from a file and prints.
"""


def read_file(filename=""):

    """
    Reads from file name and prints its
    content to the stdout.

    Args:
    - filename - input file name
    """
    with open(filename) as f:
        read_file = f.read()
        print(read_file, end="")
