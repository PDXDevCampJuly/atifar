__author__ = 'Ati'

import unittest
from monster import Monster


class ScoreTest(unittest.TestCase):
    """Test the functionality of the Monster class score function."""

    def setUp(self):
        self.new_monster = Monster("Cookie")

    def tearDown(self):
        del self.new_monster

    def test_score_no_win(self):
        """
        Initialize health to 1. Call function with 7 and check that 7 is
        returned and status is unchanged.
        """

        self.new_monster.health = 1
        original_status = self.new_monster.status

        # Call function
        victory_points = self.new_monster.score(7)

        self.assertEqual(victory_points, 7,
                         "Expected t for victory points.")
        self.assertEqual(self.new_monster.status, original_status,
                         "Status should have remained {}".
                         format(original_status))

    def test_score_winning(self):
        """
        Initialize health to 16. Call function with 7 and check that 7 is
        returned and status is 'WINNING'.
        """

        self.new_monster.health = 16

        # Call function
        victory_points = self.new_monster.score(7)

        self.assertEqual(victory_points, 7,
                         "Expected t for victory points.")
        self.assertEqual(self.new_monster.status, "WINNING",
                         "Status should be 'WINNING'")


if __name__ == '__main__':
    unittest.main()
