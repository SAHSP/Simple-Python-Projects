# Tic-Tac-Toe Game

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if there is a winner
def check_winner(board, player):
    # Check all winning combinations
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                        (0, 4, 8), (2, 4, 6)]             # diagonals
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (i.e., a tie)
def is_board_full(board):
    return ' ' not in board

# Main function to handle the Tic-Tac-Toe game logic
def play_game():
    # Initialize the board
    board = [' ' for _ in range(9)]
    
    # Current player ("X" or "O")
    current_player = "X"
    
    # Game loop
    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
        
        # Check if the move is valid
        if board[move] == ' ':
            board[move] = current_player
        else:
            print("Invalid move! Try again.")
            continue
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! 🎉")
            break
        
        # Check if the game is a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie! 🤝")
            break
        
        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
