from typing import List

from Card import Card
from random import shuffle


class CardPool:
    cards: List[Card]

    def __init__(self, number_of_decks=4):
        self.cards = []
        for n in range(number_of_decks):
            for value in Card.get_values():
                for suit in Card.get_suits():
                    self.cards.append(Card(value, suit))
        self.shuffle_cards()

    def shuffle_cards(self):
        """Puts the contents in cards in random order
        Input: None
        Output: None"""

        shuffle(self.cards)

    def remove_top_deck(self):
        """This method returns the card at the top of the deck
            Input: None
            Output: The card on position 0 of the cards list"""

        return self.cards.pop(0)

    def __str__(self):
        return '[{}]'.format(', '.join(map(str, self.cards)))
