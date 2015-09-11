__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_view
from unittest.mock import patch



class PromptPlayerNameTest(unittest.TestCase):
    """Tests functionality of prompt_player_name function."""
    @patch('builtins.input', return_value='George')
    def test_player_name_valid(self, inputted_value):
        """Mock input a “name” and makes sure “name” is returned."""
        new_view = connect4_view.Connect4View()
        player_name = new_view.prompt_player_name()
        self.assertEqual(player_name, "George")


if __name__ == '__main__':
    unittest.main()
