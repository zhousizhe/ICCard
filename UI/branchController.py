from PyQt5.QtWidgets import QWidget
import sys
import tkinter as tk

import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

from UI import DButil

sys.path.append("..")
from UI.tree import Ui_Form_Tree_View


class branchCtroller(Ui_Form_Tree_View):
    def __init__(self):
        Ui_Form_Tree_View.__init__(self)

    def test_click(self):

        lineEdit = self.form5.findChild(QLineEdit, "lineEdit")
        branch_no = lineEdit.text()
        comboBox = self.form5.findChild(QComboBox, "comboBox")
        name = comboBox.currentText()
        lineEdit2 = self.form5.findChild(QLineEdit, "lineEdit_2")
        person = lineEdit2.text()
        lineEdit_3 = self.form5.findChild(QLineEdit, "lineEdit_3")
        close_time = lineEdit_3.text()
        comboBox_2 = self.form5.findChild(QComboBox, "comboBox_2")
        province = comboBox_2.currentText()
        comboBox_4 = self.form5.findChild(QComboBox, "comboBox_4")
        district = comboBox_4.currentText()
        lineEdit4 = self.form5.findChild(QLineEdit, "lineEdit_4")
        description = lineEdit4.text()
        print(description+"dddddddddddddddddddddddddddddd")
        lineEdit5 = self.form5.findChild(QLineEdit, "lineEdit_5")
        telephone = lineEdit5.text()
        lineEdit6 = self.form5.findChild(QLineEdit, "lineEdit_6")
        open_time = lineEdit6.text()
        lineEdit7 = self.form5.findChild(QLineEdit, "lineEdit_7")
        mac_address = lineEdit7.text()
        comboBox_3 = self.form5.findChild(QComboBox, "comboBox_3")
        city = comboBox_3.currentText()
        lineEdit9 = self.form5.findChild(QLineEdit, "lineEdit_9")
        address = lineEdit9.text()

        if branch_no.strip() == '' or person.strip() == '' or close_time.strip() == '' or description.strip() == ''or telephone.strip() == '' or open_time.strip() == '' or mac_address.strip() == '' or address.strip() == '':

            if branch_no.strip() == '':
                QMessageBox.information(self, "提示信息",
                                        "网点编号不能为空！")
                return

            if person.strip() == '':
                QMessageBox.information(self, "提示信息",
                                        "网络联系人不能为空！")
                return

            if close_time.strip() == '':
                QMessageBox.information(self, "提示信息",
                                        "结束营业时间不能为空！")
                return

            if description.strip() == '':
                QMessageBox.information(self, "提示信息",
                                        "网点名称不能为空！")
                return

            if telephone.strip() == '':
                QMessageBox.information(self, "提示信息",
                                        "网点电话不能为空！")
                return

            if open_time.strip() == '':
                QMessageBox.information(self, "提示信息",
                                        "开始营业时间不能为空！")
                return

            if mac_address.strip() == '':
                QMessageBox.information(self, "提示信息",
                                        "MAC地址不能为空！")
                return

            if address.strip() == '':
                QMessageBox.information(self, "提示信息",
                                        "详细地址不能为空！")
                return
        else:
            print( "INSERT INTO t_iccard_branch (branch_no, name, person, close_time, province, district, description, telephone, open_time, mac_address, city, address) "
                "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') " % (
                branch_no, name, person, close_time, province, district, description, telephone, open_time, mac_address,
                city, address))
            sql = "INSERT INTO t_iccard_branch (branch_no, name, person, close_time, province, district, description, telephone, open_time, mac_address, city, address)  " \
                  "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') " % (
                branch_no, name, person, close_time, province, district, description, telephone, open_time, mac_address,
                city, address)
            c2c = DButil.conn_excu_sql(sql)
            QMessageBox.information(self, "保存","添加成功")
            self.refush()
            c2c[0].close()
            c2c[1].close()


    def refush(self):
        self.form5.findChild(QLineEdit, "lineEdit").clear()
        self.form5.findChild(QLineEdit, "lineEdit_2").clear()
        self.form5.findChild(QLineEdit, "lineEdit_3").clear()
        self.form5.findChild(QLineEdit, "lineEdit_4").clear()
        self.form5.findChild(QLineEdit, "lineEdit_5").clear()
        self.form5.findChild(QLineEdit, "lineEdit_6").clear()
        self.form5.findChild(QLineEdit, "lineEdit_7").clear()
        self.form5.findChild(QLineEdit, "lineEdit_9").clear()