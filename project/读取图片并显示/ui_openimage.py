# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_openimage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1144, 750)
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(130, 130, 351, 251))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(680, 140, 351, 251))
        self.label_2.setObjectName("label_2")
        self.btn_image = QtWidgets.QPushButton(Form)
        self.btn_image.setGeometry(QtCore.QRect(170, 560, 93, 28))
        self.btn_image.setObjectName("btn_image")

        self.retranslateUi(Form)
        self.btn_image.clicked.connect(self.slot_open_image)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_1.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.btn_image.setText(_translate("Form", "选择图片"))