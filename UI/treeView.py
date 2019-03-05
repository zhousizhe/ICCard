# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treeView.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Tree_View1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setFixedWidth(800)
        Form.setFixedHeight(600)
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(0, 100, 200, 500))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "电动车充点卡管理系统"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "电动车充点卡管理系统"))
        self.treeWidget.setHeaderHidden(True)
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "IC卡"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "办卡"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Form", "充值"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("Form", "IC卡信息管理"))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("Form", "充值信息查询"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "网点"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "创建网点"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("Form", "网点信息管理"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Form", "营业员"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("Form", "添加营业员"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("Form", "营业员信息管理"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("Form", "营业员密码修改"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
