from src.deck import Deck
from src.io import CLI
from src.gamemaster import GameMaster

def main():
    global kill
    global ui
    global num_decks
    global deck
    game = GameMaster(deck)

    game.deal()

    while game.active:
        print(ui.update(game))
        if not game.blackjack():
            game.handle_player_input(ui.player_move(deck.count()), kill)

    print(ui.update(game))

kill = False
ui = CLI()
print(ui.intro)

num_decks = ui.get_decks()
if num_decks == 'q':
    kill = True

deck = Deck(num_decks)

while not kill:
    main()
    if not ui.play_again():
        kill = True
