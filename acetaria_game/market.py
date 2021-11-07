class Stall():
    def __init__(self, deck):
        self.positions = [None]*3
        self.deck = deck

    def fill(self):
        if self.positions[0] == None:
            self.positions[0] = self.deck.draw_card()
            self.fill()
        elif self.positions[1] == None:
            self.positions[0].flip()
            self.positions[1] = self.positions[0]
            self.positions[0] = None
            self.fill()
        elif self.positions[2] == None:
            self.positions[0].flip()
            self.positions[2] = self.positions[0]
            self.positions[0] = None
            self.fill()
        else:
            return

    def print_stall(self):
        for veg in self.positions:
            print(veg.id, veg.side.value, end=", ")
        print()


class Market():
    def __init__(self, deck):
        self.deck = deck
        self.stalls = [Stall(deck), Stall(deck), Stall(deck)]

    def fill_stalls(self):
        for stall in self.stalls:
            stall.fill()

    def show(self):
        for stall in self.stalls:
            stall.print_stall()
