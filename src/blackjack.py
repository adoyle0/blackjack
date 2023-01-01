from src.player import Player

class Blackjack:
    def __init__(self, deck):
        self.deck = deck
        self.active = True
        self.players = [Player('Dealer'), Player('Player')] # 5-9 seats
        self.dealer = self.players[0] # Mickey
        self.player = self.players[1] #   Mouse

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
                status = player.name + ' has Blackjack!'

        return status
    def deal(self):
        for player in self.players:
            for _ in range(2):
                player.hand.append(self.deck.draw())

    def blackjack(self):
        for player in self.players:
            if player.blackjack(self):
                self.active = False
                return True

        return False

    def handle_player_input(self, input, kill):
        match input:
            case 'y':
                self.active = False
            case 'q':
                self.active = False
                kill = True
            case 'n':
                self.active = False
            case 'h':
                self.player.hand.append(self.deck.draw())
                if self.player.bust(self):
                    self.active = False
            case 's':
                self.active = False
                while self.dealer.score(self) < 17:
                    self.dealer.hand.append(self.deck.draw())

