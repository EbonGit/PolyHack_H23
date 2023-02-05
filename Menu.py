from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout

import Training


class Ui_MenuWindow(object):

    def __init__(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.train_button = QtWidgets.QPushButton()
        self.get_fit_button = QtWidgets.QPushButton()
        self.exit_button = QtWidgets.QPushButton()
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 736)
        MainWindow.setWindowTitle("Training")

        # setup central widget
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.resize(414, 736)

        self.verticalLayout.addItem(self.verticalSpacer)
        self.verticalLayout.addWidget(self.get_fit_button)
        self.verticalLayout.addWidget(self.train_button)
        self.verticalLayout.addWidget(self.exit_button)

        self.get_fit_button.setText("Morning")
        self.train_button.setText("Train")
        self.exit_button.setText("Exit")

        self.train_button.clicked.connect(self.train)

    def train(self):
        print("eeee")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    menu = Ui_MenuWindow()
    menu.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
