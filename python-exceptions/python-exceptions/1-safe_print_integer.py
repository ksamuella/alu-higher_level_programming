#!/usr/bin/python3
"""Module that safely prints an integer."""


def safe_print_integer(value):
    """Print value as an integer if possible.

    Returns True if printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
