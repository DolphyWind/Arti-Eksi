from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import PickingGame
import GuessingGame
import game
from global_values import *
import howToPlay

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Create the window
        self.windowSize = (300, 400)
        self.setGeometry(100, 100, self.windowSize[0], self.windowSize[1])
        self.setWindowTitle("Artı Eksi")
        self.center()

        # Create UI
        self.UI()

        # Show Window
        self.show()

    def UI(self):
        # Layouts
        self.mainHBox = QtWidgets.QHBoxLayout()
        self.mainVBox = QtWidgets.QVBoxLayout()
        self.buttonVBox = QtWidgets.QVBoxLayout()

        # Title text
        self.title = QtWidgets.QLabel("Artı Eksi")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setFont(title_font)

        # Guess Button
        self.guessButton = QtWidgets.QPushButton("Tahmin Et")
        self.guessButton.setFont(normal_font)
        self.guessButton.setFixedSize(mbs[0], mbs[1])
        self.guessButton.clicked.connect(self.playGuess)
        self.guessButtonLayout = QtWidgets.QHBoxLayout()
        self.guessButtonLayout.addStretch()
        self.guessButtonLayout.addWidget(self.guessButton)
        self.guessButtonLayout.addStretch()

        # Pick Button
        self.pickButton = QtWidgets.QPushButton("Sayı Tut")
        self.pickButton.setFont(normal_font)
        self.pickButton.setFixedSize(mbs[0], mbs[1])
        self.pickButton.clicked.connect(self.playPick)
        self.pickButtonLayout = QtWidgets.QHBoxLayout()
        self.pickButtonLayout.addStretch()
        self.pickButtonLayout.addWidget(self.pickButton)
        self.pickButtonLayout.addStretch()

        # How to play Button
        self.howToButton = QtWidgets.QPushButton("Nasıl oynanır?")
        self.howToButton.setFont(normal_font)
        self.howToButton.setFixedSize(mbs[0], mbs[1])
        self.howToButton.clicked.connect(self.howToPlay)
        self.howToButtonLayout = QtWidgets.QHBoxLayout()
        self.howToButtonLayout.addStretch()
        self.howToButtonLayout.addWidget(self.howToButton)
        self.howToButtonLayout.addStretch()

        # Design
        self.buttonVBox.addStretch()
        self.buttonVBox.addLayout(self.guessButtonLayout)
        self.buttonVBox.addLayout(self.pickButtonLayout)
        self.buttonVBox.addLayout(self.howToButtonLayout)
        self.buttonVBox.addStretch()

        self.mainVBox.addStretch()
        self.mainVBox.addWidget(self.title)
        self.mainVBox.addStretch()
        self.mainVBox.addLayout(self.buttonVBox)
        self.mainVBox.addStretch()

        self.mainHBox.addStretch()
        self.mainHBox.addLayout(self.mainVBox)
        self.mainHBox.addStretch()

        self.setLayout(self.mainHBox)

    def playGuess(self):
        game.findAllPossibleAnswers()
        self.guessWindow = GuessingGame.GuessingGame(self)

    def playPick(self):
        game.findAllPossibleAnswers()
        self.pgWindow = PickingGame.PickingGame(self)

    def howToPlay(self):
        self.htpWindow = howToPlay.HowToPlay(self)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()