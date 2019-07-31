import sys
from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QWidget, QApplication,QMainWindow

from PyQt5.QtWidgets import QWidget, QApplication,QMainWindow

# 1
class Icon(QWidget):
    def __init__(self, parent=None):
        super(Icon, self).__init__(parent)
        self.initUI()

    # 2
    def initUI(self):
        self.setFixedSize(850,500)  # 固定了窗口大小
        # self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('客户端登录测试')
        self.setWindowIcon(QIcon('./images/cloud.ico'))


    # def getPicture(self):
    #     win = QMainWindow()
    #     win.setStyleSheet("#MainWindow{border-image:url(./images/background.jpg);}")
    #


if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = Icon()
    icon.show()
    # QMainWindow.setFixedSize(760, 440)  # 规定窗口大小

    sys.exit(app.exec_())
