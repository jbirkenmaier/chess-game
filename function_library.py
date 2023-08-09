class piece():
    def __init__(self, name, position):
        self.name=name
        self.position=position
        self.capability = self.powers(self.name)

    def powers(self, name):
        pass
