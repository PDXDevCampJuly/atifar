__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_model



class GetGameBoardTest(unittest.TestCase):
    """Test functionality of get_game_board function."""

    def setUp(self):
        self.new_model = connect4_model.Connect4Model()

    def tearDown(self):
        del self.new_model

    def test_get_game_board(self):
        """Set up a game board. Check that the same data is returned."""
        self.new_model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]
        test_game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]
        game_board = self.new_model.get_game_board()
        self.assertEqual(test_game_board, game_board)



if __name__ == '__main__':
    unittest.main()

