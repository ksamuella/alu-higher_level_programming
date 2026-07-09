#!/usr/bin/python3
"""Module that replaces an element of a list at a specific position."""


def replace_in_list(my_list, idx, element):
    """Replace my_list[idx] with element, in place."""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
