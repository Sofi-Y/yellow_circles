import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
import random
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 466)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 340, 231, 51))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(50, 240, 461, 51))
        self.textEdit.setObjectName("textEdit")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Кнопка"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Нажмите кнопку для появления кругов</span></p></body></html>"))


class Yellow(QWidget, Ui_Form):
    def __init__(self):
        super(QWidget, self).__init__()
        self.radius = int(random.choice([_ for _ in range(1, 1000)]))
        self.setupUi(self)
        self.should_paint_circle = False
        self.pushButton.clicked.connect(self.nnn)
        self.setWindowTitle('Oкружности')

    def paintEvent(self, event):
        super().paintEvent(event)
        colors = [Qt.yellow, Qt.red, Qt.black, Qt.green]
        color = random.choice(colors)
        if self.should_paint_circle:
            painter = QPainter(self)
            painter.setPen(QPen(color, 8, Qt.SolidLine))
            painter.drawEllipse(40, 40, self.radius, self.radius)

    def nnn(self):
        self.should_paint_circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec())



