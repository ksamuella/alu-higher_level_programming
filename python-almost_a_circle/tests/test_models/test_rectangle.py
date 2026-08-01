#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def test_is_base_subclass(self):
        """Test that Rectangle inherits from Base."""
        r = Rectangle(2, 3)
        self.assertIsInstance(r, Base)

    def test_basic_attributes(self):
        """Test width, height, x, y are correctly assigned."""
        r = Rectangle(10, 2, 1, 3)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)

    def test_default_x_y(self):
        """Test default x and y are 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_id_passed(self):
        """Test that a passed id is used."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width_type_error(self):
        """Test width validation raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_height_type_error(self):
        """Test height validation raises TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_width_value_error(self):
        """Test width <= 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_height_value_error(self):
        """Test height <= 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_type_error(self):
        """Test x validation raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {}, 0)

    def test_y_value_error(self):
        """Test y < 0 raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_setter_validation(self):
        """Test that setters also validate."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10

    def test_area(self):
        """Test area calculation."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_str(self):
        """Test the __str__ representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with ordered args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update with keyword args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1, height=2, y=3, width=4, id=99)
        self.assertEqual(str(r), "[Rectangle] (99) 1/3 - 4/2")

    def test_to_dictionary(self):
        """Test to_dictionary contains all expected keys/values."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(
            d, {"id": r.id, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_roundtrip(self):
        """Test that update(**to_dictionary()) reproduces the instance."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
