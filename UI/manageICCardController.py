import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit, QComboBox, QAbstractItemView, QTableWidget, QTableWidgetItem, QMessageBox, QLabel

from UI import DButil, userDetailController, cacheUtil, xmlUtil
from UI.userDetail import Ui_userFrame
from PyQt5.QtCore import Qt


def iniquery(self):
    cardNum = self.form3.findChild(QLineEdit, "cardNum")  # 卡号
    userName = self.form3.findChild(QLineEdit, "userName")  # 用户名
    phone = self.form3.findChild(QLineEdit, "phone")  # 手机号
    branch = self.form3.findChild(QComboBox, "branch")  # 网点
    branchlable = self.form3.findChild(QLabel, "label_5")  # 网点
    roleId = cacheUtil.getCache("rid")
    uid = cacheUtil.getCache("uid")
    iccardInformationSql = "SELECT card_no,ic_money,open_branch_name,open_card_time,open_operator_name," \
                           "blacklist_f,valid_time,user_name,phone,papers_num FROM t_iccard WHERE deleted=0 "
    paralist = []
    if cardNum.text().strip() != '':
        iccardInformationSql = iccardInformationSql+" and card_no like '%%%s%%'"
        paralist.append(cardNum.text())
    if userName.text().strip() != '':
        iccardInformationSql = iccardInformationSql+" and user_name like '%%%s%%'"
        paralist.append(userName.text())
    if phone.text().strip() != '':
        iccardInformationSql = iccardInformationSql+" and phone like '%%%s%%'"
        paralist.append(phone.text())
    if branch.currentText().strip() != '':
        iccardInformationSql = iccardInformationSql+" and open_branch_name like '%%%s%%'"
        paralist.append(branch.currentText())
    roleIds = xmlUtil.getValue("ICCard", "roleType", "value")
    roleIdsArr = roleIds.split(",")
    if str(roleId) not in roleIdsArr:   # 管理员权限-配置文件读
        branch.hide()
        branchlable.hide()
        iccardInformationSql = \
            iccardInformationSql + \
            " and open_operator_name = (select description from t_iccard_branch WHERE user_id = '%s')"
        paralist.append(uid)
    else:
        branch.show()
        branchlable.show()
    if len(paralist) > 1:
        iccardInformationSql = iccardInformationSql % tuple(paralist)
    elif len(paralist) > 0:
        iccardInformationSql = iccardInformationSql % paralist[0]
    iccardInformationSqlResult = DButil.conn_excu_sql(iccardInformationSql)
    cur = iccardInformationSqlResult[0]
    conn = iccardInformationSqlResult[1]
    result = cur.fetchall()
    table = self.form3.findChild(QTableWidget, 'tableWidget')
    rows = result
    row = len(result)  # 取得记录个数，用于设置表格的行数
    cur.close()
    conn.close()
    if row < 1:
        table.clearContents()
        return
    vol = len(rows[0])  # 取得字段数，用于设置表格的列数
    table.setRowCount(row)
    table.setColumnCount(vol)
    # table = QtWidgets.QTableWidget
    # 初始化加载页面时表格内容不可修改
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
    # table.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
    table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只有行选中
    table.clearSelection()  # 取消选中

    for i in range(row):
        for j in range(vol):
            temp_data = rows[i][j]  # 临时记录，不能直接插入表格
            if temp_data is None:
                temp_data = ""
            data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
            table.setItem(i, j, data)


def queryOpenBranchName(self):
    branch = self.form3.findChild(QComboBox, "branch")  # 网点
    branch.clear()
    queryOpenBranchNameSql = "SELECT op.name AS name FROM t_user_operator op LEFT JOIN t_user_base base ON base.user_id = op.user_id WHERE base.deleted = 0"
    queryOpenBranchNameResult = DButil.conn_excu_sql(queryOpenBranchNameSql)
    cur = queryOpenBranchNameResult[0]
    conn = queryOpenBranchNameResult[1]
    result = cur.fetchall()
    cur.close()
    conn.close()
    branchs = ["", ]
    for data in result:
        branchs.append(str(data[0]))
    branch.addItems(branchs)

def cardPin(self):
    table = self.form3.findChild(QTableWidget, 'tableWidget')
    idCardNoList = []
    cardNosString = ""
    selectedRanges = table.selectedRanges()
    tempsize = 1
    for range in selectedRanges:
        row = range.topRow()
        modle = table.model()
        # indexId = modle.index(row, 0)  # 列数据:id
        indexCardNo = modle.index(row, 0)  # 列数据:cardNo
        # dataId = modle.data(indexId)
        dataCardNo = modle.data(indexCardNo)
        cardNosString = cardNosString + dataCardNo + ","
        if tempsize % 3 == 0:
            cardNosString = cardNosString + "\n"
        idCardNoList.append(dataCardNo)
        tempsize = tempsize+1

    if len(selectedRanges) <= 0:
        QMessageBox.warning(self, "错误", "未选中行！", QMessageBox.Close)
        return
    # 获得选中行的id
    reply = QMessageBox.question(self, '警告', "是否要对卡号："+cardNosString+"进行销卡？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
        for no in idCardNoList:
            updateIcCardSql = "UPDATE t_iccard SET deleted = %d,close_card_time='%s' where card_no='%s'" \
                              % (1, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), no)
            try:
                c2c = DButil.conn_excu_sql(updateIcCardSql)
                c2c[0].close()
                c2c[1].close()
            except BaseException:
                QMessageBox.warning(self, "错误", "销卡失败！", QMessageBox.Close)
                return
        QMessageBox.information(self, "成功", "销卡成功！", QMessageBox.Close)
    iniquery(self)

def transfer(self):
    table = self.form3.findChild(QTableWidget, 'tableWidget')
    idCardNoList = []
    cardNosString = ""
    selectedRanges = table.selectedRanges()
    tempsize = 1
    for range in selectedRanges:
        row = range.topRow()
        modle = table.model()
        # indexId = modle.index(row, 0)  # 列数据:id
        indexCardNo = modle.index(row, 0)  # 列数据:cardNo
        # dataId = modle.data(indexId)
        dataCardNo = modle.data(indexCardNo)
        cardNosString = cardNosString + dataCardNo + ","
        if tempsize % 3 == 0:
            cardNosString = cardNosString + "\n"
        idCardNoList.append(dataCardNo)
        tempsize = tempsize + 1

    if len(selectedRanges) <= 0:
        QMessageBox.warning(self, "错误", "未选中行！", QMessageBox.Close)
        return

    widget = QtWidgets.QWidget()
    ui = Ui_userFrame()
    ui.setupUi(widget)
    ui.serchButton.clicked.connect(lambda: userDetailController.serch_userDetail(self))
    ui.commitButton.clicked.connect(lambda: userDetailController.commit_userDetail(self, idCardNoList, cardNosString))
    self.userDetail = widget
    self.userDetail.setWindowFlags(Qt.Tool)
    self.userDetail.show()
    # self.userDetail.raise_()


def removeException(self):
    table = self.form3.findChild(QTableWidget, 'tableWidget')
    idCardNoList = []
    cardNosString = ""
    selectedRanges = table.selectedRanges()
    tempsize = 1
    for range in selectedRanges:
        row = range.topRow()
        modle = table.model()
        # indexId = modle.index(row, 0)  # 列数据:id
        indexCardNo = modle.index(row, 0)  # 列数据:cardNo
        # dataId = modle.data(indexId)
        dataCardNo = modle.data(indexCardNo)
        cardNosString = cardNosString + dataCardNo + ","
        if tempsize % 3 == 0:
            cardNosString = cardNosString + "\n"
        idCardNoList.append(indexCardNo)
        tempsize = tempsize + 1

    if len(selectedRanges) <= 0:
        QMessageBox.warning(self, "错误", "未选中行！", QMessageBox.Close)
        return
    # 获得选中行的id
    reply = QMessageBox.question(self, '警告', "是否要对卡号：" + cardNosString + "进行解除异常？", QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No)
    if reply == QMessageBox.Yes:
        for no in idCardNoList:
            updateIcCardSql = "UPDATE t_iccard SET error_f = %d where card_no='%s'" \
                              % (0, no)
            try:
                c2c = DButil.conn_excu_sql(updateIcCardSql)
                c2c[0].close()
                c2c[1].close()
            except BaseException:
                QMessageBox.warning(self, "错误", "解除异常失败！", QMessageBox.Close)
                return
        QMessageBox.information(self, "成功", "解除异常成功！", QMessageBox.Close)
    iniquery(self)

