from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

import pandas as pd
import random

IMAGE_SIZE = 170

class Ui_MainWindow(object):

    def __init__(self):

        self.data = pd.read_csv("out.csv")
        print(self.data.head())

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.verticalLayout = QVBoxLayout()

        self.label_image_top = QtWidgets.QLabel(self.centralwidget)
        self.label_image_bottom = QtWidgets.QLabel(self.centralwidget)
        self.label_image_shoes = QtWidgets.QLabel(self.centralwidget)

        self.nope_button = QtWidgets.QPushButton(self.centralwidget)
        self.yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button = QtWidgets.QPushButton(self.centralwidget)

        self.index = random.randint(0, 99)
        self.getImages()
        self.image_top_index = self.images_indexes["top"]
        self.image_bottom_index = self.images_indexes["bottom"]
        self.image_shoes_index = self.images_indexes["shoes"]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 736)
        MainWindow.setWindowTitle("Training")

        # setup central widget
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.resize(414, 736)

        # setup layouts
        self.horizontalLayout.setObjectName("horizontalLayoutWidget")
        self.verticalLayout.setObjectName("verticalLayoutWidget")

        # setup images*
        self.label_image_top.setAlignment(Qt.AlignCenter)
        self.label_image_bottom.setAlignment(Qt.AlignCenter)
        self.label_image_shoes.setAlignment(Qt.AlignCenter)

        # setup buttons
        self.nope_button.clicked.connect(lambda : self.feedback(False))
        self.nope_button.setText("Nope")
        self.yes_button.clicked.connect(lambda: self.feedback(True))
        self.yes_button.setText("Yeet")
        self.close_button.clicked.connect(self.save)
        self.close_button.setText("Done")

        # add to layouts
        self.verticalLayout.addWidget(self.label_image_top)
        self.verticalLayout.addWidget(self.label_image_bottom)
        self.verticalLayout.addWidget(self.label_image_shoes)
        self.verticalLayout.addWidget(self.close_button)
        self.horizontalLayout.addWidget(self.nope_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.yes_button)


    def feedback(self, result):
        if result:
            self.data["result"].iloc[self.index] = 1
            print(f"J'aime ! "
                  f"\n top_index : {self.image_top_index},"
                  f"\n bottom_index : {self.image_bottom_index},"
                  f"\n top_index : {self.image_shoes_index} ")
        else:
            self.data["result"].iloc[self.index] = 0
            print(f"Je n'aime pas !"
                  f"\n top_index : {self.image_top_index},"
                  f"\n bottom_index : {self.image_bottom_index},"
                  f"\n top_index : {self.image_shoes_index} ")


        self.getImages()


    def loadImages(self, top, bottom, shoes):

        top_path = f"images/t_{top}.jpg"
        bottom_path = f"images/short_{bottom}.jpg"
        shoes_path = f"images/shoes_{shoes}.jpg"


        self.pixmap1 = QtGui.QPixmap(top_path)
        self.pixmap2 = QtGui.QPixmap(bottom_path)
        self.pixmap3 = QtGui.QPixmap(shoes_path)
        self.label_image_top.setPixmap(
            self.pixmap1.scaled(IMAGE_SIZE, IMAGE_SIZE, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.label_image_bottom.setPixmap(
            self.pixmap2.scaled(IMAGE_SIZE, IMAGE_SIZE, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.label_image_shoes.setPixmap(
            self.pixmap3.scaled(IMAGE_SIZE, IMAGE_SIZE, Qt.KeepAspectRatio, Qt.FastTransformation))

    def getImages(self):
        self.index = random.randint(0, 99)
        self.images_indexes = self.data.iloc[self.index]
        self.image_top_index = self.images_indexes["top"]
        self.image_bottom_index = self.images_indexes["bottom"]
        self.image_shoes_index = self.images_indexes["shoes"]
        self.loadImages(self.image_top_index, self.image_bottom_index, self.image_shoes_index)

    def save(self):
        print('updates done to csv at line : ', self.index)
        self.data.to_csv('out.csv')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
