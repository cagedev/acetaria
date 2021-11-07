import uuid
from .deck import Deck
from .market import Market
from .constants import GameState, TurnState, Veggie


class Game():
    def __init__(self):
        self.id = uuid.uuid4()
        self.max_number_of_players = 6
        self.players = []
        self.round = 0
        self.deck = Deck()
        self.game_state = GameState.WAITING_FOR_PLAYERS
        self.turn_state = TurnState.DRAW

        self.host_connected = False
        self.quitting = False

    def add_player(self, player):
        if len(self.players) < self.max_number_of_players:
            self.players.append(player)
        else:
            raise Exception('Maximum number of players already reached.')

    def test(self):
        # TODO: Move testing to seperate tests suite
        # deck = Deck()
        self.deck.setup(3)
        self.deck.print_cards()

        self.market = Market(self.deck)
        self.market.fill_stalls()
        self.market.show()
        self.deck.print_cards()

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
