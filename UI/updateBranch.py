# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateBranch.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class updateBranch_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 636)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 72, 25))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 210, 41, 25))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(280, 400, 101, 31))
        self.save.setObjectName("save")
        self.names = QtWidgets.QLineEdit(Form)
        self.names.setGeometry(QtCore.QRect(170, 90, 190, 21))
        self.names.setObjectName("names")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 170, 91, 25))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.branchNum = QtWidgets.QLineEdit(Form)
        self.branchNum.setGeometry(QtCore.QRect(170, 50, 190, 21))
        self.branchNum.setObjectName("branchNum")
        self.phone = QtWidgets.QLineEdit(Form)
        self.phone.setGeometry(QtCore.QRect(170, 130, 190, 21))
        self.phone.setObjectName("phone")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 50, 72, 25))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 91, 25))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.person = QtWidgets.QLineEdit(Form)
        self.person.setGeometry(QtCore.QRect(170, 170, 190, 21))
        self.person.setObjectName("person")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(100, 400, 101, 31))
        self.cancel.setObjectName("cancel")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 250, 31, 25))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 290, 31, 25))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(80, 330, 71, 25))
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(170, 330, 190, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.provinces = QtWidgets.QComboBox(Form)
        self.provinces.setGeometry(QtCore.QRect(170, 210, 141, 21))
        self.provinces.setObjectName("provinces")
        self.citys = QtWidgets.QComboBox(Form)
        self.citys.setGeometry(QtCore.QRect(170, 250, 141, 21))
        self.citys.setObjectName("citys")
        self.districts = QtWidgets.QComboBox(Form)
        self.districts.setGeometry(QtCore.QRect(170, 290, 141, 21))
        self.districts.setObjectName("districts")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "网点电话:"))
        self.label_5.setText(_translate("Form", "省:"))
        self.save.setText(_translate("Form", "保存"))
        self.label_4.setText(_translate("Form", "网点联系人:"))
        self.label.setText(_translate("Form", "网点编号:"))
        self.label_2.setText(_translate("Form", "运营商名称:"))
        self.cancel.setText(_translate("Form", "取消"))
        self.label_6.setText(_translate("Form", "市:"))
        self.label_7.setText(_translate("Form", "区:"))
        self.label_8.setText(_translate("Form", "网点名称:"))

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=updateBranch_Form()
    ui.setupUi(widget)
    # widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())