#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a QSlider widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QSlider,
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        sld = QSlider(Qt.Horizontal, self) #创建一个水平的QSlider
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png')) #创建一个QLabel组件并给它设置一个静音图标
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()


    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('../mask/image/file.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('../mask/image/close.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('../mask/image/mask.png'))
        else:
            self.label.setPixmap(QPixmap('../mask/image/quit.png'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())