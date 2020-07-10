class Card:
    """Represents a playing card, defined by a value and a suit."""

    @staticmethod
    def get_values():
        """This function returns all the values a card can have
            Input: None
            Output: A list of string containg"""

        return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    @staticmethod
    def get_suits():
        """ Returns all the suits a card can have
        Input: None
        Output: A list of strings containing the symbols of the possible suits"""

        return ['♠', '♥', '♣', '♦']

    def __init__(self, value, suit):
        """
        Creator function of the class Card, described by a value and a suit
        :param value: String Value of the card, the possible values reassemble the ones in the french deck:
        ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        :param suit:  String ASCII character containing the suit of the card
        """
        self.value = value
        self.suit = suit

    def __str__(self):
        return '{}{}'.format(self.value, self.suit)
