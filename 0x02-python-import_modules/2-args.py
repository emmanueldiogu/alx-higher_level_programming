#!/usr/bin/python3

from sys import argv


print("{} {}".format(len(argv[1:]), 'argument' if (len(argv[1:]) == 1) else 'arguments'))
count = 1
for i in argv[1:]:
    print("{}: {}".format(count, i))
    count += 1
