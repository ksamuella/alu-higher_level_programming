#!/usr/bin/python3
"""Module that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Return the Python object represented by the JSON file filename."""
    with open(filename, "r") as f:
        return json.load(f)
