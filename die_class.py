""" A generic Die class module. It optionally accepts a list of strings to make up the sides of the die.
"""
from random import choice

class Die:
    """
    This class allows the creation of a custom die.
    """


    def __init__(self, custom_faces=[1, 2, 3, 4, 5, 6]):
        """ Generate die object with the faces corresponding to the argument list elements.
        :param custom_faces: list
        :return: None
        """
        try:
            self.current_value = custom_faces[0]
        except IndexError:
            print("Die must have at least one face. Creating the die with a single 'No face'.")
            self.current_value = "No face"
            self.possible_values = ["No face"]
        else:
            self.possible_values = custom_faces


    def __repr__(self):
        """ Return representation string of a die.
        :return:string
        """
        return str(self.current_value)


    def roll(self):
        """ Return a randomly selected face of the die.
        :return: self.current_value
        """
        self.current_value = choice(self.possible_values)
        return self.current_value


if __name__ == "__main__":
    custom_faces = ["Doc", "Dopey", "Bashful", "Grumpy", "Sneezy", "Sleepy", "Happy"]

    def test_default_die_integer_faces():
        default_die = Die()
        print("Created die. It prints out like this:", default_die)
        print("It has the following sides: {}".format(", ".join(map(str, default_die.possible_values))))
        print("It has {} face(s).".format(len(default_die.possible_values)))
        print("Currently the '{}' face is showing.".format(default_die.current_value))
        default_die.roll()
        print("After rolling the '{}' face is showing.".format(default_die.current_value))
        default_die.roll()
        default_die.roll()
        default_die.roll()
        print("After three more rolls the '{}' face is showing.".format(default_die.current_value))


    def test_custom_die_string_faces(custom_faces):
        dwarf_die = Die(custom_faces)
        print("Created die. It prints out like this:", dwarf_die)
        print("It has the following sides: {}".format(", ".join(map(str, dwarf_die.possible_values))))
        print("It has {} face(s).".format(len(dwarf_die.possible_values)))
        print("Currently the '{}' face is showing.".format(dwarf_die.current_value))
        dwarf_die.roll()
        print("After rolling the '{}' face is showing.".format(dwarf_die.current_value))
        dwarf_die.roll()
        dwarf_die.roll()
        print("After two more rolls the '{}' face is showing.".format(dwarf_die.current_value))


    def test_no_face_die():
        no_face_die = Die([])
        print("Created die. It prints out like this:", no_face_die)
        print("It has the following sides: {}".format(", ".join(map(str, no_face_die.possible_values))))
        print("Created die with sides: {}".format(", ".join(no_face_die.possible_values)))
        print("It has {} face(s).".format(len(no_face_die.possible_values)))
        print("Currently the '{}' face is showing.".format(no_face_die.current_value))
        no_face_die.roll()
        print("After rolling the '{}' face is showing.".format(no_face_die.current_value))


    test_default_die_integer_faces()
    print()
    test_custom_die_string_faces(custom_faces)
    print()
    test_no_face_die()
