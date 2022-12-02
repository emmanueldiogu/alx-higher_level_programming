#!/usr/bin/python3

def no_c(my_string):
    for strng in my_string:
        if strng == 'c' or strng == 'C':
            strng = ''
        print(strng, end='')
    return ''
