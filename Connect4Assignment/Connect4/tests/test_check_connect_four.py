__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_controller


class CheckConnectFourTest(unittest.TestCase):
    """Test functionality of check_connect_four function."""

    def setUp(self):
        self.new_controller = connect4_controller.Connect4Controller()

    def tearDown(self):
        del self.new_controller

    def test_connect_four_vertical_found(self):
        """Set up game_board that includes a column with four adjacent "r".
        Check that the function returns True."""
        # Four reds at top of column
        self.new_controller.model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["r", "b", "r", "r", "r", "r"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]
        self.assertEqual(self.new_controller.check_connect_four(), True)

        # Four reds in middle of column
        self.new_controller.model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "r", "r", "b"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]
        self.assertEqual(self.new_controller.check_connect_four(), True)

        # Four reds at bottom of column
        self.new_controller.model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["r", "r", "r", "r", "r", "b"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]
        self.assertEqual(self.new_controller.check_connect_four(), True)

    def test_connect_four_vertical_not_found(self):
        """Set up game_board that includes a column without four adjacent
        "r" or "b". Check that the function returns False."""
        self.new_controller.model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["r", "r", "r", "b", "r", "b"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]
        self.assertEqual(self.new_controller.check_connect_four(), False)

    def test_connect_four_horizontal_found(self):
        """Set up game_board that includes four horizontally adjacent "r".
        Check that the function returns True."""
        # Four reds starting at first column
        self.new_controller.model.game_board = [
            ["r", "r", "r"],
            ["r", "r", "b"],
            ["r", "b", "r", "b", "r", "r"],
            ["r"],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]
        self.assertEqual(self.new_controller.check_connect_four(), True)

        # Four reds starting at second column
        self.new_controller.model.game_board = [
            ["b", "r", "b"],
            ["r", "r", "r"],
            ["r", "b", "r", "r", "b", "r"],
            ["r", "b", "r"],
            ["b", "r", "r"],
            ["b", "b", "b"],
            ["r"]
        ]
        self.assertEqual(self.new_controller.check_connect_four(), True)

        # Four reds starting at third column
        self.new_controller.model.game_board = [
            ["b", "r", "r"],
            ["b", "r", "b"],
            ["r", "r", "b", "r", "r", "b"],
            ["r"],
            ["r", "r"],
            ["r", "b", "r"],
            ["b"]
        ]
        self.assertEqual(self.new_controller.check_connect_four(), True)

        # Four reds at starting at fourth column
        self.new_controller.model.game_board = [
            ["b", "r", "r"],
            ["r", "b", "b"],
            ["b", "r", "r", "r", "b", "b"],
            ["b", "r", "r", "b", "r", "r"],
            ["b", "b", "b", "b", "r", "r"],
            ["r", "r", "r", "b", "r", "b"],
            ["b", "r", "r", "r", "r", "b"]
        ]
        self.assertEqual(self.new_controller.check_connect_four(), True)

    def test_connect_four_horizontal_not_found(self):
        """Set up game_board that does not include four adjacent "r" or"b".
        Check that the function returns False."""
        self.new_controller.model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["r", "r", "r", "b", "r", "b"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]
        self.assertEqual(self.new_controller.check_connect_four(), False)

    def test_connect_four_diagonal_found(self):
        """Set up game_board that includes four diagonally adjacent "r".
        Check that the function returns True."""

        # Four reds diagonally
        self.new_controller.model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["r", "r", "b", "r", "r", "b"],
            ["b", "b", "r"],
            ["b", "r"],
            ["r", "b", "r"],
            ["r"]
        ]
        self.assertEqual(self.new_controller.check_connect_four(), True)

        # Four reds diagonally
        self.new_controller.model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["r", "r", "r", "b", "r", "b"],
            ["r", "b"],
            ["b", "r"],
            ["b", "b", "r"],
            ["r", "b", "r", "r"]
        ]
        self.assertEqual(self.new_controller.check_connect_four(), True)

    def test_connect_four_diagonal_not_found(self):
        """Set up game_board that does not include four diagonally
        adjacent "r" or "b". Check that the function returns False."""

        self.new_controller.model.game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["r", "r", "r", "b", "r", "b"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
    ]
        self.assertEqual(self.new_controller.check_connect_four(), False)

if __name__ == '__main__':
    unittest.main()

