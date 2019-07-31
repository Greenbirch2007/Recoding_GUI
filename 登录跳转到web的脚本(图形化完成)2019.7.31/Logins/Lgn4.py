import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget
from PyQt5 import QtCore,QtWidgets

# class MainWidget(QtWidgets):
#     def __init__(self):
#         self.count = 0
#         QWidget.__init__(self)
#         self.setMinimumSize(600,300)  # 设置窗口最小尺寸
#         self.setMaximumSize(600,300)  # 设置窗口最大尺寸
#
#
#
# if __name__ =="__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mw = MainWidget()
#     mw.show()
#     sys.exit(app.exec_())

app = QApplication(sys.argv)
win = QMainWindow()

#设置窗口标题与初始大小
win.setWindowTitle("界面背景图片设置")
# win.resize(350, 250)
win.setFixedSize(760,440)  # 规定窗口大小
#设置对象名称
win.setObjectName("MainWindow")

# #todo 1 设置窗口背景图片
win.setStyleSheet("#MainWindow{border-image:url(./images/background.jpg);}")

#todo 2 设置窗口背景色
#win.setStyleSheet("#MainWindow{background-color: yellow}")

win.show()
sys.exit(app.exec_())
