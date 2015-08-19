__author__ = 'Ati'

import unittest
from testable_angry_dice import AngryDice


class IsGameOverTest(unittest.TestCase):
    """Test the functionality of the AngryDice class is_game_over
    function."""

    def setUp(self):
        self.new_angry_dice = AngryDice()

    def tearDown(self):
        del self.new_angry_dice

    def test_is_game_over_player_won(self):
        """Generate winning die, cheated and stage combinations. Call
        _test_is_die_held_in_wrong_stage() with all input combinations."""

        # test_input_cases =
        # [(die_a_value, die_b_value, cheated_a, cheated_b, stage, ok_output),]
        test_input_cases = [
            ("6", "5", False, False, 3, True),
            ("5", "6", False, False, 3, True),
        ]

        for test_io in test_input_cases:
            self._test_is_game_over(*test_io)

    def test_is_game_over_cheating(self):
        """Generate representative die, cheated and stage combinations. Call
        _test_is_die_held_in_wrong_stage() with all input combinations."""

        # test_input_cases =
        # [(die_a_value, die_b_value, cheated_a, cheated_b, stage, ok_output),]
        test_input_cases = [
            ("6", "5", True, False, 3, False),
            ("5", "6", False, True, 3, False),
            ("6", "6", True, True, 3, False),
            ("6", "6", True, False, 3, False),
            ("6", "6", False, True, 3, False),
        ]

    def test_is_game_over_stage_1_2(self):
        """Generate representative die, cheated and stage combinations. Call
        _test_is_die_held_in_wrong_stage() with all input combinations."""

        # test_input_cases =
        # [(die_a_value, die_b_value, cheated_a, cheated_b, stage, ok_output),]
        test_input_cases = [
            ("6", "5", False, False, 2, False),
            ("5", "6", False, False, 1, False),
            ("ANGRY", "ANGRY", False, False, 1, False),
            ("4", "1", False, False, 2, False),
            ("2", "2", False, False, 1, False),
        ]

        for test_io in test_input_cases:
            self._test_is_game_over(*test_io)

    def _test_is_game_over(self, die_a_value, die_b_value, cheated_a,
                           cheated_b, stage, ok_output):
        """Set both die's value, both cheated attribute and game_stage.
        Check that the output of tested function matches ok_output."""

        self.new_angry_dice.die_a.current_value = die_a_value
        self.new_angry_dice.die_b.current_value = die_b_value
        self.new_angry_dice.just_cheated_a = cheated_a
        self.new_angry_dice.just_cheated_b = cheated_b
        self.new_angry_dice.game_stage = stage

        self.assertEqual(self.new_angry_dice.is_game_over(), ok_output,
                         "Incorrect output for die_a:{}, cheated_a:{}, "
                         "die_b:{}, cheated_b:{} in stage:{}."
                         .format(die_a_value, cheated_a, die_b_value,
                                 cheated_b, stage))


if __name__ == '__main__':
    unittest.main()
