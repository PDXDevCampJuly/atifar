__author__ = 'Ati'

class Monster:
    """A monster class for the game of King of Tokyo."""

    def __init__(self, name):
        self.name = name
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def reset(self):
        """Reset Monster to its defaults."""
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def in_tokyo(self):
        """Returns True if Monster's status is 'In Tokyo'."""
        return self.status == "In Tokyo"

    def flee(self):
        """Prompts Monster to see if they want to flee Tokyo. If "y",
        return True. If "", return False."""
        while True:
            user_input = input(
                "Do you want to flee Tokyo? (Y/y - yes, N/n - no: ")
            if user_input.lower() == 'y':
                return True
            elif user_input.lower() == 'n':
                return False
            else:
                print("Please enter only 'Y', 'y', 'N', or 'n'.")

    def heal(self, heal_points):
        """Add the passed int to the Monster's health up to but not exceeding
        10."""
        if type(heal_points) != type(10):
            raise TypeError
        if heal_points + self.health <= 10:
            self.health += heal_points

    def attack(self, attack_points):
        """Subtract the passed int from the Monster's health, returning health.
        if health is <= 0, set status to"K.O.'d"."""
        pass

    def score(self, victory_points):
        """Add passed int to Monster's victory_points, and return
        victory_points. If the Monster's victory_points >= 20, set status
        to "WINNING"."""
        pass


