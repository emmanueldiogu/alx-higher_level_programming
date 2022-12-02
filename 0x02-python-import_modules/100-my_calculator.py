#!/usr/bin/python3

from sys import argv, exit
from calculator_1 import add, sub, mul, div

def basic_operations():
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if len(argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif not argv[2] in ops.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    
    print("{} {} {} = {}".format(a, argv[2], b, ops[argv[2]](a, b)))


if __name__ == "__main__":
    basic_operations()
