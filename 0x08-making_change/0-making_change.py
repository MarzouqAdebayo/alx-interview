#!/usr/bin/python3
"""Making Change module '0-making_change.py' """


def makeChange(coins, sum):
    """Calculates the fewest number of coins
    needed to make change given a sum and a list
    of coins
    """
    if sum <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(sorted_coins)
    rem = sum
    no_of_change = 0
    i = 0
    while rem > 0:
        if i > n - 1:
            return -1
        soln = rem // sorted_coins[i]
        if soln >= 1:
            no_of_change += soln
            rem = rem % sorted_coins[i]
        i += 1
    if rem != 0:
        return -1
    return no_of_change
