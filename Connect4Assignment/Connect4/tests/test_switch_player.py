__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_controller


class SwitchPlayerTest(unittest.TestCase):
    """Test functionality of switch_player function."""

    def setUp(self):
        self.new_controller = connect4_controller.Connect4Controller()

    def tearDown(self):
        del self.new_controller

    def test_switch_player(self):
        """Stored current active player.Check function causes the current
        active player to switch"""

        self.new_controller.model.active_player = 0
        self.new_controller.switch_player()
        self.assertEqual(self.new_controller.model.active_player, 1)

        self.new_controller.switch_player()
        self.assertEqual(self.new_controller.model.active_player, 0)


if __name__ == '__main__':
    unittest.main()

