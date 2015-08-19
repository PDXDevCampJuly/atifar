__author__ = 'Ati'

import unittest
from testable_angry_dice import AngryDice


class RegisterPlayerCheatingTest(unittest.TestCase):
    """Test the functionality of the AngryDice class register_player_cheating
    function."""

    def setUp(self):
        self.new_angry_dice = AngryDice()

    def tearDown(self):
        del self.new_angry_dice

    def test_register_player_cheating_die_a_not_6_hold(self):
        """Set die_a's value to "1", just_cheated_a to False.
        Call function: ("a", []).
        Check that function returns False."""

        self.new_angry_dice.die_a.current_value = "1"

        self.new_angry_dice.register_player_cheating("a", [])

        self.assertEqual(self.new_angry_dice.just_cheated_a, False,
                         "Die 'a' unexpectedly registered cheated.")

    def test_register_player_cheating_die_a_is_6_hold(self):
        """Set die_a's value to "6", just_cheated_a to False.
        Call function: ("a", []).
        Check that just_cheated_a is True."""

        self.new_angry_dice.die_a.current_value = "6"
        self.new_angry_dice.just_cheated_a = False

        self.new_angry_dice.register_player_cheating("a", [])

        self.assertEqual(self.new_angry_dice.just_cheated_a, True,
                         "Die 'a' failed to change to cheated.")

    def test_register_player_cheating_die_a_not_6_nohold(self):
        """Set die_a's value to "1", just_cheated_a to False.
        Call function: ("a", ["a"]).
        Check that just_cheated_a is unchanged."""

        self.new_angry_dice.die_a.current_value = "1"
        self.new_angry_dice.just_cheated_a = False

        self.new_angry_dice.register_player_cheating("a", ["a"])

        self.assertEqual(self.new_angry_dice.just_cheated_a, False,
                         "Die 'a' unexpectedly registered cheated.")

    def test_register_player_cheating_die_a_is_6_nohold(self):
        """Set die_a's value to "6", just_cheated_a to False.
        Call function: ("a", ["a"]).
        Check that just_cheated_a is unchanged."""

        self.new_angry_dice.die_a.current_value = "6"
        self.new_angry_dice.just_cheated_a = False

        self.new_angry_dice.register_player_cheating("a", ["a"])

        self.assertEqual(self.new_angry_dice.just_cheated_a, False,
                         "Die 'a' unexpectedly registered cheated.")

    def test_register_player_cheating_die_b_not_6_hold(self):
        """Set die_b's value to "1", just_cheated_b to False.
        Call function: ("b", []).
        Check that just_cheated_b is unchanged."""

        self.new_angry_dice.die_b.current_value = "1"
        self.new_angry_dice.just_cheated_b = False

        self.new_angry_dice.register_player_cheating("b", [])

        self.assertEqual(self.new_angry_dice.just_cheated_b, False,
                         "Die 'b' unexpectedly registered cheated.")

    def test_register_player_cheating_die_b_is_6_hold(self):
        """Set die_b's value to "6", just_cheated_b to False.
        Call function: ("b", []).
        Check that just_cheated_b is True."""

        self.new_angry_dice.die_b.current_value = "6"
        self.new_angry_dice.just_cheated_b = False

        self.new_angry_dice.register_player_cheating("b", [])

        self.assertEqual(self.new_angry_dice.just_cheated_b, True,
                         "Die 'b' failed to change to cheated.")

    def test_register_player_cheating_die_b_not_6_nohold(self):
        """Set die_b's value to "1", just_cheated_b to False.
        Call function: ("b", ["b"]).
        Check that just_cheated_b is unchanged."""

        self.new_angry_dice.die_b.current_value = "1"
        self.new_angry_dice.just_cheated_b = False

        self.new_angry_dice.register_player_cheating("b", ["b"])

        self.assertEqual(self.new_angry_dice.just_cheated_b, False,
                         "Die 'b' unexpectedly registered cheated.")

    def test_register_player_cheating_die_b_is_6_nohold(self):
        """Set die_b's value to "6", just_cheated_b to False.
        Call function: ("b", ["b"]).
        Check that just_cheated_b is unchanged."""

        self.new_angry_dice.die_b.current_value = "6"
        self.new_angry_dice.just_cheated_b = False

        self.new_angry_dice.register_player_cheating("b", ["b"])

        self.assertEqual(self.new_angry_dice.just_cheated_b, False,
                         "Die 'b' unexpectedly registered cheated.")

    def test_register_player_cheating_wrong_die_hold_ab(self):
        """Set both die's value to "6", just_cheated_a, just_cheated_b to False.
        Call function: ("c34", []). Check that just_cheated_a and just_cheated_b
        are unchanged."""

        self.new_angry_dice.die_a.current_value = "6"
        self.new_angry_dice.die_b.current_value = "6"
        self.new_angry_dice.just_cheated_a = False
        self.new_angry_dice.just_cheated_b = False

        self.new_angry_dice.register_player_cheating("c34", [])

        self.assertEqual(self.new_angry_dice.just_cheated_a, False,
                         "Die 'a' unexpectedly registered cheated.")
        self.assertEqual(self.new_angry_dice.just_cheated_b, False,
                         "Die 'b' unexpectedly registered cheated.")


if __name__ == '__main__':
    unittest.main()
