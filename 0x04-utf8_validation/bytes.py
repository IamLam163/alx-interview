def validUTF8(data):
    num_bytes = 0 
    for byte in data: # itr through dataset
        if num_bytes == 0: # means if we're at start of a new char & 1st bit is 0 
            if byte >> 5 == 0b110: # if first 3 bits are 110 means 2 byte char
                num_bytes = 1 # need to read 1 more byte
            elif byte >> 4 == 0b1110: # means this is 3 byte char
                num_bytes = 2 # need to read 2 more bytes
            elif byte >> 3 == 0b11110: # means this is 4 byte char
                num_bytes = 3 # need to read 3 more bytes
            elif byte >> 7: # this checks if we're in range of data
                return False #if we're out of range return false
        else:
            if byte >> 6 != 0b10: #if we're in the middle if a multibyte char, the two most significant bits of the bytes must be 10, 
                return False #if it is not return false
            num_bytes -= 1 #dcr num_bytes by 1 bcuz one more byte of cur char has been processed
    return num_bytes == 0 #ensures when this condition is met, we've gone through everything in the data set
data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
