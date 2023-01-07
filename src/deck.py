import random

class Deck:
    def __init__(self, n_decks):
        self.cards = []
        self.n_decks = int(n_decks)

    def count(self):
        return len(self.cards)

    def shuffle(self):
        suits = '♠♥♦♣'
        cards = 'A234567890JQK'

        for _ in range(self.n_decks):
            self.cards +=  [card + suit for card in cards for suit in suits]

    def check(self):
        if self.count() < 1:
            self.shuffle()

    def draw(self):
        self.check()
        return self.cards.pop(random.choice(range(self.count())))

