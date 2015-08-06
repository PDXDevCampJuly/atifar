from blackjack import Deck, Player, Blackjack
def random_tests_of_deck_and_player():
    tarot = Deck()
    tarot.generate_shuffled_deck()
    for card in tarot.cards:
        card.print_card()
    jenny = Player("Jenny")

    while jenny.want_another_card():
        jenny.hand.add_card(tarot.draw_card())

    print("Is the deck empty", tarot.is_empty())

    print("is Jenny Busted", jenny.is_busted())

def test_blackjack():
    gameboard = Blackjack()
    # print(gameboard.dealer.dealers_goal)
    # gameboard.tell_dealer_value(20)
    # print(gameboard.dealer.dealers_goal)

test_blackjack()