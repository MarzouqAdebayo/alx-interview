#!/usr/bin/python3

isWinner = __import__("0-prime_game").isWinner
primes = __import__("0-prime_game").sieve_of_eratosthenes


print(primes(1))
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(5, [1])))
print("Winner: {}".format(isWinner(5, [])))
# print("Winner: {}".format(isWinner(5, [])))
# print("Winner: {}".format(isWinner(5, [])))
