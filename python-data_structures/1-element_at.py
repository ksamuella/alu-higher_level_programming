#!/usr/bin/python3
"""Module that retrieves an element from a list, C-style."""


def element_at(my_list, idx):
    """Return the element at idx, or None if idx is out of range."""
    if idx < 0:
        return None
    if idx > len(my_list) - 1:
        return None
    return my_list[idx]
