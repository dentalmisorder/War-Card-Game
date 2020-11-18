"""
GAME SETUP AND GAME SETTINGS, ALSO A START POINT
IF YOU WANT TO START A GAME, JUST RUN game.py (THIS ONE)
(YOU CAN SETUP HOW MANY CARDS ARE DRAWN AT WAR 
AND BOTH PLAYERS START AMOUNT OF CARDS)
"""

#imports
import random
import player
import deck
import card

#setup
player_one = player.Player('Player1')
player_two = player.Player('Player2')

new_deck = deck.Deck()
new_deck.shuffle()

how_many_cards_at_war = 5
players_should_get = int(len(new_deck.all_cards) / 2)

#we can adjust cards for players by typing in range(amount of cards for each player)
for card in range(players_should_get):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    #GAME STARTS

    round_num += 1
    print(f'Round: {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player one has no cards left! Player Two wins!')
        break

    if len(player_two.all_cards) == 0:
        print('Player two has no cards left! Player One wins!')
        break
    
    #START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())

    at_war = True

    #while at WAR
    while at_war:
        if player_one_cards[-1].card_value > player_two_cards[-1].card_value:
            #if player one card was greater value then p2 cards
            #player one take all the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False #war ends cause p1 got all the cards (he won)
        elif player_two_cards[-1].card_value > player_one_cards[-1].card_value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False #war ends cause p2 got all the cards (he won)
        else:
            print('WAR!')

            if len(player_one.all_cards) < how_many_cards_at_war:
                print('Player One cant fight..')
                print('Player Two wins!')
                game_on = False
                break

            elif len(player_two.all_cards) < how_many_cards_at_war:
                print('Player Two cant fight..')
                print('Player One wins!')
                game_on = False
                break

            else:
                for num in range(how_many_cards_at_war):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())