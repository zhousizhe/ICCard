# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rechargeSearch1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk

from PyQt5.QtGui import QFont


class rechargeSearch_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(40, 5, 200, 20))
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 70, 50, 25))
        self.label.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(240, 70, 80, 25))
        self.label_3.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, tk.Tk().winfo_screenwidth() * 0.75 - 270,
                                                  tk.Tk().winfo_screenheight() * 0.8 - 60 - 190))
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
        self.phone = QtWidgets.QLineEdit(Form)
        self.phone.setGeometry(QtCore.QRect(540, 70, 150, 25))
        self.phone.setObjectName("phone")
        self.userName = QtWidgets.QLineEdit(Form)
        self.userName.setGeometry(QtCore.QRect(310, 70, 150, 25))
        self.userName.setObjectName("userName")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(470, 70, 80, 25))
        self.label_4.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(700, 70, 80, 25))
        self.label_5.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.search = QtWidgets.QPushButton(Form)
        self.search.setGeometry(QtCore.QRect(930, 70, 150, 25))
        self.search.setObjectName("search")
        self.cardNum = QtWidgets.QLineEdit(Form)
        self.cardNum.setGeometry(QtCore.QRect(80, 70, 150, 25))
        self.cardNum.setText("")
        self.cardNum.setObjectName("cardNum")
        self.branch = QtWidgets.QComboBox(Form)
        self.branch.setGeometry(QtCore.QRect(770, 70, 150, 25))
        self.branch.setObjectName("branch")
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
        self.label.setText(_translate("Form", "卡号："))
        self.label_3.setText(_translate("Form", "用户名称："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "IC卡号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "用户名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "充值金额"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "充值时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "网点编号"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "网点名称"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "操作员编号"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "操作员名称"))
        self.label_4.setText(_translate("Form", "用户手机："))
        self.label_5.setText(_translate("Form", "营业网点："))
        self.search.setText(_translate("Form", "搜索"))
        self.title.setText(_translate("Form", "充值信息查询"))
        self.title.setFont(QFont("Roman times", 12, QFont.Bold))

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=rechargeSearch_Form()
    ui.setupUi(widget)
    # widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())