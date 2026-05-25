#!/usr/bin/env python3
"""Read and print the contents of a text file.

This module provides a helper function to open a file in read mode,
read its contents using UTF-8 encoding, and print them without adding
extra newline characters.
"""


def read_file(filename=""):
    """Read a text file and print its contents.

    Args:
        filename (str): The path to the file to read.
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
