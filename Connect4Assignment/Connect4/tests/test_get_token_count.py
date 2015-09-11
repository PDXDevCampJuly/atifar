__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_model


class GetTokenCountTest(unittest.TestCase):
    """Test functionality of get_token_count function."""

    def setUp(self):
        self.new_model = connect4_model.Connect4Model()

    def tearDown(self):
        del self.new_model

    def test_get_token_count(self):
        """Return the value of token_count."""

        self.new_model.token_count = 32

        self.assertEqual(self.new_model.get_token_count(), 32)


if __name__ == '__main__':
    unittest.main()

