#!/usr/bin/python3
"""Module '0-minoperations.py' contains minoperations"""


def minOperations(n: int):
    """Computes the fewest number of operations needed to give exactly
    n 'H' characters"""
    if not isinstance(n, int):
        return 0
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
