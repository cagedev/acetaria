class Player():
    def __init__(self, name=None):
        self.connected = False
        self.hand = []
        self.name = name
        self.id = uuid.uuid4()