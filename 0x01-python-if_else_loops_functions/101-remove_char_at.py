#!/usr/bin/python3
def remove_char_at(str, n):
    """
    return the string without the nth char
    """
    new_str = ""
    for i in range(len(str)):
        if i == n:
            continue
        new_str += str[i]
    return new_str
