import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class OpenImage(QWidget):

    def __init__(self, path):
        super().__init__()
        self.title = 'Image View'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.path = path
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel(self)
        pixmap = QPixmap(self.path)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.show()