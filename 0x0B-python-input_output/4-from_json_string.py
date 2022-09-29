#!/usr/bin/python3
"""
Module 4-JSON string to object
"""

import json


def from_json_string(my_str):
    """
    changing from json to string

    Args:
    - my_str: a json file

    Return: Returns a string file
    """

    return json.loads(my_str)
