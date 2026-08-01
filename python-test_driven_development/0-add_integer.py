#!/usr/bin/python3
"""Module for adding two integers.

This module defines a single function, add_integer, which adds
two numbers together after validating and casting them.
"""


def add_integer(a, b=98):
    """Add two integers, casting floats to int first.

    Raises TypeError if a or b is not an int or float.

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(2.1, 3.9)
    5
    >>> add_integer(-5, -10)
    -15
    >>> add_integer(0, 0)
    0
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
