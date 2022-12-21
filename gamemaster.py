from player import Player

class GameMaster:
    active = True
    players = [Player('Dealer'), Player('Player')] # 5-9 seats
    dealer = players[0]
    player = players[1]

    def score(self):
        if self.dealer.score() == self.player.score():
            self.active = False
            print('Push.')
        elif self.dealer.score() > self.player.score():
            self.active = False
            print('House wins.')
        elif self.dealer.score() < self.player.score():
            self.active = False
            print('You win!')
