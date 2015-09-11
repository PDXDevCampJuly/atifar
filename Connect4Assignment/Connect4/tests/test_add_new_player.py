__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_controller
from unittest.mock import patch

class AddNewPlayerTest(unittest.TestCase):
    """Test functionality of add_new_player function."""

    def setUp(self):
        self.new_controller = connect4_controller.Connect4Controller()

    def tearDown(self):
        del self.new_controller

    @patch('builtins.input', return_value="George")
    def test_add_new_player_zero(self, inputted_value):
        """Provide mock input with “George” for player 0 and check that the
        function updated player 0’s name."""

        self.new_controller.add_new_player(0)
        self.assertEqual(self.new_controller.model.players[0], ["George", "r"])





if __name__ == '__main__':
    unittest.main()

