#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import randint, choice
from sys import exit
from string import ascii_lowercase

words = ["test"]
numWrong = 0
listedWord = [None]

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson(inputFileName=None):
    global words
    global listedWord

    # Populate word list with all the words from an input file
    # Remove elemnts of the word list that contain any character other than lowercase letters
    if inputFileName is not None:
        with open(inputFileName, "r") as inpFile:
            allWords = inpFile.read().strip().split()
            words = onlyContainLowerCaseLetters(allWords)

    # Greet the user
    print("Let's play a game of hangperson!")

    # Randomly select a word from the list of words
    word = choice(words)

    # Make the randomly selected word into a list object
    listedWord = list(word)

    # Make another list the same length as the word, but with
    # '_' instead of letters. This will track the user's progress.
    # Use the variable name currentState
    currentState = list("_" * len(word))

    # Print the initial state of the game
    printHangperson(currentState)

    # Start the game! Loop until the user either wins or loses
    while currentState != listedWord and numWrong < 6:
        guess = userGuess(currentState)
        currentState = updateState(guess, currentState)
        printHangperson(currentState)

    # Determine if the user won or lost, and then tell them accordingly
    if currentState == listedWord:
        print("Congratulations! You have survived.")
    else:
        print("Sorry, you have been hanged.")

# This function removes all elements of the allWords list that contain any
# character other than lowercase letters, then returns the remaining list.
#
# returns list of strings
def onlyContainLowerCaseLetters(allWords):
    for word in allWords[:]:
        for char in word:
            if char not in ascii_lowercase:
                allWords.remove(word)
    return allWords

# This helpful function prompts the user for a guess,
# accepting only single letters.
# DO CHANGE
#
# returns a letter
def userGuess(currentState):
    guess = ""
    while len(guess) != 1:
        guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ").lower()
        if len(guess) == 1 and guess in ascii_lowercase:
            if guess in currentState:
                print("You have already guessed this letter. Try again.")
                guess = ""
            else:
                break
        elif guess == 'exit':
            print("Game over. Bye!")
            exit()
        else:
            print("That is not a valid guess. Try again!")
            guess = ""
    return guess


# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState):
    global numWrong

    # First, determine if the letter guessed is in the word.
    # If it isn't, tell the user and update the numWrong var
    # If it is, congratulate them and update the state of the game.
    #    To update the state, make sure to replace ALL the '_' with
    #    the guessed letter.
    if guess in listedWord:
        guessMatchCount = listedWord.count(guess)
        if guessMatchCount > 1:
            print("The letter {} appears in the word {} time(s).".format(repr(guess), guessMatchCount))
        else:
            print("The letter {} appears in the word 1 time.".format(repr(guess)))
        for i, c in enumerate(listedWord):
            if guess == c:
                currentState[i] = c
    else:
        print("The letter {} does not appear in the word.".format(repr(guess)))
        numWrong += 1

    return currentState


# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state):
    person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
    print()

    if numWrong > 0:
        print(person[0])

    if numWrong > 1:
        print(person[numWrong-1])

    print("\n\n")

    for i in state:
        print(i, end=" ")

    print("\n")

# This line runs the program on import of the module
hangperson("words.txt")
