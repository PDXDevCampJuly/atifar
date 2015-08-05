import blackjack

tarot = blackjack.Deck()
tarot.generate_shuffled_deck()
for card in tarot.cards:
    card.print_card()
jenny = blackjack.Player("Jenny")

while jenny.want_another_card():
    jenny.hand.add_card(tarot.draw_card())

print("Is the deck empty", tarot.is_empty())

print("is Jenny Busted", jenny.is_busted())

