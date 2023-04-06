#!/usr/bin/python3
'''finding the minimum operations using prime factors'''


def minOperations(n):
    '''function finds the minimum operations using prime factors
    e.g if n = 12, prime factors = [2, 2, 3] when added = 7 operations'''
    if n == 1:  # if there's only H return 0
        return 0
    factor = 2  # start at the lowest possible prime factor
    operations = 0  # operations gets the no of operations

    while factor * factor <= n:  # factor squared is less or = n
        if n % factor == 0:  # checks for all the prime factors
            operations += factor  # adds the factor to operations
            n //= factor  # n divides factor to reduce n for next iteration
        else:
            factor += 1  # if number is not a factor, increment the factor
    if n > 1:  # adds the remaining prime factors of n
        operations += n
    return operations
