BOARD_SIZE = 8

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < BOARD_SIZE and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens_util(board, col, solutions):
    if col >= BOARD_SIZE:
        solutions.append([row[:] for row in board])
        return

    for row in range(BOARD_SIZE):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens_util(board, col + 1, solutions)
            board[row][col] = 0

def print_board(board):
    for r in range(BOARD_SIZE):
        print(" ".join("Q" if board[r][c] == 1 else "." for c in range(BOARD_SIZE)))
    print()

board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
solutions = []
solve_n_queens_util(board, 0, solutions)

print(f"Total solutions: {len(solutions)}\n")
for idx, sol in enumerate(solutions[:3], 1):
    print(f"Solution {idx}:")
    print_board(sol)
