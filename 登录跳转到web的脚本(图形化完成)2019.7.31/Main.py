import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# from Ui_Main import Ui_MainWindow  # 由.UI文件生成.py文件后，导入创建的GUI类

import math
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import cv2 as cvcv

from class_Detection import Detection


class Ui_Main(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Ui_Main, self).__init__()
        self.setupUi(self)

        # 将点击事件与槽函数进行连接
        self.btn_video.clicked.connect(self.btn_video_fuc)

    def btn_video_fuc(self):
        filename = QFileDialog.getOpenFileName(self, 'open file', './')

        self.timer_camera = QTimer(self)

        self.cap = cvcv.cv2.VideoCapture(filename[0])

        self.timer_camera.timeout.connect(self.show_pic)
        self.timer_camera.start(10)  # 1毫秒

    def show_pic(self):
        dc = Detection()
        success, frame = self.cap.read()

        if success:
            show = dc.process_image(frame)
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(showImage))
            self.label.setScaledContents(True)  # 图片自适应
            self.timer_camera.start(10)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Main()
    window.show()
    sys.exit(app.exec_())