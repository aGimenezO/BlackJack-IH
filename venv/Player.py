class Player:
    def __init__(self, name, stack=500, is_human=True):
        self.name = name
        self.stack = stack
        self.hand = []
        self.amount_bet = 0
        self.is_human = is_human

    def __str__(self):
        return '{} {}€'.format(self.name, self.stack)

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def show_hand(self, bet=False):
        if bet:
            print(f"{self.name}:{[str(card) for card in self.hand]} =  {self.get_hand_value()} Bet amount: "
                  f"{self.amount_bet}€\n")
        else:
            print(f"{self.name}:{[str(card) for card in self.hand]} =  {self.get_hand_value()}\n")

    def hand_allows_double(self):
        return self.get_hand_value() in [10, 11]

    def hand_allows_split(self):
        return len(self.hand) == 2 and self.hand[0].value == self.hand[1].value

    def get_action(self):
        options = ['Hit', 'Stand']
        if self.hand_allows_double():
            options.append('Double')
        if self.hand_allows_split():
            options.append('Split')
        input_string = 'Which action would you like to do?\n'
        for i in range(len(options)):
            input_string += f"{i} - {options[i]}\n"
        while True:
            action = eval(input(input_string))
            if action < len(options):
                return options[action]
            else:
                print(
                    'The input you entered doesn\'t match with any of the possibilities, please enter a correct number')

    def get_hand_value(self):
        value = 0
        value_aces = 0
        aces = 0
        for card in self.hand:
            if card.value == 'A':
                aces += 1
                value += 11
            elif card.value in ['J', 'Q', 'K']:
                value += 10
            else:
                value += int(card.value)
        if aces and value > 21:
            while value > 21 and aces:
                aces -= 1
                value -= 10
        return str(value)

    def input_bet_amount(self):
        try:
            bet_amount = eval(input(f"Which amount would you like to bet? Stack: {self.stack}€\n"))
        except Exception:
            print('A problem ocurred, please re-enter the amount you would like to bet\n')
        bet_amount = 0
        if bet_amount <= 0:
            bet_amount = 0
        self.amount_bet = bet_amount
        if bet_amount > self.stack:
            return self.stack
        return bet_amount


class Dealer(Player):
    def __init__(self):
        super().__init__(name='Dealer')
        self.hand = []
        self.is_human = False
        self.stack = '999999999999999'

    def show_hand(self, showdown=False):
        if showdown:
            print(f"{self.name}:{[str(card) for card in self.hand]} =  {self.get_hand_value()}\n")
        elif len(self.hand) > 1:
            print(f"{self.name}:[?,{self.hand[1]}] =  {self.get_hand_value(showdown=True)} \n")

    def get_hand_value(self, showdown=False):
        value = 0
        value_aces = 0
        aces = 0
        for card in self.hand[1:]:
            if card.value == 'A':
                aces += 1
                value += 11
            elif card.value in ['J', 'Q', 'K']:
                value += 10
            else:
                value += int(card.value)
        if aces and value > 21:
            while value > 21 and aces:
                aces -= 1
                value -= 10
        return str(value)
