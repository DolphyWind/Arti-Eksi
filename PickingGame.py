from PyQt5 import QtWidgets, QtGui, QtCore
import game
from global_values import *

class PickingGame(QtWidgets.QWidget):

    def __init__(self, parentWindow: QtWidgets.QWidget):
        super(PickingGame, self).__init__()

        # Create the window
        self.setGeometry(100, 100, windowSize[0], windowSize[1])
        self.setWindowTitle("Sayı Tut")
        self.center()

        # Close Parent Window
        self.parentWindow = parentWindow
        self.parentWindow.close()

        # Pick a random guess
        self.ai_guess = game.ai_pickRandom()

        # Create UI
        self.UI()

        # Show Window
        self.show()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.parentWindow.show()
        a0.accept()

    def UI(self):
        # Layouts
        self.plusMinusHBox = QtWidgets.QHBoxLayout()
        self.buttonHBox = QtWidgets.QHBoxLayout()
        self.mainVBox = QtWidgets.QVBoxLayout()
        self.mainHBox = QtWidgets.QHBoxLayout()

        # Guess Text
        self.guessText = QtWidgets.QLabel("Tahminim: " + str(self.ai_guess))
        self.guessText.setAlignment(QtCore.Qt.AlignCenter)
        self.guessText.setFont(guess_font)

        # Plus and minus text
        self.plusText = QtWidgets.QLabel("+")
        self.plusText.setAlignment(QtCore.Qt.AlignCenter)
        self.plusText.setFont(guess_font)

        self.minusText = QtWidgets.QLabel("-")
        self.minusText.setAlignment(QtCore.Qt.AlignCenter)
        self.minusText.setFont(guess_font)

        # Plus Spin Box
        self.plusSpinBox = QtWidgets.QSpinBox()
        self.plusSpinBox.setRange(0, game.digits)
        self.plusSpinBox.setFont(guess_font)

        # Minus Spin Box
        self.minusSpinBox = QtWidgets.QSpinBox()
        self.minusSpinBox.setRange(0, game.digits)
        self.minusSpinBox.setFont(guess_font)

        # Send Button
        self.sendButton = QtWidgets.QPushButton("Gönder")
        self.sendButton.setFont(guess_font)
        self.sendButton.setFixedSize(mbs[0], mbs[1])
        self.sendButton.clicked.connect(self.step)

        # Layouts
        self.plusMinusHBox.addWidget(self.plusText)
        self.plusMinusHBox.addWidget(self.plusSpinBox)
        self.plusMinusHBox.addStretch()
        self.plusMinusHBox.addWidget(self.minusText)
        self.plusMinusHBox.addWidget(self.minusSpinBox)

        self.buttonHBox.addStretch()
        self.buttonHBox.addWidget(self.sendButton)
        self.buttonHBox.addStretch()

        self.mainVBox.addStretch()
        self.mainVBox.addWidget(self.guessText)
        self.mainVBox.addStretch()
        self.mainVBox.addLayout(self.plusMinusHBox)
        self.mainVBox.addStretch()
        self.mainVBox.addLayout(self.buttonHBox)
        self.mainVBox.addStretch()

        self.mainHBox.addStretch()
        self.mainHBox.addLayout(self.mainVBox)
        self.mainHBox.addStretch()

        self.setLayout(self.mainHBox)

    def step(self):
        minus = self.minusSpinBox.value()
        plus = self.plusSpinBox.value()
        self.minusSpinBox.setValue(0)
        self.plusSpinBox.setValue(0)
        if plus == game.digits:
            QtWidgets.QMessageBox.about(self, "Başardım", "Nasıl buldum ama :D")
            self.close()
        game.ai_solve(self.ai_guess, minus, plus)
        try:
            self.ai_guess = game.ai_pickRandom()
            self.guessText.setText("Tahminim: " + str(self.ai_guess))
        except IndexError:
            QtWidgets.QMessageBox.about(self, "Hata", "Bilgileri girerken bir hata yaptınız.")
            self.close()


    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())