# no_of_hands, card_per_hand, use_joker, no_of_decks
import random

def get_deck(joker=False, shuffle=False):
    suits = ['♠', '♥', '♦', '♣']
    ranks = [str(x) for x in range(2,11)] + ['J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    if joker:
        deck.extend([('*', '*')] * 2)
    if shuffle:
        random.shuffle(deck)
    return deck

my_deck = get_deck(joker=True)
print(len(my_deck), my_deck)
