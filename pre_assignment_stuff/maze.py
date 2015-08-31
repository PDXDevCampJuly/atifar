# This is a-maze-ing maze.
from random import randint

def start():
    print("Welcome to the A-Maze-ing Maze! I dare you to escape!\n")
    next_room = room0()
    while next_room != exit:
        next_room = next_room()
    exit()

# description: A description of the current room
# doors: dictionary with door: location tuples
def process_user_movement(description, doors):
    # Print the description of the current room
    print(description)

    # Print the available doors or random choice options. Loop until user's choice is valid.
    while True:
        possible_dirs = list(doors.keys())
        # Occasionally offer the user to select a random direction to proceed in
        you_are_in_casino = (5 < randint(1, 7))
        if you_are_in_casino:
            # Provide optional random choice
            print("Do you feel lucky, chump? ", end="")
            feeling_lucky = input("Type 'y' to proceed in a random direction.").lower()
        else:
            feeling_lucky = ""
        if feeling_lucky == "y":
            # User agrees to proceed in random direction
            # Select random direction
            chosen_dir = possible_dirs[randint(0, len(possible_dirs) - 1)]
            print("Moving on through door at ", chosen_dir)
        else:
            # User input requested
            # Prompt for what doors they want
            print("You may proceed in the following directions: ", end="")
            possible_dirs.append("or type exit to give up.")
            print(*possible_dirs, sep=", ")
            chosen_dir = input("In which direction do you want to go?")
        chosen_dir = chosen_dir.lower()
        if chosen_dir not in doors:
            if chosen_dir == "exit":
                print("Bye, quitter!")
                return exit
            else:
                print("I'm sorry. There is no door in that direction. Try again!")
        else:
            # Valid response: Go to the correct location
            break
    # Return the door to proceed through
    return doors[chosen_dir]

def room0():
    # description
    description = "You are now in a tiny round room where small time magic happens."

    # doors: where those doors go
    doors = {"east": room3, "west": room2}

    # ask for user input on the next direction, then return selected direction
    return process_user_movement(description, doors)

def room1():
    # description
    description = "This is a mediocre room."

    # doors: where those doors go
    doors = {"east": room3, "south": room2, "north": room0}

    # ask for user input on the next direction, then return selected direction
    return process_user_movement(description, doors)

def room2():
    # description
    description = "This is a cool room."

    # doors: where those doors go
    doors = {"east": room3, "south": room1}

    # ask for user input on the next direction, then return selected direction
    return process_user_movement(description, doors)

def room3():
    # description
    description = "This is a scary room. Choose wisely to get to a friendlier place."

    # doors: where those doors go
    doors = {"east": room4, "west": room2}

    # ask for user input on the next direction, then return selected direction
    return process_user_movement(description, doors)

def room4():
    # description
    description = "This is a super hot room. Keep your cool!"

    # doors: where those doors go
    doors = {"north": room0, "south": way_out}

    # ask for user input on the next direction, then return selected direction
    return process_user_movement(description, doors)

def way_out():
    # Exit form the maze
    print("Congratulations! You have escaped.")
    exit()

if __name__ == "__main__":
    start()