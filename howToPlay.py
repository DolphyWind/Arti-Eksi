from PyQt5 import QtWidgets, QtGui, QtCore
from global_values import *

class HowToPlay(QtWidgets.QWidget):

    def __init__(self, parentWindow: QtWidgets.QWidget):
        super(HowToPlay, self).__init__()

        # Create the window
        self.setGeometry(100, 100, windowSize[0], windowSize[1])
        self.setWindowTitle("Nasıl Oynanır?")
        self.center()

        self.parentWindow = parentWindow
        self.parentWindow.close()

        # Create UI
        self.UI()

        # Show Window
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def UI(self):
        # Layouts
        self.goBackButtonHBox = QtWidgets.QHBoxLayout()
        self.mainVBox = QtWidgets.QVBoxLayout()
        self.mainHBox = QtWidgets.QHBoxLayout()

        # Go Back Button
        self.goBackButton = QtWidgets.QPushButton("Geri Dön")
        self.goBackButton.setFont(normal_font)
        self.goBackButton.setFixedSize(mbs[0], mbs[1])
        self.goBackButton.clicked.connect(self.close)
        self.goBackButtonHBox.addStretch()
        self.goBackButtonHBox.addWidget(self.goBackButton)
        self.goBackButtonHBox.addStretch()

        # Information
        self.informationText = QtWidgets.QLabel(howToPlayStr)
        self.informationText.setAlignment(QtCore.Qt.AlignJustify)
        self.informationText.setFont(information_font)

        # Title
        self.titleText = QtWidgets.QLabel("Nasıl Oynanır?")
        self.titleText.setAlignment(QtCore.Qt.AlignCenter)
        self.titleText.setFont(title_font)

        # Layouts
        self.mainVBox.addStretch()
        self.mainVBox.addWidget(self.titleText)
        self.mainVBox.addStretch()
        self.mainVBox.addWidget(self.informationText)
        self.mainVBox.addStretch()
        self.mainVBox.addLayout(self.goBackButtonHBox)
        self.mainVBox.addStretch()

        self.mainHBox.addStretch()
        self.mainHBox.addLayout(self.mainVBox)
        self.mainHBox.addStretch()

        self.setLayout(self.mainHBox)

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.parentWindow.show()
        a0.accept()