from deck import Deck
from screen import Screen
from gamemaster import GameMaster

def main():
    screen = Screen()
    num_decks = input('How many decks? (1-8): ')

    game = GameMaster()
    deck = Deck()
    if deck.count_below(4):
        deck.shuffle(num_decks)

    for player in game.players:
        for _ in range(2):
            player.hand.append(deck.draw())

    dealer = game.players[0]
    player = game.players[1]


    while game.active:
        screen.update(game.players)
        if game.active:
            user_input = input(str(deck.count()) + ' cards left in deck.\n[H]it or [S]tand? ')
        else:
            user_input = input('Play again? [Y/n] ')
            
        match user_input.lower():
            case 'q':
                game.active = False
            case 'n':
                game.active = False
            case 'h':
                player.hand.append(deck.draw())
                if player.bust():
                    game.active = False
                    print('Player Bust!')
            case 's':
                while dealer.score() < 17:
                    dealer.hand.append(deck.draw())
                game.score()

main()
