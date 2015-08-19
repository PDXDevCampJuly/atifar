__author__ = 'Ati'

import unittest
from testable_angry_dice import AngryDice


class RollDiceTest(unittest.TestCase):
    """Test the functionality of the AngryDice class roll_dice
    function."""

    def setUp(self):
        self.new_angry_dice = AngryDice()

    def tearDown(self):
        del self.new_angry_dice

    def test_roll_dice_none(self):
        """Set values of die_a and die_b to any value.
        Call tested function with empty list.
        Check that neither die value changed."""

        self.new_angry_dice.die_a.current_value = "bebop"
        self.new_angry_dice.die_b.current_value = 29
        self.new_angry_dice.roll_dice([])

        self.assertEqual(self.new_angry_dice.die_a.current_value, "bebop",
                         "Die_a was erroneously rolled.")
        self.assertEqual(self.new_angry_dice.die_b.current_value, 29,
                         "Die_b was erroneously rolled.")

    def test_roll_dice_die_a(self):
        """Set values of die_a and die_b to any value other than the die's
        possible values. Call tested function with ["a"] argument.
        Check that die_a value has changed to a possible value, but die_b
        has not changed."""

        self.new_angry_dice.die_a.current_value = "bebop"
        self.new_angry_dice.die_b.current_value = 29
        self.new_angry_dice.roll_dice(["a"])

        self.assertIn(self.new_angry_dice.die_a.current_value,
                      self.new_angry_dice.angry_die_faces,
                      "Die_a was not rolled.")
        self.assertEqual(self.new_angry_dice.die_b.current_value, 29,
                         "Die_b was erroneously rolled.")

    def test_roll_dice_die_b(self):
        """Set values of die_a and die_b to any value other than the die's
        possible values. Call tested function with ["b"] argument.
        Check that die_b value has changed to a possible value, but die_a
        has not changed."""

        self.new_angry_dice.die_a.current_value = "bebop"
        self.new_angry_dice.die_b.current_value = 29
        self.new_angry_dice.roll_dice(["b"])

        self.assertIn(self.new_angry_dice.die_b.current_value,
                      self.new_angry_dice.angry_die_faces,
                      "Die_b was not rolled.")
        self.assertEqual(self.new_angry_dice.die_a.current_value, "bebop",
                         "Die_a was erroneously rolled.")

    def test_roll_dice_bad_argument(self):
        """Generate a list of improper argument types. Call tested function
        with those arguments. Check that an TypeError exception is raised."""

        bad_args = [23.7, "barf", ['b', 3]]
        for bad_arg in bad_args:
            self._test_roll_dice_bad_argument(bad_arg)

    def _test_roll_dice_bad_argument(self, bad_arg):
        """Call tested function with "argonaut" argument.
        Check that a TypeError exception is raised."""

        self.assertRaises(TypeError,
                          self.new_angry_dice.roll_dice, bad_arg)

if __name__ == '__main__':
    unittest.main()
