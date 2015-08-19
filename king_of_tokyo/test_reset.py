__author__ = 'Ati'

import unittest
from monster import Monster


class ResetTest(unittest.TestCase):
    """Test the functionality of the Monster class reset function."""

    def test_reset(self):
        """Set status to "Oops", health to -200 and victory_points to 90 on
        a Monster class object, new_monster. Call reset() then check that
        new_monster's status, health and victory_points attributes were
        restored to their initial values."""

        new_monster = Monster("Cookie")
        new_monster.status = "Oops"
        new_monster.health = -200
        new_monster.victory_points = 90
        new_monster.reset()
        self.assertEqual(new_monster.status, "Out of Tokyo")
        self.assertEqual(new_monster.health, 10)
        self.assertEqual(new_monster.victory_points, 0)

        del new_monster


if __name__ == '__main__':
    unittest.main()
