#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""

    def test_is_rectangle_subclass(self):
        """Test that Square inherits from Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_basic_attributes(self):
        """Test that width and height equal size."""
        s = Square(5, 2, 3)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_default_x_y(self):
        """Test default x and y are 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_area(self):
        """Test area calculation for a square."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_str(self):
        """Test the __str__ representation."""
        s = Square(5)
        self.assertEqual(str(s), "[Square] ({}) 0/0 - 5".format(s.id))

    def test_size_getter(self):
        """Test the size getter returns width."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test the size setter updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_validation(self):
        """Test size setter validation raises TypeError."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_update_args(self):
        """Test update with ordered args (id, size, x, y)."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Test update with keyword args."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_to_dictionary(self):
        """Test to_dictionary contains all expected keys/values."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(
            d, {"id": s.id, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_roundtrip(self):
        """Test that update(**to_dictionary()) reproduces the instance."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
