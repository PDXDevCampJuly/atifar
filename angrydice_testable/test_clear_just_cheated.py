__author__ = 'Ati'

import unittest
from testable_angry_dice import AngryDice


class ClearJustCheatedTest(unittest.TestCase):
    """Test the functionality of the AngryDice class clear_just_cheated
    function."""

    def setUp(self):
        self.new_angry_dice = AngryDice()

    def tearDown(self):
        del self.new_angry_dice

    def test_clear_just_cheated_none(self):
        """Set values of just_cheated_a and just_cheated_b to True.
        Call tested function with empty list.
        Check that neither just_cheated_x value changed."""

        self.new_angry_dice.just_cheated_a = True
        self.new_angry_dice.just_cheated_b = True
        self.new_angry_dice.clear_just_cheated([])

        self.assertEqual(self.new_angry_dice.just_cheated_a, True,
                         "The just_cheated_a attribute was cleared.")
        self.assertEqual(self.new_angry_dice.just_cheated_b, True,
                         "The just_cheated_b attribute was cleared.")

    def test_clear_just_cheated_die_a(self):
        """Set values of just_cheated_a and just_cheated_b to True.
        Call tested function with ["a"] argument.
        Check that just_cheated_a value has changed to False, but
        just_cheated_b has not changed."""

        self.new_angry_dice.just_cheated_a = True
        self.new_angry_dice.just_cheated_b = True
        self.new_angry_dice.clear_just_cheated(["a"])

        self.assertEqual(self.new_angry_dice.just_cheated_a, False,
                         "The just_cheated_a attribute failed to clear.")
        self.assertEqual(self.new_angry_dice.just_cheated_b, True,
                         "The just_cheated_b attribute was cleared.")

    def test_clear_just_cheated_die_b(self):
        """Set values of just_cheated_a and just_cheated_b to True.
        Call tested function with ["b"] argument.
        Check that just_cheated_b value has changed to False, but
        just_cheated_a has not changed."""

        self.new_angry_dice.just_cheated_a = True
        self.new_angry_dice.just_cheated_b = True
        self.new_angry_dice.clear_just_cheated(["b"])

        self.assertEqual(self.new_angry_dice.just_cheated_b, False,
                         "The just_cheated_b attribute failed to clear.")
        self.assertEqual(self.new_angry_dice.just_cheated_a, True,
                         "The just_cheated_a attribute was cleared.")

    def test_clear_just_cheated_bad_argument(self):
        """Generate a list of improper argument types. Call tested function
        with those arguments. Check that an TypeError exception is raised."""

        bad_args = [23.7, "barf", ['b', 3]]
        for bad_arg in bad_args:
            self._test_clear_just_cheated_bad_argument(bad_arg)

    def _test_clear_just_cheated_bad_argument(self, bad_arg):
        """Call tested function with "argonaut" argument.
        Check that a TypeError exception is raised."""

        self.assertRaises(TypeError,
                          self.new_angry_dice.clear_just_cheated, bad_arg)

if __name__ == '__main__':
    unittest.main()
