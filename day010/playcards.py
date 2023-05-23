suits = ['♠', '♥', '♦', '♣']
ranks = [str(x) for x in range(2, 11)] + ['J', 'Q', 'K', 'A']

deck = [(x, y) for x in ranks for y in suits] + [('*', '*'), ('*', '*')]

no_of_decks = 3

decks = deck * no_of_decks

print(len(decks))
print(decks.shuffle())