#!/usr/bin/env python3
"""Write text to a file.

This module provides a helper function to open a file in write mode
and write a string to it using UTF-8 encoding.
"""

def write_file(filename="", text=""):
    """Write a string to a text file.

    Args:
        filename (str): The path to the file to write.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        content = file.write(text)
        return content
