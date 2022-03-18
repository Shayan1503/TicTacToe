"""
To test runtime and AI logic
"""
import random
from player import AI
from board import Board
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
    global Winner
    while True:

        turn(board, player1)
        if board.isWinner(player1.shape):
            Winner = player1.shape
            break
        elif not board.movesAvailable():
            Winner = ""
            break

        turn(board, player2)
        if board.isWinner(player1.shape):
            Winner = player2.shape
            break
        elif not board.movesAvailable():
            Winner = ""
            break


# playing a turn of each player; works for both user and computer
def turn(board, player):
    if player.shape == 'X':
        move = player.move()
        if board.legalMove(move):
            board.update(move, player.shape)
    else:
        move = random.choice(board.state["available_moves"])
        board.update(move, player.shape)


number_test = int(input("Enter how many tests you want to do: "))
start = timeit.default_timer()
for test in range(0, number_test):
    board = Board()
    player1 = AI('X', 0, board)  # AI
    player2 = AI('O', 0, board)  # randomised player

    play(board, player1, player2)

    if player1.shape == Winner:
        record["won"] += 1
    elif player2.shape == Winner:
        record["lose"] += 1
    else:
        record["tie"] += 1

end = timeit.default_timer()
won = record["won"]
lose = record["lose"]
tie = record["tie"]
print(f"Did {number_test} tests. It took {end - start}s")
print(f"Won {won} time(s).")
print(f"Lost {lose} time(s).")
print(f"Had a tie {tie} time(s).")
input()
