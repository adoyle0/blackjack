from src.deck import Deck
from src.screen import Screen
from src.gamemaster import GameMaster

def main():
    global kill
    global screen
    global num_decks
    global deck
    game = GameMaster()

    for player in game.players:
        for _ in range(2):
            player.hand.append(deck.draw())

    dealer = game.dealer
    player = game.player


    while game.active:
        screen.update(game)
        if player.blackjack():
            game.active = False
            print('Blackjack!')
            break

        if game.active:
            user_input = input(str(deck.count()) + ' cards left in deck.\n[H]it or [S]tand? ')

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
                    if player.bust(game):
                        game.active = False
                case 's':
                    game.active = False
                    while dealer.score(game) < 17:
                        dealer.hand.append(deck.draw())


        screen.update(game)
        if not game.active:
            game.score()


kill = False
screen = Screen()

print(screen.intro)

num_decks = input('How many decks? (1-8): ')
deck = Deck(num_decks)

while not kill:
    main()
    user_input = input('Play again? [Y/n] ')
    match user_input.lower():
        case 'n':
            kill = True

