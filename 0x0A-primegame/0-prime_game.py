#!/usr/bin/python3
"""
Prime Game Interview Question
"""


def isPrime(n):
    """Checks if a number is prime"""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """function returns winner"""
    maria = 0
    ben = 0
    for i in range(x):
        noRounds = nums[i]
        prime_count = sum(isPrime(num) for num in range(2, noRounds + 1))

        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
