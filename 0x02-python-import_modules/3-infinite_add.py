#!/usr/bin/python3

from sys import argv


def do_something():
    count = 0
    for i in argv[1:]:
        count += int(i)
    print("{}".format(count))


if __name__ == "__main__":
    do_something()
