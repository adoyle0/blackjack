class Screen:
    def __init__(self):
        self.title = '''\
                                                        
 .oPYo. 8               8        o               8      
 8   `8 8               8        8               8      
o8YooP' 8 .oPYo. .oPYo. 8  .o    8 .oPYo. .oPYo. 8  .o  
 8   `b 8 .oooo8 8    ' 8oP'     8 .oooo8 8    ' 8oP'   
 8    8 8 8    8 8    . 8 `b.    8 8    8 8    . 8 `b.  
 8oooP' 8 `YooP8 `YooP' 8  `o. oP' `YooP8 `YooP' 8  `o. 
:......:..:.....::.....:..::......::.....::.....:..::...
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::'''

        self.clear = '\033c' 
        self.intro = self.clear + self.title
        self.deck = '''\
┌────────┐┐┐┐┐┐
│░░░░░░░░││││││
│░░░░░░░░││││││
│░░░░░░░░││││││
│░░░░░░░░││││││
│░░░░░░░░││││││
└────────┘┘┘┘┘┘'''

        self.hidden_part = f'''\
┌──
│░░
│░░
│░░
│░░
│░░
└──'''

        self.hidden_rest = f'''\
──────┐
░░░░░░│
░░░░░░│
░░░░░░│
░░░░░░│
░░░░░░│
──────┘'''

        self.card_rest = f'''\
──────┐
      │
      │
      │
      │
      │
──────┘'''

    def make_card(self, vs, style):
        value = vs[0]
        value = '10' if value == '0' else value + ' '
        suit =  vs[1] + ' '

        # request text (not emoji) render of preceeding glyph but can break some fonts
        # suit += '\uFE0E'

        card_part = f'''\
┌──
│{value}
│{suit}
│  
│  
│  
└──'''

        match style:
            case 'deck': 
                return self.deck
            case 'card_rest':
                return self.card_rest
            case 'hidden_part':
                return self.hidden_part
            case 'hidden_rest':
                return self.hidden_rest
            case 'card_part':
                return card_part

    def print_hand(self, player, game):
        player_cards = [self.make_card(card,'card_part') for card in player.hand]

        if player.name == 'Dealer' and game.active:
            player_cards[0] = self.make_card('na','hidden_part')

        player_cards.append(self.make_card('na','card_rest'))
        card_slices = [str(card).splitlines() for card in player_cards]

        for i in range(7):
            clist = [card_slice[i] for card_slice in card_slices]
            carriage = ''
            for chunk in clist:
                carriage += chunk
            print(carriage)

    def update(self, game):
        print(self.clear)
        print(self.title)
        for player in game.players:
            print('  '+player.name,'''\
                                     Score:''', player.score(game))
            self.print_hand(player, game)
