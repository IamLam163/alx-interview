#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the 
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """function determines the fewest number of coins 
    needed to meet a given amount total."""
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
    return -1
