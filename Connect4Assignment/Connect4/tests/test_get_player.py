__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_model


class GetPlayerTest(unittest.TestCase):
    """Test functionality of get_player function."""

    def setUp(self):
        self.new_model = connect4_model.Connect4Model()

    def tearDown(self):
        del self.new_model

    def test_get_existing_player(self):
        """Set up players model attribute with [["Gee", "b"], ["George",
        "r"]] Check that the return value matches what the test set up."""

        self.new_model.players = [
            ["Gee", "b"],
            ["George", "r"]
        ]
        player = self.new_model.get_player(0)
        self.assertEqual(player, ["Gee", "b"])
        player = self.new_model.get_player(1)
        self.assertEqual(player, ["George", "r"])

    def test_get_non_existing_player(self):
        """Set up players model attribute with [["Gee", "b"], ["George",
        "r"]] Check that the function raises an IndexError exception when
        called with a player index of 6."""
        self.new_model.players = [
            ["Gee", "b"],
            ["George", "r"]
        ]

        self.assertEqual(self.new_model.get_player(6), None)

    def test_get_player_invalid_arg(self):
        """Set up players model attribute with [["Gee", "b"], ["George",
        "r"]] Check that the function raises an IndexError exception when
        called with a string passed in for player."""
        self.new_model.players = [
            ["Gee", "b"],
            ["George", "r"]
        ]

        self.assertEqual(self.new_model.get_player("Yoyoyo"), None)


if __name__ == '__main__':
    unittest.main()

