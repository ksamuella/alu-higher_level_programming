#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Represent a base geometry shape."""

    def area(self):
        """Raise an exception since area is not implemented here."""
        raise Exception("area() is not implemented")
