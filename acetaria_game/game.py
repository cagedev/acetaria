from .deck import Deck
from .market import Market
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
        deck = Deck()
        deck.setup(3)
        deck.print_cards()

        market = Market(deck)
        market.fill_stalls()
        market.show()
        deck.print_cards()

        # for i in range(18):
        #     print("-----")
        #     print("->", deck.draw_card().id)
        #     deck.print_cards()

        # hand = {
        #     Veggie.CARROT: 0,
        #     Veggie.PEPPER: 6,
        #     Veggie.TOMATO: 2,
        #     Veggie.LETTUCE: 3,
        #     Veggie.ONION: 4,
        #     Veggie.CABBAGE: 0
        # }
        # print(hand)
        # for card in deck.cards:
        #     print(card.description, "->", card.get_score(hand))
