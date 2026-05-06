#!/usr/bin/env python3
for alphabet in range(ord('a'), ord('z') + 1):
    if not alphabet == ord('e') and not alphabet == ord('q'):
        print("{:c}".format(alphabet), end="")
print()
