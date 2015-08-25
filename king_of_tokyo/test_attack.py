__author__ = 'Ati'

import unittest
from monster import Monster


class AttackTest(unittest.TestCase):
    """Test the functionality of the Monster class attack function."""

    def setUp(self):
        self.new_monster = Monster("Cookie")

    def tearDown(self):
        del self.new_monster

    def test_attack_stay_alive(self):
        """
        Initialize health to 10. Call function with 7 and check that 3 is
        returned and status is unchanged.
        """
        self.new_monster.health = 10
        original_status = self.new_monster.status

        # Call function
        new_health = self.new_monster.attack(7)

        self.assertEqual(new_health, 3,
                         "Expected 3 for updated health.")
        self.assertEqual(self.new_monster.status, original_status,
                         "Status should have remained {}".
                         format(original_status))

    def test_attack_ko_ed(self):
        """
        Initialize health to 10. Call function with 12 and check that -2 is
        returned and status is "K.O.'d".
        """

        self.new_monster.health = 10

        # Call function
        new_health = self.new_monster.attack(12)
        
        self.assertEqual(new_health, -2,
                         "Expected 3 for updated health.")
        self.assertEqual(self.new_monster.status, "K.O.'d",
                         "Status should be K.O.'d")


if __name__ == '__main__':
    unittest.main()
