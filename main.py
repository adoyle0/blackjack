from src.deck import Deck
from src.screen import Screen
from src.gamemaster import GameMaster

def main():
    global kill
    global screen
    global num_decks
    deck = Deck()
    game = GameMaster()

    if num_decks == 'q':
        game.active = False

    if deck.count_below(4):
        deck.shuffle(num_decks)

    for player in game.players:
        for _ in range(2):
            player.hand.append(deck.draw())

    dealer = game.dealer
    player = game.player

    while game.active:
        screen.update(game.players)

        if game.active:
            user_input = input(str(deck.count()) + ' cards left in deck.\n[H]it or [S]tand? ')

            if not user_input:
                user_input = 's'
            
        match user_input.lower():
            case 'y':
                game.active = False
            case 'q':
                game.active = False
                kill = True
            case 'n':
                game.active = False
            case 'h':
                player.hand.append(deck.draw())
            case 's':
                while dealer.score() < 17:
                    dealer.hand.append(deck.draw())

        screen.update(game.players)
        game.score()

        if not game.active:
            user_input = input('Play again? [Y/n] ')

kill = False
screen = Screen()
print(screen.show_intro())
num_decks = input('How many decks? (1-8): ')
while not kill:
    main()
