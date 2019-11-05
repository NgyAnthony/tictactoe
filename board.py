class Board:
    """
    Board est le modèle.
    """
    def __init__(self):
        self.matrix = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]

    def set_token(self, row, col, player):
        "Méthode qui permet le placement du coup effectué dans la matrice."
        self.matrix[row][col] = player