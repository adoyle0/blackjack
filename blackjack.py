from src.deck import Deck
from src.io import CLI
from src.gamemaster import GameMaster

def main():
    global kill
    global ui
    global num_decks
    global deck
    game = GameMaster()

    for player in game.players:
        for _ in range(2):
            player.hand.append(deck.draw())

    dealer = game.dealer
    player = game.player

    while game.active:
        ui.update(game)

        if game.active:
            match ui.player_move(deck).lower():
                case 'y':
                    game.active = False
                case 'q':
                    game.active = False
                    kill = True
                case 'n':
                    game.active = False
                case 'h':
                    player.hand.append(deck.draw())
                    if player.bust(game):
                        game.active = False
                case 's':
                    game.active = False
                    while dealer.score(game) < 17:
                        dealer.hand.append(deck.draw())
            ui.update(game)

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
