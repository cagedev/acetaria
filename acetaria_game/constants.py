from enum import Enum, auto

class Veggie(Enum):
    CARROT = auto()
    PEPPER = auto()
    TOMATO = auto()
    LETTUCE = auto()
    ONION = auto()
    CABBAGE = auto()


class CardSide(Enum):
    POINT = 0
    VEGGIE = 1


class TurnState(Enum):
    DRAW = auto()  # Current player may either draw 1 rule or 2 veggies
    FLIP = auto()  # Current player may flip one of their rules to a veggie
    REPLENISH = auto()  # Cards are replenished from the deck


class GameState(Enum):
    WAITING_FOR_PLAYERS = auto()
    SETUP = auto()
    PLAYING = auto()
    FINISHED = auto()