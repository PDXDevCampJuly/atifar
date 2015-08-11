""" Single player angry dice game. The detailed description of the game are:

ANGRY DICE – An assignment in patience.
---------------------------------------------
Create a new module called 'angry_dice.py'.In this module, create a program that lets a
Single Player play Angry Dice.

When the game starts, it should display:
--------------------------------------------------
Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!
Stage 1 you need to roll 1 & 2
Stage 2 you need to roll ANGRY & 4
Stage 3 you need to roll 5 & 6
You can lock a die needed for your current stage and just roll the other one, but beware!
If you ever get 2 ANGRY's at once, you have to restart to Stage 1!
Also, you can never lock a 6! That's cheating!

To roll the dice, simply input the name of the die you want to roll. Their names are a and b.
--------------------------------------------------

Within the program, there should be 2 dice, made with your Die class. They should have the sides:
   ["1","2","ANGRY","4","5","6"]
and be named 'a' and 'b'.

Once the game starts, you should present your user with their initial roll in the display format:
--------------------------------------------------
You rolled:
   a = [  5  ]
   b = [  ANGRY  ]

You are in Stage 2
Roll dice:
--------------------------------------------------
The if the characters 'a' and/or 'b' are input, as part of ANY string, the program should roll the corresponding dice.

If a die has a currentValue of 6 and isn't rolled, the program should tell the user they're cheating and not enable
them to win until the 6 is rerolled.
--------------------------------------------------
You're cheating! You cannot lock a 6! You cannot win
until you reroll it!
You rolled:
   a = [  6  ]
   b = [  ANGRY  ]

You are in Stage 3
Roll dice:
--------------------------------------------------
The game should automagically progress them through the 3 stages and determine when they win. It should also reset
them back to Stage1 if they roll two ANGRY dice.

When the user gets 2 Angry Dice, the game should display:
--------------------------------------------------
WOW, you're ANGRY!
Time to go back to Stage 1!
--------------------------------------------------

When the user wins, the program should display:
--------------------------------------------------
You've won! Calm down!
--------------------------------------------------
"""

import die_class


class AngryDice:
    """ Angry dice game class.
    """

    # Faces for both angry dice
    angry_die_faces = ["1", "2", "ANGRY", "4", "5", "6"]

    def __init__(self):
        """ Generate two dice, a and b. Initialize game_stage, just_cheated and game_won attributes.
        """
        self.a = die_class.Die(self.angry_die_faces)
        self.b = die_class.Die(self.angry_die_faces)
        self.game_stage = 1
        self.just_cheated_a = False
        self.just_cheated_b = False
        self.game_won = False


    def display_welcome_message(self):
        print("Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!")
        print("Stage 1 you need to roll 1 & 2")
        print("Stage 2 you need to roll ANGRY & 4")
        print("Stage 3 you need to roll 5 & 6")
        print("You can lock a die needed for your current stage and just roll the other one, but beware!")
        print("If you ever get 2 ANGRY's at once, you have to restart to Stage 1!")
        print("Also, you can never lock a 6! That's cheating!")
        print("\nTo roll the dice, simply input the name of the die you want to roll. Their names are a and b.")


    def process_user_input(self, dice_to_roll):
        """ Prompt for user input. Return a list of strings (referring to dice) to roll.
        :return: list: any combination of "a" and "b"
        """
        def is_die_held_in_wrong_stage(die):
            """ Return True if die is illegal to hold in current stage.
            :param die: object of class Die
            :return:Boolean
            """
            if self.game_stage == 1:
                return die.current_value not in die.possible_values[0:2]
            if self.game_stage == 2:
                return die.current_value not in die.possible_values[2:4]
            if self.game_stage == 3:
                return die.current_value not in die.possible_values[4:6]


        def handle_player_cheating(dice_to_roll):
            """ If either die is not rolled while it has a value of 6, display admonition and add it to
            dice_to_roll list.
            """
            # If player attempts to hold both dice with value 6, display message that they are cheating
            if dice_to_roll == [] and self.a.current_value == "6" and self.b.current_value == "6":
                print("You're cheating! You cannot win until you reroll both dice!")
                self.just_cheated_a = True
                self.just_cheated_b = True
            # If player attempts to hold only die 'a' with value 6, display message that they are cheating
            elif "a" not in dice_to_roll and self.a.current_value == "6":
                print("You're cheating! You cannot lock a 6! You cannot win until you reroll it!")
                # Force rolling die 'a'
                self.just_cheated_a = True
            # If player attempts to hold only die 'b' with value 6, display message that they are cheating
            elif "b" not in dice_to_roll and self.b.current_value == "6":
                print("You're cheating! You cannot lock a 6! You cannot win until you reroll it!")
                # Force rolling die 'b'
                self.just_cheated_b = True

        user_input = input("Roll dice:")
        # Start with empty list of dice to roll
        # dice_to_roll = []
        if "a" in user_input:
            dice_to_roll.append("a")
        if "b" in user_input:
            dice_to_roll.append("b")
        # Handle cheating
        handle_player_cheating(dice_to_roll)
        # If user attempts to illegally hold die 'a' in the current stage ...
        if "a" not in dice_to_roll and is_die_held_in_wrong_stage(self.a):
            # Force rolling die 'a'
            dice_to_roll.append("a")
        # If user attempts to illegally hold die 'b' in the current stage ...
        if "b" not in dice_to_roll and is_die_held_in_wrong_stage(self.b):
            # Force rolling die 'b'
            dice_to_roll.append("b")
        # return dice_to_roll


    def roll_dice(self, dice_to_roll):
        """ Roll selected dice. Update and display their current values.
        :param dice_to_roll:
        """
        if "a" in dice_to_roll:
            self.a.roll()
            self.just_cheated_a = False
        if "b" in dice_to_roll:
            self.b.roll()
            self.just_cheated_b = False
        # Display current dice values
        print("You rolled:\n   a = [  {}  ]\n   b = [  {}  ]\n".format(self.a, self.b))

    def is_game_over(self):
        """ Return True if in Stage 3 the values of the dice are "5" and "6" and not cheating.
        """
        if self.just_cheated_a or self.just_cheated_b:
            return False
        if self.game_stage == 3:
            return (self.a.current_value == "5" and self.b.current_value == "6" or
                    self.a.current_value == "6" and self.b.current_value == "5")


    def is_advancing_to_next_stage(self):
        """ Return True if in Stage 1 the values of the dice are "1" and "2", or
        if in Stage 2 the values of the dice are "ANGRY" and "4".
        """
        if self.game_stage == 1:
            return (self.a.current_value == "1" and self.b.current_value == "2" or
                    self.a.current_value == "2" and self.b.current_value == "1")
        if self.game_stage == 2:
            return (self.a.current_value == "ANGRY" and self.b.current_value == "4" or
                    self.a.current_value == "4" and self.b.current_value == "ANGRY")


    def handle_angry_dice(self):
        # If player rolled two "ANGRY" dice, display "you are angry" message and reset stage value.
        if self.a.current_value == "ANGRY" and self.b.current_value == "ANGRY":
            print("WOW, you're ANGRY!\nTime to go back to Stage 1!")
            self.game_stage = 1


    def play_angry_dice(self):
        """ Top level function to run the angry dice game.
        """
        self.display_welcome_message()
        # Once the user hits ENTER the game starts.
        input("Press ENTER to start!")
        # Roll both dice at the beginning of the game
        self.roll_dice(["a", "b"])
        # If player rolled two "ANGRY" dice, display "you are angry" message and reset stage value.
        self.handle_angry_dice()
        # Advance to Stage 2 if rolled 1 and 2
        if self.is_advancing_to_next_stage():
            self.game_stage += 1
        # Display current stage
        print("You are in Stage {}".format(self.game_stage))
        # Loop on sequence below until user wins
        while not self.game_won:
            # Get user to select dice to roll. Enforce rules about illegal attempts to hold dice.
            dice_to_roll = []
            self.process_user_input(dice_to_roll)
            # Roll dice.
            self.roll_dice(dice_to_roll)
            # If player rolled two "ANGRY" dice, display "you are angry" message and reset stage value.
            self.handle_angry_dice()
            # If player won, update game_won attribute break out of this loop.
            if self.is_game_over():
                self.game_won = True
                break
            # If player advances to next stage, increment game_stage attribute
            elif self.is_advancing_to_next_stage():
                self.game_stage += 1
            # Display current stage
            print("You are in Stage {}".format(self.game_stage))
        # Player won! Display victory message!
        print("You've won! Calm down!")


if __name__ == "__main__":
    ang_die = AngryDice()
    ang_die.play_angry_dice()
