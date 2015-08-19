__author__ = 'Ati'

import unittest
from testable_angry_dice import AngryDice
from unittest.mock import patch
from io import StringIO

class DisplayCurrentDiceTest(unittest.TestCase):
    """Test the functionality of the AngryDice class display_current_dice
    function."""

    # Mocks being sys.stdout and will stor whet's print()'d into
    # mock_stdout
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_current_dice(self, mock_stdout):

        """Set values of die_a and die_b to some values.
        Call tested function, and check that the expected string was output."""

        self.new_angry_dice = AngryDice()

        self.new_angry_dice.die_a.current_value = "2"
        self.new_angry_dice.die_b.current_value = "5"

        expected_output = "You rolled:\n   a = [  2  ]\n   b = [  5  ]\n\n"
        self.new_angry_dice.display_current_dice()

        self.assertEqual(expected_output, mock_stdout.getvalue())

        del self.new_angry_dice


if __name__ == '__main__':
    unittest.main()
