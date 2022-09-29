#!/usr/bin/python3
"""
A module 3-returns a json file.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of my_obj.

    Args:
      - my_obj: string to represent
      - Return: JSON represenstation
    """
    return json.dumps(my_obj)
