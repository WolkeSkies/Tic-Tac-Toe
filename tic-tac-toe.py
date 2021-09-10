from tkinter import *


class Game:
    def __init__(self, board):
        self.root = Tk()
        self.board = board
        self.board_values = []
        self.board_values_pos = []
        self.board()

    def refresh(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def move(self, row, column):
        print(self.board_values)
        self.board_values[row][column] = "X"
        self.board()

    def board(self):
        self.refresh()
        for row in range(self.board):
            self.board_values.append([])
            for column in range(self.board):
                self.board_values[row].append(None)
        print(self.board_values)
        self.root.mainloop()


Game(3)
