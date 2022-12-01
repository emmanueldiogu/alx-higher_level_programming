#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def do_something():
    a = 10
    b = 5
    
    print("{} + {} = {}".format(a, b, add(a=a, b=b)))
    print("{} - {} = {}".format(a, b, sub(a=a, b=b)))
    print("{} * {} = {}".format(a, b, mul(a=a, b=b)))
    print("{} / {} = {}".format(a, b, div(a=a, b=b)))


if __name__ == "__main__":
    do_something()