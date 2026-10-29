"""A simple two-player XOX (Tic-Tac-Toe) game using basic Python."""


def show_board(board):
    """Print the nine squares with their current contents."""
    print()
    for row in range(3):
        start = row * 3
        print(" " + " | ".join(board[start:start + 3]))
        if row < 2:
            print("---+---+---")
    print()


def has_won(board, mark):
    """Check each row, column, and diagonal for three matching marks."""
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]

    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] == mark:
            return True
    return False


def play_game():
    # The numbered squares help players choose a position.
    board = [str(number) for number in range(1, 10)]
    current_player = "X"
    moves = 0

    print("Welcome to XOX! Choose a square from 1 to 9.")

    while moves < 9:
        show_board(board)
        choice = input(f"Player {current_player}, choose a square: ").strip()

        # Conditions reject anything except an available square number.
        if choice not in "123456789" or len(choice) != 1:
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice) - 1
        if board[position] in ("X", "O"):
            print("That square is taken. Choose an empty one.")
            continue

        board[position] = current_player
        moves += 1

        if has_won(board, current_player):
            show_board(board)
            print(f"Player {current_player} wins! Great game!")
            return

        # Switch turns after a valid move.
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    show_board(board)
    print("It's a draw!")


if __name__ == "__main__":
    play_game()
