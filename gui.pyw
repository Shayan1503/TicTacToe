"""
GUI for the game
"""
import sys
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

    def start(self):
        self.frame.pack()
        self.createButtons()

        self.root.title("Tic Tac Toe")
        self.root.mainloop()

    def createButtons(self):
        for position in range(0, 9):
            button = Button(self.frame, bg="#30b8b3", text=" ", font=("Helvetica", 25),
                            height=2, width=4, command=lambda move=position: self.click(move))
            button.grid(row=math.floor(position / 3), column=position % 3)
            self.buttons.append(button)

    def click(self, move):
        self.buttons[move].config(text='X', state=DISABLED, bg="#3bd1c7",
                                  disabledforeground='red', relief='sunken')
        self.board.update(move, 'X')

        if self.board.movesAvailable():
            move = self.ai.move()
            self.buttons[move].config(text='O', state=DISABLED, bg="#3bd1c7",
                                      disabledforeground='blue', relief='sunken')
            self.board.update(move, 'O')

            if self.board.isWinner('O'):
                self.endScreen("Yay! I win!")
        else:
            self.endScreen("It's a tie.")

    def endScreen(self, message):
        retry = messagebox.askyesno(title="Game over", message=message+"\nWant to play again?")
        self.root.destroy()
        if retry:
            GUI().start()


if __name__ == '__main__':
    GUI().start()
