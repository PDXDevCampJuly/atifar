__author__ = 'summerlynbryant'

class Connect4Model:
    """

    """

    def __init__(self):
        self.token_count = 42
        self.game_board = [[], [], [], [], [], [], []]
        self.active_player = 0
        self.players = [["", "r"], ["", "b"]]

    def get_token_count(self):
        """
        Returns token count
        :return: int
        """
        return self.token_count

    def decrement_token_count(self):
        """Decrement token count by 1"""

        self.token_count -= 1

    def is_column_open(self, column):
        """
        Return True if the chosen column is open in the game_board or False if
        it is full. Return None when called with a non-existent column.
        :param column: int
        :return: boolean/None
        """
        if column < 0 or column > 6:
            return None
        elif len(self.game_board[column]) < 6:
            return True
        else:
            return False

    def get_game_board(self):
        """
        Returns the game board
        :return:list of list of string
        """
        return self.game_board

    def place_token(self, column, color):
        """
        Adds token passed in into the column that’s passed in. Return False
        (unsuccessful operation) if the selected column is full, otherwise
        return True. Return None when called with an invalid arg, such as int
        outside of the range 0 to 6 or str being other than either “r” or “b”.
        :param column: int
        :param color: string
        :return:boolean
        """
        if self.is_column_open(column) is None or color not in ["r", "b"]:
            return None
        elif self.is_column_open(column):
            self.game_board[column].append(color)
            return True
        else:
            return False

    def get_player(self, player):
        """
        Returns the list of name and color for the player in the players data
        structure. If the player passed in is an int but doesn’t point to a
        player, then it should return None. If arg passed in is
        not int then will return None.

        :param player:
        :return:list of list of string
        """

        if type(player) != type(1):
            return None

        if player < 0 or player > 1:
            return None

        return self.players[player]

    def switch_active_player(self):
        """This function switches the active player variable to the other
        player."""
        if self.active_player == 0:
            self.active_player = 1
        elif self.active_player == 1:
            self.active_player = 0

    def get_active_player(self):
        """
        Returns active player
        :return: int
        """
        return self.active_player
