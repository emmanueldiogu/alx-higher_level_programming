#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for s in str:
        if i != n:
            print(s, end="")
        i += 1
    return ""
