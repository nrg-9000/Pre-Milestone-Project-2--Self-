"""
here we shall create the Deck class
on initialise, this will create a deck of 52 cards
we will create a shuffle function to shuffle the deck
we will create a remove function to remove a card of the deck
"""


import Card_Block
from random import shuffle


class Deck:

    # initialising the class by creating a Deck of cards
    def __init__(self):
        self.all_cards = []  # all decks should start with an empty hand

        for suits in Card_Block.suits:
            for ranks in Card_Block.ranks:
                created_card = Card_Block.Card(suits, ranks)
                self.all_cards.append(created_card)

    # creating a shuffle method
    def shuffle(self):
        shuffle(self.all_cards)

    # creating a remove method to remove the first card
    def deal_one(self):
        return self.all_cards.pop()  # we had to add the 0 to make sure the first card gets removed (from the top of the deck)


if __name__ == '__main__':
    print('Please run Game_Block!')
