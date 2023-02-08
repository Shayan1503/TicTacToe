"""
Board layout for the game
"""
import math


class Board:

    def __init__(self):
        # state is a dictionary that represents the current 'state' of the board
        self.state = {
            "available_moves": [0, 1, 2, 3, 4, 5, 6, 7, 8],
            "X_moves": [],
            "O_moves": []
        }

    def movesAvailable(self):
        return len(self.state["available_moves"]) != 0

    def legalMove(self, move):
        if self.movesAvailable():
            return move in self.state["available_moves"]
        return False

    # updating the state of the board
    def update(self, move, shape):
        state = self.state
        # updating state
        if shape == 'X':
            state["X_moves"].append(move)
        else:
            state["O_moves"].append(move)
        state["available_moves"].remove(move)

    def isWinner(self, shape):
        if shape == 'X':
            moves = self.state["X_moves"]
        else:
            moves = self.state["O_moves"]

        # checking horizontal win
        if (0 in moves and 1 in moves and 2 in moves) or \
                (3 in moves and 4 in moves and 5 in moves) or \
                (6 in moves and 7 in moves and 8 in moves):
            return True

        # checking vertical win
        if (0 in moves and 3 in moves and 6 in moves) or \
                (1 in moves and 4 in moves and 7 in moves) or \
                (2 in moves and 5 in moves and 8 in moves):
            return True

        # checking diagonal win
        if (0 in moves and 4 in moves and 8 in moves) or \
                (2 in moves and 4 in moves and 6 in moves):
            return True

        return False

    # undoing a move
    def undo(self, move, shape):
        state = self.state
        # undoing state
        if shape == 'X':
            state["X_moves"].remove(move)
        else:
            state["O_moves"].remove(move)
        state["available_moves"].append(move)

    def renew(self):
        self.state["available_moves"] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.state["X_moves"] = []
        self.state["O_moves"] = []
