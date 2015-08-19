__author__ = 'Ati'

import unittest
from testable_angry_dice import AngryDice


class IsAdvancingToNextStageTest(unittest.TestCase):
    """Test the functionality of the AngryDice class is_advancing_to_next_stage
    function."""

    def setUp(self):
        self.new_angry_dice = AngryDice()

    def tearDown(self):
        del self.new_angry_dice

    def test_is_advancing_to_next_stage_yes(self):
        """Generate advancing die and stage combinations. Call
        _test_is_die_held_in_wrong_stage() with all input combinations."""

        # test_input_cases =
        # [(die_a_value, die_b_value, stage, ok_output),]
        test_input_cases = [
            ("1", "2", 1, True),
            ("2", "1", 1, True),
            ("ANGRY", "4", 2, True),
            ("4", "ANGRY", 2, True),
        ]

        for test_io in test_input_cases:
            self._test_is_game_over(*test_io)

    def test_is_advancing_to_next_stage_no(self):
        """Generate some non-advancing die and stage combinations. Call
        _test_is_die_held_in_wrong_stage() with all input combinations."""

        # test_input_cases =
        # [(die_a_value, die_b_value, stage, ok_output),]
        test_input_cases = [
            ("1", "2", 2, False),
            ("2", "1", 3, False),
            ("1", "1", 1, False),
            ("1", "1", 2, False),
            ("1", "1", 3, False),
            ("ANGRY", "1", 1, False),
            ("ANGRY", "1", 2, False),
        ]

        for test_io in test_input_cases:
            self._test_is_game_over(*test_io)

    def _test_is_game_over(self, die_a_value, die_b_value, stage, ok_output):
        """Set both die's value and game_stage.
        Check that the output of tested function matches ok_output."""

        self.new_angry_dice.die_a.current_value = die_a_value
        self.new_angry_dice.die_b.current_value = die_b_value
        self.new_angry_dice.game_stage = stage

        self.assertEqual(self.new_angry_dice.is_advancing_to_next_stage(),
                         ok_output,
                         "Incorrect output for die_a:{}, "
                         "die_b:{} in stage:{}."
                         .format(die_a_value, die_b_value, stage))


if __name__ == '__main__':
    unittest.main()
