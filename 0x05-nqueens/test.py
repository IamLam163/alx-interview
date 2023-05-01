def nqueens(n):
    """function uses recursive backtracking"""
    if not isinstance(n, int):
        print("N must be a number")
        return None
    if n < 4:
        print("N must be at least 4")
        return None

    col = set()
    posDiag = set()  # r+c
    negDiag = set()  # r-c

    res = []
    board = [['.' for i in range(n)] for j in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."

    backtrack(0)
    return res


print(nqueens(4))
