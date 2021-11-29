from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel

from life import Life
from guess import Guess
from number import Number



class UpDownGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set number range
        self.numberRange = 50

        # Layout
        mainLayout = QGridLayout()

        # Game name label
        self.gameName = QLabel()
        self.gameName.setText("UP-DOWN Game")
        self.gameName.setFont(QtGui.QFont("궁서", 20))
        mainLayout.addWidget(self.gameName, 0, 0, 1, 2)

        # Difficulty Layout
        difficultyLayout = QHBoxLayout()

        # Difficulty buttons
        self.difficulty_Easy = QToolButton()
        self.difficulty_Easy.setText("Easy")
        self.difficulty_Easy.clicked.connect(self.difficultyClicked)
        difficultyLayout.addWidget(self.difficulty_Easy)
        self.difficulty_Normal = QToolButton()
        self.difficulty_Normal.setText("Normal")
        self.difficulty_Normal.clicked.connect(self.difficultyClicked)
        difficultyLayout.addWidget(self.difficulty_Normal)
        self.difficulty_Hard = QToolButton()
        self.difficulty_Hard.setText("Hard")
        self.difficulty_Hard.clicked.connect(self.difficultyClicked)
        difficultyLayout.addWidget(self.difficulty_Hard)
        mainLayout.addLayout(difficultyLayout, 1, 0)

        # Display current life
        self.currentLife = QLineEdit()
        self.currentLife.setReadOnly(True)
        self.currentLife.setAlignment(Qt.AlignLeft)
        mainLayout.addWidget(self.currentLife, 2, 0)

        # Display message
        self.messageBox = QLineEdit()
        self.messageBox.setReadOnly(True)
        self.messageBox.setAlignment(Qt.AlignLeft)
        self.messageBox.setText("Select Difficulty(default: Easy)")
        mainLayout.addWidget(self.messageBox, 3, 0)

        # Input number
        self.numberInput = QLineEdit()
        mainLayout.addWidget(self.numberInput, 4, 0)

        # guess button
        self.guessButton = QToolButton()
        self.guessButton.setText("Guess")
        self.guessButton.clicked.connect(self.guessClicked)
        mainLayout.addWidget(self.guessButton, 4, 1)

        # newGame button
        self.newGameButton = QToolButton()
        self.newGameButton.setText("NewGame")
        self.newGameButton.clicked.connect(self.newGame)
        mainLayout.addWidget(self.newGameButton, 5, 1)

        # Display recent record
        self.recentRecord = QTextEdit()
        self.recentRecord.setText("")
        mainLayout.addWidget(self.recentRecord, 6, 0)

        self.setLayout(mainLayout)

        self.setWindowTitle("UP-DOWN game")

        self.newGame()

    def newGame(self):
        self.numberRange = 50
        self.life = Life()
        self.number = Number()
        self.guess = Guess(self.number.getRandomNumber(self.numberRange))
        self.gameOver = False

        self.currentLife.setText("Remaining Lives: " + str(self.life.getRemainingLives()))
        self.messageBox.setText("Select Difficulty(default: Easy)")
        self.recentRecord.clear()
        self.numberInput.clear()

    def guessClicked(self):
        try:
            guessedNumber = int(self.numberInput.text())
        except:
            self.numberInput.clear()
            self.messageBox.setText("Enter Only Number")
            return

        # Clear numberInput
        self.numberInput.clear()

        # GameOver set text
        if self.gameOver == True:
            self.messageBox.setText("GameOver")
            return

        # if guessedNumber out of range
        if guessedNumber > self.numberRange or guessedNumber < 1:
            self.messageBox.setText("Enter Number (1~{})" .format(self.numberRange))
            return

        if self.guess.guess(guessedNumber):
            self.messageBox.setText("Correct")
            self.gameOver = True
            return

        # Decrease 1 life
        self.life.decreaseLife()
        self.messageBox.setText("Decrease 1 Life")
        self.currentLife.setText("Remaining Lives: " + str(self.life.getRemainingLives()))

        if self.life.getRemainingLives() == 0:
            self.messageBox.setText("Fail + secret number: " + str(self.guess.getSecretNumber()))
            self.gameOver = True
            return

        self.recentRecord.append("Recent Input Number: " + str(guessedNumber) + self.guess.getRecentRecord())



    def difficultyClicked(self):

        button = self.sender()
        key = button.text()

        if key == 'Easy':
            self.numberRange = 50
        elif key == 'Normal':
            self.numberRange = 100
        else:
            self.numberRange = 200

        self.guess = Guess(self.number.getRandomNumber(self.numberRange))
        self.messageBox.setText("Enter Number (1~{})" .format(self.numberRange))


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = UpDownGame()
    game.show()
    sys.exit(app.exec_())
