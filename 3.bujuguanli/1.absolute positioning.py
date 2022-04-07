#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 绝对定位的应用
# 元素不会随着我们更改窗口的位置和大小而变化。
# 不能适用于不同的平台和不同分辨率的显示器
# 更改应用字体大小会破坏布局
# 如果我们决定重构这个应用，需要全部计算一下每个元素的位置和大小

"""
ZetCode PyQt5 tutorial

This example shows three labels on a window
using absolute positioning.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())