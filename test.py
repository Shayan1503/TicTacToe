"""
To test runtime and AI logic
"""
import random
from player import AI
from visual import Board
import timeit


Winner = ""
record = {
    "won": 0,
    "lose": 0,
    "tie": 0
}


# driver method
# player1 goes first, player2 goes second
def play(board, player1, player2):
    while True:

        turn(board, player1)
        if winner_exists(board) or not board.moves_available():
            break

        turn(board, player2)
        if winner_exists(board) or not board.moves_available():
            break


# playing a turn of each player; works for both user and computer
def turn(board, player):
    if player.shape == 'X':
        move = player.move()
        if board.legal_move(move):
            board.update_board(move, player.shape)
    else:
        move = random.choice(board.state["available_moves"])
        board.update_board(move, player.shape)


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
def winner(final_board, player1, player2):
    if winner_exists(final_board):
        if player1.shape in Winner:
            record["won"] += 1
        elif player2.shape in Winner:
            record["lose"] += 1
    else:
        record["tie"] += 1


number_test = int(input("Enter how many tests you want to do: "))
start = timeit.default_timer()
for test in range(0, number_test):
    board = Board()
    player1 = AI('X', 0, board)  # AI
    player2 = AI('O', 0, board)  # randomised player

    play(board, player1, player2)

    winner(board, player1, player2)

end = timeit.default_timer()
won = record["won"]
lose = record["lose"]
tie = record["tie"]
print(f"Did {number_test} tests. It took {end - start}s")
print(f"Won {won} time(s).")
print(f"Lost {lose} time(s).")
print(f"Had a tie {tie} time(s).")
input()
