from src.cardprinter import CardPrinter
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
        print(self.title)
        for player in player_list:
            print('  '+player.name,
            '\t\t\t\t      Score:',player.score())
            printer.print_hand(player)
    
    def show_intro(self):
        print('\033c', end='')
        print(self.title)
