from tkinter import *


class Game:
    def __init__(self, board):
        self.root = Tk()
        self.board_size = board
        self.board_values = []
        self.board_values_pos = []
        self.board_buttons = []
        self.row = 0
        self.column = 0
        self.screen = 0
        self.turn = 0
        self.board()

    def refresh(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.draw_board()

    def empty_board(self):
        for row in range(self.board_size):
            self.board_values.append([])
            self.board_values_pos.append([])
            self.board_buttons.append([])
            for column in range(self.board_size):
                self.board_values[row].append(" ")
                self.board_values_pos[row].append([row, column])
                Button(self.root, text=self.board_values[row][column], height=5, width=10,
                       command=lambda r=row, c=column: self.move([r, c])).grid(row=row, column=column)
        self.screen = 1

    def draw_board(self):
        for row in range(self.board_size):
            for column in range(self.board_size):
                Button(self.root, text=self.board_values[row][column], height=5, width=10,
                       command=lambda r=row, c=column: self.move([r, c])).grid(row=row, column=column)

    def move(self, pos):
        self.turn += 1
        if self.turn % 2 == 1:
            self.board_values[pos[0]][pos[1]] = "X"
        else:
            self.board_values[pos[0]][pos[1]] = "O"
        print(self.check_win())
        self.refresh()

    def check_win(self):
        # Horizontal
        count = 0
        for row in self.board_values:
            for column in row:
                if count == 0:
                    fvalue = column
                if fvalue == column:
                    count += 1
                if count == self.board_size and fvalue == "X":
                    print("True")
                    return "X"
                if count == self.board_size and fvalue == "O":
                    return "O"
        """# Vertical
        count = 0
        for column in range(len(self.board_values[0])):
            values = []
            for row in range(len(self.board_values)):
                if count == 0:
                    fvalue = self.board_values[row][column]
                if fvalue == self.board_values[row][column]:
                    count += 1
                values.append(self.board_values[row][column])
                if count == self.board_size and fvalue == "X":
                    return "X"""

    def board(self):
        if self.screen == 0:
            self.empty_board()
        else:
            self.draw_board()
        self.root.mainloop()


Game(3)
