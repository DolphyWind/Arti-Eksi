from PyQt5 import QtWidgets, QtGui, QtCore
import game
from global_values import *


class GuessingGame(QtWidgets.QWidget):

    def __init__(self, parentWindow: QtWidgets.QWidget):
        super(GuessingGame, self).__init__()

        # Create the window
        self.windowSize = (300, 400)
        self.setGeometry(100, 100, self.windowSize[0], self.windowSize[1])
        self.setWindowTitle("Sayı Tut")
        self.center()

        self.picked = game.ai_pickRandom()
        self.playerGuesses = 0
        self.guessList = []
        self.hintList = []

        # Create UI
        self.UI()

        # Close Parent Window
        self.parentWindow = parentWindow
        self.parentWindow.close()

        # Show window
        self.show()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.parentWindow.show()
        a0.accept()

    def UI(self):
        # Layouts
        self.mainVBox = QtWidgets.QVBoxLayout()
        self.mainHBox = QtWidgets.QHBoxLayout()
        self.tbLayout = QtWidgets.QHBoxLayout()
        self.infoTextLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout = QtWidgets.QHBoxLayout()

        # Info Label
        self.infoLabel = QtWidgets.QLabel("Bir sayı tuttum.\nBakalım tahmin edebilecek misin...")
        self.infoLabel.setFont(normal_font)
        self.infoLabel.wordWrap = True
        self.infoLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.infoTextLayout.addStretch()
        self.infoTextLayout.addWidget(self.infoLabel)
        self.infoTextLayout.addStretch()


        # Guess TextBox
        self.guessTextBox = QtWidgets.QLineEdit()
        self.guessTextBox.setMaxLength(game.digits)
        self.guessTextBox.textChanged.connect(self.checkText)
        self.guessTextBox.setPlaceholderText("Tahmin...")
        self.setFont(information_font)
        self.guessTextBox.setFixedWidth(mbs[0])
        self.guessTextBox.setMaximumWidth(200)

        self.tbLayout.addStretch()
        self.tbLayout.addWidget(self.guessTextBox)
        self.tbLayout.addStretch()

        # Send button
        self.sendButton = QtWidgets.QPushButton("Gönder")
        self.sendButton.setFixedSize(mbs[0], mbs[1])
        self.sendButton.clicked.connect(self.step)
        self.buttonLayout.addStretch()
        self.buttonLayout.addWidget(self.sendButton)
        self.buttonLayout.addStretch()

        # Design

        self.mainVBox.addLayout(self.infoTextLayout)
        self.mainVBox.addStretch()
        self.mainVBox.addLayout(self.tbLayout)
        self.mainVBox.addLayout(self.buttonLayout)
        self.mainVBox.addStretch()

        self.mainHBox.addStretch()
        self.mainHBox.addLayout(self.mainVBox)
        self.mainHBox.addStretch()

        self.setLayout(self.mainHBox)

    def checkText(self):
        txt = self.guessTextBox.text()
        newtxt = str()
        for i in txt:
            n = ord(i) - ord('0')
            if n >= 0 and n <= 9:
                newtxt += i
        self.guessTextBox.setText(newtxt)

    def step(self):
        user_guess = self.guessTextBox.text()
        if len(user_guess) != game.digits:
            QtWidgets.QMessageBox.about(self, "Hata", "Girdiğiniz tahmin çok kısa")
            return

        if len(set(user_guess)) != len(user_guess):
            QtWidgets.QMessageBox.about(self, "Hata", "Girdiğiniz tahmin tekrarlı sayılar içeriyor")
            return

        self.playerGuesses += 1
        user_guess = int(user_guess)
        plus = game.ai_findPlus(self.picked, user_guess)
        minus = game.ai_findMinus(self.picked, user_guess)

        self.guessList.append(str(user_guess))
        self.hintList.append((str(plus), str(minus)))

        final_str = "Tahminlerin\t\tİpuçlarım\n"
        for i in range(len(self.guessList)):
            final_str += self.guessList[i] + "\t\t\t+" + self.hintList[i][0] + " -" + self.hintList[i][1] + "\n"
        if plus == game.digits:
            QtWidgets.QMessageBox.about(self, "Bravo", f"Tuttuğum sayıyı {self.playerGuesses} tahminde buldun.")
            self.close()

        self.infoLabel.setAlignment(QtCore.Qt.AlignTop)
        self.infoLabel.setText(final_str)
        self.guessTextBox.clear()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())