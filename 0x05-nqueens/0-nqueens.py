#!/usr/bin/python3
""""""
import sys
from typing import Tuple


def get_input() -> int:
    """Gets the value of n from the commandline and validates it"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def get_attacking_diagonals(N, x, y):
    """Gets and returns all attacking diagonals for the given coordinate"""
    if x < 0 or x > N - 1 or y < 0 or y > N - 1:
        return []
    diagonals = [(x, y)]
    current_x = x - 1
    current_y = y - 1
    while current_x >= 0 and current_y >= 0:
        diagonals.append((current_x, current_y))
        current_x -= 1
        current_y -= 1
    current_x = x - 1
    current_y = y + 1
    while current_x >= 0 and current_y <= N - 1:
        diagonals.append((current_x, current_y))
        current_x -= 1
        current_y += 1
    current_x = x + 1
    current_y = y - 1
    while current_x <= N - 1 and current_y >= 0:
        diagonals.append((current_x, current_y))
        current_x += 1
        current_y -= 1
    current_x = x + 1
    current_y = y + 1
    while current_x <= N - 1 and current_y <= N - 1:
        diagonals.append((current_x, current_y))
        current_x += 1
        current_y += 1
    return diagonals


def is_non_attacking_square(N: int, possible_solution, x: int, y: int):
    """Checks if a queen can be placed in a square without
    it attacking any other queen
    """
    for [i, j] in possible_solution:
        if x == i:
            return False
        if y == j:
            return False
        if (x, y) in get_attacking_diagonals(N, i, j):
            return False
    return True


def move_to_next_square(N: int, x: int, y: int) -> Tuple[int, int]:
    """Moves to the next square based on N"""
    if y < N - 1:
        y += 1
    else:
        y = 0
        x += 1
    return (x, y)


def build_solution(N: int, x: int, y: int, built_solution=[], calls=0):
    """Recursively builds a solution for given a starting square"""
    calls += 1
    i = x
    j = y
    while i <= N - 1 and j <= N - 1:
        if is_non_attacking_square(N, built_solution, i, j):
            built_solution.append([i, j])
        i, j = move_to_next_square(N, i, j)
    if len(built_solution) == N:
        return built_solution
    if len(built_solution) == 0:
        return built_solution
    last = built_solution.pop()
    if len(built_solution) == 0:
        return built_solution
    i, j = move_to_next_square(N, last[0], last[1])
    return build_solution(N, i, j, built_solution, calls)


def nqueens(N=4):
    """Gets a set of solutions for the N queens problem"""
    for i in range(0, N):
        for j in range(0, N):
            solution = build_solution(N, i, j, [])
            # print(f"{i},{j}: {solution}")
            if len(solution) == N:
                print(solution)


n = get_input()
nqueens(n)
