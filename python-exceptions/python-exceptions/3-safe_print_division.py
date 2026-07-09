#!/usr/bin/python3
"""Module that safely divides two integers, printing the result."""


def safe_print_division(a, b):
    """Divide a by b, printing the result even if an error occurs."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
