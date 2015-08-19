__author__ = 'Ati'

import unittest
from testable_angry_dice import AngryDice
from unittest.mock import patch


class ProcessUserInputTest(unittest.TestCase):
    """Test the functionality of the AngryDice class process_user_input
    function."""

    def setUp(self):
        self.new_angry_dice = AngryDice()

    def tearDown(self):
        del self.new_angry_dice

    # Will mock the input for 1 input prompt
    @patch('builtins.input', return_value='')
    def test_process_user_input_empty(self, input_value):
        """Test if an empty list is generated as output if the user doesn't
        input anything."""

        dice_to_roll = self.new_angry_dice.process_user_input()
        self.assertEqual([], dice_to_roll, "Output list is not empty.")

    @patch('builtins.input', return_value='a')
    def test_process_user_input_only_a(self, input_value):
        """Test if the correct list is generated as output if the user
        inputs 'a'."""

        dice_to_roll = self.new_angry_dice.process_user_input()
        self.assertEqual(['a'], dice_to_roll,
                         "Output list does not equal ['a'].")

    @patch('builtins.input', return_value='b')
    def test_process_user_input_only_b(self, input_value):
        """Test if the correct list is generated as output if the user
        inputs 'b'."""

        dice_to_roll = self.new_angry_dice.process_user_input()
        self.assertEqual(['b'], dice_to_roll,
                         "Output list does not equal ['b'].")

    @patch('builtins.input', return_value='ab')
    def test_process_user_input_a_and_b(self, input_value):
        """Test if the correct list is generated as output if the user
        inputs 'ab'."""

        dice_to_roll = self.new_angry_dice.process_user_input()
        self.assertIn('a', dice_to_roll, "'a' is missing from output list.")
        self.assertIn('b', dice_to_roll, "'b' is missing from output list.")

    @patch('builtins.input', return_value='l1a! a')
    def test_process_user_input_junk_and_a(self, input_value):
        """Test if the correct list is generated as output if the user
        inputs a string that contains at least one 'a' but no 'b'."""

        dice_to_roll = self.new_angry_dice.process_user_input()
        self.assertEqual(['a'], dice_to_roll,
                         "Output list does not equal ['a'].")

    @patch('builtins.input', return_value='bln!bb 7')
    def test_process_user_input_junk_and_b(self, input_value):
        """Test if the correct list is generated as output if the user
        inputs a string that contains at least one 'b' but no 'a'."""

        dice_to_roll = self.new_angry_dice.process_user_input()
        self.assertEqual(['b'], dice_to_roll,
                         "Output list does not equal ['b'].")


if __name__ == '__main__':
    unittest.main()
