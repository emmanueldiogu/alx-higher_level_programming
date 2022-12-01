#!/usr/bin/python3
from add_0 import add


def do_something():
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a=a, b=b)))


if __name__ == "__main__":
    do_something()
