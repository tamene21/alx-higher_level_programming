#!/usr/bin/python3
class Square:
    '''Represents a square.
    private instance attribute: size
    instantiation with size (no type /value verification).
    '''

    def __init__(self, size):
        '''initializes the data'''
        self.__size = size
