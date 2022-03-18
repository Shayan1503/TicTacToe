"""
Player interface and its subclasses for the game
"""
import math
from abc import abstractmethod
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

    # optimal move from computer; uses minimax algorithm
    def move(self):
        if len(self.board.state["available_moves"]) == 9:
            return random.choice(self.board.state["available_moves"])
        else:
            optimal_move = self.minimax(self.shape, self.board, -math.inf, math.inf)["move_position"]
            return optimal_move

    # minimax algorithm for ai with alpha-beta pruning
    def minimax(self, player, board, alpha, beta):
        # setting things up
        ai = self.shape
        human = 'X' if ai == 'O' else 'O'

        # termination state
        if board.isWinner(human):
            return {
                "move_position": None,
                "weight": -1
            }
        elif board.isWinner(ai):
            return {
                "move_position": None,
                "weight": 1
            }
        elif not board.movesAvailable():
            return {
                "move_position": None,
                "weight": 0
            }

        # setting up a variable that will store the best move
        if player == ai:
            best = {
                "move_position": None,
                "weight": -math.inf  # need to maximize weight
            }
        else:
            best = {
                "move_position": None,
                "weight": math.inf  # need to minimize weight
            }

        # going through all the possible moves
        curr_info = {}
        available_moves = copy.deepcopy(board.state["available_moves"])
        for move in available_moves:
            board.update(move, player)

            if player == ai:
                result = self.minimax(human, board, alpha, beta)
            else:
                result = self.minimax(ai, board, alpha, beta)
            curr_info["weight"] = result["weight"]
            curr_info["move_position"] = move

            # undoing the move
            board.undo(move, player)

            # choosing the best move
            if player == ai:
                if curr_info["weight"] > best["weight"]:
                    best = copy.deepcopy(curr_info)
                if result["weight"] > alpha:
                    alpha = result["weight"]
                if alpha >= beta:
                    break
            else:
                if curr_info["weight"] < best["weight"]:
                    best = copy.deepcopy(curr_info)
                if result["weight"] < beta:
                    beta = result["weight"]
                if alpha >= beta:
                    break
        return best
