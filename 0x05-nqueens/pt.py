#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]"""

    # Check the row on the left side
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, N, solutions):
    """Use backtracking to find all solutions"""
    # Base case: If all queens are placed, store the solution
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Try placing queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col, N):
            # Place queen
            board[row][col] = 1

            # Recur to place rest of the queens
            solve_nqueens(board, col + 1, N, solutions)

            # Backtrack: remove queen to try other positions
            board[row][col] = 0


def validate_input():
    """Validate command line input"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


def main():
    # Validate input
    N = validate_input()

    # Initialize the chessboard
    board = [[0 for x in range(N)] for y in range(N)]

    # Store all solutions
    solutions = []

    # Find all solutions
    solve_nqueens(board, 0, N, solutions)

    # Print solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
