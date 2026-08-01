#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def test_id_public(self):
        """Test that id is public."""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_id_none_increments(self):
        """Test that id is auto-assigned when None."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_no_args(self):
        """Test Base with no arguments at all."""
        b = Base()
        self.assertIsInstance(b.id, int)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with a list of dictionaries."""
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(result, '[{"id": 1}]')

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        result = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(result, [{"id": 1}])

    def test_save_to_file_rectangle(self):
        """Test save_to_file creates a Rectangle.json file."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"id": 1', content)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """Test save_to_file with None saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_create_rectangle(self):
        """Test create for Rectangle."""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test create for Square."""
        s1 = Square(5, 2, 3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_load_from_file_no_file(self):
        """Test load_from_file when no file exists."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_roundtrip(self):
        """Test load_from_file after save_to_file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
