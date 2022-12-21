from cardprinter import CardPrinter
printer = CardPrinter()

class Screen:
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


    def update(self, player_list):
        print('\033c', end='')
        print(title)
        for player in player_list:
            print('  '+player.name,
            '\t\t\t\t      Score:',player.score())
            printer.print_hand(player)
    
    def player_display_score(self, player):
        card_scores = player_score(player)
        if sum(card_scores) > 21:
            if 11 in card_scores:
                index = card_scores.index(11)
                card_scores[index] = 1
        if player == 'Dealer' and game_active == True:
            return sum(card_scores[1:])
        else:
            return sum(card_scores)
    def intro():
        print('\033c', end='')
        print(screen.title)
