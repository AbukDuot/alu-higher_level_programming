#!/usr/bin/python3
"""
Module - 1-square
Defines a class square with a private instance attribute size
"""


class Square:
    """
    A class square with private instance attribute size
    """
    def _init_(self,size):
        """
        Initialize a new square with the given size

        Args:
        size (int): The size of the new square object.

        Returns:
        None
        """
        self._size = size
