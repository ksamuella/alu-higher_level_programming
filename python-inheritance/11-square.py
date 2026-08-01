#!/usr/bin/python3
"""Module that defines a Square class with its own string
representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the printable representation of the square."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
