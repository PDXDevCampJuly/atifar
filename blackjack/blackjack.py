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


    def present_hand(self, name):
        """Print the entire hand and the current value of it on the screen."""
        print("\n{}'s hand's value is {}".format(name, self.value))
        if len(self.cards) > 0:
            for card in self.cards[:-1]:
                card.print_card()
                print(", ", end = "")
            self.cards[-1].print_card()
            print()


class Player:
    """A class that represents a player in the game. A player has a name and a hand.
    """
    def __init__(self, player_name):
        """Create an empty hand. Initialize player's name."""
        self.hand = Hand()
        self.player_name = player_name


    def want_another_card(self):
        """Prompt the player if they want another card.
        Returns True if player does.
        """
        while True:
            want_another_card = input("Do you want another card? Enter Y/y for yes or N/n for no.")
            if want_another_card.lower() == "y" or want_another_card.lower() == "n":
                break
            print("I did not understand. Please enter only 'Y/y' or 'N/n'!")
        return want_another_card.lower() == "y"


    def is_busted(self):
        """Return True if player is busted."""
        return self.hand.value > 21


class Dealer(Player):
    """A class that represents the dealer."""
    def __init__(self, dealer_name="Dealer"):
        Player.__init__(self, dealer_name)


    def want_another_card(self):
        """Returns True if dealer's goal has not been met yet.
        """
        return self.hand.value <= 17


class Blackjack:
    """A class for the blackjack game. It controls the flow of the entire game."""
    def __init__(self):
        #Generate empty list to hold players
        self.players = []
        #List of players that have not yet busted
        self.players_still_alive = []
        #Generate dealer
        self.dealer = Dealer()
        #Generate the deck.
        self.deck = Deck()

    #Ask user how many players will participate. Store this number in Blackjack.
    def generate_players(self, num_players):
        """This function will generate all the human players in the game"""
        #Get player's names. Create list of players. Create dealer.
        for people in range(num_players):
            name = input("Name of " + " player " + str(people + 1) + ":")
            self.players.append(Player(name))
        self.players_still_alive = self.players[:]


    def run_game(self):
        """Run the game. This is the entry function to the game."""
        #Shuffle deck of cards
        self.deck.generate_shuffled_deck()
        #Generate players
        print("Welcome to this blackjack table.\n")
        self.generate_players(int(input("How many people are playing!: ")))
        #Deal in players and dealer
        print("Let's deal in everyone.")
        self.deal_in_players()
        #Display everyone's hand
        self.show_opening_hand()
        print("Let's play.")
        #Iterate over all players
        for player in self.players:
            print()
            player.hand.present_hand(player.player_name)
            #Deal player cards until busted or they stop
            while not player.is_busted():
                if player.want_another_card():
                    #Add card to player's hand
                    player.hand.add_card(self.deck.draw_card())
                    #Display player's hand
                    player.hand.present_hand(player.player_name)
                else:
                    break
            if player.is_busted():
                print("{} is busted.".format(player.player_name))

        #Update list of players still in the game
        for player in self.players:
            if player.is_busted():
                self.players_still_alive.remove(player)

        #It's the dealer's turn to play.
        print("\nIt's the Dealers turn now!\n")
        while not self.dealer.is_busted():
            if self.dealer.want_another_card():
                #Add card to dealer's hand
                self.dealer.hand.add_card(self.deck.draw_card())
                #Display dealer's hand
                self.dealer.hand.present_hand(self.dealer.player_name)
            else:
                break

        #Check who won. Display the end result.
        self.wrap_up_game()


    def wrap_up_game(self):
        """Check who won. Display the end result."""
        #If a player got 21, they won...
        winning_player = []
        for player in self.players_still_alive:
            if player.hand.value == 21 or self.dealer.hand.value > 21 or player.hand.value > self.dealer.hand.value:
                winning_player.append(player)
            #check who didn't get 21, but is higher then the dealer
        number_of_winning_players = len(winning_player)
        if number_of_winning_players > 0:
            print(("\nThe winners are: " if number_of_winning_players > 1 else "\nThe winner is: ") +
                  ", ".join([player.player_name for player in winning_player]))
        elif self.dealer.is_busted():
            print("Nobody wins.")
        else:
            print("The dealer wins.")


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
            gamer.hand.present_hand(gamer.player_name)
        #Display dealer's hand.
        print()
        self.dealer.hand.present_hand(self.dealer.player_name)
        print("-" * 30)


##############################################################################
# BEGIN TEST CODE
def test_card():
    print("Testing Card")
    joker = Card("red","joker")
    print("The face: " + joker.face)
    print("the suit: " + joker.suit)
    print("Testing print_card")
    joker.print_card()
    print()

def test_deck():
    print("\nTesting Deck")
    tarot = Deck()
    print("Number of cards in deck, should be empty:", len(tarot.cards))
    tarot.generate_shuffled_deck()
    print("Number of cards in deck, should be 52:", len(tarot.cards))
    print("Testing draw_card()")
    random_card = tarot.draw_card()
    random_card.print_card()
    print()
    print("Number of cards in deck, should be 51:", len(tarot.cards))

def test_hand():
    print("\nTesting Hand")
    poker = Hand()
    print("Number of cards in hand, should be empty: ", len(poker.cards))
    print("Testing present_hand of James on empty hand")
    poker.present_hand("James")
    print("Initial value of hand, should be zero:", poker.value)
    print("Checking add_card, adding ace of hearts ")
    poker.add_card(Card("Hearts","A"))
    poker.present_hand("James")
    print("Value of hand, should be 11:", poker.value)
    print("Checking add_card, adding ace of clubs ")
    poker.add_card(Card("Clubs","A"))
    poker.present_hand("James")
    print("Value of hand, should be 12:", poker.value)
    print("Checking add_card, adding king of clubs ")
    poker.add_card(Card("Clubs","K"))
    poker.present_hand("James")
    print("Value of hand, should be 12:", poker.value)

def test_player():
    print("\nTesting Player")
    print("Creating player Mary.")
    mary = Player("Mary")
    print("The player's name is '{}'".format(mary.player_name))
    print("Player Mary has the following hand:", mary.hand)
    print("Checking is_busted(), should be False.", mary.is_busted())
    print("Adding three cards, adding king of hearts, king of clubs, king of diamonds.")
    mary.hand.add_card(Card("Hearts","K"))
    mary.hand.add_card(Card("Clubs","K"))
    mary.hand.add_card(Card("Diamonds","K"))
    print("Checking is_busted(), should be True.", mary.is_busted())
    #Player.want_another_card() will be tested as part of Blackjack.run_game()

def test_dealer():
    print("\nTesting Dealer")
    print("Creating dealer with default name.")
    mary = Dealer()
    print("The dealer's name is '{}'".format(mary.player_name))
    print("Dealer has the following hand:", mary.hand)
    print("Testing want_another_card()  should be True", mary.want_another_card())
    print("Checking is_busted(), should be False.", mary.is_busted())
    print("Adding one cards, adding king of hearts")
    mary.hand.add_card(Card("Hearts","K"))
    mary.hand.present_hand("Dealer")
    print("Testing want_another_card() should be True", mary.want_another_card())
    print("Adding one cards, adding king of clubs")
    mary.hand.add_card(Card("Clubs","K"))
    mary.hand.present_hand("Dealer")
    print("Testing want_another_card, should be False", mary.want_another_card())
    print("Adding one cards, adding king of Spades")
    mary.hand.add_card(Card("Spades","K"))
    mary.hand.present_hand("Dealer")
    print("Checking is_busted(), should be True.", mary.is_busted())


def test_blackjack():
    #Create blackjack object
    game = Blackjack()
    #Check that attributes initialized correctly
    print("Number of players (should be 0):", len(game.players))
    print("Number of players_still_alive (should be 0):", len(game.players_still_alive))
    print("Dealer object:", game.dealer)
    print("Deck object):", game.deck)
    # game.generate_players() has been tested interactively
    print("checking deal in players, with manually added players")
    game.players = [Player("Jeff"), Player("Deno"), Player("Jane")]
    game.players_still_alive = game.players[:]
    game.deal_in_players()
    print("Number of players (should be 3):", len(game.players))
    print("Number of players_still_alive (should be 3):", len(game.players_still_alive))








    #Check generate_players()

    #Check run_game()







# END TEST CODE
##############################################################################





if __name__ == "__main__":
    game = Blackjack()
    game.run_game()
