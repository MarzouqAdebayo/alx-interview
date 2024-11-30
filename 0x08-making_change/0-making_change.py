#!/usr/bin/python3
"""Making Change module '0-making_change.py' """


def makeChangeInEff(coins, sum):
    if sum <= 0:
        return 0
    table = {0: 0}
    for i in range(1, sum + 1):
        for coin in coins:
            sub = i - coin
            if sub < 0:
                break
            curr = table.get(i, sum + 1)
            prev = table.get(sub, sum + 1)
            table[i] = min(prev + 1, curr)
    if table.get(sum) and (table[sum] <= 0 or table[sum] > sum):
        return -1
    return table[sum]


def makeChange(coins, sum):
    if sum <= 0 or len(coins) <= 0:
        return 0
    sorted_coins = sorted(coins)
    n = len(sorted_coins)
    rem = sum
    no_of_change = 0
    i = n - 1
    while rem > 0:
        if i > n - 1 or i < 0:
            break
        soln = rem // sorted_coins[i]
        if soln >= 1:
            no_of_change += soln
            rem = rem - (soln * sorted_coins[i])
        i -= 1
    if rem != 0:
        return -1
    return no_of_change
