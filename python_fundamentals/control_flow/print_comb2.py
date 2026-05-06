#!/usr/bin/env python3
for n in range(0, 100):
    if n == 99:
        print(f"{99:02d}", end='\n')
        break
    print(f"{n:02d}, ", end="")
