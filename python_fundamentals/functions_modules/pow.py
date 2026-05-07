#!/usr/bin/env python3
def pow(a, b):
    count = 0
    result = 1
    if (b < 0):
        b = -b
        while (count < b):
            count += 1
            result = result * a
        result = 1/result
        return result
    else:
        while (count < b):
            count += 1
            result = result * a
        return result
