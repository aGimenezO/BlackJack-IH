from Player import Player
from Player import Dealer
from CardPool import CardPool


class Table:
    def __init__(self, playerName, decksUsed=6, dealerstopS17=False):
        self.players = [Player(playerName)]
        self.dealer = Dealer()
        self.dealerStopsAtS17 = dealerstopS17
        self.card_pool = CardPool()

    def deal_top(self, player):
        '''Takes the top card in the cardpool and gives it to the player received
        Input: Player
        Output: None
        '''
        player.add_card_to_hand(self.card_pool.remove_top_deck())

    def play_round(self):
        '''Plays all the actions since the start of the betting phase for all players in the game
        Input: None
        Output: None'''
        playing_players = self.enter_bets()
        self.give_cards()
        for player in self.players:
            if player.name in playing_players:
                self.print_current_state(player)
                self.play_hand(player)

    def play_hand(self, player):
        '''Let's a player choose its actions to play a hand of blackjack once the bets have been made and the cards
        have been given to each player
        Input: Player
        Output: None'''
        if player.get_hand_value() == 21:

        while player.get_hand_value() < 21:
        action = player.get_action()
        if action == 'Hit':
            self.deal_top(player)

    def print_current_state(self, player):
        self.dealer.show_hand()
        player.show_hand(bet=True)

    def give_cards(self):
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
