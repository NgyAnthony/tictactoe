import os
from tkinter import *  # Module used for GUI.
from tkinter import messagebox  # Module used for the 'Play Again' prompt.
from logic_handler import LogicHandler


class Client:
    def __init__(self, logic_instance):
        self.logic_instance = logic_instance

    def create_ui(self, master):
        self.frame = Frame(master=master, width=640, height=400)
        self.frame.pack()

        self.button0_0 = Button(self.frame, width=20, height=5, text=" ", command=lambda: self.button_clicked(self.button0_0))
        self.button0_1 = Button(self.frame, width=20, height=5, text=" ", command=lambda: self.button_clicked(self.button0_1))
        self.button0_2 = Button(self.frame, width=20, height=5, text=" ", command=lambda: self.button_clicked(self.button0_2))
        self.button1_0 = Button(self.frame, width=20, height=5, text=" ", command=lambda: self.button_clicked(self.button1_0))
        self.button1_1 = Button(self.frame, width=20, height=5, text=" ", command=lambda: self.button_clicked(self.button1_1))
        self.button1_2 = Button(self.frame, width=20, height=5, text=" ", command=lambda: self.button_clicked(self.button1_2))
        self.button2_0 = Button(self.frame, width=20, height=5, text=" ", command=lambda: self.button_clicked(self.button2_0))
        self.button2_1 = Button(self.frame, width=20, height=5, text=" ", command=lambda: self.button_clicked(self.button2_1))
        self.button2_2 = Button(self.frame, width=20, height=5, text=" ", command=lambda: self.button_clicked(self.button2_2))

        self.label = Label(master, text="Welcome to Tic-Tac-Toe")
        self.button_reset = Button(master, text="Reset", command=lambda: os.execl(sys.executable, sys.executable, *sys.argv))
        self.button_quit = Button(master, text="Quit", command=self.frame.quit)

    def show_ui(self):
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

    def show_first_player(self):
        firstplayer = self.logic_instance.who_starts()
        self.label.config(text="Player {} will start.".format(firstplayer))

    def button_clicked(self, button):
        self.modify_button(button)
        winner = self.show_winner()
        self.reset(winner)

    def modify_button(self, button):
        legalstate, next_player = self.logic_instance.handle_interaction(button)
        if legalstate == "Legal":
            self.label.config(text="It's now {}'s turn.".format(next_player))
        elif legalstate == "Illegal":
            self.label.config(text="Your move is illgeal, it's still {}'s turn.".format(next_player))

    def show_winner(self):
        "Label is modified to make the winner appear on GUI."
        winner = self.logic_instance.check_winner()
        if winner is not None and winner != "Illegal":
            self.label.config(text='"{}" won !'.format(winner))
        elif winner == "Illegal":
            self.label.config(text='"{}" won !'.format("Case already used!"))
        return winner  # return statement is used in the reset function

    def reset(self, winner):
        if logic_instance.winner_status is True:
            answer = messagebox.askyesno("Question", "{} won ! Do you want to play again ?".format(winner))
            if answer is True:
                os.execl(sys.executable, sys.executable, *sys.argv)
            elif answer is False:
                self.frame.quit()


if __name__ == '__main__':
    logic_instance = LogicHandler()

    root = Tk()
    root.geometry("640x500")

    client = Client(logic_instance)
    client.create_ui(root)
    client.show_ui()
    client.show_first_player()

    root.mainloop()
    root.destroy()
