from src.deck import Deck
from src.io import CLI
from src.blackjack import Blackjack
from src.controller import PlayerController

def main():
    player = PlayerController()
    screen = CLI()

    print(screen.intro)

    deck = Deck(player.get_decks())
    
    while player.seated:
        game = Blackjack(deck)
        game.deal()
        game.check_player_blackjack()
        print(screen.update(game))
    
        while game.active:
            game.update(player.get_input(deck.count()))
            print(screen.update(game))

        player.ask_deal_again()
main()
