# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLineEdit, QApplication

class Ui_Form_User_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 170)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 50, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 50, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 50, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(210, 70, 50, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.hide()
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 120, 75, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 120, 75, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(Form.close)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 120, 20))
        self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit.setValidator(QIntValidator())
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 20, 120, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(80, 70, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.loginType = QtWidgets.QComboBox(Form)
        self.loginType.setGeometry(QtCore.QRect(260, 70, 121, 22))
        self.loginType.setObjectName("loginType")
        self.loginType.addItem("")
        self.loginType.addItem("")
        self.loginType.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.label.setText(_translate("Form", "手机号："))
        self.label_2.setText(_translate("Form", "密码："))
        self.label_3.setText(_translate("Form", "串口："))
        self.label_4.setText(_translate("Form", "模式："))
        self.pushButton.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.comboBox.setItemText(0, _translate("Form", "COM3"))
        self.comboBox.setItemText(1, _translate("Form", "COM2"))
        self.comboBox.setItemText(2, _translate("Form", "COM1"))
        self.loginType.setItemText(0, _translate("Form", "联网"))
        self.loginType.setItemText(1, _translate("Form", "离线"))



