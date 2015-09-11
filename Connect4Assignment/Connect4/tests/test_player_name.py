__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_view
from unittest.mock import patch
from io import StringIO


class PromptPlayerNameTest(unittest.TestCase):
    """Test functionality of prompt_player_name function."""

    def setUp(self):
        self.new_view = connect4_view.Connect4View()

    def tearDown(self):
        del self.new_view

    @patch('builtins.input', return_value="George")
    @patch('sys.stdout', new_callable=StringIO)
    def test_player_name_valid(self, mock_stdout, inputted_value):
        """Mock input a “name” and makes sure “name” is returned."""


        name_text = "What’s your name?\n"
        player_name = self.new_view.prompt_player_name()

        self.assertEqual(mock_stdout.getvalue(), name_text)

        self.assertEqual(player_name, "George")










if __name__ == '__main__':
    unittest.main()

