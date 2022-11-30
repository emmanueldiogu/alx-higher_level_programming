#!/usr/bin/python3
def islower(c):
    if type(c) == str and len(c) == 1:
        if (ord(c) >= 97 and ord(c) < 123):
            return True
        else:
            return False
    else:
        return False
