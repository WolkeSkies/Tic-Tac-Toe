# William Henson
# Tic Tac Toe Gui
# 09/17/2021
from tkinter import *
from tkinter import messagebox

class Game:
    def __init__(self):
        self.root = Tk()
        self.board_size = 0
        self.board_values = []
        self.board_values_pos = []
        self.board_buttons = []
        self.row = 0
        self.column = 0
        self.screen = 0
        self.turn = 1
        self.main_menu()

    def main_menu(self):
        def board():
            self.screen = 0
            self.board_size = int(board_size.get())
            self.refresh()

        board_size = StringVar()
        Label(self.root, text="Size of Grid:").grid(row=0, column=0)
        Entry(self.root, textvariable=board_size).grid(row=1, column=0)
        Button(self.root, text="Enter", command=lambda: board()).grid(row=1, column=1)
        self.root.mainloop()

    def refresh(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        if self.screen == 0:
            self.empty_board()
        elif self.check_win() is None:
            self.draw_board()
        else:
            self.winner_screen()

    def winner_screen(self):
        def restart():
            self.screen = 0
            self.refresh()

        Label(self.root, text=self.check_win() + " Wins!").grid(row=0, column=1)
        Button(self.root, text="Play Again!", bg="green", command=restart).grid(row=2, column=2)
        Button(self.root, text="Return To Main Menu", bg="red").grid(row=2, column=0)

    def empty_board(self):
        self.board_values = []
        for row in range(self.board_size):
            self.board_values.append([])
            for column in range(self.board_size):
                self.board_values[row].append(" ")
                Button(self.root, text=self.board_values[row][column], height=5, width=10,
                       command=lambda r=row, c=column: self.move([r, c])).grid(row=row, column=column)
        self.screen = 1

    def draw_board(self):
        for row in range(self.board_size):
            for column in range(self.board_size):
                Button(self.root, text=self.board_values[row][column], height=5, width=10,
                       command=lambda r=row, c=column: self.move([r, c])).grid(row=row, column=column)

    def move(self, pos):
        if self.turn % 2 == 1 and self.board_values[pos[0]][pos[1]] == " ":
            self.board_values[pos[0]][pos[1]] = "X"
            self.turn += 1
        elif self.board_values[pos[0]][pos[1]] == " ":
            self.board_values[pos[0]][pos[1]] = "O"
            self.turn += 1
        print(self.check_win())
        self.refresh()

    def check_win(self):
        # Horizontal
        for row in self.board_values:
            vertical = []
            for column in row:
                vertical.append(column)
                count = 0
            for value in vertical:
                if value == " " or value != column:
                    break
                else:
                    count += 1
            if count == self.board_size:
                if value == "X":
                    return "X"
                else:
                    return "O"

        # Vertical
        for i in range(self.board_size):
            vertical = []
            count = 0
            for row in range(self.board_size):
                vertical.append(self.board_values[row][0])
            fvalue = vertical[0]
            for value in vertical:
                if fvalue == value:
                    count += 1
            if count == self.board_size:
                return value

        # Diagonal

        diagonal = []
        reverse_diagonal = []
        for row in range(len(self.board_values)):
            diagonal.append(self.board_values[row][row])
            reverse_diagonal.append(self.board_values[row][((self.board_size - 1) - row)])
        count = 0
        for value in diagonal:
            if value == diagonal[0] and value != " ":
                count += 1
                if count == self.board_size:
                    return value
            else:
                break
        count = 0
        for value in reverse_diagonal:
            if value == reverse_diagonal[0] and value != " ":
                count += 1
                if count == self.board_size:
                    return value
            else:
                break


Game()
