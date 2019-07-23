# # # # #第三节布局管理
# # # #
# # # # # pyQt5布局有两种方式，绝对布局和布局类
# # # #
# # # # # 绝对定位　　程序指定每个控件的位置和大小　(以像素为单位)
# # # # # 绝对定位有以下限制：
# # # # # 1. 如果我们调整窗口，控件的大小和位置不会改变
# # # # # 2. 在各种平台上应用程序看起来会不一样
# # # # # 3.如果改变字体，我们的应用程序的布局就会改变
# # # # # 4. 如果我们决定改变我们的布局，我们必须完全重做我们的布局
# # # #
# # # #
# # # # import sys
# # # # from PyQt5.QtWidgets import QWidget,QLabel,QApplication
# # # #
# # # # class Example(QWidget):
# # # #     def __init__(self):
# # # #         super().__init__()
# # # #         self.initUI()
# # # #
# # # #     def initUI(self):
# # # #         lbl1 = QLabel("Zetcode",self)
# # # #         lbl1.move(15,10)
# # # #
# # # #
# # # #         lbl2 = QLabel('tutorials',self)
# # # #         lbl2.move(35,40)
# # # #
# # # #         lbl3 = QLabel("for programmers",self)
# # # #         lbl3.move(55,70)
# # # #
# # # #
# # # #         self.setGeometry(300,300,250,150)
# # # #         self.setWindowTitle("Absolute")
# # # #         self.show()
# # # #
# # # #
# # # # if __name__ =="__main__":
# # # #     app = QApplication(sys.argv)
# # # #     ex = Example()
# # # #     sys.exit(app.exec_())
# # #
# # #
# # # # 框布局 Boxlayout
# # #
# # # # 我们使用QHBoxLayout和QVBoxLayout,来分别创建横向布局和纵向布局
# # #
# # #
# # # import sys
# # # from PyQt5.QtWidgets import (QWidget,QPushButton,
# # #                              QHBoxLayout,QVBoxLayout,QApplication)
# # #
# # # class Example(QWidget):
# # #     def __init__(self):
# # #         super().__init__()
# # #
# # #         self.initUI()
# # #
# # #
# # #     def initUI(self):
# # #         okButton = QPushButton("OK")
# # #         cancelButton = QPushButton("Cancel")
# # #
# # #         hbox = QHBoxLayout()
# # #         hbox.addStretch(1)
# # #         hbox.addWidget(okButton)
# # #         hbox.addWidget(cancelButton)
# # #
# # #
# # #
# # #         vbox = QVBoxLayout()
# # #         vbox.addStretch(1)
# # #         vbox.addLayout(hbox)
# # #
# # #
# # #         self.setLayout(vbox)
# # #
# # #         self.setGeometry(300,300,300,150)
# # #         self.setWindowTitle("Buttions")
# # #         self.show()
# # #
# # # if __name__ =="__main__":
# # #     app = QApplication(sys.argv)
# # #     ex = Example()
# # #     sys.exit(app.exec_())
# #
# # # 在这个例子中，我们使用HBoxLayout,QVBoxLayout并添加伸展因子，
# # # 在窗口的右下角显示两个按钮
# #
# #
# # #　我们创建一个水平布局和添加一个伸展因子和两个按钮。
# # # 两个按钮前的伸展增加了一个可伸缩的空间，这将推动他们靠右显示
# # # 创建一个垂直布局，并添加伸展因子，让水平布局显示在窗口底部
# #
# #
# # # 表格布局QGridLayout
# #
# # # 表格布局将空间分为行和列。我们使用QGridLayout类创建一个网格布局
# #
# # import sys
# # from PyQt5.QtWidgets import (QWidget, QGridLayout,
# #     QPushButton, QApplication)
# #
# # class Example(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()
# #
# #     def initUI(self):
# #         grid = QGridLayout()
# #         self.setLayout(grid)
# #
# #         names = ['Cls',"Bck","","Close",
# #                  "7"'8','9','/',
# #                  "4","5","6","*",
# #                  "1","2","3","-",
# #                  "0",".","=","+"]
# #
# #         positions = [(i,j) for i in range(5) for j in range(4)]
# #         for position,name in zip(positions,names):
# #             if name =="":
# #                 continue
# #             button = QPushButton(name)
# #             grid.addWidget(button,*position)
# #
# #
# #         self.move(300,150)
# #         self.setWindowTitle("Calculator")
# #         self.show()
# #
# #
# # if __name__ =="__main__":
# #     app = QApplication(sys.argv)
# #     ex = Example()
# #     sys.exit(app.exec_())
# #
# #  创建一个网格的按钮
# # QGridLayout的实例被创建并设置应用程序窗口的布局
# #
# #
# # 这些按钮标签
# #
# #
# # 我们创建一个网格中位置的列表  创建按钮并使用addWidget()方法添加到布局中
# #
# #
# # 控件可以在网格中跨越多个行或列。再
# #
# import sys
# from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
#     QTextEdit, QGridLayout, QApplication)
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         title = QLabel("Title")
#         author = QLabel("Author")
#         review = QLabel("Review")
#
#         titleEdit = QLineEdit()
#         authorEdit  = QLineEdit()
#         reviewEdit = QLineEdit()
#
#         grid = QGridLayout()
#         grid.setSpacing(10)
#
#         grid.addWidget(title,1,0)
#         grid.addWidget(titleEdit,1,1)
#
#         grid.addWidget(author,2,0)
#         grid.addWidget(authorEdit,2,1)
#
#         grid.addWidget(review,3,0)
#         grid.addWidget(reviewEdit,3,1,5,1)
#
#         self.setLayout(grid)
#
#         self.setGeometry(300,300,350,300)
#         self.setWindowTitle("Review")
#         self.show()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# 我们创建一个窗口，其中有三个标签，两个