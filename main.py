from src.deck import Deck
from src.io import CLI
from src.blackjack import Blackjack

def main():
    kill = False
    ui = CLI()
    print(ui.intro)
    num_decks = ui.get_decks()
    if num_decks in 'qx':
        kill = True
    deck = Deck(num_decks)
    
    while not kill:
        game = Blackjack(deck)
    
        game.deal()
    
        while game.active:
            print(ui.update(game))
            if not game.blackjack():
                game.handle_player_input(ui.player_move(deck.count()), kill)
    
        print(ui.update(game))
    
        if not ui.play_again():
            kill = True
main()    
