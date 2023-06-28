#!/usr/bin/python3
"""This module defines a class Square"""
class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialises the data"""
        self.__size = size
        """size is a private attribute of the class Square. The instance"""
        if type(size) != int:
            """size must be an integer, otherwise raise a TypeError exception"""
            raise TypeError("size must be an integer")
        """if size is less than 0, raise a ValueError exception"""
        if size < 0:
            """size must be >= 0"""
            raise ValueError("size must be >= 0")
