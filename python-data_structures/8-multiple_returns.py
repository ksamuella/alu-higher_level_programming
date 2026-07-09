#!/usr/bin/python3
"""Module that returns the length and first character of a string."""


def multiple_returns(sentence):
    """Return a tuple (length, first_character) of sentence."""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
