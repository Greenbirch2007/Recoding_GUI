import re
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtCore import Qt, pyqtSlot
from PassWordEdit import PwdLineEdit
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class LogIn_UI(QMainWindow):

    def __init__(self, parent=None):
        super(LogIn_UI, self).__init__(parent)
        self.SetupUi()
        self.pushButton.clicked.connect(self.test)

    def test(self):
        self.hide()

    def SetupUi(self):
        self.setObjectName("MainWindow")
        self.resize(500, 300)  # 设置大小
        self.setWindowTitle("XX登录界面")  # 设置标题
        self.setFixedSize(self.width(), self.height())  # 禁止最大化
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\\Image\\10.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)  # 设置窗口的图标
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(130, 180, 91, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setText("记住账号")
        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setGeometry(QtCore.QRect(280, 180, 91, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setText("自动登录")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(135, 230, 230, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("登录")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(120, 70, 260, 90))
        self.tableWidget.setObjectName("tableWidget")
        self.TableSet()
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 75, 72, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("注册账号")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 120, 72, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText("修改密码")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(25, 80, 70, 70))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFlat(True)  # 设置按键边框取消
        self.pushButton_2.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_2.setIcon(QtGui.QIcon("..\\Image\\16.jpg"))

    def TableSet(self):
        self.table = self.tableWidget
        self.table.setColumnCount(1)
        self.table.setRowCount(2)
        # 设置表头隐藏显示
        self.table.setVerticalHeaderLabels(['账号', '密码'])
        self.table.verticalHeader().setVisible(True)
        self.table.horizontalHeader().setVisible(False)
        # 设置行高列宽
        self.table.setColumnWidth(0, 220)
        self.table.setRowHeight(0, 44)
        self.table.setRowHeight(1, 44)
        # 账号密码设置
        self.PassWordSet()
        self.IdentitySet()
        self.table.setCellWidget(0, 0, self.IdentityItem)
        self.table.setCellWidget(1, 0, self.PassWordItem)
        # @pyqtSlot()

    def IdentitySet(self):
        self.IdentityItem = QLineEdit()
        self.IdentityItem.installEventFilter(self)
        self.IdentityItem.setClearButtonEnabled(True)

    def PassWordSet(self):
        self.PassWordItem = PwdLineEdit()
        self.PassWordItem.installEventFilter(self)
        # self.PassWordItem.setText("hello")
        # 禁止右键菜单
        self.PassWordItem.setClearButtonEnabled(True)
        self.PassWordItem.setContextMenuPolicy(Qt.NoContextMenu)
        self.PassWordItem.setPlaceholderText("密码>8位 可输入数字字母字符")
        # self.PassWordItem.setEchoMode(QLineEdit.Password)

    @pyqtSlot()
    def on_PassWordItem_editingFinished(self):
        regex_pwd = "^([A-Z]|[a-z]|[0-9]|[`~!@#$%^&*()+=|{}':;',\\\\[\\\\].<>/?~！@#￥%……&*（）——+|{}【】‘；：”“'。，、？]){6,16}$"
        self.pwd1 = self.lineEdit_2.GetPassword()
        if len(self.pwd1) > 0:
            self.lineEdit_6.clear()
            rrpwd = re.compile(regex_pwd)
            if rrpwd.match(self.pwd1) is None:
                self.lineEdit_6.setText('密码不符合要求!')
        else:
            self.lineEdit_6.setText('密码未填写!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LogIn_UI()
    ui.show()
    sys.exit(app.exec_())
