"""
Board layout for the Tic-Tac-Toe game
"""
import math


class Board:

    def __init__(self):
        # state is a dictionary that represents the current 'state' of the board
        self.state = {
            "available_moves": [0, 1, 2, 3, 4, 5, 6, 7, 8],
            "X_moves": [],
            "O_moves": [],
            "all_moves": []
        }
        # visual representation of the board via a matrix
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    def moves_available(self):
        return len(self.state["available_moves"]) != 0

    def legal_move(self, move):
        if self.moves_available():
            return move in self.state["available_moves"]
        return False

    # updating the board along with the state
    def update_board(self, move, shape):
        self.update_state(move, shape)

        state = self.state
        for pos in range(9):
            if pos in state["all_moves"]:
                if pos in state["X_moves"]:
                    self.board[math.floor(pos / 3)][pos % 3] = 'X'
                elif pos in state["O_moves"]:
                    self.board[math.floor(pos / 3)][pos % 3] = 'O'

    # updating the state alone; may join it with method update_board()
    def update_state(self, move, shape):
        state = self.state

        if shape == 'X':
            state["X_moves"].append(move)
        else:
            state["O_moves"].append(move)

        state["all_moves"] = state["X_moves"] + state["O_moves"]
        for move in state["all_moves"]:
            if move in state["available_moves"]:
                state["available_moves"].remove(move)

    def print_board(self):
        for row in self.board:
            for pos in row:
                print(f"|{pos}|", end="")
            print()

    # printing an initial layout of the board with boxes numbered
    def print_initial_board(self):
        counter = 0
        for i in range(3):
            for j in range(3):
                print(f"|{counter}|", end="")
                counter += 1
            print()
