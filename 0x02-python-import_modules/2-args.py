#!/usr/bin/python3

from sys import argv


def do_something():
    print("{} {}".format(len(argv[1:]), 'argument:' if (len(argv[1:]) == 1) else 'arguments:'))
    count = 1
    for i in argv[1:]:
        print("{}: {}".format(count, i))
        count += 1

if __name__ == "__main__":
    do_something()