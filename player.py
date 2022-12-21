class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def tally_hand(self):
        cards = [card[0] for card in self.hand]
        cards = ['11' if card == 'A' else card for card in cards]
        scores = [10 if card in 'JQK0' else int(card) for card in cards]
        return scores

    def score(self):
        score = sum(self.tally_hand())
        if score > 21 and 11 in self.tally_hand():
            return score - 10
        else:
            return score

    def bust(self):
        if self.score() > 21:
            return True
