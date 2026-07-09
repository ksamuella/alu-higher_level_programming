#!/usr/bin/python3
"""Module that safely prints an integer, reporting errors to stderr."""
import sys


def safe_print_integer_err(value):
    """Print value as an integer if possible.

    Returns True if printed successfully, False otherwise.
    On failure, prints the exception to stderr.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
