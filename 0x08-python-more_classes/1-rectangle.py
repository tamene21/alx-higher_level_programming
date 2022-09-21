#!/usr/bin/python3
"""This module creates a rectangle"""


class Rectangle:
"""
class that creat a rectangle
"""
def __init__(self, width=0, height=0):
    """Constructor initialize the class rectangle
    Keyword Arguments:
       width {int} -- width of the rectangle (default: {0})
       height {int} -- height of the rectangle (default: {0})
       """
    self.width = width
    self.height = height

    @property
def width(self):

