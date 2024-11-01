import requests
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


# Creating a Window class that inherits from QMainWindow
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Downloader")
        self.setGeometry(300, 250, 1000, 700)


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()