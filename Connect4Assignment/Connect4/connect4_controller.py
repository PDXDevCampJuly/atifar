__author__ = 'summerlynbryant'

import connect4_model
import connect4_view


class Connect4Controller:
    """ This is the Controller class for the Connect4 game. """

    def __init__(self):
        self.model = connect4_model.Connect4Model()
        self.view = connect4_view.Connect4View()

    def start_game(self):
        """This is the main function that runs the whole game """
        self.view.show_instructions()
        self.add_new_player(0)
        self.add_new_player(1)
        while True:
            active_player = self.model.get_active_player()
            player_name, color = self.model.get_player(active_player)
            self.view.show_game_board(self.model.get_game_board())
            move = self.view.prompt_player_to_move(player_name, color)

            if not self.model.place_token(move, color):
                print("Couldn't place token.")
                continue

            self.model.decrement_token_count()
            if self.check_connect_four():
                self.view.show_game_board(self.model.get_game_board())
                self.view.declare_winner(player_name)
                break

            if self.check_draw():
                self.view.show_game_board(self.model.get_game_board())
                self.view.declare_draw()
                break

            self.model.switch_active_player()

    def add_new_player(self, player):
        """Prompt player for name and stores it in the players attribute
        that corresponds to the arg, player 0 is assigned color "r", and
        player 1 is assigned "b" """
        player_name = self.view.prompt_player_name()
        self.model.players[player] = [player_name, "r" if player == 0 else "b"]

    def switch_player(self):
        """This function switches the player’s turn."""
        self.model.switch_active_player()

    def check_connect_four(self):
        """Analyze the game_board and return True if a winning pattern is
        found, else return False."""
        game_board = [
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"]
        ]

        # Augment game board to have full length columns
        gb = self.model.get_game_board()
        for row_idx, column in enumerate(gb):
            for col_idx, element in enumerate(column):
                game_board[row_idx][col_idx] = element

        # vertical check
        # Check each consecutive four tokens in each column starting with
        # positions 0, 1, and 2
        for col in game_board:
            for i in range(3):
                token = col[i]
                if token == "r" or token == "b":
                    if token == col[i + 1] and token == col[i + 2] and token \
                            == col[i + 3]:
                        return True

        # horizontal check
        # Check each consecutive four tokens in each row starting with
        # positions 0, 1, 2, 3
        transposed = [[row[i] for row in game_board] for i in range(6)]
        for col in transposed:
            for i in range(4):
                token = col[i]
                if token == "r" or token == "b":
                    if token == col[i + 1] and token == col[i + 2] and token \
                            == col[i + 3]:
                        return True

        # Diagonal check
        # Check each consecutive four tokens in each column starting with
        # positions 0, 1, and 2
        gb = game_board
        for r in range(4):
            for k, col in enumerate(game_board):
                for i in range(3):
                    token = gb[r][i]
                    if token == "r" or token == "b":
                        if token == gb[r + 1][i + 1] and \
                                        token == gb[r + 2][i + 2] and \
                                        token == gb[r + 3][i + 3]:
                            return True

        # Check each consecutive four tokens in each column starting with
        # positions 0, 1, and 2
        transposed = []
        for i in reversed(game_board):
            transposed.append(i)
        gb = transposed
        for r in range(4):
            for k, col in enumerate(transposed):
                for i in range(3):
                    token = gb[r][i]
                    if token == "r" or token == "b":
                        if token == gb[r + 1][i + 1] and \
                                        token == gb[r + 2][i + 2] and \
                                        token == gb[r + 3][i + 3]:
                            return True
        # All checks failed
        return False

    def check_draw(self):
        """Checks the the get_token_count.  If the token count is 0, then
        return True, else return False."""
        return self.model.get_token_count() == 0

if __name__ == "__main__":
    connect4 = Connect4Controller()
    connect4.start_game()
