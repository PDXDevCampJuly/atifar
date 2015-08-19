__author__ = 'Ati'

import unittest
from monster import Monster


class InTokyoTest(unittest.TestCase):
    """Test the functionality of the Monster class in_tokyo function."""

    def setUp(self):
        self.new_monster = Monster("Cookie")

    def tearDown(self):
        del self.new_monster

    def test_in_tokyo_yes(self):
        """Set status to "In Tokyo" on a Monster class object, new_monster.
        Check that in_tokyo() returns True."""
        self.new_monster.status = "In Tokyo"
        self.assertEqual(self.new_monster.in_tokyo(), True)

    def test_in_tokyo_no(self):
        """Set status to "" on a Monster class object, new_monster.
        Check that in_tokyo() returns False."""
        self.new_monster.status = ""
        self.assertEqual(self.new_monster.in_tokyo(), False)

    def test_in_tokyo_invalid(self):
        """Set status to -78.3 on a Monster class object, new_monster.
        Check that in_tokyo() returns False."""
        self.new_monster.status = -78.3
        self.assertEqual(self.new_monster.in_tokyo(), False)


if __name__ == '__main__':
    unittest.main()
