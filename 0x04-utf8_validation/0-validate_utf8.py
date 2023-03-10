#!/usr/bin/python3
"""
Will validate UTF8 module
"""


def validUTF8(data):
    """validUTF8
    Determines if given data set represents a valid UTF-8 encoding.
    """
    valid = 0
    for value in data:
        byte = value & 255
        if valid:
            if byte >> 6 != 2:
                return False
            valid -= 1
            continue
        while (1 << abs(7 - valid)) & byte:
            valid += 1
        if valid == 1 or valid > 4:
            return False
        valid = max(valid - 1, 0)
    return valid == 0
