class Guess:
    def __init__(self, number):
        self.secretNumber = number
        self.recentRecord = ""

    def guess(self, number):
        if number == self.secretNumber:
            return True
        else:
            if number > self.secretNumber:
                self.recentRecord = "(Down)"
            else:
                self.recentRecord = "(Up)"
            return False

    def getRecentRecord(self):
        return self.recentRecord

    def getSecretNumber(self):
        return self.secretNumber
