# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assistant_information.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk

from PyQt5.QtGui import QFont


class Assistant_Information_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(40, 5, 200, 20))
        self.title.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.title.setObjectName("title")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 90, 171, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(380, 40, 91, 25))
        self.label_3.setAlignment(QtCore.Qt.AlignLeft |QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(710, 40, 81, 25))
        self.label_4.setAlignment(QtCore.Qt.AlignLeft |QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 91, 25))
        self.label.setAlignment(QtCore.Qt.AlignLeft |QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 90, 171, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 90, 171, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 190, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(455, 40, 190, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(800, 40, 190, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 150, tk.Tk().winfo_screenwidth() * 0.75 - 270,
                                                  tk.Tk().winfo_screenheight() * 0.8 - 150-110))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        self.pushButton_4.setText(_translate("Form", "修改营业员"))
        self.label_3.setText(_translate("Form", "网点名称："))
        self.label_4.setText(_translate("Form", "操作员姓名："))
        self.label.setText(_translate("Form", "操作员编号："))
        self.pushButton_5.setText(_translate("Form", "搜索营业员"))
        self.pushButton_3.setText(_translate("Form", "删除营业员"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "操作员编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "真实姓名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "身份证号"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "联系电话"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "所属网点编号"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "所属网点名称"))
        self.title.setText(_translate("Form", "营业员信息管理"))
        self.title.setFont(QFont("Roman times", 12, QFont.Bold))
        self.title.setGeometry(QtCore.QRect(40, 0, 190, 20))

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Assistant_Information_Form()
    ui.setupUi(widget)
    # widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())