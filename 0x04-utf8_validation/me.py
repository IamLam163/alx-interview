#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if (byte & 0b10000000) == 0b00000000:
                num_bytes = 0
            elif (byte & 0b11100000) == 0b11000000:
                num_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                num_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                num_bytes = 3
            else:
                return False
        else:
            if (byte & 0b11000000) != 0b10000000:
                return False
            num_bytes -= 1
    return num_bytes == 0


data = [467, 133, 108]
print(validUTF8(data))
data = [240, 188, 128, 167]
print(validUTF8(data))
data = [235, 140]
print(validUTF8(data))
data = [345, 467]
print(validUTF8(data))
data = [250, 145, 145, 145, 145]
print(validUTF8(data))
data = [0, 0, 0, 0, 0, 0]
print(validUTF8(data))
data = []
print(validUTF8(data))
