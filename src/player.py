class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def tally_hand(self):
        cards = [card[0] for card in self.hand]
        cards = ['11' if card == 'A' else card for card in cards]
        scores = [10 if card in 'JQK0' else int(card) for card in cards]
        return scores

    def score(self, game):
        if self.name == 'Dealer' and game.active:
            score = sum(self.tally_hand()[1:])
        else:
            score = sum(self.tally_hand())

        if score > 21 and 11 in self.tally_hand():
            return score - 10
        else:
            return score

    def bust(self, game):
        if self.score(game) > 21:
            return True

    def blackjack(self, game):
        if game.active and self.name == 'Dealer':
            return False
        elif self.tally_hand() in [[10,11],[11,10]]:
            return True
