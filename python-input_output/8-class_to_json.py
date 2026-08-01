#!/usr/bin/python3
"""Module that returns a JSON-serializable dict description of an object."""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization."""
    return obj.__dict__
