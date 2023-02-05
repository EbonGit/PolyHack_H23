from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import sys
import Training
import morning


class MenuWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.resize(414, 736)

        self.centralwidget = QWidget(self)
        self.setWindowIcon(QIcon('image/logo.png'))
        self.setWindowTitle("Dress me")

        self.train_button = QPushButton("Train")
        self.train_button.clicked.connect(self.show_training_window)
        self.get_fit_button = QPushButton("Morning")
        self.get_fit_button.clicked.connect(self.show_morning_window)
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.exit)
        self.back_label = QLabel(self)

        pixmap = QPixmap("image/background.jpg")
        self.back_label.setPixmap(pixmap.scaled(380, 736, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.back_label.resize(414, 736)
        self.back_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        #self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum,
                                                    #QSizePolicy.Expanding)

        self.setCentralWidget(self.centralwidget)

        # self.verticalLayout.addWidget(self.gif_image_label)
        # self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.addWidget(self.back_label)
        self.verticalLayout.addWidget(self.get_fit_button)
        self.verticalLayout.addWidget(self.train_button)
        self.verticalLayout.addWidget(self.exit_button)


    def show_training_window(self):
        self.training_window = Training.TrainingWindow()
        self.training_window.setupUi()
        self.training_window.show()

    def show_morning_window(self, checked):
        self.morning_window = morning.MorningWindow()
        self.morning_window.setupUi()
        self.morning_window.show()

    def exit(self):
        sys.exit()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MenuWindow()
    w.show()
    app.exec()
