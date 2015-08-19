__author__ = 'Ati'

import unittest
from testable_angry_dice import AngryDice


class IsDieHeldInWrongStageTest(unittest.TestCase):
    """Test the functionality of the AngryDice class is_die_held_in_wrong_stage
    function."""

    def setUp(self):
        self.new_angry_dice = AngryDice()

    def tearDown(self):
        del self.new_angry_dice

    def test_is_die_held_in_wrong_stage(self):
        """Generate all input and correct output value combinations. Call
        _test_is_die_held_in_wrong_stage() with all input combinations."""

        # test_input_cases = [(die_value, stage, ok_output),...]
        test_input_cases = [
            ("1", 1, False),
            ("2", 1, False),
            ("ANGRY", 1, True),
            ("4", 1, True),
            ("5", 1, True),
            ("6", 1, True),
            ("1", 2, True),
            ("2", 2, True),
            ("ANGRY", 2, False),
            ("4", 2, False),
            ("5", 2, True),
            ("6", 2, True),
            ("1", 3, True),
            ("2", 3, True),
            ("ANGRY", 3, True),
            ("4", 3, True),
            ("5", 3, False),
            ("6", 3, False),
        ]

        for test_io in test_input_cases:
            self._test_is_die_held_in_wrong_stage(*test_io)

    def _test_is_die_held_in_wrong_stage(self, die_value, stage, ok_output):
        """Set die_a's value to die_value, game_stage to stage.
        Check that the output of tested function matches ok_output."""

        self.new_angry_dice.die_a.current_value = die_value
        self.new_angry_dice.game_stage = stage

        actual_out = self.new_angry_dice.is_die_held_in_wrong_stage(
            self.new_angry_dice.die_a)
        self.assertEqual(actual_out, ok_output,
                         "Incorrect output for holding a {} in stage {}."
                         .format(die_value, stage))

    def test_is_die_held_in_wrong_stage_bad_argument(self):
        """Call tested function with a float argument. Check that a
        TypeError exception is generated."""

        self.assertRaises(TypeError,
                          self.new_angry_dice.is_die_held_in_wrong_stage, 54.8)


if __name__ == '__main__':
    unittest.main()
