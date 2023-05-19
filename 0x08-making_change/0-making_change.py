#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """function determines the fewest number of coins
    needed to meet a given amount total."""
    counter = 0
    if total <= 0:
        return 0
    sort = sorted(coins, reverse=True)
    for i in range(len(sort)):
        while sort[i] <= total:
            total = total - sort[i]
            counter += 1
    if total == 0:
        return counter
    return -1


"""
    if total <= 0:
        return
    sorted_coins = sorted(coins, reverse=True)
    coin_counter = 0

    for coin in sorted_coins:
        while coin <= total:
            total -= coin
            coin_counter += 1
    if total == 0:
        return coin_counter
    return -1"""
