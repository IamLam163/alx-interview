def minOperations(n):
    if n == 1:
        return 0
    operations = 0
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1
    if n > 1:
        operations += n

    return operations

'''
def minOperations(n):
    if n == 1:    # If n is 1, then we only need to insert a single H character
        return 0

    operations = 0    # Counter for the number of operations performed
    factor = 2    # Starting factor for the Copy All operation

    while n > 1:
        while n % factor == 0:    # Repeatedly perform Copy All and Paste operations as long as possible
            operations += 2
            n /= factor
        factor += 1

    if n == 1:    # If we successfully obtain n H characters, return the number of operations performed
        return operations
    else:    # If n cannot be obtained, return 0
        return 0
'''
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

