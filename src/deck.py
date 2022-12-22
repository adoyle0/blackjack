import random

class Deck:
    cards = []

    def count(self):
        return len(self.cards)

    def shuffle(self, n_decks):
        n_decks = 1 if not n_decks or n_decks not in '12345678' else n_decks
        n_decks = int(n_decks)
        n_decks = 8 if n_decks > 8 else n_decks
        suits = '♠♥♦♣'
        cards = 'A234567890JQK'
      # cards = 'A0A0A0A0A0A0A'
        while n_decks > 0:
            self.cards +=  [card + suit for card in cards for suit in suits]
            n_decks -= 1
    
    def count_below(self, n):
        if self.count() < n:
            return True

    def draw(self):
        return self.cards.pop(random.choice(range(self.count())))
