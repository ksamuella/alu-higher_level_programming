#!/usr/bin/python3
"""Module that defines a MyList class that inherits from list."""


class MyList(list):
    """A list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
