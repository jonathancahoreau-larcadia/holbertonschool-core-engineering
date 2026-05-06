#!/usr/bin/env python3
def uppercase(str):
    print(*[chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in str], sep="")
