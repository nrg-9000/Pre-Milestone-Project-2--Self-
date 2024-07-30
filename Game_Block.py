"""
There will be two players
New deck will be created, shuffled and split between the two players
We will check if any players have zero cards in their hands - outer while loop
We will make current round hands from the total cards of the players
We will check for a WAR situation - inner while loop
"""

import Deck_Block
import Player_Block

# creating two players
player_one = Player_Block.Player('One')
player_two = Player_Block.Player('Two')

# creating a new deck
new_deck = Deck_Block.Deck()
new_deck.shuffle()   # shuffling new deck

# splitting the deck between the two players
for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# starting game logic
game_on = True
round_number = 0  # this is to keep count of the number of rounds played

# other while loop to check if any of the players have 0 cards in their hands
while game_on:
    round_number += 1
    print(f'Round number {round_number}')

    if len(player_one.all_cards) == 0:
        print('Player One has no cards in their hands')
        print('Player Two wins!!!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two has no cards in their hands')
        print('Player One wins!!!')
        game_on = False
        break

    # starting a new round

    player_one_hand = []
    player_one_hand.append(player_one.remove_cards())
    
    player_two_hand = []
    player_two_hand.append(player_two.remove_cards())
    
    # assuming start of WAR
    at_war = True

    while at_war and player_one_hand and player_two_hand:

        if player_one_hand[-1].value > player_two_hand[-1].value:
            player_one.add_cards(player_one_hand)
            player_one.add_cards(player_two_hand)

            at_war = False

        elif player_two_hand[-1].value > player_one_hand[-1].value:
            player_two.add_cards(player_one_hand)
            player_two.add_cards(player_two_hand)

            at_war = False

        else:
            
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print('Player One unable to declair War!')
                print('Player Two wins!!!')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declair War!')
                print('Player One wins!!!')
                game_on = False
                break

            else:
                for i in range(5):
                    if len(player_one.all_cards) > 0:  # suggested by chatGPT after infinite loop 
                        player_one_hand.append(player_one.remove_cards())
                    if len(player_two.all_cards) > 0:  # suggested by chatGPT after infinite loop
                        player_two_hand.append(player_two.remove_cards())