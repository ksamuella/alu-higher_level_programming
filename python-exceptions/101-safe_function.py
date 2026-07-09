#!/usr/bin/python3
"""Module that safely executes a function."""
import sys


def safe_function(fct, *args):
    """Call fct with args, returning its result.

    Returns None and prints the exception to stderr on failure.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
