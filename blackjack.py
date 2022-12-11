title = '''\
                                                        
 .oPYo. 8               8        o               8      
 8   `8 8               8        8               8      
o8YooP' 8 .oPYo. .oPYo. 8  .o    8 .oPYo. .oPYo. 8  .o  
 8   `b 8 .oooo8 8    ' 8oP'     8 .oooo8 8    ' 8oP'   
 8    8 8 8    8 8    . 8 `b.    8 8    8 8    . 8 `b.  
 8oooP' 8 `YooP8 `YooP' 8  `o. oP' `YooP8 `YooP' 8  `o. 
:......:..:.....::.....:..::......::.....::.....:..::...
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::'''

import random

def make_card(vs, style):
    value = vs[0]

    if value == '0':
        value = '10'
    else:
        value += ' '

    suit =  vs[1] + ' '

    # request text render of preceeding glyph but can break some fonts
    # suit += '\uFE0E'

    deck = '''\
┌────────┐┐┐┐┐┐
│░░░░░░░░││││││
│░░░░░░░░││││││
│░░░░░░░░││││││
│░░░░░░░░││││││
│░░░░░░░░││││││
└────────┘┘┘┘┘┘'''
    card_rest = f'''\
──────┐
      │
      │
      │
      │
      │
──────┘'''
    hidden_part = f'''\
┌──
│░░
│░░
│░░
│░░
│░░
└──'''
    hidden_rest = f'''\
──────┐
░░░░░░│
░░░░░░│
░░░░░░│
░░░░░░│
░░░░░░│
──────┘'''
    card_part = f'''\
┌──
│{value}
│{suit}
│  
│  
│  
└──'''

    if style == 'deck': 
        return deck
    elif style == 'card_rest':
        return card_rest
    elif style == 'hidden_part':
        return hidden_part
    elif style == 'hidden_rest':
        return hidden_rest
    elif style == 'card_part':
        return card_part

def generate_deck(n_decks):
    n_decks = int(n_decks)
    if n_decks > 8:
        n_decks = 8
    suits = '♠♥♦♣'
    cards = 'A234567890JQK'
    deck = []

    while n_decks > 0:
        deck +=  [card + suit for card in cards for suit in suits]
        n_decks -= 1
    return deck

def draw_card(player):
    players.get(player).append(play_deck.pop(random.choice(range(len(play_deck)))))

def print_hand(player):
    player_cards = [make_card(card,'card_part') for card in players.get(player)]
    if player == 'Dealer' and game_active == True:
        player_cards[0] = make_card('na','hidden_part')
    player_cards.append(make_card('na','card_rest'))
    card_slices = [str(card).splitlines() for card in player_cards]
    for i in range(7):
        clist = [card_slice[i] for card_slice in card_slices]
        carriage = ''
        for chunk in clist:
            carriage += chunk
        print(carriage)

def deal():
    for i in range(2):
        for player in players:
            draw_card(player)

def show_board():
    print('\033c', end='')
    print(title)
    for player in players:
        print('  '+player,
        '\t\t\t\t      Score:',player_score(player))
        print_hand(player)

def score_hand(player):
    hand = [card[0] for card in players.get(player)]

    if hand == ['0','1'] or hand == ['1','0']:
        game_active = False
        gameover = player, 'has blackjack!'
        return [21]

    hand =   ['1' if card == 'A' else card for card in hand]
    scores = [10 if card in 'JQK0' else int(card) for card in hand]
    return scores

def player_score(player):
    card_scores = score_hand(player)

    if sum(card_scores) < 11:
        if 1 in card_scores:
            index = card_scores.index(1)
            card_scores[index] = 11

    if player == 'Dealer' and game_active == True:
        return sum(card_scores[1:])

    else:
        return sum(card_scores)

def main():
    global players
    global play_deck
    global game_active
    global gameover

    gameover = 'Error'

    if len(play_deck) < 4:
        play_deck = generate_deck(num_decks)

    # 5-9 seats
    players = {'Dealer': [],
               'Player': []}
    
    deal()
    game_active = True

    while game_active == True:
        show_board()
        user_input = input(str(len(play_deck)) + ' cards left in deck\n[H]it or [S]tand? ')
    
        if user_input.lower() == 'q':
            gameover = 'q'
            game_active = False

        elif user_input.lower() == 'r':
            game_active = False
        
        elif user_input.lower() == 'h':
            draw_card('Player')
    
        elif user_input.lower() == 's':
            game_active = False

            if player_score('Dealer') == 21:
                gameover = 'Dealer has blackjack!'
                break

            while player_score('Dealer') < 17:
                draw_card('Dealer')

            if player_score('Dealer') > 21:
                gameover = 'Dealer Bust!'

            elif player_score('Dealer') == player_score('Player'):
                gameover = 'Push.'

            elif player_score('Dealer') > player_score('Player'):
                gameover = 'House wins.'

            elif player_score('Dealer') < player_score('Player'):
                gameover = 'You win!'

        if player_score('Player') > 21:
            gameover = 'Bust!'
            game_active = False

kill = False
play_deck = []

num_decks = input('How many decks? (1-8): ')

while kill == False:
    main()
    if gameover == 'q':
        kill = True
        break
    show_board()
    user_input = input(gameover + '\nPlay again? [Y/n] ')
    if user_input.lower() == 'n':
        kill = True

