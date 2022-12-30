from src.player import Player

class GameMaster:
    def __init__(self):
        self.active = True
        self.players = [Player('Dealer'), Player('Player')] # 5-9 seats
        self.dealer = self.players[0]
        self.player = self.players[1]
        self.blackjack = False

    def score(self):
        status = 'Error'

        if self.dealer.score(self) == self.player.score(self):
            self.active = False
            status = 'Push.'
        elif self.dealer.score(self) > self.player.score(self):
            self.active = False
            status = 'House wins.'
        elif self.dealer.score(self) < self.player.score(self):
            self.active = False
            status = 'You win!'

        for player in self.players:
            if player.score(self) > 21:
                self.active = False
                status = player.name + ' Bust!'
            elif player.blackjack(self):
                self.active = False
                self.blackjack = True
                status = player.name + ' has Blackjack!'

        return status
