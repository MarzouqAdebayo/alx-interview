#!/usr/bin/python3
"""Making Change module '0-making_change.py' """


def makeChange(coins, sum):
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
