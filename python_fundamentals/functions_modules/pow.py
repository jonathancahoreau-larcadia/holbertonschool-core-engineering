#!/usr/bin/env python3
def pow(a, b):
    count = 0
    result = 1
    while (count < b):
        count += 1
        result = result * a
    return result
