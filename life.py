class Life:
    def __init__(self):
        self.remainingLives = 7

    def getRemainingLives(self):
        return self.remainingLives

    def decreaseLife(self):
        self.remainingLives -= 1