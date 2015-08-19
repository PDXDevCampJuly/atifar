__author__ = 'Ati'

import unittest
from angry_dice import AngryDice
from die_class import Die


class DieRollTest(unittest.TestCase):
    """Test the functionality of the Die class roll function."""

    def setUp(self):
        self.possible_values = [1, 2, 3, "Dog", "Cat", "Hippo"]
        self.new_die = Die(self.possible_values)

        # print(self.shortDescription())

    def tearDown(self):
        del self.possible_values
        del self.new_die
        # print("Just ran test:")
        # print(self._testMethodName)

    def test_roll_once(self):
        """Roll die once, and ensure returned value is in possible_values."""

        self.assertIn(self.new_die.roll(), self.possible_values,
                      "Rolled value was not in possible values of Die.")

    def test_rolled_value_changes(self):
        """Roll die a number of times and make sure it changes its value between rolls."""

        holding_value = self.new_die.roll()
        for i in range(10):
            if self.new_die.roll() != holding_value:
                print("Rolled die '{}' value is different "
                      "than holding value '{}'."
                      .format(self.new_die.current_value, holding_value))
                self.assertTrue(True)
                return

        self.assertTrue(False, "Rolled die value did not change in 10 rolls.")

    def test_current_value_is_updated_to_rolled_value(self):
        """Roll die a number of times and make sure its value updates according to the rolled value."""

        self.new_die.current_value = 9
        self.assertEqual(self.new_die.roll(), self.new_die.current_value,
                         "Die's value did not update to the rolled value.")


if __name__ == '__main__':
    unittest.main()