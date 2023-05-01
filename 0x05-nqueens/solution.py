import sys


def is_valid(board, row, col):
    for r, c in board:
        if r == row or c == col or r + c == row + col or r - c == row - col:
            return False
    return True


def n_queens(n, board=[]):
    if len(board) == n:
        print(board)
    else:
        for col in range(n):
            if is_valid(board, len(board), col):
                n_queens(n, board + [(len(board), col)])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

n_queens(n)
