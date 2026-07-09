#!/usr/bin/python3
"""Module that prints all integers of a list, one per line."""


def print_list_integer(my_list=[]):
    """Print all integers of a list, one integer per line."""
    for i in my_list:
        print("{:d}".format(i))
