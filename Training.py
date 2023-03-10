from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap, QMovie, QIcon
from PyQt5 import QtCore

import pandas as pd
import generate_data
import random
import model_keras

IMAGE_SIZE = 170
STARTING = 63

class TrainingWindow(QWidget):

    def __init__(self):
        #generate_data.init()
        super().__init__()
        self.data = pd.read_csv("out.csv")

        #self.centralwidget = QWidget(w)
        self.horizontalLayout = QHBoxLayout(self)
        self.verticalLayout = QVBoxLayout()

        self.label_image_top = QLabel(self)
        self.label_image_bottom = QLabel(self)
        self.label_image_shoes = QLabel(self)

        self.nope_button = QPushButton(self)
        self.yes_button = QPushButton(self)
        self.done_button = QPushButton(self)

        self.index = STARTING
        self.getImages()
        self.image_top_index = self.images_indexes["top"]
        self.image_bottom_index = self.images_indexes["bottom"]
        self.image_shoes_index = self.images_indexes["shoes"]

        self.loadingWindow = loadingWindow()
        print('on est ouvert')
    def call_model(self):
        self.loadingWindow.show()
        QtCore.QCoreApplication.processEvents()
        self.k()

    def k(self):
        model_keras.main()

    def closeWindow(self):
        self.loadingWindow.closewindow()
        super().close()

    def setupUi(self):
        # MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(414, 736)
        # MainWindow.setWindowTitle("Training")

        self.setWindowIcon(QIcon('image/logo.png'))
        self.setWindowTitle("Dress me")

        # setup central widget
        self.setObjectName("centralwidget")
        self.resize(414, 736)

        # setup layouts
        self.horizontalLayout.setObjectName("horizontalLayoutWidget")
        self.verticalLayout.setObjectName("verticalLayoutWidget")

        # setup images*
        self.label_image_top.setAlignment(Qt.AlignCenter)
        self.label_image_bottom.setAlignment(Qt.AlignCenter)
        self.label_image_shoes.setAlignment(Qt.AlignCenter)

        # setup buttons
        self.nope_button.clicked.connect(lambda: self.feedback(False))
        self.nope_button.setText("Nope")
        self.yes_button.clicked.connect(lambda: self.feedback(True))
        self.yes_button.setText("Yeet")
        #self.close_button.clicked.connect(self.save)

        self.done_button.clicked.connect(self.call_model)

        self.done_button.clicked.connect(self.closeWindow)
        self.done_button.setText("Done")

        # add to layouts
        self.verticalLayout.addWidget(self.label_image_top)
        self.verticalLayout.addWidget(self.label_image_bottom)
        self.verticalLayout.addWidget(self.label_image_shoes)
        self.verticalLayout.addWidget(self.done_button)
        self.horizontalLayout.addWidget(self.nope_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.yes_button)
    def feedback(self, result):
        if result:
            self.data["result"].iloc[self.index] = 1
            # print(f"J'aime ! "
            #       f"\n top_index : {self.image_top_index},"
            #       f"\n bottom_index : {self.image_bottom_index},"
            #       f"\n top_index : {self.image_shoes_index} ")
        else:
            self.data["result"].iloc[self.index] = 0
            # print(f"Je n'aime pas !"
            #       f"\n top_index : {self.image_top_index},"
            #       f"\n bottom_index : {self.image_bottom_index},"
            #       f"\n top_index : {self.image_shoes_index} ")
        self.save()
        self.getImages()

    def loadImages(self, top, bottom, shoes):

        top_path = f"image/top_{top}.png"
        bottom_path = f"image/bottom_{bottom}.png"
        shoes_path = f"image/shoes_{shoes}.png"

        self.pixmap1 = QPixmap(top_path)
        self.pixmap2 = QPixmap(bottom_path)
        self.pixmap3 = QPixmap(shoes_path)
        self.label_image_top.setPixmap(
            self.pixmap1.scaled(IMAGE_SIZE, IMAGE_SIZE, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.label_image_bottom.setPixmap(
            self.pixmap2.scaled(IMAGE_SIZE, IMAGE_SIZE, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.label_image_shoes.setPixmap(
            self.pixmap3.scaled(IMAGE_SIZE, IMAGE_SIZE, Qt.KeepAspectRatio, Qt.FastTransformation))

    def getImages(self):
        if(self.index < 63):
            self.index += 1
            print(self.index)
        else:
            new_row = pd.DataFrame({'top': [random.randint(1, 4)], 'bottom': [random.randint(1,4)], 'shoes': [random.randint(1,4)], 'result': [-1]})
            self.data = pd.concat([self.data, new_row])
            print(self.data.tail())
            self.index += 1

        self.images_indexes = self.data.iloc[self.index]
        self.image_top_index = self.images_indexes["top"]
        self.image_bottom_index = self.images_indexes["bottom"]
        self.image_shoes_index = self.images_indexes["shoes"]
        self.loadImages(self.image_top_index, self.image_bottom_index, self.image_shoes_index)

    def save(self):
        self.data.to_csv('out.csv', index=False)


class loadingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dress me")
        self.setWindowIcon(QIcon('image/logo.png'))

        self.setStyleSheet("background-color : black;")
        self.gif_image_label = QLabel(self)

        # set qmovie as label
        self.movie = QMovie("image/loading_resize.gif")
        self.gif_image_label.setMovie(self.movie)

        self.movie.start()
        self.gif_image_label.move(75, 75)

        self.resize(200, 200)

    def closewindow(self):
        self.close()

if __name__ == "__main__":
    pass
