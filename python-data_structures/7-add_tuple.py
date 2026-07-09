#!/usr/bin/python3
"""Module that adds two tuples of integers."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Return a tuple that is the element-wise addition of the first
    two elements of tuple_a and tuple_b, padding with 0 if needed."""
    a = list(tuple_a[:2]) + [0, 0]
    b = list(tuple_b[:2]) + [0, 0]
    return (a[0] + b[0], a[1] + b[1])
