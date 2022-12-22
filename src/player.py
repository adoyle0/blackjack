class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.blackjack = False
        self.bust = False

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
            self.bust = True

    def blackjack(self):
        if self.tally_hand() in [[10,11],[11,10]]:
            self.blackjack = True

    def check(self):
        self.bust()
        self.blackjack()
