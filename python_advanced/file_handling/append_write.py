#!/usr/bin/env python3
"""Append text to a file.

This module defines a helper function that opens a file in append mode
and writes a string to it using UTF-8 encoding.
"""

def append_write(filename="", text=""):
    """Append a string to a text file.

    Args:
        filename (str): The path to the file to append to.
        text (str): The text to add to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        content = file.write(text)
        return content
