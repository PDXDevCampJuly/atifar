__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_view
from unittest.mock import patch


class PromptPlayerToMoveTest(unittest.TestCase):
    """Test functionality of prompt_player_to_move function."""

    def setUp(self):
        self.new_view = connect4_view.Connect4View()

    def tearDown(self):
        del self.new_view

    @patch('builtins.input', return_value=3)
    def test_move_prompt_valid_move(self, inputted_value):
        """We mock the standard input and provide 3 as the user input. Check
        that function returns 3."""
        move = self.new_view.prompt_player_to_move("George", "r")
        text_move = 'Your move.\n'
        self.assertEqual(move, 3)

    @patch('builtins.input', side_effect=[7, 2])
    def test_move_prompt_invalid_move(self, inputted_value):
        """We mock the standard input and provide 7, 2 as the user
        input. Check that the player is re-prompted the first time,
        then 2 is returned."""
        move = self.new_view.prompt_player_to_move("George", "r")

        self.assertEqual(move, 2)


if __name__ == '__main__':
    unittest.main()

