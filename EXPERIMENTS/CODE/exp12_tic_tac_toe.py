def print_board(board):
    for r in range(3):
        print(f" {board[r][0]} | {board[r][1]} | {board[r][2]} ")
        if r < 2:
            print("---|---|---")
    print()

def check_winner(board, player):
    for r in range(3):
        if all(board[r][c] == player for c in range(3)):
            return True
    for c in range(3):
        if all(board[r][c] == player for r in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game(moves):
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Initial Board:")
    print_board(board)

    for r, c in moves:
        if board[r][c] == " ":
            board[r][c] = current_player
            print(f"Player {current_player} places at ({r}, {c}):")
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                return

            if is_board_full(board):
                print("Game is a Draw!")
                return

            current_player = "O" if current_player == "X" else "X"

sample_game_moves = [
    (0, 0), (1, 1),
    (0, 1), (1, 0),
    (0, 2)
]

play_game(sample_game_moves)
