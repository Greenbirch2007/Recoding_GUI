import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class hello_mainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(hello_mainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.browser=QWebEngineView()
        #加载外部的web界面
        self.browser.load(QUrl('http://47.93.239.86:3389'))
        # self.browser.load(QUrl('https://www.haolizi.net/example/view_20217.html'))


        self.setCentralWidget(self.browser)


    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.WindowModal)
        # mainWindow.setFixedSize(1200, 688)
        mainWindow.setWindowIcon(QIcon('u.ico')) # 加入小图标成功

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "开始浏览的页面"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = hello_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())



