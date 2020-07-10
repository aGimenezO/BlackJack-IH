class Player:
    def __init__(self, name, stack=100):
        """
        Creator function of the class player, instantiating a name, its stack and an empty hand and a bet amount = 0
        :param name: The name of the Player
        :param stack: The amount of money a player has to play
        """
        self.name = name
        self.stack = stack
        self.hand = []
        self.amount_bet = 0

    def __str__(self):
        return '{} {}€'.format(self.name, self.stack)

    def add_card_to_hand(self, card):
        """
        Adds to the players hand the card received
        :param card: The card to be added to the players hand
        """
        self.hand.append(card)

    def show_hand(self, bet=False):
        """
        Prints the players current hand, showing the amount bet aswell if requested via the parameter "bet"
        :param bet: Indicates if we want to include the bet amount by the player in the printed message
        """
        if bet:
            print(f"{self.name}:{[str(card) for card in self.hand]} =  {self.get_hand_value()} Bet amount: "
                  f"{self.amount_bet}€\n")
        else:
            print(f"{self.name}:{[str(card) for card in self.hand]} =  {self.get_hand_value()}\n")

    def hand_allows_double(self):
        """
        Checks if a hand can be optable to do the double action, this can only be with an 9,10 or 11 and the player
        has enought stack to pay for another time the initial bet amount
        :return: Boolean
        """
        return self.get_hand_value() in [9, 10, 11] and self.stack > self.amount_bet * 2

    def hand_allows_split(self):
        """
        Checks if a hand is optable for doing a split action, creating 2 hands to play
        :return: Boolean
        """
        return False
        # This is the correct line that should be used once a proper structure of split management is added
        return len(self.hand) == 2 and self.hand[0].value == self.hand[1].value

    def get_action(self):
        """
        List the actions that are possible to do for the player, depending on the current game state, the possible options
        right now are Hit,Stand and double, and SPLIT should be implemented.
        :return: Returns the action chosen to perform by the player
        """
        options = ['Hit', 'Stand']
        if self.hand_allows_double():
            options.append('Double')
        if self.hand_allows_split():
            options.append('Split')
        input_string = 'Which action would you like to do?\n'
        for i in range(len(options)):
            input_string += f"{i+1} - {options[i]}\n"
        while True:
            action = eval(input(input_string))-1
            if action < len(options):
                break
            else:
                print(
                    'The input you entered doesn\'t match with any of the possibilities, please enter a correct number')
        return options[action]

    def get_hand_value(self):
        """
        :return:
        """
        value = 0
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
        return value

    def has_blackjack(self):
        """
        Determines if the player has a natural 21, that being a hand of 2 cards, an Ace and a 10, which can be in the
        form of a figure card
        :return: Boolean
        """
        return len(self.hand) == 2 and self.get_hand_value() == 21

    def input_bet_amount(self):
        """
        This functions lets the player choose how much money do they want to put into the pot
        :return: Integer amount indicating the bet amount
        """
        while True:
            try:
                bet_amount = eval(input(f"Which amount would you like to bet? Stack: {self.stack}€\n"))
            except Exception:
                print('A problem ocurred, please re-enter the amount you would like to bet\n')
            break
        if bet_amount < 0:
            bet_amount = 0
        self.amount_bet = min(bet_amount, self.stack)
        self.stack = self.stack - bet_amount
        return self.amount_bet


class Dealer(Player):

    def __init__(self):
        super().__init__(name='Dealer')
        self.hand = []
        self.is_human = False
        self.stack = '999999999999999'

    def show_hand(self, showdown=False):
        """
        This function prints the Dealer's hand , hiding the first card if the player hasn't still ended his actions
        :param showdown: Indicates if the player has ended their action phase
        """
        if showdown:
            print(f"{self.name}:{[str(card) for card in self.hand]} =  {self.get_hand_value(showdown=True)}\n")
        elif len(self.hand) > 1:
            print(f"{self.name}:[?,{self.hand[1]}] =  {self.get_hand_value(showdown=False)} \n")

    def get_hand_value(self, showdown=False):
        """
        Returns the total value of the dealers hand. While the player has not ended his action the first card is not counted since it has not been revelaed yet.
        :param showdown: Indicates if the first card has to be shown if True or not show it otherwise
        :return: Integer indicating the value of the hand
        """
        value = 0
        aces = 0
        for card in self.hand[1 - showdown:]:
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
        return value

    def has_blackjack(self):
        """
        Returns if the dealer has a natural 21
        :return: Boolean indicating if length of hand is 2 value is 21
        """
        return len(self.hand) == 2 and self.get_hand_value(showdown=True) == 21
