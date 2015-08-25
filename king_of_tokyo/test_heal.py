__author__ = 'Ati'

import unittest
from monster import Monster


class HealTest(unittest.TestCase):
    """Test the functionality of the Monster class heal function."""

    def setUp(self):
        self.new_monster = Monster("Cookie")

    def tearDown(self):
        del self.new_monster

    def test_heal_health_gt_10(self):
        """
        Call the heal method with 6 to add to the initial value of 10.
        Check that the health attribute remains unchanged.
        """

        health = self.new_monster.health

        # Call function
        self.new_monster.heal(6)

        self.assertEqual(health, self.new_monster.health)

    def test_heal_health_le_10(self):
        """
        Set health to 2. Call the heal method with 6 to add.
        Check that the health attribute changes to 8.
        """

        self.new_monster.health = 2

        # Call function
        self.new_monster.heal(6)

        self.assertEqual(self.new_monster.health, 8)

    def test_heal_negative_health_le_10(self):
        """
        Call the heal method with -6 to add.
        Check that the health attribute changes to 4.
        """

        # Call function
        self.new_monster.heal(-6)

        self.assertEqual(4, self.new_monster.health)

    def test_heal_negative_health_lt_0(self):
        """
        Call the heal method with -16 to add.
        Check that the health attribute changes to -6.
        """

        # Call function
        self.new_monster.heal(-16)

        self.assertEqual(-6, self.new_monster.health)


if __name__ == '__main__':
    unittest.main()
