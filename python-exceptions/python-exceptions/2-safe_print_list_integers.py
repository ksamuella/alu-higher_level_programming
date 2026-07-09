#!/usr/bin/python3
"""Module that prints the first x elements of a list, integers only."""


def safe_print_list_integers(my_list=[], x=0):
    """Print up to x integers from my_list, skipping non-integers.

    Returns the real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
