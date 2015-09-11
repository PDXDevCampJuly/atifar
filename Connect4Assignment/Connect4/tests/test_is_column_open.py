__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_model


class IsColumnOpenTest(unittest.TestCase):
    """Test functionality of is_column_open function."""

    def setUp(self):
        self.new_model = connect4_model.Connect4Model()

    def tearDown(self):
        del self.new_model

    def test_place_token_non_full_column(self):
        """Set up game_board to have a non-full column. Check that True is
        returned."""
        self.new_model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b", "r", "r"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]

        return_value = self.new_model.is_column_open(5)
        self.assertEqual(return_value, True)

    def test_is_open_column_full_column(self):
        """Set up game_board to have a full column. Check that False is
        returned."""

        self.new_model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b", "r", "r"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]

        return_value = self.new_model.is_column_open(2)
        self.assertEqual(return_value, False)

    def test_is_open_column_non_existent(self):
        """Set up game_board. Check that None is returned when the argument
        points to an non-existent column."""
        self.new_model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b", "r", "r"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]

        return_value = self.new_model.is_column_open(9)
        self.assertEqual(return_value, None)


if __name__ == '__main__':
    unittest.main()

