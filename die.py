# This is a dice faking module

from random import randint

def roll(max):
    r = randint(1, max)
    return r

def roll_a_bunch(max, numOfDice=3):
    rolls = []
    for i in range(numOfDice):
        rolls.append(roll(max))
    return rolls

def roll_distro(max, numOfDice=3):
    rolls = roll_a_bunch(max, numOfDice)
    distribution = {}

    for each in rolls:
        currentCount = distribution.get(each, 0)
        distribution[each] = currentCount + 1

    output = ""
    for roll in distribution:
        output += "Number " + str(roll) + " was rolled " + str(distribution[roll]) + " times.\n"
    print(output)
