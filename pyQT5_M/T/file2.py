# # # # #!/usr/bin/python3
# # # # #-*- coding:utf-8 -*-
# # # #
# # # #
# # # # import sys
# # # # # 基本控件位于pyqt5.qtwidgets模块中
# # # #
# # # #
# # # # from PyQt5.QtWidgets import QApplication,QWidget
# # # #
# # # #
# # # # if __name__=="__main__":
# # # #     #每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数
# # # #     app = QApplication(sys.argv)
# # # #     # QWidget部件是pyqt5所有用户界面对象的基类。它为QWidget提供默认构造函数。默认构造函数没有父类
# # # #     w = QWidget()
# # # #     # resize()方法调整窗口的大小。这里是250x宽，150x高
# # # #     w.resize(250,150)
# # # #     # move()方法移动窗口再屏幕上的位置　x= 300,y=300坐标
# # # #     w.move(300,300)
# # # #     # 设置窗口的标题
# # # #     w.setWindowTitle("Simple")
# # # #     #显示在屏幕上
# # # #     w.show()
# # # #
# # # #
# # # #     # 系统exit()方法确保应用程序干净的退出
# # # #     #的exec_()方法有下划线。因为执行是一个python关键字，因此，exec_()代替
# # # #     sys.exit(app.exec_())
# # #
# # # # 应用程序的图标
# # #
# # # # 应用程序图标是一个小的图像，通常再标题栏的左上角显示。
# # #
# # #
# # # import sys
# # # from PyQt5.QtWidgets import QApplication,QWidget
# # # from PyQt5.QtGui import QIcon
# # #
# # #
# # # class Example(QWidget):
# # #     def __init__(self):
# # #         super().__init__()
# # #         self.initUI()  # 界面绘制交给InitUI方法
# # #
# # #     def initUI(self):
# # #         # 设置窗口的位置和大小
# # #         self.setGeometry(300,300,300,220)
# # #
# # #         # 设置窗口的标题
# # #         self.setWindowTitle('Icon')
# # #         # 设置窗口的图标，引用当前目录下的web.png
# # #         self.setWindowIcon(QIcon('tang_logo.png'))
# # #         # self.setWindowIcon(QIcon('webwxgeticon.jpeg'))
# # #
# # #         # 显示窗口
# # #         self.show()
# # #
# # #
# # # if __name__ == '__main__':
# # #     #创建应用程序和对象
# # #     app = QApplication(sys.argv)
# # #     ex = Example()
# # #     sys.exit(app.exec_())
# #
# # # 提示语
# #
# #
# # import sys
# # from PyQt5.QtWidgets import (QWidget,QToolTip,QPushButton,
# #                              QApplication)
# #
# # from PyQt5.QtGui import QFont
# #
# #
# # class Example(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #
# #
# #
# #         self.initUI()
# #
# #
# #     def initUI(self):
# #         # 这种静态的方法设置一个用于显示工具提示的字体。
# #         # 我们使用10px滑体字体
# #
# #         # 创建一个提示，我们称之为settooltip()方法。
# #         # 我们可以使用丰富的文本格式
# #         self.setToolTip("这是一个<b>QWidget</b> widget")
# #
# #         # 创建一个PushButton并为他设置一个tooltip
# #         btn = QPushButton("Button",self)
# #         btn.setToolTip("这是一个<b>QPushButton</b> widget")
# #
# #         # btn.sizeHint() 显示默认尺寸
# #
# #         btn.resize(btn.sizeHint())
# #
# #         # 移动窗口的位置
# #         btn.move(50,50)
# #
# #         self.setGeometry(300,300,300,200)
# #         self.setWindowTitle("Tooltips")
# #         self.show()
# #
# #
# # if __name__ =='__main__':
# #     app = QApplication(sys.argv)
# #     ex= Example()
# #     sys.exit(app.exec_())
#
#
# # 关闭窗口
# # 关闭一个窗口可以点击标题栏上的x
#
#
# import sys
# from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
# from PyQt5.QtCore import QCoreApplication
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         qbtn= QPushButton("Quit",self)
#         qbtn.clicked.connect(QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(50,50)
#
#
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle("Quit button")
#         self.show()
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# 消息框

# 默认情况下，入股单击x按钮窗口就关闭了。


import sys
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Message box~")
        self.show()


    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self,"Message",
                                     "你是准备退出吗？",QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())