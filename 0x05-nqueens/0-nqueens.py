#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard.
"""
import sys


def isValid(board, row, col):
    """checks if the queen move is valid"""
    for r, c in board:
        if r == row or c == col or r + c == row + col or r - c == row - col:
            return False
    return True


def nqueens(n, board=[]):
    """function uses recursive backtracking"""
    if len(board) == n:
        print(board)
    else:
        for col in range(n):
            if isValid(board, len(board), col):
                nqueens(n, board + [(len(board), col)])


if len(sys.argv) != 2:
    print("Usuage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

nqueens(n)
