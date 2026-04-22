N = 8

def is_safe(board, row, col):
    # Check row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(board, col):
    if col == N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve(board, col + 1):
                return True

            board[i][col] = 0  # backtrack

    return False

board = [[0]*N for _ in range(N)]

if solve(board, 0):
    for row in board:
        print(row)
else:
    print("No solution")


# Explanation:
# We place queens one column at a time.
# is_safe() checks if placing a queen is valid.
# If conflict occurs, we backtrack and try another position.
# Backtracking helps in finding a valid solution.