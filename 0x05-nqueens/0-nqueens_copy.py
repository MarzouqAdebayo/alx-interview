#!/usr/bin/python3
"""Module '0-nqueens.py' """
import sys
import time
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


def is_attacking(queen_a, queen_b):
    """"""
    if queen_a[0] == queen_b[0] or queen_a[1] == queen_b[1]:
        return True
    return abs(queen_a[0] - queen_b[0]) == abs(queen_a[1] - queen_b[1])


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


def is_valid_square(N: int, possible_solution, x: int, y: int):
    for item in possible_solution:
        is_attack = is_attacking(item, [x, y])
        if is_attack:
            return False
    return True


def move_to_next_square(
    N: int, x: int, y: int, nextRow: bool = False
) -> Tuple[int, int]:
    """Moves to the next square based on N"""
    if not nextRow and y < N - 1:
        y += 1
    else:
        y = 0
        x += 1
    return (x, y)


# def validate_solution(N: int, solution):
#     if len(solution) != N:
#         return False
#     for i, j in solution:
#         if is_non_attacking_square(N, solution, i, j):
#             return False
#     return True


def validate_solution(N: int, solution):
    if len(solution) != N:
        return False
    for i, j in solution:
        if is_valid_square(N, solution, i, j):
            return False
    return True


def generate_squares(N: int, i: int, j: int, solution=[]):
    while i <= N - 1 and j <= N - 1:
        if is_valid_square(N, solution, i, j):
            solution.append([i, j])
            i, j = move_to_next_square(N, i, j, nextRow=True)
        else:
            i, j = move_to_next_square(N, i, j)
    return solution


def build_solution(N: int, i: int, j: int, all_solutions=[]):
    solution = []
    x = i
    y = j
    while True:
        solution = generate_squares(N, x, y, solution)
        if not len(solution):
            return None
        if len(solution) == N:
            all_solutions.append(solution)
        if len(solution) > 0:
            new_i, new_j = solution.pop()
            x, y = move_to_next_square(N, new_i, new_j)
        else:
            break
    return None


def nqueens(N=4):
    """Gets a set of solutions for the N queens problem"""
    for i in range(0, N):
        # solution = build_solution(N, i, j, [], [i, j])
        solution = build_solution(N, 0, i)
        if solution:
            print(solution)


n = get_input()
start_time = time.perf_counter()
nqueens(n)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
