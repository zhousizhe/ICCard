# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_informations.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk

from PyQt5.QtGui import QFont


class Manage_Informations_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(40, 5, 200, 20))
        self.title.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.title.setObjectName("title")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 90, 160, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(520, 40, 25, 25))
        self.label_3.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(740, 40, 70, 25))
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(550, 40, 130, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 90, 160, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 40, 130, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 25, 25))
        self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(810, 40, 180, 25))
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 90, 160, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(70, 40, 130, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(280, 40, 25, 25))
        self.label_2.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, tk.Tk().winfo_screenwidth() * 0.75 - 270,
                                                  tk.Tk().winfo_screenheight() * 0.8 - 60 - 220))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 0, 10, 1024))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", "搜索网点"))
        self.label_3.setText(_translate("Form", "区："))
        self.label_4.setText(_translate("Form", "网点名称："))
        self.comboBox_3.setItemText(0, _translate("Form", "请选择"))
        self.pushButton_4.setText(_translate("Form", "修改网点"))
        self.comboBox_2.setItemText(0, _translate("Form", "请选择"))
        self.label.setText(_translate("Form", "省："))
        self.pushButton_3.setText(_translate("Form", "撤销网点"))
        self.comboBox.setItemText(0, _translate("Form", "请选择"))
        self.label_2.setText(_translate("Form", "市："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "网点编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "所属运营商名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "网点电话"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "网点联系人"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "省份"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "所在市"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "所在区"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "网点名称"))
        self.title.setText(_translate("Form", "网点信息管理"))
        self.title.setFont(QFont("Roman times", 12, QFont.Bold))
        self.title.setGeometry(QtCore.QRect(40, 0, 190, 20))
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Manage_Informations_Form()
    ui.setupUi(widget)
    # widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())