from functools import reduce
from .constants import Veggie
from .card import Card


class Deck():

    def __init__(self):
        self.cards = []

    def load(self):
        # TODO: Load all cards from file
        # Currently only CARROT cards
        self.cards.extend([
            Card(101, Veggie.CARROT, lambda v: reduce(lambda x, y: x+5 if y >=
                                                      3 else x, list(v.values())), "5 / groentesoort met minstens 3 kaarten"),
            Card(102, Veggie.CARROT, lambda v: 0 if v[Veggie.CABBAGE] == 0 else (
                7 if v[Veggie.CABBAGE] % 2 == 0 else 3), "CABBAGE \n even aantal = 7 \n oneven aantal = 3"),
            Card(103, Veggie.CARROT, lambda v: 2 *
                 v[Veggie.CABBAGE], "2 / CABBAGE"),
            Card(104, Veggie.CARROT, lambda v: 3 *
                 v[Veggie.CABBAGE] - 2*v[Veggie.TOMATO], "3 / CABBAGE \n -2 / TOMATO"),
            Card(105, Veggie.CARROT, lambda v: 1 *
                 v[Veggie.CABBAGE] + 1*v[Veggie.LETTUCE], "1 / CABBAGE \n 1 / LETTUCE"),
            Card(106, Veggie.CARROT, lambda v: 1 *
                 v[Veggie.CABBAGE] + 1*v[Veggie.PEPPER], "1 / CABBAGE \n 1 / PEPPER"),
            Card(107, Veggie.CARROT, lambda v: 2*v[Veggie.CABBAGE] + 1*v[Veggie.LETTUCE] -
                 2*v[Veggie.CARROT], "2 / CABBAGE \n 1 / LETTUCE \n -2 / CARROT"),
            Card(108, Veggie.CARROT, lambda v: 3*v[Veggie.CABBAGE] - 1*v[Veggie.LETTUCE] -
                 1*v[Veggie.CARROT], "3 / CABBAGE \n -1 / LETTUCE \n -1 / CARROT"),
            Card(109, Veggie.CARROT, lambda v: 4*v[Veggie.CABBAGE] - 2*v[Veggie.PEPPER] -
                 2*v[Veggie.ONION], "4 / CABBAGE \n -2 / PEPPER \n -2 / ONION"),
            Card(110, Veggie.CARROT, lambda v: 2*v[Veggie.CABBAGE] + 2*v[Veggie.TOMATO] -
                 4*v[Veggie.LETTUCE], "2 / CABBAGE \n 2 / TOMATO \n -4 / LETTUCE"),
            Card(111, Veggie.CARROT, lambda v: 5 *
                 (v[Veggie.CABBAGE] // 2), "CABBAGE + CABBAGE = 5"),
            Card(112, Veggie.CARROT, lambda v: 8 *
                 (v[Veggie.CABBAGE] // 3), "CABBAGE + CABBAGE + CABBAGE = 8"),
            Card(113, Veggie.CARROT, lambda v: 5 *
                 (min(v[Veggie.TOMATO], v[Veggie.LETTUCE])), "TOMATO + LETTUCE = 5"),
            Card(114, Veggie.CARROT, lambda v: 5 *
                 (min(v[Veggie.ONION], v[Veggie.PEPPER])), "ONION + PEPPER = 5"),
            Card(115, Veggie.CARROT, lambda v: 8 *
                 (min(v[Veggie.PEPPER], v[Veggie.CABBAGE], v[Veggie.TOMATO])), "PEPPER + CABBAGE + TOMATO = 8"),
            Card(116, Veggie.CARROT, lambda v: 8 *
                 (min(v[Veggie.CARROT], v[Veggie.CABBAGE], v[Veggie.ONION])), "CARROT + CABBAGE + ONION = 8"),
            # TODO: requires hands from all players
            Card(117, Veggie.CARROT, lambda v: 0, "meeste CABBAGE = 10"),
            Card(118, Veggie.CARROT, lambda v: 0, "minste CABBAGE = 7"),
        ])

    def setup(self, number_of_players):
        # 2-6 players
        # cards: number_of_players * 3 of each veg
        self.number_of_players = number_of_players
        self.max_number_of_veggies = 3 * self.number_of_players
        # (number_of_players * 18 total)
        # 1. Start with full deck
        # 2. Shuffle
        # 3. Iterate over cards, counting veggie_type
        # 4. After reaching max_number_of_veggies,
        # 5. remove remaining cards of that vegetable type

    def draw_card(self):
        pass
