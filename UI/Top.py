# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Top.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk

class Top_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(1024, 50)
        self.quit = QtWidgets.QPushButton(Form)
        self.quit.setGeometry(QtCore.QRect(tk.Tk().winfo_screenwidth()*0.75-130, 5, 40, 40))
        self.quit.setObjectName("quit")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(tk.Tk().winfo_screenwidth()*0.75-80, 5, 40, 40))
        self.cancel.setObjectName("cancel")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 70, 1920, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.quit.setText(_translate("Form", "退出"))
        self.cancel.setText(_translate("Form", "注销"))

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Top_Form()
    ui.setupUi(widget)
    # widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())