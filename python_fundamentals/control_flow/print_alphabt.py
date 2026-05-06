#!/usr/bin/env python3
for code in range(ord('a'), ord('z') + 1):
    ch = chr(code)
    if ch in ('e', 'q'):
        continue
    print(ch, end="")
print()
