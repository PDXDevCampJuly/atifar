from itertools import product
from random import shuffle


class Card:
    """ This is a structure for holding cards, defining them for the other classes.
    A card has a suit and a face, though the suit is vestigial.
    """
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face


    def print_card(self):
        """ This will print out the card to the screen."""
        print("{} of {}".format(self.face, self.suit), end="")


class Deck:
    """ This is the deck of cards we are playing from. It will hold a list of cards, shuffle that deck,
    deal cards to players, and track if the deck is empty.
    """
    def __init__(self):
        """Initialize an empty list of cards."""
        self.cards = []


    def generate_shuffled_deck(self):
        """ Generate the deck and shuffle it."""
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        faces = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        for this_card in product(suits,faces):
            self.cards.append(Card(this_card[0],this_card[1]))
        shuffle(self.cards)


    def draw_card(self):
        """ Remove a card from the end of the shuffled deck and return it."""
        return self.cards.pop()


    def is_empty(self):
        """ Return True if the deck has been exhausted."""
        return len(self.cards) == 0


class Hand:
    """A class that holds the set of cards of a player. It maintains the value of the hand."""
    def __init__(self):
        """Create an empty list of cards and a zero value."""
        self.cards = []
        self.value = 0


    def update_value(self):
        """ Update the value attribute with the current value of the deck."""
        card_values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11
        }

        # Add up the values of all the cards. Count number of aces.
        current_value = 0
        num_of_aces = 0
        for card in self.cards:
            current_value += card_values[card.face]
            if card.face == "A":
                num_of_aces += 1

        # If values add up to a bust, use "A" value = 1 for aces up to the max number of aces.
        while current_value > 21:
            if num_of_aces == 0:
                break
            current_value -= 10
            num_of_aces -= 1

        # Update hand's value.
        self.value = current_value


    def add_card(self, dealt_card):
        """Add the dealt card to the current hand."""
        self.cards.append(dealt_card)
        self.update_value()


    def present_hand(self):
        """Print the entire hand and the current value of it on the screen."""
        for card in self.cards[:-1]:
            card.print_card()
            print(", ", end = "")
        self.cards[-1].print_card()
        print("\nThe hand's value is {}".format(self.value))


class Player:
    """A class that represents a player in the game. A player has a name and a hand.
    """
    def __init__(self, player_name):
        """Create an empty hand. Initialize player's name."""
        self.hand = Hand()
        self.player_name = player_name


    def want_another_card(self):
        """Present the player's current hand, then prompt the player if they want another card.
        Returns True if player enters does.
        """
        self.hand.present_hand()
        while True:
            want_another_card = input("Do you want another card? Enter Y/y for yes or N/n for no.")
            if want_another_card.lower() == "y" or want_another_card.lower() == "n":
                break
            print("I did not understand. Please enter only 'Y/y' or 'N/n'!")
        return want_another_card.lower() == "y"


    def is_busted(self):
        """Return True if player is busted."""
        return self.hand.value > 21





class Blackjack:
    """A class for the blackjack game. It controls the flow of the entire game."""
    def __init__(self):
        self.players =[]
        #Generate dealer
        self.dealer = Dealer()
        #Generate the deck.
        self.deck = Deck()
        self.deck.generate_shuffled_deck()
        #Generate players
        self.generate_players(int(input("How many people are playing!: ")))
        self.deal_in_players()
        #Display everyone's hand
        self.show_opening_hand()

    #Ask user how many players will participate. Store this number in Blackjack.
    def generate_players(self, num_players):
        """This function will generate all the human players in the game"""
        #Get player's names. Create list of players. Create dealer.
        for people in range(num_players):
            name = input("Name of " + str(people + 1) + " player: ")
            self.players.append(Player(name))


    #Deal each player two cards from deck. Deal dealer one card.
    def deal_in_players(self):
        for gamers in self.players:
            gamers.hand.add_card(self.deck.draw_card())
            gamers.hand.add_card(self.deck.draw_card())
        #Deal dealer one card
        self.dealer.hand.add_card((self.deck.draw_card()))

    #Display everyone's hand
    def show_opening_hand(self):
        for gamer in self.players:
            print("{} has".format(gamer.player_name), end = " ")
            gamer.hand.present_hand()
            print()
        #Display dealer's hand.
        print("{} has shown the".format(self.dealer.player_name), end = " ")
        self.dealer.hand.present_hand()
        print()

    #updates the dealer on the highest value
    def tell_dealer_value(self, value):
        self.dealer.update_highest_hand_value(value)
    #Iterate over all players.
    # Let each player be dealt cards until they pass or go bust. After each player stops,
    # update highest value in the game.

    #Let the dealer be dealt more cards until it stops.

    #Check all players' hand and dealer's hand to see who won or lost
    #Announce reults.


class Dealer(Player):
    """A class that represents the dealer."""
    def __init__(self, dealer_name="Dealer"):
        Player.__init__(self, dealer_name)
        self.dealers_goal = 17


    #This will update the highest hand value in the game so that the dealer program knows it.
    def update_highest_hand_value(self, value):
        if value > self.dealers_goal:
            self.dealers_goal = value

    def run_dealer(self):
        """Implement dealer's behavior."""
        pass
        #Dealer draws cards until
            # dealer hand value is at least 17
            # dealer hand value is no worse than the best player hand
            # dealer goes bust

