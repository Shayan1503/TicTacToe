"""
Player interface and its subclasses for the Tic-Tac-Toe game
"""
import math
from abc import abstractmethod
from Visual import Board
import random
import copy


# Parent class
class Player:

    def __init__(self, shape, score):
        self.shape = shape
        self._score = score

    @abstractmethod
    def move(self):
        pass

    # getter method for score
    @property
    def score(self):
        return self._score

    # setter method for score
    @score.setter
    def score(self, new_score):
        self._score = new_score


# Child class for the user
class User(Player):

    def __init__(self, shape, score):
        super().__init__(shape, score)

    def move(self):
        return int(input("Enter your move: "))


# Child class for the computer
class AI(Player):

    def __init__(self, shape, score, board):
        super().__init__(shape, score)
        self.board = board

    # purely random move from computer
    # def move(self):
    #     moves_available = self.board.state["available_moves"]
    #     return random.choice(moves_available)

    # optimal move from computer; uses minimax algorithm
    def move(self):
        if len(self.board.state["available_moves"]) == 9:
            return random.choice(self.board.state["available_moves"])
        else:
            optimal_move = self.minimax(self.shape, self.board)["move_position"]
            return optimal_move

    # minimax algorithm for tictactoe ai
    def minimax(self, player, board):
        # setting things up
        ai = self.shape
        human = 'X' if ai == 'O' else 'O'
        curr_board = copy.deepcopy(board)

        # termination state
        if self.is_winner(human, curr_board):
            return {
                "move_position": None,
                "weight": -1
            }
        elif self.is_winner(ai, curr_board):
            return {
                "move_position": None,
                "weight": 1
            }
        elif not curr_board.moves_available():
            return {
                "move_position": None,
                "weight": 0
            }

        # setting up a variable that will store the best move
        if player == ai:
            best = {
                "move_position": None,
                "weight": -math.inf
            }
        else:
            best = {
                "move_position": None,
                "weight": math.inf
            }

        # going through all the possible moves
        curr_info = {}
        available_moves = copy.deepcopy(curr_board.state["available_moves"])
        for move in available_moves:
            # curr_info = {}
            curr_board.update_board(move, player)

            if player == ai:
                result = self.minimax(human, curr_board)
            else:
                result = self.minimax(ai, curr_board)
            curr_info["weight"] = result["weight"]
            curr_info["move_position"] = move

            curr_board = copy.deepcopy(board)

            # choosing the best move
            if player == ai:
                if curr_info["weight"] > best["weight"]:
                    best = copy.deepcopy(curr_info)
            else:
                if curr_info["weight"] < best["weight"]:
                    best = copy.deepcopy(curr_info)

        return best

    # return True if the given player is a winner
    # better method of finding winner may exist; look further into it
    # using 'in' to reduce runtime
    def is_winner(self, player, board):
        if player == 'X':
            moves = board.state["X_moves"]
        else:
            moves = board.state["O_moves"]

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
