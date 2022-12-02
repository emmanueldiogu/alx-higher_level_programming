#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

def basic_operations():
    operators = ['*', '-', '+', '/']
    print(len(argv[1:]))
    if len(argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif len(argv[2]) not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    pass


if __name__ == "__main__":
    basic_operations()