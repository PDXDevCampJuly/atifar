__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_model


class SwitchActivePlayerTest(unittest.TestCase):
    """Test functionality of switch_active_player function."""

    def setUp(self):
        self.new_model = connect4_model.Connect4Model()

    def tearDown(self):
        del self.new_model

    def test_switch_active_player_zero(self):
        """Check the function changes the active_player attribute from 0 to 1"""
        self.new_model.active_player = 0
        self.new_model.switch_active_player()
        self.assertEqual(self.new_model.active_player, 1)

    def test_switch_active_player_one(self):
        """Check the function changes the active_player attribute from 1 to 0"""
        self.new_model.active_player = 1
        self.new_model.switch_active_player()
        self.assertEqual(self.new_model.active_player, 0)


if __name__ == '__main__':
    unittest.main()

