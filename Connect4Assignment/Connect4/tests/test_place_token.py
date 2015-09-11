__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_model


class PlaceTokenTest(unittest.TestCase):
    """Test functionality of place_token function."""

    def setUp(self):
        self.new_model = connect4_model.Connect4Model()

    def tearDown(self):
        del self.new_model

    def test_place_token_full_column(self):
        """Set up game_board to have a full column. Check that token is NOT
        added to this column, and that False is returned."""

        self.new_model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b", "r", "r"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]

        return_value = self.new_model.place_token(2, "r")
        self.assertEqual(len(self.new_model.game_board[2]), 6)
        self.assertEqual(return_value, False)

    def test_place_token_non_full_column(self):
        """Set up game_board to have a non full column. Check that token is
        added to this column, and that True is returned."""
        self.new_model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b", "r", "r"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]

        original_column_length = len(self.new_model.game_board[4])
        return_value = self.new_model.place_token(4, "r")
        self.assertEqual(len(self.new_model.game_board[4]),
                         original_column_length + 1)
        self.assertEqual(return_value, True)

    def test_place_token_non_existent(self):
        """Check that function returns None when called with an int that points
        to a non-existent column."""
        self.new_model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b", "r", "r"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]

        return_value = self.new_model.place_token(9, "r")
        self.assertEqual(return_value, None)

    def test_place_token_invalid_arg(self):
        """Check that function returns None when called with a invalid color."""
        self.new_model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b", "r", "r"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]

        return_value = self.new_model.place_token(3, "t")
        self.assertEqual(return_value, None)


if __name__ == '__main__':
    unittest.main()

