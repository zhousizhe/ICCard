import hashlib
import random

import pymysql
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QComboBox, QTableWidget, QAbstractItemView, QTableWidgetItem
from PyQt5 import QtCore, QtWidgets

from UI import DButil, chooseBranchController, manageInformationsController
from UI.chooseBranch import ChooseBranch_Form
from PyQt5.QtCore import Qt


def choose_branch(self):
    widget = QtWidgets.QWidget()
    ui = ChooseBranch_Form()
    ui.setupUi(widget)
    ui.serchButton.clicked.connect(lambda: chooseBranchController.serch_branch(self))  # 搜索
    ui.commitButton.clicked.connect(lambda: chooseBranchController.commit_branch(self))  # 确定
    ui.cancelButton.clicked.connect(lambda: chooseBranchController.cancel(self))  # 取消
    self.chooseBranch = widget
    self.chooseBranch.setWindowFlags(Qt.Window)
    self.chooseBranch.show()
    # self.userDetail.raise_()

    table = self.chooseBranch.findChild(QTableWidget, 'tableWidget')
    chooseBranchSql = "SELECT id, branch_no, description, telephone, person, open_time, close_time, user_id, name FROM t_iccard_branch WHERE deleted = 0"
    chooseBranchSqlResult = DButil.conn_excu_sql(chooseBranchSql)
    cur = chooseBranchSqlResult[0]
    conn = chooseBranchSqlResult[1]
    result = cur.fetchall()
    manageInformationsController.province(self, self.form6.findChild(QComboBox, 'comboBox'))
    rows = result
    row = len(result)  # 取得记录个数，用于设置表格的行数
    vol = len(rows[0])  # 取得字段数，用于设置表格的列数
    table.setRowCount(row)
    table.setColumnCount(vol)
    # table = QtWidgets.QTableWidget
    # 初始化加载页面时表格内容不可修改
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    for i in range(row):
        for j in range(vol):
            # print(j)
            temp_data = rows[i][j]  # 临时记录，不能直接插入表格
            if temp_data is None:
                temp_data = ""
            data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
            table.setItem(i, j, data)

    cur.close()
    conn.close()


'''
    添加营业员
    点击保存触发事件
'''
def save_click(self):

    lineEdit = self.form7.findChild(QLineEdit, "lineEdit")
    password = lineEdit.text()
    lineEdit_2 = self.form7.findChild(QLineEdit, "lineEdit_2")
    realPassword = lineEdit_2.text()
    # lineEdit_3 = self.form7.findChild(QLineEdit, "lineEdit_3")
    # operator_id = lineEdit_3.text()
    lineEdit_4 = self.form7.findChild(QLineEdit, "lineEdit_4")
    real_name = lineEdit_4.text()
    lineEdit_5 = self.form7.findChild(QLineEdit, "lineEdit_5")
    id_number = lineEdit_5.text()
    lineEdit_6 = self.form7.findChild(QLineEdit, "lineEdit_6")
    phone = lineEdit_6.text()
    lineEdit_7 = self.form7.findChild(QLineEdit, "lineEdit_7")
    branch_no = lineEdit_7.text()
    lineEdit_8 = self.form7.findChild(QLineEdit, "lineEdit_8")
    branch_name = lineEdit_8.text()
    lineEdit_9 = self.form7.findChild(QLineEdit, "lineEdit_9")
    user_name = lineEdit_9.text()
    comboBox_5 = self.form7.findChild(QComboBox, "comboBox_5")
    role_id = comboBox_5.currentText()

    if user_name.strip() == '' or password.strip() == '' or realPassword.strip() == '' or branch_no.strip() == '':
        if user_name.strip() == '':
            QMessageBox.information(self, "提示信息",
                                    "用户名称不能为空！")
            return

        if password.strip() == '':
            QMessageBox.information(self, "提示信息",
                                    "用户密码不能为空！")
            return

        if realPassword.strip() == '':
            QMessageBox.information(self, "提示信息",
                                    "确认密码不能为空！")
            return

        if branch_no.strip() == '':
            QMessageBox.information(self, "提示信息",
                                    "网点编号不能为空！")
            return
    else:
        if password != realPassword:
            QMessageBox.information(self, "提示信息",
                                    "请确保两次输入密码相同！")
            return
        operator_id = ""
        # 生成递增operator_id
        createOperatorIdSql = "SELECT operator_id FROM t_user_base where deleted=0 ORDER BY operator_id DESC LIMIT 1"
        createOperatorIdSqlResult = DButil.conn_excu_sql(createOperatorIdSql)
        cur = createOperatorIdSqlResult[0]
        conn = createOperatorIdSqlResult[1]
        result = cur.fetchall()
        cur.close()
        conn.close()
        for data in result:
            operator_id = str(int(data[0])+1)
        if role_id == '管理员':
            roleId = 4
        else:
            roleId = 5

            # uid = cacheUtil.getCache("uid")
        userId = random.randrange(1000000000000000000, 9999999999999999999)
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        print(
            "INSERT INTO t_user_base (user_id, user_name, password, operator_id, real_name, id_number, phone, branch_no, branch_name, role_id) "
            "VALUES(%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d) " % (
                userId, user_name, password, operator_id, real_name, id_number, phone, branch_no, branch_name, roleId))
        assistantInsertSql = "INSERT INTO t_user_base (user_id, user_name, password, operator_id, real_name, id_number, phone, branch_no, branch_name, role_id)  " \
                             "VALUES(%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d) " % (userId, user_name, md5.hexdigest(), operator_id, real_name, id_number, phone, branch_no, branch_name, roleId)

    DButil.conn_excu_sql(assistantInsertSql)
    refush(self)
    QMessageBox.information(self, "保存", "添加成功")


'''
    添加营业员
    重置按钮
'''
def refush(self):
    self.form7.findChild(QLineEdit, "lineEdit").clear()
    self.form7.findChild(QLineEdit, "lineEdit_2").clear()
    # self.form7.findChild(QLineEdit, "lineEdit_3").clear()
    self.form7.findChild(QLineEdit, "lineEdit_4").clear()
    self.form7.findChild(QLineEdit, "lineEdit_5").clear()
    self.form7.findChild(QLineEdit, "lineEdit_6").clear()
    self.form7.findChild(QLineEdit, "lineEdit_7").clear()
    self.form7.findChild(QLineEdit, "lineEdit_8").clear()
    self.form7.findChild(QLineEdit, "lineEdit_9").clear()