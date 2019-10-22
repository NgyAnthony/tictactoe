import random
import os
from tkinter import *
from tkinter import messagebox


class App:
    def __init__(self, master, game):
        self.game = game
        self.winner_status = False
        frame = Frame(master=master, width=640, height=400)
        frame.pack()

        self.button0_0 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button0_0))
        self.button0_1 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button0_1))
        self.button0_2 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button0_2))

        self.button1_0 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button1_0))
        self.button1_1 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button1_1))
        self.button1_2 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button1_2))

        self.button2_0 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button2_0))
        self.button2_1 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button2_1))
        self.button2_2 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button2_2))

        self.label = Label(master, text="Welcome to Tic-Tac-Toe")
        self.button_reset = Button(master, text="Reset", command=lambda: os.execl(sys.executable, sys.executable, *sys.argv))
        self.button_quit = Button(master, text="Quit", command=frame.quit)

        self.button0_0.grid(row=0, column=0, sticky=NW, pady=2)
        self.button0_1.grid(row=0, column=1, sticky=N, pady=2)
        self.button0_2.grid(row=0, column=2, sticky=NE, pady=2)

        self.button1_0.grid(row=1, column=0, sticky=W, pady=2)
        self.button1_1.grid(row=1, column=1, pady=2)
        self.button1_2.grid(row=1, column=2, sticky=E, pady=2)

        self.button2_0.grid(row=2, column=0, sticky=SW, pady=2)
        self.button2_1.grid(row=2, column=1, sticky=S, pady=2)
        self.button2_2.grid(row=2, column=2, sticky=SE, pady=2)

        self.label.pack()
        self.button_reset.pack()
        self.button_quit.pack()

    def modify_button(self, button):
        if button['text'] == " ":
            button.config(text=self.game.current_player)
            info = button.grid_info()
            game.set_token(int(info['row']), int(info['column']), self.game.current_player)
            winner = game.check_winner()
            game.show_winner(self.label, winner)
            self.reset(winner)

            if self.winner_status is False:
                if self.game.current_player == self.game.player1:
                    self.game.current_player = self.game.player2
                    self.label.config(text="It's now {}'s turn.".format(self.game.player2))
                elif self.game.current_player == self.game.player2:
                    self.game.current_player = self.game.player1
                    self.label.config(text="It's now {}'s turn.".format(self.game.player1))
        else:
            self.label.config(text="Case already used !")

    def reset(self, winner):
        if len(winner) != 0:
            self.winner_status = True
            answer = messagebox.askyesno("Question", "Player {} won ! Do you want to play again ?".format(winner))
            if answer is True:
                game.wipe_board()
                game.who_starts()
                self.winner_status = False
                self.button0_0.config(text=" ")
                self.button0_1.config(text=" ")
                self.button0_2.config(text=" ")

                self.button1_0.config(text=" ")
                self.button1_1.config(text=" ")
                self.button1_2.config(text=" ")

                self.button2_0.config(text=" ")
                self.button2_1.config(text=" ")
                self.button2_2.config(text=" ")

            else:
                root.destroy()


class Board:
    def __init__(self):
        self.matrix = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]

    def set_token(self, row, col, player):
        self.matrix[row][col] = player

    def wipe_board(self):
        self.matrix = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]


class LogicHandler(Board):
    def __init__(self):
        super().__init__()
        self.current_player = None
        self.player1 = "x"
        self.player2 = "o"

    def who_starts(self):
        self.current_player = random.choice(["x", "o"])

    def check_horizontal(self):
        for row in range(len(self.matrix)):
            if len(set(self.matrix[row])) == 1 and None not in self.matrix[row]:
                temp_winner = self.matrix[row][1]
                return temp_winner

    def check_vertical(self):
        for col in range(3):
            if self.matrix[0][col] == self.matrix[1][col] == self.matrix[2][col]:
                temp_winner = self.matrix[0][col]
                if temp_winner is not None:
                    return temp_winner

    def check_cross(self):
        if (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2]) or \
                (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0]):
            temp_winner = self.matrix[1][1]
            return temp_winner

    def check_winner(self):
        v = self.check_vertical()
        h = self.check_horizontal()
        c = self.check_cross()
        winner = list(filter(None, [v, h, c]))
        return winner

    def show_winner(self, label, winner):
        if len(winner) == 1:
            label.config(text='The "{}" player won !'.format(winner[0]))


if __name__ == '__main__':
    game = LogicHandler()
    game.who_starts()

    root = Tk()
    root.geometry("640x500")
    app = App(root, game)

    root.mainloop()
    root.destroy()