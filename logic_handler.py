from board import Board
import random


class LogicHandler(Board):
    """
    LogicHandler inherits the Board to be able to easily interact with it.
    """
    def __init__(self):
        super().__init__()
        self.current_player = None
        self.winner_status = False
        self.player1 = "x"
        self.player2 = "o"
        self.play_nb = 0

    def who_starts(self):
        self.current_player = random.choice(["x", "o"])
        return self.current_player

    def handle_interaction(self, button):
        if button['text'] == " ":
            button.config(text=self.current_player)
            info = button.grid_info()
            self.set_token(int(info['row']), int(info['column']), self.current_player)

            if self.winner_status is False:
                if self.current_player == self.player1:
                    self.current_player = self.player2
                    self.play_nb += 1
                    return "Legal", self.player2
                elif self.current_player == self.player2:
                    self.current_player = self.player1
                    self.play_nb += 1
                    return "Legal", self.player1

        # Indicate illegal move.
        else:
            return "Illegal", self.current_player

    def child_check_horizontal(self):
        "For each row, check if the player set three plays in this row."
        for row in range(len(self.matrix)):
            if len(set(self.matrix[row])) == 1 and None not in self.matrix[row]:
                # Set removes duplicates, if the remainer is one it means entire row is occupied.
                temp_winner = self.matrix[row][1]
                return temp_winner

    def child_check_vertical(self):
        "Row is static, if each vertically aligned moves are valid, winner is returned."
        for col in range(3):
            if self.matrix[0][col] == self.matrix[1][col] == self.matrix[2][col]:
                temp_winner = self.matrix[0][col]
                if temp_winner is not None:
                    return temp_winner

    def child_check_cross(self):
        "Check for the two use cases (diagonal left and right)"
        if (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2]) or \
                (self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0]):
            temp_winner = self.matrix[1][1]
            return temp_winner

    def check_winner(self):
        "Call all methods and return the winner if there is one"
        v = self.child_check_vertical()
        h = self.child_check_horizontal()
        c = self.child_check_cross()
        winner_list = list(filter(None, [v, h, c]))
        winner = None
        if "x" in winner_list:
            winner = "x"
        elif "o" in winner_list:
            winner = "o"
        elif "x" in winner_list and "o" in winner_list:
            print("An error has been found.")
        elif winner is None and self.play_nb == 9:
            winner = "Nobody"
        return winner
