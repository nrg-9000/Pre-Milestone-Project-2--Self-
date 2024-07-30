"""
Player Block will have 2 player each with a hand of cards
Each player can add or remove cards from their hands
Cards will be removed from the top and added to the bottom of the hand
If we have multiple cards being added, then we will use .extend() and .append() if there is only one cards
This will stop creating nested lists - thus breaking the logic
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []  # starts with empty hand

    def remove_cards(self):
        return self.all_cards.pop(0) 
        

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):  # checking to see if there are multiple cards incoming
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards in their hands'


if __name__ == '__main__':
    print('Please run Game_Block!')
