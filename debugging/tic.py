#!/usr/bin/python3

def print_board(board):
    """Print the game board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        # MODIFICATION: Don't print dashes after the last row
        if i < len(board) - 1:
            print("-" * 9)

def check_winner(board):
    """Check if there's a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Check diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

# MODIFICATION: Added function to check if board is full (draw condition)
def is_board_full(board):
    """Check if the board is completely filled."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main game function."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    # MODIFICATION: Changed while condition to check for both winner and draw
    while True:
        print_board(board)
        
        # MODIFICATION: Added try-except block to handle invalid input
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            # MODIFICATION: Check if input is within valid range
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Row and column must be 0, 1, or 2.")
                continue
            
            # Check if the spot is already taken
            if board[row][col] == " ":
                board[row][col] = player
                
                # MODIFICATION: Check for winner BEFORE changing player
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                
                # MODIFICATION: Check for draw
                if is_board_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                
                # Switch player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        
        # MODIFICATION: Catch ValueError for non-numeric input
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        
        # MODIFICATION: Catch IndexError for out of range input
        except IndexError:
            print("Invalid input! Row and column must be 0, 1, or 2.")

tic_tac_toe()
