__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_model


class DecrementTokenCountTest(unittest.TestCase):
    """Test functionality of decrement_token_count function."""

    def setUp(self):
        self.new_model = connect4_model.Connect4Model()

    def tearDown(self):
        del self.new_model

    def test_decrement_token_count(self):
        """Check that the function subtracts one from the token_count."""

        self.new_model.token_count = 32
        self.new_model.decrement_token_count()
        self.assertEqual(self.new_model.token_count, 31)


if __name__ == '__main__':
    unittest.main()

