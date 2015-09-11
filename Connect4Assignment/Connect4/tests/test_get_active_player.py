__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_model


class GetActivePlayerTest(unittest.TestCase):
    """Test functionality of get_active_player function."""

    def setUp(self):
        self.new_model = connect4_model.Connect4Model()

    def tearDown(self):
        del self.new_model

    def test_active_player(self):
        """Check that the return value is equal to the value of the
        active_player with more than one value."""

        self.new_model.active_player = 0
        self.assertEqual(self.new_model.get_active_player(), 0)
        self.new_model.active_player = 1
        self.assertEqual(self.new_model.get_active_player(), 1)


if __name__ == '__main__':
    unittest.main()

