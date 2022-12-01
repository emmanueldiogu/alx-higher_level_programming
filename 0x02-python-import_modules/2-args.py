#!/usr/bin/python3

from sys import argv


print("{} arguments".format(len(argv[1:])))
count = 1
for i in argv[1:]:
    print("{}: {}".format(count, i))
    count += 1
