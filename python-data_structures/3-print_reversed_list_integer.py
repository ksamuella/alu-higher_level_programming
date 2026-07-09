#!/usr/bin/python3
"""Module that prints all integers of a list, in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order, one per line."""
    for i in reversed(my_list):
        print("{:d}".format(i))
