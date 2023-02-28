import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
import random
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


class Yellow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        uic.loadUi('Ui.ui', self)
        self.radius = int(random.choice([_ for _ in range(1, 1000)]))
        self.should_paint_circle = False
        self.pushButton.clicked.connect(self.nnn)
        self.setWindowTitle('Жёлтые окружности')

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            painter.drawEllipse(40, 40, self.radius, self.radius)

    def nnn(self):
        self.should_paint_circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec())



