

import os
themes = ['1.认识PyQt5','2.Python基本语法','3.Qt Designer的使用','4.PyQt5基本窗口空间','5.PyQt5高级界面空间'
          ,'6.PyQt5布局管理','7.PyQt5信号和槽','8.PyQt5图形和特效','9.PyQt5扩展应用'
          ,'10.PyQt5实战一：经典程序开发','11.PyQt5实战二：金融领域应用']

for item in themes:
    dir_path = '/home/wo/Recoding_GUI/PyQt5快速开发与实战/' + item
    os.mkdir(dir_path)