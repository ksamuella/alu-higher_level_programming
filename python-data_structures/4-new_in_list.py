#!/usr/bin/python3
"""Module that replaces an element in a copy of a list."""


def new_in_list(my_list, idx, element):
    """Return a new list with my_list[idx] replaced by element."""
    if idx < 0 or idx > len(my_list) - 1:
        return list(my_list)
    new_list = list(my_list)
    new_list[idx] = element
    return new_list
