#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this program, we can press on a button with a left mouse
click or drag and drop the button with  the right mouse click.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys

class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)
    #从QPushButton继承一个Button类，
    # 然后重构QPushButton的两个方法:mouseMoveEvent()和mousePressEvent().mouseMoveEvent()是拖拽开始的事件。

    def mouseMoveEvent(self, e):
        #我们只劫持按钮的右键事件，左键的操作还是默认行为。
        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        #创建一个QDrag对象，用来传输MIME-based数据。
        dropAction = drag.exec_(Qt.MoveAction)
        #拖放事件开始时，用到的处理函数式start().

    def mousePressEvent(self, e):
    #左键点击按钮，会在控制台输出“press”。注意，我们在父级上也调用了mousePressEvent()方法，
    # 不然的话，我们是看不到按钮按下的效果的。
        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('press')


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)


    def dragEnterEvent(self, e):

        e.accept()


    def dropEvent(self, e):

        position = e.pos()
        self.button.move(position)
        #在dropEvent()方法里，我们定义了按钮按下后和释放后的行为，获得鼠标移动的位置，然后把按钮放到这个地方。
        e.setDropAction(Qt.MoveAction)
        e.accept()
        #指定放下的动作类型为moveAction。

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()