"""
the card class will be used to make the individual cards
this class will contain three elements - suits, rand and value
the value will be a numerical which can be used to easily compare the cards
"""

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
value = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suits, rank):
        self.suits = suits
        self.rank = rank
        self.value = value[rank]

    def __str__(self):
        return f'{self.rank} of {self.suits}'


if __name__ == '__main__':
    print('Please run Game_Block!')
