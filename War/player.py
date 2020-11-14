"""
Player class that holds a deck of cards and can show card (remove from list)
and can add cards (if won someone in a fight)
"""
import card
import random

class Player():

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def add_cards(self, card):
        if type(card) == type([]):
            self.all_cards.extend(card)
        else:
            self.all_cards.append(card)

    def remove_card(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

spylestia = Player('Spylestia')
new_card = card.Card(random.choice(card.random_names), random.choice(card.clans), random.choice(card.ranks))
spylestia.add_cards(new_card)

print(spylestia.all_cards[0])
print(spylestia)