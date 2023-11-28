#!/usr/bin/python3
def islower(c):
    """
    return True if is lower else return false
    """
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False
