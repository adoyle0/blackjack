class CLI:
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

    def draw_card_part(self, vs):
        value = '10' if vs[0] == '0' else vs[0] + ' '
        suit =  vs[1] + ' '

        # request text (not emoji) render of preceeding glyph but can break some fonts
        # suit += '\uFE0E'

        return f'''\
┌──
│{value}
│{suit}
│  
│  
│  
└──'''

    def draw_player_hand(self, player, game):
        card_stack = [self.draw_card_part(card) for card in player.hand]
        card_stack.append(self.card_rest)

        if player.name == 'Dealer' and game.active:
            card_stack[0] = self.hidden_part

        card_slices = [card.splitlines() for card in card_stack]
        card_height = len(card_slices[0])

        buffer = ''
        for i in range(card_height):
            buffer += ''.join([card_slice[i] for card_slice in card_slices])+'\n'

        return buffer[:-1]

    def show_players(self, game):
        buffer = ''
        for player in game.players:
            buffer += f"\n  {player.name}{37*' '}Score: {player.score(game)}\n{self.draw_player_hand(player, game)}"

        return buffer

    def update(self, game):
        buffer = f'{self.clear}{self.title}{self.show_players(game)}'
        if not game.active:
            buffer += '\n' + game.score()

        return buffer



