#!/usr/bin/env python3
"""
method that determines if a given data set represents a valid UTF-8 encoding.
"""

# step1: initilize a variable to track the byte
# step2: itr through the data set
# step3: check condition for a single bytes
# step4: if it is a single bytes check n+1 bit
# step5: fl

def validUTF8(data):
    """method that determines if a given data set represents a valid UTF-8 encoding.
    """ 
    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
