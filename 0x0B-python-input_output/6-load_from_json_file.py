#!/usr/bin/python3
"""
Module 6- load from JSON file
creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    creates an object from a JSON filename.

    Args:
    - filename: name of the JSON file
    Return: the object
    """
    with open(filename, 'r') as f:
        return json.load(f)
