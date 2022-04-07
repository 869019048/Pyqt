#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a QCalendarWidget widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
    QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        #选择一个日期时，QDate的点击信号就触发了，把这个信号和我们自己定义的showDate()方法关联起来。
        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate() #使用selectedDate()方法获取选中的日期，
        self.lbl.setText(date.toString()) #然后把日期对象转成字符串，在标签里面显示出来

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()


    def showDate(self, date):

        self.lbl.setText(date.toString())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())