#!/usr/bin/env python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)), end="")
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)), end="")
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)), end="")
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)), end="")
