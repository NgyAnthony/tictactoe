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