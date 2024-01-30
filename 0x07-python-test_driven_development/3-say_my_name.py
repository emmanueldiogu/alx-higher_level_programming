#!/usr/bin/python3
"""Print my name is <first_name> <last_name>
first_name and last_name must be strings otherwise, raise TypeError
"""


def say_my_name(first_name, last_name=""):
    """Function to print "My name is ..."

    Args:
        first_name (str): First name must be a string
        last_name (str, optional): Last name. Defaults to "".
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))