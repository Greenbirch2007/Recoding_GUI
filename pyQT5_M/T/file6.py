# # # # # # # # # # # # # # # # # # # # # #  对话框窗口或对话框是现代GUI应用程序。
# # # # # # # # # # # # # # # # # # # # # #一个对话框被定义为两个或两个以上的人之间的谈话。
# # # # # # # # # # # # # # # # # # # # # # 在计算机应用程序对话框窗口用于"交谈"应用程序。
# # # # # # # # # # # # # # # # # # # # # # 一个对话框用于输入数据，修改数据，更改应用程序设置等
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # QInputDialog
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # QInputDialog提供了一种简单方便的对话框从用户得到一个值。输入值
# # # # # # # # # # # # # # # # # # # # # # 可以是字符串，一个数字，或一个项目从一个列表
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # # # # # # # # from PyQt5.QtWidgets import (QWidget,QPushButton,QLineEdit,
# # # # # # # # # # # # # # # # # # # # #                              QInputDialog,QApplication)
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # class Example(QWidget):
# # # # # # # # # # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # # # # # # # # # #         self.initUI()
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #     def initUI(self):
# # # # # # # # # # # # # # # # # # # # #         self.btn  = QPushButton("Dialog",self)
# # # # # # # # # # # # # # # # # # # # #         self.btn.move(20,20)
# # # # # # # # # # # # # # # # # # # # #         self.btn.clicked.connect(self.showDialog)
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #         self.le = QLineEdit(self)
# # # # # # # # # # # # # # # # # # # # #         self.le.move(130,22)
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #         self.setGeometry(300,300,200,150)
# # # # # # # # # # # # # # # # # # # # #         self.setWindowTitle("Input dialog")
# # # # # # # # # # # # # # # # # # # # #         self.show()
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #     def showDialog(self):
# # # # # # # # # # # # # # # # # # # # #         text,ok =QInputDialog.getText(self,"Input Dialog",
# # # # # # # # # # # # # # # # # # # # #                                       "Enter your name:")
# # # # # # # # # # # # # # # # # # # # #         if ok:
# # # # # # # # # # # # # # # # # # # # #             self.le.setText(str(text))
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # # # # # # # # # #     ex = Example()
# # # # # # # # # # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # 显示一个按钮和一个文本框，用户点击按钮显示一个输入框，
# # # # # # # # # # # # # # # # # # # # # 用户输入信息会显示在文本框中。
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # 代码显示输入对话框。第一个字符串是一个对话框标题，
# # # # # # # # # # # # # # # # # # # # # 第二个对话框中的消息。对话框返回输入的文本和一个布尔值。
# # # # # # # # # # # # # # # # # # # # # 点击ok按钮，布尔值是True
# # # # # # # # # # # # # # # # # # # # # 对话框收到的文本西欧系会显示在文本框中
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #　QColorDialog显示一个用于选择颜色值的对话框
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # # # # # # # from PyQt5.QtWidgets import (QWidget,QPushButton,QFrame,
# # # # # # # # # # # # # # # # # # # #                              QColorDialog,QApplication)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # from PyQt5.QtGui import QColor
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # class Example(QWidget):
# # # # # # # # # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # # # # # # # # #         self.initUI()
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #     def initUI(self):
# # # # # # # # # # # # # # # # # # # #         col = QColor(0,0,0)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #         self.btn = QPushButton("Dialog",self)
# # # # # # # # # # # # # # # # # # # #         self.btn.move(20,20)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #         self.btn.clicked.connect(self.showDialog)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #         self.frm = QFrame(self)
# # # # # # # # # # # # # # # # # # # #         self.frm.setStyleSheet("QWidget {background-color:%s}"
# # # # # # # # # # # # # # # # # # # #                                % col.name())
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #         self.frm.setGeometry(130,22,100,100)
# # # # # # # # # # # # # # # # # # # #         self.setGeometry(300,300,250,180)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #         self.setWindowTitle("Color dialog")
# # # # # # # # # # # # # # # # # # # #         self.show()
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #     def showDialog(self):
# # # # # # # # # # # # # # # # # # # #         col = QColorDialog.getColor()
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #         if col.isValid():
# # # # # # # # # # # # # # # # # # # #             self.frm.setStyleSheet("QWidget { background-color:%s}"
# # # # # # # # # # # # # # # # # # # #                                    % col.name())
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # # # # # # # # #     ex = Example()
# # # # # # # # # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # # # # # # from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
# # # # # # # # # # # # # # # # # # #                              QSizePolicy, QLabel, QFontDialog, QApplication)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # class Example(QWidget):
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #         self.initUI()
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #     def initUI(self):
# # # # # # # # # # # # # # # # # # #         vbox = QVBoxLayout()
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #         btn = QPushButton('Dialog', self)
# # # # # # # # # # # # # # # # # # #         btn.setSizePolicy(QSizePolicy.Fixed,
# # # # # # # # # # # # # # # # # # #                           QSizePolicy.Fixed)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #         btn.move(20, 20)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #         vbox.addWidget(btn)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #         btn.clicked.connect(self.showDialog)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #         self.lbl = QLabel('Knowledge only matters', self)
# # # # # # # # # # # # # # # # # # #         self.lbl.move(130, 20)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #         vbox.addWidget(self.lbl)
# # # # # # # # # # # # # # # # # # #         self.setLayout(vbox)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #         self.setGeometry(300, 300, 250, 180)
# # # # # # # # # # # # # # # # # # #         self.setWindowTitle('Font dialog')
# # # # # # # # # # # # # # # # # # #         self.show()
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #     def showDialog(self):
# # # # # # # # # # # # # # # # # # #         font, ok = QFontDialog.getFont()
# # # # # # # # # # # # # # # # # # #         if ok:
# # # # # # # # # # # # # # # # # # #             self.lbl.setFont(font)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # # # # # # # #     ex = Example()
# # # # # # # # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # # # # # from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
# # # # # # # # # # # # # # # # # #                              QAction, QFileDialog, QApplication)
# # # # # # # # # # # # # # # # # # from PyQt5.QtGui import QIcon
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # class Example(QMainWindow):
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #         self.initUI()
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #     def initUI(self):
# # # # # # # # # # # # # # # # # #         self.textEdit = QTextEdit()
# # # # # # # # # # # # # # # # # #         self.setCentralWidget(self.textEdit)
# # # # # # # # # # # # # # # # # #         self.statusBar()
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #         openFile = QAction(QIcon('open.png'), 'Open', self)
# # # # # # # # # # # # # # # # # #         openFile.setShortcut('Ctrl+O')
# # # # # # # # # # # # # # # # # #         openFile.setStatusTip('Open new File')
# # # # # # # # # # # # # # # # # #         openFile.triggered.connect(self.showDialog)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #         menubar = self.menuBar()
# # # # # # # # # # # # # # # # # #         fileMenu = menubar.addMenu('&File')
# # # # # # # # # # # # # # # # # #         fileMenu.addAction(openFile)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #         self.setGeometry(300, 300, 350, 300)
# # # # # # # # # # # # # # # # # #         self.setWindowTitle('File dialog')
# # # # # # # # # # # # # # # # # #         self.show()
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #     def showDialog(self):
# # # # # # # # # # # # # # # # # #         fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #         if fname[0]:
# # # # # # # # # # # # # # # # # #             f = open(fname[0], 'r')
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #             with f:
# # # # # # # # # # # # # # # # # #                 data = f.read()
# # # # # # # # # # # # # # # # # #                 self.textEdit.setText(data)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # # # # # # #     ex = Example()
# # # # # # # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # # # # from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
# # # # # # # # # # # # # # # # # from PyQt5.QtCore import Qt
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # class Example(QWidget):
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #         self.initUI()
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #     def initUI(self):
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #         cb = QCheckBox('Show title', self)
# # # # # # # # # # # # # # # # #         cb.move(20, 20)
# # # # # # # # # # # # # # # # #         cb.toggle()
# # # # # # # # # # # # # # # # #         cb.stateChanged.connect(self.changeTitle)
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #         self.setGeometry(300, 300, 250, 150)
# # # # # # # # # # # # # # # # #         self.setWindowTitle('QCheckBox')
# # # # # # # # # # # # # # # # #         self.show()
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #     def changeTitle(self, state):
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #         if state == Qt.Checked:
# # # # # # # # # # # # # # # # #             self.setWindowTitle('QCheckBox')
# # # # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # # # #             self.setWindowTitle('')
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # # # # # #     ex = Example()
# # # # # # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # # # from PyQt5.QtWidgets import (QWidget, QPushButton,
# # # # # # # # # # # # # # # #                              QFrame, QApplication)
# # # # # # # # # # # # # # # # from PyQt5.QtGui import QColor
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # class Example(QWidget):
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         self.initUI()
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #     def initUI(self):
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         self.col = QColor(0, 0, 0)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         redb = QPushButton('Red', self)
# # # # # # # # # # # # # # # #         redb.setCheckable(True)
# # # # # # # # # # # # # # # #         redb.move(10, 10)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         redb.clicked[bool].connect(self.setColor)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         greenb = QPushButton('Green', self)
# # # # # # # # # # # # # # # #         greenb.setCheckable(True)
# # # # # # # # # # # # # # # #         greenb.move(10, 60)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         greenb.clicked[bool].connect(self.setColor)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         blueb = QPushButton('Blue', self)
# # # # # # # # # # # # # # # #         blueb.setCheckable(True)
# # # # # # # # # # # # # # # #         blueb.move(10, 110)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         blueb.clicked[bool].connect(self.setColor)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         self.square = QFrame(self)
# # # # # # # # # # # # # # # #         self.square.setGeometry(150, 20, 100, 100)
# # # # # # # # # # # # # # # #         self.square.setStyleSheet("QWidget { background-color: %s }" %
# # # # # # # # # # # # # # # #                                   self.col.name())
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         self.setGeometry(300, 300, 280, 170)
# # # # # # # # # # # # # # # #         self.setWindowTitle('Toggle button')
# # # # # # # # # # # # # # # #         self.show()
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #     def setColor(self, pressed):
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         source = self.sender()
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         if pressed:
# # # # # # # # # # # # # # # #             val = 255
# # # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # # #             val = 0
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         if source.text() == "Red":
# # # # # # # # # # # # # # # #             self.col.setRed(val)
# # # # # # # # # # # # # # # #         elif source.text() == "Green":
# # # # # # # # # # # # # # # #             self.col.setGreen(val)
# # # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # # #             self.col.setBlue(val)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #         self.square.setStyleSheet("QFrame { background-color: %s }" %
# # # # # # # # # # # # # # # #                                   self.col.name())
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # # # # #     ex = Example()
# # # # # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # # from PyQt5.QtWidgets import (QWidget, QSlider,
# # # # # # # # # # # # # # #                              QLabel, QApplication)
# # # # # # # # # # # # # # # from PyQt5.QtCore import Qt
# # # # # # # # # # # # # # # from PyQt5.QtGui import QPixmap
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # class Example(QWidget):
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #         self.initUI()
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     def initUI(self):
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #         sld = QSlider(Qt.Horizontal, self)
# # # # # # # # # # # # # # #         sld.setFocusPolicy(Qt.NoFocus)
# # # # # # # # # # # # # # #         sld.setGeometry(30, 40, 100, 30)
# # # # # # # # # # # # # # #         sld.valueChanged[int].connect(self.changeValue)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #         self.label = QLabel(self)
# # # # # # # # # # # # # # #         self.label.setPixmap(QPixmap('audio.ico'))
# # # # # # # # # # # # # # #         self.label.setGeometry(160, 40, 80, 30)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #         self.setGeometry(300, 300, 280, 170)
# # # # # # # # # # # # # # #         self.setWindowTitle('QSlider')
# # # # # # # # # # # # # # #         self.show()
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     def changeValue(self, value):
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #         if value == 0:
# # # # # # # # # # # # # # #             self.label.setPixmap(QPixmap('audio.ico'))
# # # # # # # # # # # # # # #         elif value > 0 and value <= 30:
# # # # # # # # # # # # # # #             self.label.setPixmap(QPixmap('min.ico'))
# # # # # # # # # # # # # # #         elif value > 30 and value < 80:
# # # # # # # # # # # # # # #             self.label.setPixmap(QPixmap('med.ico'))
# # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # #             self.label.setPixmap(QPixmap('max.ico'))
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # # # #     ex = Example()
# # # # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # from PyQt5.QtWidgets import (QWidget, QProgressBar,
# # # # # # # # # # # # # #                              QPushButton, QApplication)
# # # # # # # # # # # # # # from PyQt5.QtCore import QBasicTimer
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # class Example(QWidget):
# # # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         self.initUI()
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     def initUI(self):
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         self.pbar = QProgressBar(self)
# # # # # # # # # # # # # #         self.pbar.setGeometry(30, 40, 200, 25)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         self.btn = QPushButton('Start', self)
# # # # # # # # # # # # # #         self.btn.move(40, 80)
# # # # # # # # # # # # # #         self.btn.clicked.connect(self.doAction)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         self.timer = QBasicTimer()
# # # # # # # # # # # # # #         self.step = 0
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         self.setGeometry(300, 300, 280, 170)
# # # # # # # # # # # # # #         self.setWindowTitle('QProgressBar')
# # # # # # # # # # # # # #         self.show()
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     def timerEvent(self, e):
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         if self.step >= 100:
# # # # # # # # # # # # # #             self.timer.stop()
# # # # # # # # # # # # # #             self.btn.setText('Finished')
# # # # # # # # # # # # # #             return
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         self.step = self.step + 1
# # # # # # # # # # # # # #         self.pbar.setValue(self.step)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     def doAction(self):
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #         if self.timer.isActive():
# # # # # # # # # # # # # #             self.timer.stop()
# # # # # # # # # # # # # #             self.btn.setText('Start')
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             self.timer.start(100, self)
# # # # # # # # # # # # # #             self.btn.setText('Stop')
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # # #     ex = Example()
# # # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # # #
# # # # # # # # # # # # # import sys
# # # # # # # # # # # # # from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
# # # # # # # # # # # # #                              QLabel, QApplication)
# # # # # # # # # # # # # from PyQt5.QtCore import QDate
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # class Example(QWidget):
# # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # #
# # # # # # # # # # # # #         self.initUI()
# # # # # # # # # # # # #
# # # # # # # # # # # # #     def initUI(self):
# # # # # # # # # # # # #         cal = QCalendarWidget(self)
# # # # # # # # # # # # #         cal.setGridVisible(True)
# # # # # # # # # # # # #         cal.move(20, 20)
# # # # # # # # # # # # #         cal.clicked[QDate].connect(self.showDate)
# # # # # # # # # # # # #
# # # # # # # # # # # # #         self.lbl = QLabel(self)
# # # # # # # # # # # # #         date = cal.selectedDate()
# # # # # # # # # # # # #         self.lbl.setText(date.toString())
# # # # # # # # # # # # #         self.lbl.move(130, 260)
# # # # # # # # # # # # #
# # # # # # # # # # # # #         self.setGeometry(300, 300, 350, 300)
# # # # # # # # # # # # #         self.setWindowTitle('Calendar')
# # # # # # # # # # # # #         self.show()
# # # # # # # # # # # # #
# # # # # # # # # # # # #     def showDate(self, date):
# # # # # # # # # # # # #         self.lbl.setText(date.toString())
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # #     ex = Example()
# # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # #
# # # # # # # # # # # # import sys
# # # # # # # # # # # # from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
# # # # # # # # # # # #                              QLabel, QApplication)
# # # # # # # # # # # # from PyQt5.QtGui import QPixmap
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # class Example(QWidget):
# # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # #
# # # # # # # # # # # #         self.initUI()
# # # # # # # # # # # #
# # # # # # # # # # # #     def initUI(self):
# # # # # # # # # # # #         hbox = QHBoxLayout(self)
# # # # # # # # # # # #         pixmap = QPixmap("t.png")
# # # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # #         lbl = QLabel(self)
# # # # # # # # # # # #         lbl.setPixmap(pixmap)
# # # # # # # # # # # #
# # # # # # # # # # # #         hbox.addWidget(lbl)
# # # # # # # # # # # #         self.setLayout(hbox)
# # # # # # # # # # # #
# # # # # # # # # # # #         self.move(300, 200)
# # # # # # # # # # # #         self.setWindowTitle('Red Rock')
# # # # # # # # # # # #         self.show()
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # #     ex = Example()
# # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # import sys
# # # # # # # # # # # from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
# # # # # # # # # # #                              QSplitter, QStyleFactory, QApplication)
# # # # # # # # # # # from PyQt5.QtCore import Qt
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # class Example(QWidget):
# # # # # # # # # # #     def __init__(self):
# # # # # # # # # # #         super().__init__()
# # # # # # # # # # #
# # # # # # # # # # #         self.initUI()
# # # # # # # # # # #
# # # # # # # # # # #     def initUI(self):
# # # # # # # # # # #         hbox = QHBoxLayout(self)
# # # # # # # # # # #
# # # # # # # # # # #         topleft = QFrame(self)
# # # # # # # # # # #         topleft.setFrameShape(QFrame.StyledPanel)
# # # # # # # # # # #
# # # # # # # # # # #         topright = QFrame(self)
# # # # # # # # # # #         topright.setFrameShape(QFrame.StyledPanel)
# # # # # # # # # # #
# # # # # # # # # # #         bottom = QFrame(self)
# # # # # # # # # # #         bottom.setFrameShape(QFrame.StyledPanel)
# # # # # # # # # # #
# # # # # # # # # # #         splitter1 = QSplitter(Qt.Horizontal)
# # # # # # # # # # #         splitter1.addWidget(topleft)
# # # # # # # # # # #         splitter1.addWidget(topright)
# # # # # # # # # # #
# # # # # # # # # # #         splitter2 = QSplitter(Qt.Vertical)
# # # # # # # # # # #         splitter2.addWidget(splitter1)
# # # # # # # # # # #         splitter2.addWidget(bottom)
# # # # # # # # # # #
# # # # # # # # # # #         hbox.addWidget(splitter2)
# # # # # # # # # # #         self.setLayout(hbox)
# # # # # # # # # # #
# # # # # # # # # # #         self.setGeometry(300, 300, 300, 200)
# # # # # # # # # # #         self.setWindowTitle('QSplitter')
# # # # # # # # # # #         self.show()
# # # # # # # # # # #
# # # # # # # # # # #     def onChanged(self, text):
# # # # # # # # # # #         self.lbl.setText(text)
# # # # # # # # # # #         self.lbl.adjustSize()
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # #     ex = Example()
# # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # #
# # # # # # # # # # import sys
# # # # # # # # # # from PyQt5.QtWidgets import (QWidget, QLabel,
# # # # # # # # # #                              QComboBox, QApplication)
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # class Example(QWidget):
# # # # # # # # # #     def __init__(self):
# # # # # # # # # #         super().__init__()
# # # # # # # # # #
# # # # # # # # # #         self.initUI()
# # # # # # # # # #
# # # # # # # # # #     def initUI(self):
# # # # # # # # # #         self.lbl = QLabel("Ubuntu", self)
# # # # # # # # # #
# # # # # # # # # #         combo = QComboBox(self)
# # # # # # # # # #         combo.addItem("Ubuntu")
# # # # # # # # # #         combo.addItem("Mandriva")
# # # # # # # # # #         combo.addItem("Fedora")
# # # # # # # # # #         combo.addItem("Arch")
# # # # # # # # # #         combo.addItem("Gentoo")
# # # # # # # # # #
# # # # # # # # # #         combo.move(50, 50)
# # # # # # # # # #         self.lbl.move(50, 150)
# # # # # # # # # #
# # # # # # # # # #         combo.activated[str].connect(self.onActivated)
# # # # # # # # # #
# # # # # # # # # #         self.setGeometry(300, 300, 300, 200)
# # # # # # # # # #         self.setWindowTitle('QComboBox')
# # # # # # # # # #         self.show()
# # # # # # # # # #
# # # # # # # # # #     def onActivated(self, text):
# # # # # # # # # #         self.lbl.setText(text)
# # # # # # # # # #         self.lbl.adjustSize()
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # #     ex = Example()
# # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # import sys
# # # # # # # # # from PyQt5.QtWidgets import (QPushButton, QWidget,
# # # # # # # # #                              QLineEdit, QApplication)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # class Button(QPushButton):
# # # # # # # # #     def __init__(self, title, parent):
# # # # # # # # #         super().__init__(title, parent)
# # # # # # # # #
# # # # # # # # #         self.setAcceptDrops(True)
# # # # # # # # #
# # # # # # # # #     def dragEnterEvent(self, e):
# # # # # # # # #
# # # # # # # # #         if e.mimeData().hasFormat('text/plain'):
# # # # # # # # #             e.accept()
# # # # # # # # #         else:
# # # # # # # # #             e.ignore()
# # # # # # # # #
# # # # # # # # #     def dropEvent(self, e):
# # # # # # # # #
# # # # # # # # #         self.setText(e.mimeData().text())
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # class Example(QWidget):
# # # # # # # # #     def __init__(self):
# # # # # # # # #         super().__init__()
# # # # # # # # #
# # # # # # # # #         self.initUI()
# # # # # # # # #
# # # # # # # # #     def initUI(self):
# # # # # # # # #         edit = QLineEdit('', self)
# # # # # # # # #         edit.setDragEnabled(True)
# # # # # # # # #         edit.move(30, 65)
# # # # # # # # #
# # # # # # # # #         button = Button("Button", self)
# # # # # # # # #         button.move(190, 65)
# # # # # # # # #
# # # # # # # # #         self.setWindowTitle('Simple drag & drop')
# # # # # # # # #         self.setGeometry(300, 300, 300, 150)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # if __name__ == '__main__':
# # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # #     ex = Example()
# # # # # # # # #     ex.show()
# # # # # # # # #     app.exec_()
# # # # # # # #
# # # # # # # # import sys
# # # # # # # # from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
# # # # # # # # from PyQt5.QtCore import Qt, QMimeData
# # # # # # # # from PyQt5.QtGui import QDrag
# # # # # # # #
# # # # # # # #
# # # # # # # # class Button(QPushButton):
# # # # # # # #     def __init__(self, title, parent):
# # # # # # # #         super().__init__(title, parent)
# # # # # # # #
# # # # # # # #     def mouseMoveEvent(self, e):
# # # # # # # #
# # # # # # # #         if e.buttons() != Qt.RightButton:
# # # # # # # #             return
# # # # # # # #
# # # # # # # #         mimeData = QMimeData()
# # # # # # # #
# # # # # # # #         drag = QDrag(self)
# # # # # # # #         drag.setMimeData(mimeData)
# # # # # # # #         drag.setHotSpot(e.pos() - self.rect().topLeft())
# # # # # # # #
# # # # # # # #         dropAction = drag.exec_(Qt.MoveAction)
# # # # # # # #
# # # # # # # #     def mousePressEvent(self, e):
# # # # # # # #
# # # # # # # #         QPushButton.mousePressEvent(self, e)
# # # # # # # #
# # # # # # # #         if e.button() == Qt.LeftButton:
# # # # # # # #             print('press')
# # # # # # # #
# # # # # # # #
# # # # # # # # class Example(QWidget):
# # # # # # # #     def __init__(self):
# # # # # # # #         super().__init__()
# # # # # # # #
# # # # # # # #         self.initUI()
# # # # # # # #
# # # # # # # #     def initUI(self):
# # # # # # # #         self.setAcceptDrops(True)
# # # # # # # #
# # # # # # # #         self.button = Button('Button', self)
# # # # # # # #         self.button.move(100, 65)
# # # # # # # #
# # # # # # # #         self.setWindowTitle('Click or Move')
# # # # # # # #         self.setGeometry(300, 300, 280, 150)
# # # # # # # #
# # # # # # # #     def dragEnterEvent(self, e):
# # # # # # # #         e.accept()
# # # # # # # #
# # # # # # # #     def dropEvent(self, e):
# # # # # # # #         position = e.pos()
# # # # # # # #         self.button.move(position)
# # # # # # # #
# # # # # # # #         e.setDropAction(Qt.MoveAction)
# # # # # # # #         e.accept()
# # # # # # # #
# # # # # # # #
# # # # # # # # if __name__ == '__main__':
# # # # # # # #     app = QApplication(sys.argv)
# # # # # # # #     ex = Example()
# # # # # # # #     ex.show()
# # # # # # # #     app.exec_()
# # # # # # #
# # # # # # # import sys
# # # # # # # from PyQt5.QtWidgets import QWidget, QApplication
# # # # # # # from PyQt5.QtGui import QPainter, QColor, QFont
# # # # # # # from PyQt5.QtCore import Qt
# # # # # # #
# # # # # # #
# # # # # # # class Example(QWidget):
# # # # # # #     def __init__(self):
# # # # # # #         super().__init__()
# # # # # # #
# # # # # # #         self.initUI()
# # # # # # #
# # # # # # #     def initUI(self):
# # # # # # #         self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
# # # # # # # \u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
# # # # # # # \u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'
# # # # # # #
# # # # # # #         self.setGeometry(300, 300, 280, 170)
# # # # # # #         self.setWindowTitle('Draw text')
# # # # # # #         self.show()
# # # # # # #
# # # # # # #     def paintEvent(self, event):
# # # # # # #         qp = QPainter()
# # # # # # #         qp.begin(self)
# # # # # # #         self.drawText(event, qp)
# # # # # # #         qp.end()
# # # # # # #
# # # # # # #     def drawText(self, event, qp):
# # # # # # #         qp.setPen(QColor(168, 34, 3))
# # # # # # #         qp.setFont(QFont('Decorative', 10))
# # # # # # #         qp.drawText(event.rect(), Qt.AlignCenter, self.text)
# # # # # # #
# # # # # # #
# # # # # # # if __name__ == '__main__':
# # # # # # #     app = QApplication(sys.argv)
# # # # # # #     ex = Example()
# # # # # # #     sys.exit(app.exec_())
# # # # # #
# # # # # # import sys, random
# # # # # # from PyQt5.QtWidgets import QWidget, QApplication
# # # # # # from PyQt5.QtGui import QPainter, QColor, QPen
# # # # # # from PyQt5.QtCore import Qt
# # # # # #
# # # # # #
# # # # # # class Example(QWidget):
# # # # # #     def __init__(self):
# # # # # #         super().__init__()
# # # # # #
# # # # # #         self.initUI()
# # # # # #
# # # # # #     def initUI(self):
# # # # # #         self.setGeometry(300, 300, 280, 170)
# # # # # #         self.setWindowTitle('Points')
# # # # # #         self.show()
# # # # # #
# # # # # #     def paintEvent(self, e):
# # # # # #         qp = QPainter()
# # # # # #         qp.begin(self)
# # # # # #         self.drawPoints(qp)
# # # # # #         qp.end()
# # # # # #
# # # # # #     def drawPoints(self, qp):
# # # # # #         qp.setPen(Qt.red)
# # # # # #         size = self.size()
# # # # # #
# # # # # #         for i in range(1000):
# # # # # #             x = random.randint(1, size.width() - 1)
# # # # # #             y = random.randint(1, size.height() - 1)
# # # # # #             qp.drawPoint(x, y)
# # # # # #
# # # # # #
# # # # # # if __name__ == '__main__':
# # # # # #     app = QApplication(sys.argv)
# # # # # #     ex = Example()
# # # # # #     sys.exit(app.exec_())
# # # # #
# # # # #
# # # # # import sys
# # # # # from PyQt5.QtWidgets import QWidget, QApplication
# # # # # from PyQt5.QtGui import QPainter, QColor, QBrush
# # # # #
# # # # #
# # # # # class Example(QWidget):
# # # # #     def __init__(self):
# # # # #         super().__init__()
# # # # #
# # # # #         self.initUI()
# # # # #
# # # # #     def initUI(self):
# # # # #         self.setGeometry(300, 300, 350, 100)
# # # # #         self.setWindowTitle('Colours')
# # # # #         self.show()
# # # # #
# # # # #     def paintEvent(self, e):
# # # # #         qp = QPainter()
# # # # #         qp.begin(self)
# # # # #         self.drawRectangles(qp)
# # # # #         qp.end()
# # # # #
# # # # #     def drawRectangles(self, qp):
# # # # #         col = QColor(0, 0, 0)
# # # # #         col.setNamedColor('#d4d4d4')
# # # # #         qp.setPen(col)
# # # # #
# # # # #         qp.setBrush(QColor(200, 0, 0))
# # # # #         qp.drawRect(10, 15, 90, 60)
# # # # #
# # # # #         qp.setBrush(QColor(255, 80, 0, 160))
# # # # #         qp.drawRect(130, 15, 90, 60)
# # # # #
# # # # #         qp.setBrush(QColor(25, 0, 90, 200))
# # # # #         qp.drawRect(250, 15, 90, 60)
# # # # #
# # # # #
# # # # # if __name__ == '__main__':
# # # # #     app = QApplication(sys.argv)
# # # # #     ex = Example()
# # # # #     sys.exit(app.exec_())
# # # #
# # # #
# # # # import sys
# # # # from PyQt5.QtWidgets import QWidget, QApplication
# # # # from PyQt5.QtGui import QPainter, QColor, QPen
# # # # from PyQt5.QtCore import Qt
# # # #
# # # #
# # # # class Example(QWidget):
# # # #     def __init__(self):
# # # #         super().__init__()
# # # #
# # # #         self.initUI()
# # # #
# # # #     def initUI(self):
# # # #         self.setGeometry(300, 300, 280, 270)
# # # #         self.setWindowTitle('Pen styles')
# # # #         self.show()
# # # #
# # # #     def paintEvent(self, e):
# # # #         qp = QPainter()
# # # #         qp.begin(self)
# # # #         self.drawLines(qp)
# # # #         qp.end()
# # # #
# # # #     def drawLines(self, qp):
# # # #         pen = QPen(Qt.black, 2, Qt.SolidLine)
# # # #
# # # #         qp.setPen(pen)
# # # #         qp.drawLine(20, 40, 250, 40)
# # # #
# # # #         pen.setStyle(Qt.DashLine)
# # # #         qp.setPen(pen)
# # # #         qp.drawLine(20, 80, 250, 80)
# # # #
# # # #         pen.setStyle(Qt.DashDotLine)
# # # #         qp.setPen(pen)
# # # #         qp.drawLine(20, 120, 250, 120)
# # # #
# # # #         pen.setStyle(Qt.DotLine)
# # # #         qp.setPen(pen)
# # # #         qp.drawLine(20, 160, 250, 160)
# # # #
# # # #         pen.setStyle(Qt.DashDotDotLine)
# # # #         qp.setPen(pen)
# # # #         qp.drawLine(20, 200, 250, 200)
# # # #
# # # #         pen.setStyle(Qt.CustomDashLine)
# # # #         pen.setDashPattern([1, 4, 5, 4])
# # # #         qp.setPen(pen)
# # # #         qp.drawLine(20, 240, 250, 240)
# # # #
# # # #
# # # # if __name__ == '__main__':
# # # #     app = QApplication(sys.argv)
# # # #     ex = Example()
# # # #     sys.exit(app.exec_())
# # #
# # #
# # # import sys
# # # from PyQt5.QtWidgets import QWidget, QApplication
# # # from PyQt5.QtGui import QPainter, QBrush
# # # from PyQt5.QtCore import Qt
# # #
# # #
# # # class Example(QWidget):
# # #     def __init__(self):
# # #         super().__init__()
# # #
# # #         self.initUI()
# # #
# # #     def initUI(self):
# # #         self.setGeometry(300, 300, 355, 280)
# # #         self.setWindowTitle('Brushes')
# # #         self.show()
# # #
# # #     def paintEvent(self, e):
# # #         qp = QPainter()
# # #         qp.begin(self)
# # #         self.drawBrushes(qp)
# # #         qp.end()
# # #
# # #     def drawBrushes(self, qp):
# # #         brush = QBrush(Qt.SolidPattern)
# # #         qp.setBrush(brush)
# # #         qp.drawRect(10, 15, 90, 60)
# # #
# # #         brush.setStyle(Qt.Dense1Pattern)
# # #         qp.setBrush(brush)
# # #         qp.drawRect(130, 15, 90, 60)
# # #
# # #         brush.setStyle(Qt.Dense2Pattern)
# # #         qp.setBrush(brush)
# # #         qp.drawRect(250, 15, 90, 60)
# # #
# # #         brush.setStyle(Qt.DiagCrossPattern)
# # #         qp.setBrush(brush)
# # #         qp.drawRect(10, 105, 90, 60)
# # #
# # #         brush.setStyle(Qt.Dense5Pattern)
# # #         qp.setBrush(brush)
# # #         qp.drawRect(130, 105, 90, 60)
# # #
# # #         brush.setStyle(Qt.Dense6Pattern)
# # #         qp.setBrush(brush)
# # #         qp.drawRect(250, 105, 90, 60)
# # #
# # #         brush.setStyle(Qt.HorPattern)
# # #         qp.setBrush(brush)
# # #         qp.drawRect(10, 195, 90, 60)
# # #
# # #         brush.setStyle(Qt.VerPattern)
# # #         qp.setBrush(brush)
# # #         qp.drawRect(130, 195, 90, 60)
# # #
# # #         brush.setStyle(Qt.BDiagPattern)
# # #         qp.setBrush(brush)
# # #         qp.drawRect(250, 195, 90, 60)
# # #
# # #
# # # if __name__ == '__main__':
# # #     app = QApplication(sys.argv)
# # #     ex = Example()
# # #     sys.exit(app.exec_())
# #
# # import sys
# # from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
# #                              QHBoxLayout, QVBoxLayout)
# # from PyQt5.QtCore import QObject, Qt, pyqtSignal
# # from PyQt5.QtGui import QPainter, QFont, QColor, QPen
# #
# #
# # class Communicate(QObject):
# #     updateBW = pyqtSignal(int)
# #
# #
# # class BurningWidget(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #
# #         self.initUI()
# #
# #     def initUI(self):
# #
# #         self.setMinimumSize(1, 30)
# #         self.value = 75
# #         self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]
# #
# #     def setValue(self, value):
# #
# #         self.value = value
# #
# #     def paintEvent(self, e):
# #
# #         qp = QPainter()
# #         qp.begin(self)
# #         self.drawWidget(qp)
# #         qp.end()
# #
# #     def drawWidget(self, qp):
# #
# #         font = QFont('Serif', 7, QFont.Light)
# #         qp.setFont(font)
# #
# #         size = self.size()
# #         w = size.width()
# #         h = size.height()
# #
# #         step = int(round(w / 10.0))
# #
# #         till = int(((w / 750.0) * self.value))
# #         full = int(((w / 750.0) * 700))
# #
# #         if self.value >= 700:
# #
# #             qp.setPen(QColor(255, 255, 255))
# #             qp.setBrush(QColor(255, 255, 184))
# #             qp.drawRect(0, 0, full, h)
# #             qp.setPen(QColor(255, 175, 175))
# #             qp.setBrush(QColor(255, 175, 175))
# #             qp.drawRect(full, 0, till - full, h)
# #
# #         else:
# #
# #             qp.setPen(QColor(255, 255, 255))
# #             qp.setBrush(QColor(255, 255, 184))
# #             qp.drawRect(0, 0, till, h)
# #
# #         pen = QPen(QColor(20, 20, 20), 1,
# #                    Qt.SolidLine)
# #
# #         qp.setPen(pen)
# #         qp.setBrush(Qt.NoBrush)
# #         qp.drawRect(0, 0, w - 1, h - 1)
# #
# #         j = 0
# #
# #         for i in range(step, 10 * step, step):
# #             qp.drawLine(i, 0, i, 5)
# #             metrics = qp.fontMetrics()
# #             fw = metrics.width(str(self.num[j]))
# #             qp.drawText(i - fw / 2, h / 2, str(self.num[j]))
# #             j = j + 1
# #
# #
# # class Example(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #
# #         self.initUI()
# #
# #     def initUI(self):
# #         sld = QSlider(Qt.Horizontal, self)
# #         sld.setFocusPolicy(Qt.NoFocus)
# #         sld.setRange(1, 750)
# #         sld.setValue(75)
# #         sld.setGeometry(30, 40, 150, 30)
# #
# #         self.c = Communicate()
# #         self.wid = BurningWidget()
# #         self.c.updateBW[int].connect(self.wid.setValue)
# #
# #         sld.valueChanged[int].connect(self.changeValue)
# #         hbox = QHBoxLayout()
# #         hbox.addWidget(self.wid)
# #         vbox = QVBoxLayout()
# #         vbox.addStretch(1)
# #         vbox.addLayout(hbox)
# #         self.setLayout(vbox)
# #
# #         self.setGeometry(300, 300, 390, 210)
# #         self.setWindowTitle('Burning widget')
# #         self.show()
# #
# #     def changeValue(self, value):
# #         self.c.updateBW.emit(value)
# #         self.wid.repaint()
# #
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = Example()
# #     sys.exit(app.exec_())
#
# import sys, random
# from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
# from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
# from PyQt5.QtGui import QPainter, QColor
#
#
# class Tetris(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.tboard = Board(self)
#         self.setCentralWidget(self.tboard)
#
#         self.statusbar = self.statusBar()
#         self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
#
#         self.tboard.start()
#
#         self.resize(180, 380)
#         self.center()
#         self.setWindowTitle('Tetris')
#         self.show()
#
#     def center(self):
#         screen = QDesktopWidget().screenGeometry()
#         size = self.geometry()
#         self.move((screen.width() - size.width()) / 2,
#                   (screen.height() - size.height()) / 2)
#
#
# class Board(QFrame):
#     msg2Statusbar = pyqtSignal(str)
#
#     BoardWidth = 10
#     BoardHeight = 22
#     Speed = 300
#
#     def __init__(self, parent):
#         super().__init__(parent)
#
#         self.initBoard()
#
#     def initBoard(self):
#
#         self.timer = QBasicTimer()
#         self.isWaitingAfterLine = False
#
#         self.curX = 0
#         self.curY = 0
#         self.numLinesRemoved = 0
#         self.board = []
#
#         self.setFocusPolicy(Qt.StrongFocus)
#         self.isStarted = False
#         self.isPaused = False
#         self.clearBoard()
#
#     def shapeAt(self, x, y):
#         return self.board[(y * Board.BoardWidth) + x]
#
#     def setShapeAt(self, x, y, shape):
#         self.board[(y * Board.BoardWidth) + x] = shape
#
#     def squareWidth(self):
#         return self.contentsRect().width() // Board.BoardWidth
#
#     def squareHeight(self):
#         return self.contentsRect().height() // Board.BoardHeight
#
#     def start(self):
#
#         if self.isPaused:
#             return
#
#         self.isStarted = True
#         self.isWaitingAfterLine = False
#         self.numLinesRemoved = 0
#         self.clearBoard()
#
#         self.msg2Statusbar.emit(str(self.numLinesRemoved))
#
#         self.newPiece()
#         self.timer.start(Board.Speed, self)
#
#     def pause(self):
#
#         if not self.isStarted:
#             return
#
#         self.isPaused = not self.isPaused
#
#         if self.isPaused:
#             self.timer.stop()
#             self.msg2Statusbar.emit("paused")
#
#         else:
#             self.timer.start(Board.Speed, self)
#             self.msg2Statusbar.emit(str(self.numLinesRemoved))
#
#         self.update()
#
#     def paintEvent(self, event):
#
#         painter = QPainter(self)
#         rect = self.contentsRect()
#
#         boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()
#
#         for i in range(Board.BoardHeight):
#             for j in range(Board.BoardWidth):
#                 shape = self.shapeAt(j, Board.BoardHeight - i - 1)
#
#                 if shape != Tetrominoe.NoShape:
#                     self.drawSquare(painter,
#                                     rect.left() + j * self.squareWidth(),
#                                     boardTop + i * self.squareHeight(), shape)
#
#         if self.curPiece.shape() != Tetrominoe.NoShape:
#
#             for i in range(4):
#                 x = self.curX + self.curPiece.x(i)
#                 y = self.curY - self.curPiece.y(i)
#                 self.drawSquare(painter, rect.left() + x * self.squareWidth(),
#                                 boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
#                                 self.curPiece.shape())
#
#     def keyPressEvent(self, event):
#
#         if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
#             super(Board, self).keyPressEvent(event)
#             return
#
#         key = event.key()
#
#         if key == Qt.Key_P:
#             self.pause()
#             return
#
#         if self.isPaused:
#             return
#
#         elif key == Qt.Key_Left:
#             self.tryMove(self.curPiece, self.curX - 1, self.curY)
#
#         elif key == Qt.Key_Right:
#             self.tryMove(self.curPiece, self.curX + 1, self.curY)
#
#         elif key == Qt.Key_Down:
#             self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
#
#         elif key == Qt.Key_Up:
#             self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
#
#         elif key == Qt.Key_Space:
#             self.dropDown()
#
#         elif key == Qt.Key_D:
#             self.oneLineDown()
#
#         else:
#             super(Board, self).keyPressEvent(event)
#
#     def timerEvent(self, event):
#
#         if event.timerId() == self.timer.timerId():
#
#             if self.isWaitingAfterLine:
#                 self.isWaitingAfterLine = False
#                 self.newPiece()
#             else:
#                 self.oneLineDown()
#
#         else:
#             super(Board, self).timerEvent(event)
#
#     def clearBoard(self):
#
#         for i in range(Board.BoardHeight * Board.BoardWidth):
#             self.board.append(Tetrominoe.NoShape)
#
#     def dropDown(self):
#
#         newY = self.curY
#
#         while newY > 0:
#
#             if not self.tryMove(self.curPiece, self.curX, newY - 1):
#                 break
#
#             newY -= 1
#
#         self.pieceDropped()
#
#     def oneLineDown(self):
#
#         if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
#             self.pieceDropped()
#
#     def pieceDropped(self):
#
#         for i in range(4):
#             x = self.curX + self.curPiece.x(i)
#             y = self.curY - self.curPiece.y(i)
#             self.setShapeAt(x, y, self.curPiece.shape())
#
#         self.removeFullLines()
#
#         if not self.isWaitingAfterLine:
#             self.newPiece()
#
#     def removeFullLines(self):
#
#         numFullLines = 0
#         rowsToRemove = []
#
#         for i in range(Board.BoardHeight):
#
#             n = 0
#             for j in range(Board.BoardWidth):
#                 if not self.shapeAt(j, i) == Tetrominoe.NoShape:
#                     n = n + 1
#
#             if n == 10:
#                 rowsToRemove.append(i)
#
#         rowsToRemove.reverse()
#
#         for m in rowsToRemove:
#
#             for k in range(m, Board.BoardHeight):
#                 for l in range(Board.BoardWidth):
#                     self.setShapeAt(l, k, self.shapeAt(l, k + 1))
#
#         numFullLines = numFullLines + len(rowsToRemove)
#
#         if numFullLines > 0:
#             self.numLinesRemoved = self.numLinesRemoved + numFullLines
#             self.msg2Statusbar.emit(str(self.numLinesRemoved))
#
#             self.isWaitingAfterLine = True
#             self.curPiece.setShape(Tetrominoe.NoShape)
#             self.update()
#
#     def newPiece(self):
#
#         self.curPiece = Shape()
#         self.curPiece.setRandomShape()
#         self.curX = Board.BoardWidth // 2 + 1
#         self.curY = Board.BoardHeight - 1 + self.curPiece.minY()
#
#         if not self.tryMove(self.curPiece, self.curX, self.curY):
#             self.curPiece.setShape(Tetrominoe.NoShape)
#             self.timer.stop()
#             self.isStarted = False
#             self.msg2Statusbar.emit("Game over")
#
#     def tryMove(self, newPiece, newX, newY):
#
#         for i in range(4):
#
#             x = newX + newPiece.x(i)
#             y = newY - newPiece.y(i)
#
#             if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
#                 return False
#
#             if self.shapeAt(x, y) != Tetrominoe.NoShape:
#                 return False
#
#         self.curPiece = newPiece
#         self.curX = newX
#         self.curY = newY
#         self.update()
#
#         return True
#
#     def drawSquare(self, painter, x, y, shape):
#
#         colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
#                       0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
#
#         color = QColor(colorTable[shape])
#         painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
#                          self.squareHeight() - 2, color)
#
#         painter.setPen(color.lighter())
#         painter.drawLine(x, y + self.squareHeight() - 1, x, y)
#         painter.drawLine(x, y, x + self.squareWidth() - 1, y)
#
#         painter.setPen(color.darker())
#         painter.drawLine(x + 1, y + self.squareHeight() - 1,
#                          x + self.squareWidth() - 1, y + self.squareHeight() - 1)
#         painter.drawLine(x + self.squareWidth() - 1,
#                          y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)
#
#
# class Tetrominoe(object):
#     NoShape = 0
#     ZShape = 1
#     SShape = 2
#     LineShape = 3
#     TShape = 4
#     SquareShape = 5
#     LShape = 6
#     MirroredLShape = 7
#
#
# class Shape(object):
#     coordsTable = (
#         ((0, 0), (0, 0), (0, 0), (0, 0)),
#         ((0, -1), (0, 0), (-1, 0), (-1, 1)),
#         ((0, -1), (0, 0), (1, 0), (1, 1)),
#         ((0, -1), (0, 0), (0, 1), (0, 2)),
#         ((-1, 0), (0, 0), (1, 0), (0, 1)),
#         ((0, 0), (1, 0), (0, 1), (1, 1)),
#         ((-1, -1), (0, -1), (0, 0), (0, 1)),
#         ((1, -1), (0, -1), (0, 0), (0, 1))
#     )
#
#     def __init__(self):
#
#         self.coords = [[0, 0] for i in range(4)]
#         self.pieceShape = Tetrominoe.NoShape
#
#         self.setShape(Tetrominoe.NoShape)
#
#     def shape(self):
#         return self.pieceShape
#
#     def setShape(self, shape):
#
#         table = Shape.coordsTable[shape]
#
#         for i in range(4):
#             for j in range(2):
#                 self.coords[i][j] = table[i][j]
#
#         self.pieceShape = shape
#
#     def setRandomShape(self):
#         self.setShape(random.randint(1, 7))
#
#     def x(self, index):
#         return self.coords[index][0]
#
#     def y(self, index):
#         return self.coords[index][1]
#
#     def setX(self, index, x):
#         self.coords[index][0] = x
#
#     def setY(self, index, y):
#         self.coords[index][1] = y
#
#     def minX(self):
#
#         m = self.coords[0][0]
#         for i in range(4):
#             m = min(m, self.coords[i][0])
#
#         return m
#
#     def maxX(self):
#
#         m = self.coords[0][0]
#         for i in range(4):
#             m = max(m, self.coords[i][0])
#
#         return m
#
#     def minY(self):
#
#         m = self.coords[0][1]
#         for i in range(4):
#             m = min(m, self.coords[i][1])
#
#         return m
#
#     def maxY(self):
#
#         m = self.coords[0][1]
#         for i in range(4):
#             m = max(m, self.coords[i][1])
#
#         return m
#
#     def rotateLeft(self):
#
#         if self.pieceShape == Tetrominoe.SquareShape:
#             return self
#
#         result = Shape()
#         result.pieceShape = self.pieceShape
#
#         for i in range(4):
#             result.setX(i, self.y(i))
#             result.setY(i, -self.x(i))
#
#         return result
#
#     def rotateRight(self):
#
#         if self.pieceShape == Tetrominoe.SquareShape:
#             return self
#
#         result = Shape()
#         result.pieceShape = self.pieceShape
#
#         for i in range(4):
#             result.setX(i, -self.y(i))
#             result.setY(i, self.x(i))
#
#         return result
#
#
# if __name__ == '__main__':
#     app = QApplication([])
#     tetris = Tetris()
#     sys.exit(app.exec_())