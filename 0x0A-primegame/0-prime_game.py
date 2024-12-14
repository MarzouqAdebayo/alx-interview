#!/usr/bin/python3
"""Module '0-prime_gam.py' """


def sieve_of_eratosthenes(n):
    """Prints all prime numbers from 2 to n"""
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if prime[p]]


def isWinner(x, nums):
    """Simulates game play for prime game"""
    map = {"Maria": 0, "Ben": 0}
    for i in range(x):
        current_player = "Maria"
        primes = sieve_of_eratosthenes(nums[i])
        for prime in primes:
            if current_player == "Maria":
                current_player = "Ben"
            else:
                current_player = "Maria"
        if current_player == "Maria":
            map["Ben"] += 1
        else:
            map["Maria"] += 1
    return "Maria" if map["Maria"] > map["Ben"] else "Ben"
