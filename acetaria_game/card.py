from .constants import CardSide, Veggie


class Card():

    def __init__(self, id, veggie_type, scoring_function, description, side=CardSide.POINT):
        self.id = id
        self.veggie_type = veggie_type
        self.scoring_function = scoring_function
        self.description = description
        self.side = side

    def flip(self):
        if self.side == CardSide.POINT:
            self.side = CardSide.VEGGIE

    def get_score(self, veggies):
        # TODO: Check size of veggies array
        return self.scoring_function(veggies)

    def show(self):
        print(self.veggie_type.name, self.id)
