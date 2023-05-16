#!/usr/bin/env python3
import sys


def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [[0 for x in range(n)] for y in range(n)]

    # Check if a queen can be placed at the given row and column
    def is_safe(board, row, col):
        # Check this row on the left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check the upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check the lower diagonal on the left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # If no conflicts, return True
        return True

    # Recursive function to solve the N Queens problem
    def solve(board, col, solutions):
        # Base case: all queens have been placed
        if col == n:
            # Append the solution to the list of solutions
            solutions.append(board)
            return

        # Try placing a queen in each row of the current column
        for row in range(n):
            if is_safe(board, row, col):
                # Place the queen at (row, col)
                board[row][col] = 1
                # Recursively place the remaining queens
                solve(board, col + 1, solutions)
                # Remove the queen from (row, col) and backtrack
                board[row][col] = 0

    # Find all solutions to the N Queens problem
    solutions = []
    solve(board, 0, solutions)

    # Print out the solutions
    for solution in solutions:
        for row in solution:
            print(" ".join(str(x) for x in row))
        print("")


# Parse the command line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

nqueens(n)
