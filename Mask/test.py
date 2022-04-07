#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.statusBar() #底部状态栏
        self.EditIcon() #修改图标和作者
        self.layout() #功能界面布局


        #主菜单
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File') #File
        EditMenu = menubar.addMenu('Edit') #Edit
        ViewMenu = menubar.addMenu('View') #View
        HelpMenu = menubar.addMenu('Help') #Help

        #File子菜单
        Open_fileMenu = QAction('Open', self)
        Open_dir_fileMenu = QAction('Open dir', self)
        change_Save_dir_fileMenu = QAction('change Save dir', self)
        Save_fileMenu = QAction('Save', self)
        Close_fileMenu = QAction('Close', self)
        #Quit_fileMenu = QAction('Quit', self)

        fileMenu.addAction(Open_fileMenu)
        #self.Open_fileMenu(fileMenu) #Open_fileMenu 功能

        fileMenu.addAction(Open_dir_fileMenu)
        fileMenu.addAction(change_Save_dir_fileMenu)
        fileMenu.addAction(Save_fileMenu)
        fileMenu.addAction(Close_fileMenu)

        #fileMenu.addAction(Quit_fileMenu)
        self.Quit_fileMenu(fileMenu) #Quit_fileMenu 功能

        # Edit子菜单
        # View子菜单
        # Help子菜单


        #self.toolbar() #界面上其余功能

        self.center()#主窗口居中
        self.show()

    #######################################子菜单功能(File)##############################
    # File子菜单
    def Open_fileMenu(self,fileMenu):  # 打开
        openAct = QAction(QIcon('image/file.png'), '&Open', self)
        openAct.setShortcut('Ctrl+O')  #快捷键Ctrl+O退打开文件
        openAct.setStatusTip('Open image or label file')
        openAct.triggered.connect(qApp.open)
        fileMenu.addAction(openAct)

    def Quit_fileMenu(self,fileMenu):  # 退出
        exitAct = QAction(QIcon('image/quit.png'), '&Quit', self)
        exitAct.setShortcut('Ctrl+Q')  #快捷键Ctrl+Q退出应用
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)


    # Edit子菜单
    # View子菜单
    # Help子菜单

    ########################################全局功能和设计####################################
    def layout(self):
        okButton = QPushButton("OK")  # 创建按钮
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)  # 加弹性空间 会将按钮挤到窗口的右边。
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 为了布局需要，我们把这个水平布局放到了一个垂直布局盒里面
        vbox = QVBoxLayout()
        vbox.addStretch(1)  # 弹性元素会把水平布局挤到窗口的下边
        vbox.addLayout(hbox)

        self.setLayout(vbox)
    def toolbar(self):
        exitAct = QAction(QIcon('image/file.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')

        self.toolbar.addAction(exitAct)


    # def mouseMoveEvent(self, e):
    # #e代表了事件对象。里面有我们触发事件（鼠标移动）的事件对象。
    # # x()和y()方法得到鼠标的x和y坐标点，然后拼成字符串输出到QLabel组件里。
    #
    #     x = e.x()
    #     y = e.y()
    #
    #     text = "x: {0},  y: {1}".format(x, y)
    #     self.label.setText(text)



    def EditIcon(self): #修改图标和作者
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('image/mask.png'))
        self.setWindowTitle('LabelMask')

    def center(self): #主窗口居中和大小
        qr = self.frameGeometry()  # 获得主窗口所在的框架。
        cp = QDesktopWidget().availableGeometry().center()  # 获取显示器的分辨率，然后得到屏幕中间点的位置。
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.resize(600, 500)  # 调整大小

    def closeEvent(self, event): #关闭时弹窗确认
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def contextMenuEvent(self, event): #全局右击菜单

           cmenu = QMenu(self)

           newAct = cmenu.addAction("New")
           opnAct = cmenu.addAction("Open")
           quitAct = cmenu.addAction("Quit")
           action = cmenu.exec_(self.mapToGlobal(event.pos()))

           if action == quitAct:
               qApp.quit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())