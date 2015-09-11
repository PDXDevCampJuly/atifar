__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_controller


class CheckDrawTest(unittest.TestCase):
    """Test functionality of check_draw function."""

    def setUp(self):
        self.new_controller = connect4_controller.Connect4Controller()

    def tearDown(self):
        del self.new_controller

    def test_check_draw(self):
        """Set token count to 0 and check to return True"""
        self.new_controller.model.token_count = 0

        self.assertEqual(self.new_controller.check_draw(), True)

    def test_check_draw_token_left(self):
        """Set token count to 6 and check to return False"""
        self.new_controller.model.token_count = 6

        self.assertEqual(self.new_controller.check_draw(), False)


if __name__ == '__main__':
    unittest.main()

