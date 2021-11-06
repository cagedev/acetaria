from .deck import Deck
from .constants import GameState, TurnState, Veggie


class Game():
    def __init__(self):
        self.host_connected = False
        self.cards = Deck()
        self.players = []
        self.round = 0
        self.quitting = False
        self.game_state = GameState.WAITING_FOR_PLAYERS
        self.turn_state = TurnState.DRAW

    def test(self):
        hand = {
            Veggie.CARROT: 0,
            Veggie.PEPPER: 6,
            Veggie.TOMATO: 2,
            Veggie.LETTUCE: 3,
            Veggie.ONION: 4,
            Veggie.CABBAGE: 0
        }
        d = Deck()
        d.load()

        print(hand)
        for c in d.cards:
            print(c.description, "->", c.get_score(hand))
