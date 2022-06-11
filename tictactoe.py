""" Tic-Tac-Toe
Love is a game of tic-tac-toe,
Constantly waiting for the next x or o.

- Lang Leav -

Author: Lutho Masoka
"""
import os


def main():
    game = True
    players = ("X", "O")
    turn = 0
    board = create_board()

    while game:
        turn += 1
        display_board(board)
        if turn:
            player = get_current_player(players, turn)
            square = int(input(f"{player}'s turn to choose a square (1-9): "))
            valid_square = validate_input(square, board, player)
            board[valid_square - 1] = player
        
        if has_winner(board):
            game = False
            print("\nWell Done!")
        elif determine_if_draw(board):
            game = False
            print("\nDraw!")

    os.system('color 7')
    print()
    print("Game Over. Thanks for playing.")


def validate_input(user_input, board, player):
    """Validates user's input.

    Parameters: 
        user_input: The input of the user
        board: A list of intergers representing available positions
                on the board.
        player: The current player

    Return: A valid input
    """
    while user_input > (len(board) + 1) or user_input < 0 and user_input not in board:
        os.system('color 4')
        print("\nPlease select valid position on board")
        print()
        user_input = int(input(f"{player}'s turn to choose a square (1-9): ")) 
    else:
        return user_input

 
def get_current_player(players, turn):
    """Determines current player between X and O.

    Parameters: 
        players: A tuple holding both players
        turn: An interger representing the current turn

    Return: A valid input
    """
    if turn % 2 == 0:
        os.system('color 2')
        return players[1]
    else:
        os.system('color 1')
        return players[0]


def create_board():
    """Determines numbers of positions on board"""
    board = []
    for square in range(9):
        board.append(square + 1)
    return board


def display_board(board):
    """Displays positions on board.

    Parameters: 
            board: A list of intergers representing available positions
                on the board.
    """
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


def determine_if_draw(board):
    """Determines if game has a draw.

    Parameters: 
        board: A list of intergers representing available positions and occupied positions by either X or O
                on the board.

    Return: False if there is no draw otherwise True if there is.
    """
    if any(isinstance(square, int) for square in board):
        return False
    return True


def has_winner(board):
    """Determines if there is a winner.

    Parameters: 
        board: A list of intergers representing available positions and occupied positions by either X or O
                on the board.

    Return: False if there is no winner otherwise True if there is.
    """
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


if __name__ == "__main__":
    main()