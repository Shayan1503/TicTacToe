"""
GUI for the game
"""
from tkinter import *
from tkinter import messagebox
import math
from player import AI
from board import Board


class GUI:
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.buttons = []
        self.board = Board()
        self.ai = AI('O', 0, self.board)
        self.Winner = ""

    def start(self):
        self.frame.pack()
        self.createButtons()

        self.root.title("Tic Tac Toe")
        self.root.mainloop()

    def createButtons(self):
        for position in range(0, 9):
            button = Button(self.frame, bg="#30b8b3", height=7, width=14,
                            command=lambda move=position: self.click(move))
            button.grid(row=math.floor(position / 3), column=position % 3)
            self.buttons.append(button)

    def click(self, move):
        self.buttons[move].config(text='X', state=DISABLED, bg="#3bd1c7",
                                  disabledforeground='red', relief='sunken')
        self.board.update_board(move, 'X')

        if not self.board.moves_available():
            messagebox.showinfo(title="Game over", message="It's a tie")
            self.root.quit()

        move = self.ai.move()
        self.buttons[move].config(text='O', state=DISABLED, bg="#3bd1c7",
                                  disabledforeground='blue', relief='sunken')
        self.board.update_board(move, 'O')

        if self.isWinner('O'):
            self.Winner = 'O'
            messagebox.showinfo(title="Game over", message="Yay! I win!")
            self.root.quit()

    def isWinner(self, shape):
        board = self.board.board  # getting board matrix

        # checking horizontal win
        for row in board:
            current_row = "".join(row)
            if current_row == (shape * 3):
                self.Winner = shape
                return True

        # checking vertical win
        for col in range(3):
            current_col = "".join((board[0][col], board[1][col], board[2][col]))
            if current_col == (shape * 3):
                self.Winner = shape
                return True

        # checking diagonal win
        diag = "".join((board[0][0], board[1][1], board[2][2]))
        if diag == (shape * 3):
            return True
        diag = "".join((board[0][2], board[1][1], board[2][0]))
        if diag == (shape * 3):
            return True

        return False


if __name__ == '__main__':
    GUI().start()
