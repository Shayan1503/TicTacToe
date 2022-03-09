"""
A simple Tic-Tac-Toe game
"""
from player import User, AI
from visual import Board


Winner = ""


# main method
def game():
    # setting things up
    board = Board()
    while True:
        print("Choose shape: X or O")
        shape = input("> ").upper()
        if shape == 'X' or shape == 'O':
            user = User(shape, 0)
            break
        print("Please choose a shape from the given options.")
    shape = 'X' if shape == 'O' else 'O'
    comp = AI(shape, 0, board)

    ipt = input("Do you want to go first? [Y/N] ").upper()
    board.print_initial_board()
    if ipt == 'Y':
        print("You are player1 and I am player2.")
        play(board, user, comp)
    elif ipt == 'N':
        print("You are player2 and I am player1.")
        play(board, comp, user)

    winner(board, comp, user)


# driver method
# player1 goes first, player2 goes second
def play(board, player1, player2):
    while True:

        turn(board, player1, "Player1")
        if winner_exists(board) or not board.moves_available():
            break

        turn(board, player2, "Player2")
        if winner_exists(board) or not board.moves_available():
            break


# playing a turn of each player; works for both user and computer
def turn(board, player, name):
    while True:
        move = player.move()
        if board.legal_move(move):
            print(f"{name} played a move on {move}.")
            board.update_board(move, player.shape)
            board.print_board()
            break
        else:
            print("Illegal move")


# returns True when there is a winner in the current state of the game
def winner_exists(current_board):
    global Winner
    board = current_board.board
    # checking horizontal win
    for row in board:
        current_row = "".join(row)
        if current_row == "XXX" or current_row == "OOO":
            Winner = current_row
            return True

    # checking vertical win
    for col in range(3):
        current_col = "".join((board[0][col], board[1][col], board[2][col]))
        if current_col == "XXX" or current_col == "OOO":
            Winner = current_col
            return True

    # checking diagonal win
    diag1 = "".join((board[0][0], board[1][1], board[2][2]))
    diag2 = "".join((board[0][2], board[1][1], board[2][0]))

    if diag1 == "XXX" or diag1 == "OOO":
        Winner = diag1
        return True
    elif diag2 == "XXX" or diag2 == "OOO":
        Winner = diag2
        return True

    return False


# printing the winner
def winner(final_board, comp, user):
    if winner_exists(final_board):
        if comp.shape in Winner:
            print("I won!")
        elif user.shape in Winner:
            print("You won!")
    else:
        print("It's a tie.")


if __name__ == "__main__":
    game()
