
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        #�Ѵ��ڷŵ���Ļ�ϲ������ô��ڴ�С�������ֱ������Ļ�����x��y�ʹ��ڴ�С�Ŀ��ߡ�
        # Ҳ����˵���������resize()��move()�ĺ���
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('1.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())