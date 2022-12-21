class CardPrinter:
    def make_card(self, vs, style):
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
                return deck
            case 'card_rest':
                return card_rest
            case 'hidden_part':
                return hidden_part
            case 'hidden_rest':
                return hidden_rest
            case 'card_part':
                return card_part

    def print_hand(self, player):
        player_cards = [self.make_card(card,'card_part') for card in player.hand]
        if player == 'Dealer' and game_active:
            player_cards[0] = self.make_card('na','hidden_part')
        player_cards.append(self.make_card('na','card_rest'))
        card_slices = [str(card).splitlines() for card in player_cards]
        for i in range(7):
            clist = [card_slice[i] for card_slice in card_slices]
            carriage = ''
            for chunk in clist:
                carriage += chunk
            print(carriage)

