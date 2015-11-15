__author__ = 'summerlynbryant'

class Connect4View:
    """

    """

    def __init__(self):
        pass

    def show_instructions(self):
        print("\nTwo players for the game. 1st player is assigned the 'r' "
              "token. \n2nd player is assigned the 'b' token. \nOne your turn,"
              " choose a column from 0 to 6 and try to CONNECT 4!)\n")

    def declare_winner(self, player_name):
        print("{} Oh my god you WON!".format(player_name))

    def declare_draw(self):
        print("You both lose!")

    def prompt_player_to_move(self, player_name, color):
        """
        Tell player with name and color passed in to make a move and return
        player’s move. If player inputs something other than an int between 0
        and 6, re-prompt.
        :param player_name: string
        :param color: string
        :return: int
        """

        while True:

            print('{} Your move.'.format(player_name))
            move = input()
            try:
                col = int(move)
            except ValueError:
                print('Invalid move. Try again!')
                continue
            if col <= 6 and col >= 0:
                return col
            print('Invalid move. Try again!')

    def show_game_board(self, game_board):
        """
        Shows the current view of the game_board.
        """

        for i in range(5, -1, -1):
            row = '|'
            for column in game_board:
                if i < len(column):
                    row = row + column[i] + ','
                else:
                    row = row + ' ,'
            row = row[:-1] + '|'
            print(row)

    def prompt_player_name(self):
        """
        To either player print ‘What’s your name?’ and returns a name
        :return: string
        """
        print("What’s your name?")
        player_name = input()

        return player_name
