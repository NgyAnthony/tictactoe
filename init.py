import random


class Board:
    def __init__(self):
        self.matrix = [["o", None, None],
                       [None, "o", None],
                       [None, None, "o"]]


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

        try:
            print('The "{}" player won !'.format(winner[0]))
        except:
            pass


a = LogicHandler()
a.check_winner()
# Starting game
# Get random player
# First turn is random player
# Player places his mark
# Board is shown
# Check if there is a winner
# Other player places his mark
#