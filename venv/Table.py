from Player import Player
from Player import Dealer
from CardPool import CardPool


class Table:
    def __init__(self, player_name, decks_used=4):
        self.players = [Player(player_name)]
        self.dealer = Dealer()
        self.number_of_decks = decks_used
        self.card_pool = CardPool(number_of_decks=decks_used)
        self.used_card_pool = []

    def deal_top(self, player):
        """Takes the top card in the cardpool and gives it to the player received
        Input: Player
        Output: None
        """
        player.add_card_to_hand(self.card_pool.remove_top_deck())

    def play_round(self):
        """Plays all the actions since the start of the betting phase for all players in the game
        Input: None
        Output: None"""
        playing_players = self.enter_bets()
        self.give_cards()
        for player in self.players:
            if player.name in playing_players:
                self.play_hand(player)

    def play_hand(self, player):
        """Let's a player choose its actions to play a hand of blackjack once the bets have been made and the cards
        have been given to each player
        Input: Player
        Output: None"""
        if not player.has_blackjack():
            while player.get_hand_value() <= 21:
                self.print_current_state(player, sd=False)
                action = player.get_action()
                if action == 'Hit':
                    self.deal_top(player)
                if action == 'Stand':
                    break
                if action == 'Split':
                    pass
                if action == 'Double':
                    player.stack -= player.amount_bet
                    player.amount_bet *= 2
                    self.deal_top(player)
                    break
                    # If player did not bust dealer plays
            if (player.get_hand_value() <= 21):
                self.dealer_plays()
        self.print_current_state(player, sd=True)
        self.declare_winner(player)
        self.reset_table()
        print(self.players[0])

    def reset_table(self):
        """Clears all players and dealer hands storing their contents on Self.UsedCards and adds those cards
        back to the cardpool and reshuffles if the 65% of the deck has been gone through"""
        # Clear dealers hand storing used cards on a list
        while self.dealer.hand:
            self.used_card_pool.append(self.dealer.hand.pop(0))
        # Clear all players hands storing used cards on a list
        for player in self.players:
            while player.hand:
                self.used_card_pool.append(player.hand.pop(0))
        # If we're reaching certain depth on our cardpool we add the used cards back to it and then reshuffle the deck
        if len(self.card_pool.cards) < self.number_of_decks * 52 * 0.65:
            self.card_pool.add_cards(self.used_card_pool)
            self.card_pool.shuffle_cards()

    def dealer_plays(self):
        """
        While the dealer has exceeded 17 the dealer keeps dealing cards to him
        """
        while self.dealer.get_hand_value(showdown=True) < 17:
            self.deal_top(self.dealer)

    def declare_winner(self, player):
        """
        Checks if the player or the dealer won, giving the player a reward acording to it bet, except on a natural 21
        where the reword follows a 2:1 ratio
        :param player: Indicate the player that we have to check against the dealer
        """
        if player.has_blackjack():
            print(f"BLACKJACK! Player wins!{player.amount_bet * 2}\n")
            player.stack += player.amount_bet * 3
        elif player.get_hand_value() > 21:
            print('BUSTED, HOUSE WINS!\n')
        elif self.dealer.get_hand_value(showdown=True) > 21:
            print('DEALER BUSTED, PLAYER WINS!\n')
            player.stack += 2 * player.amount_bet
        elif player.get_hand_value() > self.dealer.get_hand_value(showdown=True):
            print('PLAYER IS CLOSER TO 21, PLAYER WINS!')
            player.stack += 2 * player.amount_bet
        elif self.dealer.has_blackjack():
            print('DEALER HAS BLACKJACK, HOUSE WINS!')
        elif self.dealer.get_hand_value(showdown=True) == player.get_hand_value():
            print('PUSH! PLAYER GETS BACK ITS BET')
            player.stack += player.amount_bet
        else:
            print('DEALER IS CLOSER TO 21, HOUSE WINS!')

    def print_current_state(self, player, sd=False):
        """Print both Dealers and player recieved as a parameter hands
        Input: Player
        Output: None"""
        self.dealer.show_hand(showdown=sd)
        player.show_hand(bet=True)

    def give_cards(self):
        """Gives every player 2 initial hole cards and 2 cards for the dealer"""
        # Cards for players
        for player in self.players:
            self.deal_top(player)
            self.deal_top(player)
        # Cards for the Dealer
        self.deal_top(self.dealer)
        self.deal_top(self.dealer)

    def enter_bets(self):
        """We ask for every player player if they want to play the hand and how much would they like to bet"""
        all_bets = {}
        for player in self.players:
            bet = player.input_bet_amount()
            all_bets[player.name] = bet
            player.amount_bet = bet
        return all_bets
