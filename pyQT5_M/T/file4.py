# # # # # # 第四节  Pyqt5菜单和工具栏
# # # # #
# # # # #
# # # # # # 本节我们将创建菜单和工具栏
# # # # #
# # # # #
# # # # # # 主窗口
# # # # #
# # # # # # QMainWindow类提供了一个主要的应用程序。你用它可以让应用程序添加状态栏
# # # # #
# # # # # # 状态栏  用于显示状态信息
# # # # #
# # # # #
# # # # # import sys
# # # # # from PyQt5.QtWidgets import QMainWindow,QApplication
# # # # #
# # # # # class Example(QMainWindow):
# # # # #     def __init__(self):
# # # # #         super().__init__()
# # # # #         self.initUI()
# # # # #
# # # # #     def initUI(self):
# # # # #         self.statusBar().showMessage("Ready")
# # # # #
# # # # #         self.setGeometry(300,300,250,150)
# # # # #         self.setWindowTitle("Statusbar")
# # # # #         self.show()
# # # # #
# # # # # if __name__ =="__main__":
# # # # #     app = QApplication(sys.argv)
# # # # #     ex = Example()
# # # # #     sys.exit(app.exec_())
# # # # #
# # # # #
# # # # # # 用QMainWindow创建状态栏的小窗口
# # # # #
# # # # # # 菜单栏
# # # #
# # # import sys
# # # from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
# # # from PyQt5.QtGui import QIcon
# # #
# # #
# # # class Example(QMainWindow):
# # #
# # #     def __init__(self):
# # #         super().__init__()
# # #
# # #         self.initUI()
# # #
# # #     def initUI(self):
# # #         exitAction = QAction(QIcon('t.png'), '&Exit', self)
# # #         exitAction.setShortcut('Ctrl+Q')
# # #         exitAction.setStatusTip('Exit application')
# # #         exitAction.triggered.connect(qApp.quit)
# # #
# # #         self.statusBar()
# # #
# # #         # 创建一个菜单栏
# # #         menubar = self.menuBar()
# # #         # 添加菜单
# # #         fileMenu = menubar.addMenu('&File')
# # #         # 添加事件
# # #         fileMenu.addAction(exitAction)
# # #
# # #         self.setGeometry(300, 300, 300, 200)
# # #         self.setWindowTitle('Menubar')
# # #         self.show()
# # #
# # #
# # # if __name__ == '__main__':
# # #     app = QApplication(sys.argv)
# # #     ex = Example()
# # #     sys.exit(app.exec_())
# # # #
# # # # 我们创建一个菜单栏和一个菜单。这个菜单将终止应用程序。
# # # # ctrl+ｑ的行动是可访问的快捷方式
# # #
# # #
# # # # QAction可以操作菜单栏，工具栏，或自定义键盘快捷键。
# # # # 我们创建一个事件和一个特定的图标和一个“退出”的标签。
# # # 然后，在定义该操作的快捷键
# # # 第三行创建一个鼠标指针悬停在该菜单项上时的提示
# #
# #
# # # 当我们点击菜单的时候，调用aApp.quit,终止应用程序
# #
# #
# # # 工具栏　提供了一个快速访问的入口
# #
# # import sys
# # from PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication
# # from PyQt5.QtGui import QIcon
# #
# # class Example(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()
# #
# #
# #     def initUI(self):
# #         exitAction = QAction(QIcon("t.png"),"Exit",self)
# #         exitAction.setShortcut("Ctrl+Q")
# #         exitAction.triggered.connect(qApp.quit)
# #
# #         self.toolbar = self.addToolBar("Exit")
# #         self.toolbar.addAction(exitAction)
# #
# #         self.setGeometry(300,300,300,200)
# #         self.setWindowTitle("Toolbar")
# #         self.show()
# #
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = Example()
# #     sys.exit(app.exec_())
#
#
# # 我们创建一个简单的工具栏，工具栏有一个按钮，点击关闭窗口
#
#
# # 类似于上面的菜单栏的例子，我们创建一个QAction事件。
# # 该事件有一个标签，图标和快捷键。退出窗口的方法
#
#
# # 把他们放在一起，将创建一个菜单条，工具栏和状态栏的小窗口
#
#
# import sys
# from PyQt5.QtWidgets import QMainWindow,QTextEdit,QAction,QApplication
# from PyQt5.QtGui import QIcon
#
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         textEdit = QTextEdit()
#         self.setCentralWidget(textEdit)
#
#         exitAction = QAction(QIcon('tx.jpeg'),"Exit",self)
#         exitAction.setShortcut("Ctrl+Q")
#         exitAction.setShortcut("Exit application")
#         exitAction.triggered.connect(self.close)
#
#
#         self.statusBar()
#
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu("&File")
#         fileMenu.addAction(exitAction)
#
#         toolbar = self.addToolBar("Exit")
#         toolbar.addAction(exitAction)
#
#         self.setGeometry(300,300,350,250)
#         self.setWindowTitle("Main window")
#         self.show()
#
#
#
# if __name__ =="__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# 创建了一个窗口　，我们创建了一个QTextEdit,并把他设置为窗口的布局

