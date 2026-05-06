#!/usr/bin/env python3
for dizaine in range(0, 10):
    for unite in range(dizaine + 1, 10):
        if dizaine == 8 and unite == 9:
            print(f"{dizaine}{unite}", end='\n')
            break
        print(f"{dizaine}{unite}", end=", ")
