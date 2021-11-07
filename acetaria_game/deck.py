from functools import reduce
from random import shuffle
from .constants import Veggie
from .cardstore import carrot_cards, pepper_cards
from .card import Card


class Deck():

    def __init__(self):
        self.cards = []

    def load(self):
        # TODO: Load all cards from file
        # Currently only CARROT cards
        self.cards.extend(carrot_cards)
        self.cards.extend(pepper_cards)

    def setup(self, number_of_players):
        # 2-6 players
        # cards: number_of_players * 3 of each veg
        self.number_of_players = number_of_players
        self.max_number_of_each_veggie = 3 * self.number_of_players
        # 1. Start with full deck
        self.load()
        # 2. Shuffle
     #    shuffle(self.cards)
        # 3. Iterate over cards, counting veggie_type
        for veggie_type in Veggie:
            self.limit_number_of_vegetables(
                veggie_type, self.max_number_of_each_veggie)

    def limit_number_of_vegetables(self, veggie_type, limit):
        count = 0
        cards = []
        for card in self.cards:
            if card.veggie_type == veggie_type:
                if count < limit:
                    count = count + 1
                    cards.append(card)
            else:
                cards.append(card)
        self.cards = cards

    def print_cards(self):
        for index, card in enumerate(self.cards):
            print(f'{index+1:02}', card.id, card.side.value)
            # card.show()

    def draw_card(self):
        try:
            card = self.cards.pop()
        except IndexError:
             card = Card(0, 0, lambda v: 0, "") 
        return card
