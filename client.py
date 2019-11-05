import os
from tkinter import *  # Module utilisé pour l'interface graphique.
from tkinter import messagebox  # Module utilisé pour le prompt 'voulez-vous rejouer' ?
from logic_handler import LogicHandler


class Client:
    """Le client est l'élément 'View' du modèle MVC. Ici, l'UI est défini et fait guise d'interface avec le controlleur
    Une instance du controlleur est créée et passée en argument afin d'interagir directement avec.

    Les méthodes de Client ont pour objectif d'appeler les méthodes du Controlleur en passant les arguments
    nécéssaires et de retourner la décision du controlleur pour pouvoir ensuite présenter le résultat sur Tkinter.
    """
    def __init__(self, logic_instance):
        self.logic_instance = logic_instance  # Instance du controlleur

    def create_ui(self, master):
        """"Tkinter créé un 'master' ou 'root' qui est la fenêtre brute. Ensuite, une fenêtre délimité est rajoutée à
        la fenêtre brute.

        On peut ensuite créer des 'widgets' à l'intérieur de cette fenêtre délimitée. Chaque widget doit être créé puis
        ensuite présenté avec pack(), qui est automatique, ou grid().
        """
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
        "Détermine quel joueur commence via le controlleur et modifie le label/texte approprié."
        firstplayer = self.logic_instance.who_starts()
        self.label.config(text="Player {} will start.".format(firstplayer))

    def start_game(self, master):
        "Démarrage du jeu, créer l'UI, la présenter, puis déterminer qui commence."
        self.create_ui(master)
        self.show_ui()
        self.show_first_player()

    def button_clicked(self, button):
        """Appelé lors d'une interaction avec un bouton. Permet d'appeler d'autres méthodes qui déterminent si le coup
         est possible ou si le jeu est terminé."""
        self.modify_button(button)
        winner = self.show_winner()
        self.reset(winner)

    def modify_button(self, button):
        "Cette méthode récupère le statut du coup effectué (légal ou illégal) et informe qui est le prochain joueur."
        legalstate, next_player = self.logic_instance.handle_interaction(button)
        if legalstate == "Legal":
            self.label.config(text="It's now {}'s turn.".format(next_player))
        elif legalstate == "Illegal":
            self.label.config(text="Your move is illgeal, it's still {}'s turn.".format(next_player))

    def show_winner(self):
        """Lorsque le controlleur retourne une value None, c'est qu'il n'y a pas de vainqueur. Dans le cas contraire,
         il y a soit un vainqueur soit une égalité."""
        winner = self.logic_instance.check_winner()
        if winner is not None:
            self.label.config(text='"{}" won !'.format(winner))
        return winner

    def reset(self, winner):
        """Cette méthode créée une fenêtre qui montre qui a gagné en utilisant la valeur retournée de show_winner()
        puis demande si le joueur veut rejouer."""
        if logic_instance.winner_status is True:
            answer = messagebox.askyesno("Question", "{} won ! Do you want to play again ?".format(winner))
            if answer is True:
                os.execl(sys.executable, sys.executable, *sys.argv)
            elif answer is False:
                self.frame.quit()


if __name__ == '__main__':
    logic_instance = LogicHandler()  # Instance du controlleur

    root = Tk()  # Fenêtre 'brute'
    root.geometry("640x500")

    client = Client(logic_instance)  # Création d'une instance client
    client.start_game(root)  # Appel de la fonction initiale.

    root.mainloop()
    root.destroy()
