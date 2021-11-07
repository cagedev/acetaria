from .card import Card
from .constants import Veggie

carrot_cards = [
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
]

pepper_cards = [
    Card(201, Veggie.PEPPER, lambda v: 0 if v[Veggie.CABBAGE] == 0 else (
        7 if v[Veggie.CABBAGE] % 2 == 0 else 3), "CABBAGE \n even aantal = 7 \n oneven aantal = 3"),
    Card(202, Veggie.PEPPER, lambda v: 2 *
         v[Veggie.CABBAGE], "2 / CABBAGE"),
    Card(203, Veggie.PEPPER, lambda v: 3 *
         v[Veggie.CABBAGE] - 2*v[Veggie.CARROT], "3 / CABBAGE \n -2 / CARROT"),
    Card(204, Veggie.PEPPER, lambda v: 1 *
         v[Veggie.LETTUCE] + 1*v[Veggie.TOMATO], "1 / LETTUCE \n 1 / TOMATO"),
    Card(205, Veggie.PEPPER, lambda v: 1 *
         v[Veggie.LETTUCE] + 1*v[Veggie.ONION], "1 / LETTUCE \n 1 / ONION"),
    Card(206, Veggie.PEPPER, lambda v: 2*v[Veggie.LETTUCE] + 1*v[Veggie.ONION] -
         2*v[Veggie.PEPPER], "2 / LETTUCE \n 1 / ONION \n -2 / PEPPER"),
    Card(207, Veggie.PEPPER, lambda v: 3*v[Veggie.LETTUCE] - 1*v[Veggie.ONION] -
         1*v[Veggie.PEPPER], "3 / LETTUCE \n -1 / ONION \n -1 / PEPPER"),
    Card(208, Veggie.PEPPER, lambda v: 4*v[Veggie.LETTUCE] - 2*v[Veggie.TOMATO] -
         2*v[Veggie.CABBAGE], "4 / LETTUCE \n -2 / TOMATO \n -2 / CABBAGE"),
    Card(209, Veggie.PEPPER, lambda v: 2*v[Veggie.LETTUCE] + 2*v[Veggie.CARROT] -
         4*v[Veggie.ONION], "2 / LETTUCE \n 2 / CARROT \n -4 / ONION"),
    Card(210, Veggie.PEPPER, lambda v: 5 *
         (v[Veggie.LETTUCE] // 2), "LETTUCE + LETTUCE = 5"),
    Card(211, Veggie.PEPPER, lambda v: 8 *
         (v[Veggie.LETTUCE] // 3), "LETTUCE + LETTUCE + LETTUCE = 8"),
    Card(212, Veggie.PEPPER, lambda v: 5 *
         (min(v[Veggie.CABBAGE], v[Veggie.TOMATO])), "CABBAGE + TOMATO = 5"),
    Card(213, Veggie.PEPPER, lambda v: 5 *
         (min(v[Veggie.CARROT], v[Veggie.ONION])), "CARROT + ONION = 5"),
    Card(214, Veggie.PEPPER, lambda v: 8 *
         (min(v[Veggie.TOMATO], v[Veggie.LETTUCE], v[Veggie.CARROT])), "TOMATO + LETTUCE + CARROT = 8"),
    Card(116, Veggie.PEPPER, lambda v: 8 *
         (min(v[Veggie.PEPPER], v[Veggie.LETTUCE], v[Veggie.CABBAGE])), "PEPPER + LETTUCE + CABBAGE = 8"),
    # TODO: requires hands from all players
    Card(216, Veggie.PEPPER, lambda v: 0, "meeste aantal groentekaarten = 10"),
    Card(217, Veggie.PEPPER, lambda v: 0, "meeste CABBAGE = 10"),
    Card(218, Veggie.PEPPER, lambda v: 0, "minste CABBAGE = 7"),
]

