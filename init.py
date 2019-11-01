import random  # Module used to determine who will start first.
import os  # Module used for the reset function.
from tkinter import *  # Module used for GUI.
from tkinter import messagebox  # Module used for the 'Play Again' prompt.


class App:
    """
    App contains the GUI, the game events,
    and handles all the interaction with the Board class and LogicHandler subclass.
    """
    def __init__(self, game):
        """
        :param master: is an instance of Tk(), which is the main window for Tkinter.
        :param game: is an instance of LogicHandler. Purpose: enable interaction between Tk objects and LogicHandler
        instance.
        """
        self.game = game
        self.winner_status = False
        self.play_nb = 0

    def create_ui(self, master):
        # <---Frame creation.--->
        frame = Frame(master=master, width=640, height=400)
        frame.pack()

        # <---Button creation, act as case for each move.--->
        self.button0_0 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button0_0))
        # empty text is placed as a placeholder for moves.
        # lambda is used to be able to pass a parameter in the self.modify_button method.
        self.button0_1 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button0_1))
        self.button0_2 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button0_2))

        self.button1_0 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button1_0))
        self.button1_1 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button1_1))
        self.button1_2 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button1_2))

        self.button2_0 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button2_0))
        self.button2_1 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button2_1))
        self.button2_2 = Button(frame, width=20, height=5, text=" ", command=lambda: self.modify_button(self.button2_2))

        # <-- Simple menu -->
        self.label = Label(master, text="Welcome to Tic-Tac-Toe")
        self.button_reset = Button(master, text="Reset", command=lambda: os.execl(sys.executable, sys.executable, *sys.argv))
        self.button_quit = Button(master, text="Quit", command=frame.quit)

        # <-- Make every Tkinter widget appear -->
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
        """
        Method called when button is pressed. The button widget is passed as a parameter to be modified.
        Purpose: handles showing the action of the player on the GUI and replicate said action in the logic part.
        """

        # Condition satisfied when case hasn't already been used.
        if button['text'] == " ":
            button.config(text=self.game.current_player)  # Show action in GUI
            info = button.grid_info()  # Get row and column info
            # Use Board method to replicate action in logic with the help of info
            game.set_token(int(info['row']), int(info['column']), self.game.current_player)
            winner = game.check_winner()  # Look for a winner
            game.show_winner(self.label, winner)  # Show winner if there is one
            self.reset(winner)  # Prompt user to play again if check_winner returns a value.

            # Change turn of player if there is no winner.
            if self.winner_status is False:
                if self.game.current_player == self.game.player1:
                    self.game.current_player = self.game.player2
                    self.label.config(text="It's now {}'s turn.".format(self.game.player2))
                    self.play_nb += 1
                elif self.game.current_player == self.game.player2:
                    self.game.current_player = self.game.player1
                    self.label.config(text="It's now {}'s turn.".format(self.game.player1))
                    self.play_nb += 1

        # Indicate illegal move.
        else:
            self.label.config(text="Case already used !")

    def reset(self, winner):
        """
        Winner parameter is a list, if it's not empty, it means there is a winner. When the condition is satisfied,
        automatic prompt is triggered to ask if the player wants to play again.
        """
        if len(winner) != 0 or (self.play_nb == 8 and len(winner) == 0):
            self.winner_status = True
            if self.play_nb == 8 and len(winner) == 0:
                winner = "Nobody"
            answer = messagebox.askyesno("Question", "{} won ! Do you want to play again ?".format(winner))
            if answer is True:
                game.wipe_board()
                game.who_starts(self.label)
                self.winner_status = False
                self.play_nb = -1
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
    """
    Board is used to store the matrix and simple functions to interact with the matrix.
    """
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
    """
    LogicHandler inherits the Board to be able to easily interact with it.
    """
    def __init__(self):
        super().__init__()
        self.current_player = None
        self.player1 = "x"
        self.player2 = "o"

    def who_starts(self, label):
        self.current_player = random.choice(["x", "o"])
        label.config(text="It's now {}'s turn.".format(self.current_player))

    def check_horizontal(self):
        "For each row, check if the player set three plays in this row."
        for row in range(len(self.matrix)):
            if len(set(self.matrix[row])) == 1 and None not in self.matrix[row]:
                # Set removes duplicates, if the remainer is one it means entire row is occupied.
                temp_winner = self.matrix[row][1]
                return temp_winner

    def check_vertical(self):
        "Row is static, if each vertically aligned moves are valid, winner is returned."
        for col in range(3):
            if self.matrix[0][col] == self.matrix[1][col] == self.matrix[2][col]:
                temp_winner = self.matrix[0][col]
                if temp_winner is not None:
                    return temp_winner

    def check_cross(self):
        "Check for the two use cases"
        if (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2]) or \
                (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0]):
            temp_winner = self.matrix[1][1]
            return temp_winner

    def check_winner(self):
        "Call all methods and return results of each call in a list."
        v = self.check_vertical()
        h = self.check_horizontal()
        c = self.check_cross()
        winner = list(filter(None, [v, h, c]))
        return winner

    def show_winner(self, label, winner):
        "Label is modified to make the winner appear on GUI."
        if len(winner) == 1:
            label.config(text='The "{}" player won !'.format(winner[0]))


if __name__ == '__main__':
    game = LogicHandler()

    root = Tk()
    root.geometry("640x500")
    app = App(game)
    app.create_ui(root)
    game.who_starts(app.label)

    root.mainloop()
    root.destroy()