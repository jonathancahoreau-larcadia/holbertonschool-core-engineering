#!/usr/bin/env python3
def uppercase(s):
    for c in s:
        print("{:c}".format(
            ord(c) - 32 if 'a' <= c <= 'z' else ord(c)
        ), end="")
print()
