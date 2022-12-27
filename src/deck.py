import random

class Deck:
    def __init__(self, n_decks):
        self.cards = []
        self.n_decks = n_decks

    def count(self):
        return len(self.cards)

    def shuffle(self, n_decks):
        self.cards = []
        n_decks = 1 if not n_decks or n_decks not in '12345678' else n_decks
        n_decks = int(n_decks)
        suits = '♠♥♦♣'
        cards = 'A234567890JQK'

        while n_decks > 0:
            self.cards +=  [card + suit for card in cards for suit in suits]
            n_decks -= 1

    def check(self):
        if self.count() < 1:
            self.shuffle(self.n_decks)

    def draw(self):
        self.check()
        return self.cards.pop(random.choice(range(self.count())))

