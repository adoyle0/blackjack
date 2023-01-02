class PlayerController():
    def __init__(self):
        self.seated = True

    def get_decks(self):
        user_input = input('How many decks? (1-8): ')
        if not user_input:
            return '1'
        if user_input in 'qx':
            self.seated = False
        return (int(user_input) if user_input in '12345678' else 1)

    def get_input(self, count):
        return input(f'{count} cards left in deck.\n[H]it or [S]tand? ')

    def ask_deal_again(self):
        user_input = input('Play again? [Y/n] ').lower()
        if not user_input:
            return
        elif user_input in 'qnx':
            self.seated = False

