#!/usr/bin/env python3
for alphabet in range(ord('a'), ord('z') + 1):
    if not chr(alphabet) == 'e' and not chr(alphabet) == 'q':
        print(chr(alphabet), end="")
print()
