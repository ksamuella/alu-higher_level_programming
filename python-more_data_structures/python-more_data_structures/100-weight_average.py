#!/usr/bin/python3
"""Module that returns the weighted average of a list of tuples."""


def weight_average(my_list=[]):
    """Return the weighted average of (score, weight) tuples."""
    if len(my_list) == 0:
        return 0
    total = 0
    weights = 0
    for score, weight in my_list:
        total += score * weight
        weights += weight
    if weights == 0:
        return 0
    return total / weights
