#!/usr/bin/python3
"""Module that prints text with indentation after ., ? and :."""


def text_indentation(text):
    """Print text with 2 new lines after each ., ? and : character.

    Raises TypeError if text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = result.split("\n")
    output_lines = [line.strip() for line in lines]
    output = "\n".join(output_lines)
    while output.endswith("\n\n"):
        output = output[:-1]
    print(output, end="")
