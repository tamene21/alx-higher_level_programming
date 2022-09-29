#!/usr/bin/python3
"""
Module 5- saving a file as a json file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Returns a file as saved as a json file.

    Args:
    - filename: file to write to
    - my_obj: object to write
    """
    with open(filname, 'w') as f:
        json.dump(my_obj, f)
