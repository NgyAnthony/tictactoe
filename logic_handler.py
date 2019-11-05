from board import Board
import random


class LogicHandler(Board):
    """
    LogicHandler est le controlleur et hérite du modèle "Board".
    Les méthodes du controlleur assurent l'interaction entre le client et le modèle.
    Par exemple, la vérification d'une égalité ou d'un vainqueur ou le placement d'un coup.
    """
    def __init__(self):
        super().__init__()  # Hérite de Board
        self.current_player = None
        self.winner_status = False
        self.player1 = "x"
        self.player2 = "o"
        self.play_nb = 0  # Vérifie le nombre de coups effectués.

    def who_starts(self):
        """Méthode qui définit quel joueur commence."""
        self.current_player = random.choice(["x", "o"])
        return self.current_player

    def handle_interaction(self, button):
        """Lorsque cette méthode est appellée, un bouton tkinter est passé en argument.
        Après verification de la légalité du coup (bouton occupé ou non), la méthode place le joueur
        actuel dans le modèle (matrice Board) puis ensuite l'affiche dans la vue (UI Tkinter). """
        if button['text'] == " ":
            button.config(text=self.current_player)
            # Récupère la position du bouton
            info = button.grid_info()
            # Traduit la position du bouton pour pouvoir répliquer le coup sur le modèle
            self.set_token(int(info['row']), int(info['column']), self.current_player)

            # Si il n'y a pas de vainqueur, placer le coup.
            if self.winner_status is False:
                if self.current_player == self.player1:
                    self.current_player = self.player2
                    self.play_nb += 1
                    return "Legal", self.player2
                elif self.current_player == self.player2:
                    self.current_player = self.player1
                    self.play_nb += 1
                    return "Legal", self.player1

        # Indication d'un coup illegal.
        else:
            return "Illegal", self.current_player

    def child_check_horizontal(self):
        "Pour chaque ligne, vérifier si un joueur à joué trois fois dans cette ligne."
        for row in range(len(self.matrix)):
            if len(set(self.matrix[row])) == 1 and None not in self.matrix[row]:
                # Set removes duplicates, if the remainer is one it means entire row is occupied.
                temp_winner = self.matrix[row][1]
                return temp_winner

    def child_check_vertical(self):
        "Pour chaque colonne, vérifier si un joueur à joué trois fois dans cette colonne."
        # On garde l'index pour les lignes fixe puisque la vérification se fait verticalement.
        for col in range(3):
            if self.matrix[0][col] == self.matrix[1][col] == self.matrix[2][col]:
                temp_winner = self.matrix[0][col]
                if temp_winner is not None:
                    return temp_winner

    def child_check_cross(self):
        "Vérification brute des deux cas : diagonale gauche et droite."
        if (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2]) or \
                (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0]):
            temp_winner = self.matrix[1][1]
            return temp_winner

    def check_winner(self):
        "Appel de toutes les méthodes de vérification et retourner soit un vainqueur, soit une égalité, soit rien."
        v = self.child_check_vertical()
        h = self.child_check_horizontal()
        c = self.child_check_cross()
        winner_list = list(filter(None, [v, h, c]))
        winner = None
        if "x" in winner_list:
            winner = "x"
            self.winner_status = True
        elif "o" in winner_list:
            winner = "o"
            self.winner_status = True
        elif "x" in winner_list and "o" in winner_list:
            print("An error has been found.")
        elif winner is None and self.play_nb == 9:
            winner = "Nobody"
            self.winner_status = True
        return winner
