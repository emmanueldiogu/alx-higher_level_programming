#!/usr/bin/python3
"""print text with 2 new line after ".","?",":"
Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with the message text must be a string
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: '.', '?' and ':'

    Args:
        text (str): text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    delim = ['.', ':', '?']
    n = 0
    while n < len(text):
        if text[n] in delim and n != len(text) - 1:
            print(text[n], end='')
            print('\n')
            if text[n + 1] == ' ':
                n += 1
        else:
            print(text[n], end='')
        n += 1
