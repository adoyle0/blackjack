import random

class Deck:
    def __init__(self, n_decks):
        self.cards = []
        self.n_decks = n_decks

    def count(self):
        return len(self.cards)

    def shuffle(self):
        suits = '♠♥♦♣'
        cards = 'A234567890JQK'

        decks_to_shuffle = int(self.n_decks)

        while decks_to_shuffle  > 0:
            self.cards +=  [card + suit for card in cards for suit in suits]
            decks_to_shuffle -= 1

    def check(self):
        if self.count() < 1:
            self.shuffle()

    def draw(self):
        self.check()
        return self.cards.pop(random.choice(range(self.count())))

