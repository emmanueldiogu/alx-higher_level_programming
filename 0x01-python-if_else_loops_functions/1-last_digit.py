#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if (number < 0):
    last_digit *= -1
msg = f"Last digit of {number:d} is {last_digit:d} and is "

# if the last digit is greater than 5: the string and is greater than 5
if (last_digit > 5):
    msg += "greater than 5"
    print(msg)
# if the last digit is 0: the string and is 0
elif (last_digit == 0):
    msg += "0"
    print(msg)
# if the last digit is less than 6 and not 0:
# the string and is less than 6 and not 0
elif (last_digit < 6 and last_digit != 0):
    msg += "less than 6 and not 0"
    print(msg)
