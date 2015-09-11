__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_view
from unittest.mock import patch
from io import StringIO


class ShowGameBoardTest(unittest.TestCase):
    """Test functionality of show_game_board function."""

    def setUp(self):
        self.new_view = connect4_view.Connect4View()

    def tearDown(self):
        del self.new_view

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_game_board_valid(self, mock_stdout):
        """Create sample game board. Check that the correct displayed message
        is output."""
        game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]
        game_board_view = "| , , , , , , |\n"\
                          "| , , , , , , |\n" \
                          "| , ,b, , , , |\n" \
                          "|r,b,r, , ,r, |\n" \
                          "|r,r,r, ,r,b, |\n" \
                          "|b,r,b, ,b,b,r|\n"
        self.new_view.show_game_board(game_board)
        self.assertEqual(mock_stdout.getvalue(), game_board_view)


if __name__ == '__main__':
    unittest.main()

