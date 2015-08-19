__author__ = 'Ati'

import unittest
from monster import Monster
from unittest.mock import patch


class FleeTest(unittest.TestCase):
    """Test the functionality of the Monster class flee function."""

    def setUp(self):
        self.new_monster = Monster("Cookie")

    def tearDown(self):
        del self.new_monster

    @patch('builtins.input', return_value='Y')
    def test_flee_y_upper(self, input_value):
        """Test if True is returned if the user
        inputs 'Y'."""
        self.assertEqual(self.new_monster.flee(), True,
                         "Does not flee Tokyo when input is 'Y'.")

    @patch('builtins.input', return_value='y')
    def test_flee_y_lower(self, input_value):
        """Test if True is returned if the user
        inputs 'y'."""
        self.assertEqual(self.new_monster.flee(), True,
                         "Does not flee Tokyo when input is 'y'.")

    @patch('builtins.input', return_value='N')
    def test_flee_n_upper(self, input_value):
        """Test if False is returned if the user
        inputs 'N'."""
        self.assertEqual(self.new_monster.flee(), False,
                         "Does flee Tokyo when input is 'N'.")

    @patch('builtins.input', return_value='n')
    def test_flee_n_lower(self, input_value):
        """Test if True is returned if the user
        inputs 'n'."""
        self.assertEqual(self.new_monster.flee(), False,
                         "Does flee Tokyo when input is 'n'.")

    # Test that user is prompted again if they input anything other than a
    # single Y/y or N/n. Also check that the following message is displayed
    # following the invalid input: "Please enter only 'Y', 'y', 'N', or 'n'."
    @patch('builtins.input', side_effect=['2barf', 'y'])
    def test_flee_n_lower(self, input_value):
        """Simulate the user entering '2barf' as input first, then after being
        reprompted entering 'y'.Check that True is returned."""
        self.assertEqual(self.new_monster.flee(), True,
                         "Does not flee Tokyo when first valid input is 'y'.")


if __name__ == '__main__':
    unittest.main()
