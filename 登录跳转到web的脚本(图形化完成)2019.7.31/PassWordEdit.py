#!/usr/bin/env python
# encoding: utf-8
"""
+----------------------------------------------------------------------------+
 ╱◥██◣         ∧_∧　　　 ∧_∧　　    ∧_∧　　   ∧_∧     ╱◥██◣
|田︱田田|      （^ .^）　 （^ 、^）　 （^ 0^）　 （^ Д^）  |田︱田田|
╬╬╬╬╬╬╬╬╬╬-------∪-∪-------∪-∪--------∪-∪-------∪-∪---╬╬╬╬╬╬╬╬╬╬╬
+----------------------------------------------------------------------------+
License (C) Copyright 2017-2017,  Corporation Limited.
File Name         :    PassWordEdit.py
Auther            :    samenmoer
Software Version  :    Python3.6
Email Address     :    gpf192315@163.com
Creat Time        :    2018-10-06   19:34:17
CSDN blog         :    https://blog.csdn.net/samenmoer
Description       :
------------------------------------------------------------------------------
Modification History
Data          By           Version       Change Description
==============================================================================
${time}            |                |                 |
==============================================================================
¤╭⌒╮ ╭⌒╮¤╭⌒╮ ╭⌒╮¤╭⌒╮ ╭⌒╮¤╭⌒╮  ╭⌒╮¤╭⌒╮╭⌒╮¤╭⌒╮╭⌒╮¤╭⌒╮╭⌒╮¤╭⌒╮╭⌒╮¤╭⌒╮╭⌒╮¤╭⌒╮
------------------------------------------------------------------------------
"""
from RecordLog import print_log
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QTimer


# ==========================================================================
# * Founction Name    :   ModuleInit
# * Parameter         :   None
# * Return            :   None
# * Description       :   为当前模块设置Log头，方便识别，以及其他初始化设置
# ==========================================================================
def ModuleInit():
    global LogHead
    LogHead = "[wait to fill]"

    print_log("文件初始化完成", LogHead=LogHead)
    return


class PwdLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.m_LineEditText = ""
        self.m_LastCharCount = 0
        self.Action()

    def Action(self):
        self.cursorPositionChanged[int, int].connect(self.DisplayPasswordAfterEditSlot)
        self.textEdited[str].connect(self.GetRealTextSlot)
        self.time = QTimer(self)
        self.time.setInterval(500)
        self.time.start()
        self.show()

    def DisplayPasswordAfterEditSlot(self, old, new):
        print('new:', new)
        print('old:', old)
        if old >= 0 and new >= 0:
            if new > old:
                self.time.timeout.connect(self.DisplayPasswordSlot)
            else:
                self.setCursorPosition(old)

    def DisplayPasswordSlot(self):
        self.setText(self.GetMaskString())

    def GetRealTextSlot(self, text):
        self.m_LastCharCount = len(self.m_LineEditText)

        if len(text) > self.m_LastCharCount:
            self.m_LineEditText += text[-1]
        elif len(text) <= self.m_LastCharCount:
            self.m_LineEditText = self.m_LineEditText[:-1]

    def GetMaskString(self):
        mask = ""
        count = len(self.text())
        if count > 0:
            for i in range(count):
                mask += "*"
        return mask

    def GetPassword(self):
        return self.m_LineEditText

