"""
Deck that will store all of our cards
"""
import card
import random

class Deck():

    def __init__(self):

        self.all_cards = []

        for card_clan in card.clans:
            for card_rank in card.ranks:
                created_card = card.Card(random.choice(card.random_names), card_clan, card_rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def show_all_cards(self):
        for card in self.all_cards:
            print(f'{card.card_name} | {card.card_clan} | {card.card_rank}')