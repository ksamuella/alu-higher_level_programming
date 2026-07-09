#!/usr/bin/python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, space-separated, row per line."""
    for row in matrix:
        parts = []
        for value in row:
            parts.append("{:d}".format(value))
        print(" ".join(parts))
