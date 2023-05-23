# no_of_hands, card_per_hand, use_joker, no_of_decks
import random

def get_deck(shuffle=False):
    suits = ['♠', '♥', '♦', '♣']
    ranks = [str(x) for x in range(2,11)] + ['J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    if shuffle:
        random.shuffle(deck)
    return deck

my_deck = get_deck()
print(my_deck)
my_deck2 = get_deck(shuffle=True)
print(my_deck2)















# deck = []
# for suit in suits:
#     for rank in ranks:
#         deck.append((rank, suit))
# print(deck)

# def get_shuffled_deck():
#     deck = get_deck()
#     shuffle(deck)
#     return deck