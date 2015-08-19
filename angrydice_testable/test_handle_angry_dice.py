__author__ = 'Ati'

import unittest
from testable_angry_dice import AngryDice
from unittest.mock import patch
from io import StringIO

class HandleAngryDiceTest(unittest.TestCase):
    """Test the functionality of the AngryDice class handle_angry_dice
    function."""

    # Mocks being sys.stdout and will stor whet's print()'d into
    # mock_stdout
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_angry_dice(self, mock_stdout):

        """Set values of die_a and die_b to "ANGRY" and game_stage to 2.
        Call tested function. Check that the game reset to stage 1, and that
        the expected string was output."""

        self.new_angry_dice = AngryDice()

        self.new_angry_dice.die_a.current_value = "ANGRY"
        self.new_angry_dice.die_b.current_value = "ANGRY"
        self.new_angry_dice.game_stage = 2

        expected_output = "WOW, you're ANGRY!\nTime to go back to Stage 1!\n"
        self.new_angry_dice.handle_angry_dice()

        self.assertEqual(expected_output, mock_stdout.getvalue())
        self.assertEqual(1, self.new_angry_dice.game_stage)

        del self.new_angry_dice


if __name__ == '__main__':
    unittest.main()
