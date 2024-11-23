#!/usr/bin/python3
"""Module 'debug.py' """
import sys
import time


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


def nqueens(board, col, N, solutions):
    """Gets a set of solutions for the N queens problem"""
    # if col >= N:
    #     solution = []
    #     for i in range(N):
    #         for j in range(N):
    #             if board[i][j] == 1:
    #                 solution.append([i, j])
    #     solutions.append(solution)
    #     return

    for row in range(1):
        board[row][col] = 1
        print(board[row][col])
        # if is_valid_square(N, board, row, col):
        #     board[row][col] = 1
        #     # Recursive call to place remaining queens
        #     nqueens(board, col + 1, N, solutions)
        #     # Backtracking here
        #     board[row][col] = 0


def main():
    """Main"""
    n = get_input()
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    nqueens(board, 0, n, solutions)
    print(board)
    for solution in solutions:
        print(solution)


# start_time = time.perf_counter()
main()
# end_time = time.perf_counter()
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")
