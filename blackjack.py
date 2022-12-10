motd = '''\
                                                        
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
    suit =  vs[1]

    # fuck discord
    # suit = suit + '\uFE0E'

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
    if style == 'card_rest':
        return card_rest
    if style == 'hidden_part':
        return hidden_part
    if style == 'hidden_rest':
        return hidden_rest
    if style == 'card_part':
        return card_part

def generate_deck():
    suits = '♠♥♦♣'
    cards = 'A234567890JQK'
    return [card + suit for card in cards for suit in suits]

def draw_card(player):
    global players
    global play_deck
    players.get(player).append(play_deck.pop(random.choice(range(len(play_deck)))))

def print_hand(player):
    global players
    global game_active
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
    global players
    for i in range(2):
        for player in players:
            if player != 'discard':
                draw_card(player)

def show_board():
    global players
    print('\033c', end='')
    print(motd)
    for player in players:
        if player != 'discard':
            print('  '+player,
            '\t\t\t\t      Score:',player_score(player))
            print_hand(player)

def score_hand(player):
    global players
    hand =   [card[0] for card in players.get(player)]
    hand =   ['1' if card == 'A' else card for card in hand]
    scores = [10 if card in 'JQK0' else int(card) for card in hand]
    return scores

def player_score(player):
    global players
    global game_active
    global gameover

    card_scores = score_hand(player)

    if len(card_scores) == 2 and sum(card_scores) == 11:
        game_active = False
        gameover = player + 'has blackjack!'

    if sum(card_scores) < 11:
        if 1 in card_scores:
            index = card_scores.index(1)
            card_scores[index] = 11

    if player == 'Dealer' and game_active == True:
        return sum(card_scores[1:])

    else:
        return sum(card_scores)

def main():
    global kill
    global players
    global play_deck
    global game_active
    global gameover

    gameover = 'Error'
    # 1-8 decks
    if len(play_deck) < 4:
        play_deck = generate_deck()
    # 5-9 seats
    players = {'discard':[],
               'Dealer': [],
               'Player': []}
    
    deal()
    game_active = True

    while game_active == True:
        show_board()
        user_input = input(str(len(play_deck)) + ' cards left in deck\n[H]it or [S]tand? ')
    
        if user_input.lower() == 'q':
            gameover = 'q'
            kill = True
            game_active = False
            break

        if user_input.lower() == 'r':
            game_active = False
        
        if user_input.lower() == 'h':
            draw_card('Player')
    
        if user_input.lower() == 's':
            game_active = False
            while player_score('Dealer') < 17:
                draw_card('Dealer')
            if player_score('Dealer') > 21:
                gameover = 'Dealer Bust!'
                break
            if player_score('Dealer') == player_score('Player'):
                gameover = 'Push.'
                break
            if player_score('Dealer') > player_score('Player'):
                gameover = 'House wins.'
                break
            if player_score('Dealer') < player_score('Player'):
                gameover = 'You win!'
                break

        if player_score('Player') > 21:
            gameover = 'Bust!'
            game_active = False


kill = False
play_deck = generate_deck()

while kill == False:
    main()
    for player in players:
        print(player)
    if gameover == 'q':
        break
    show_board()
    user_input = input(gameover + '\nPlay again? [Y/n] ')
    if user_input.lower() == 'n':
        kill = True

