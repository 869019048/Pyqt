#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 11:13
# @Author  : EricWei
# @Site    :
# @File    : 11.py
# @Software: PyCharm


from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from ui_openimage import Ui_Form
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
import os,sys


class window(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        super(window, self).__init__()
        self.cwd = os.getcwd()
        self.setupUi(self)
        self.labels = [self.label_1, self.label_2]
    def slot_open_image(self):
        files, filetype = QFileDialog.getOpenFileNames(self, '打开多个图片', self.cwd, "*.jpg, *.png, *.JPG, *.JPEG, All Files(*)")
        for i in range(len(files)):
            jpg = QtGui.QPixmap(files[i]).scaled(self.labels[i].width(), self.labels[i].height())
            self.labels[i].setPixmap(jpg)

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  my = window()
  my.show()
  sys.exit(app.exec_())
