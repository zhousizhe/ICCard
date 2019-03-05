from PyQt5.QtWidgets import QLineEdit, QComboBox, QAbstractItemView, QTableWidget, QTableWidgetItem, QLabel

from UI import DButil, cacheUtil, xmlUtil


def iniquery(self):
    cardNum = self.form4.findChild(QLineEdit, "cardNum")  # 卡号
    userName = self.form4.findChild(QLineEdit, "userName")  # 用户名
    phone = self.form4.findChild(QLineEdit, "phone")  # 手机号
    branch = self.form4.findChild(QComboBox, "branch")  # 网点
    branchlable = self.form4.findChild(QLabel, "label_5")  # 网点
    roleId = cacheUtil.getCache("rid")
    uid = cacheUtil.getCache("uid")
    iccardInformationSql = "SELECT icr.card_no,icr.user_name,icr.charge_amount,icr.charge_time,icr.branch_no,icr.branch_desc,icr.operator_id,icr.operator_name " \
                           "FROM t_iccard_charge_record icr " \
                           "LEFT JOIN t_iccard i " \
                           "ON icr.card_no= i.card_no " \
                           "WHERE 1 =1"
    paralist = []
    if cardNum.text().strip() != '':
        iccardInformationSql = iccardInformationSql+" and i.card_no like '%%%s%%'"
        paralist.append(cardNum.text())
    if userName.text().strip() != '':
        iccardInformationSql = iccardInformationSql+" and i.user_name like '%%%s%%'"
        paralist.append(userName.text())
    if phone.text().strip() != '':
        iccardInformationSql = iccardInformationSql+" and i.phone like '%%%s%%'"
        paralist.append(phone.text())
    if branch.currentText().strip() != '':
        iccardInformationSql = iccardInformationSql+" and i.open_branch_name like '%%%s%%'"
        paralist.append(branch.currentText())
    roleIds = xmlUtil.getValue("ICCard", "roleType", "value")
    roleIdsArr = roleIds.split(",")
    if str(roleId) not in roleIdsArr:  # 管理员权限-配置文件读
        branch.hide()
        branchlable.hide()
        iccardInformationSql = \
            iccardInformationSql + \
            " and icr.branch_desc = (select description from t_iccard_branch WHERE user_id = '%s')"
        paralist.append(uid)
    else:
        branchlable.show()
        branch.show()
    if len(paralist) > 1:
        iccardInformationSql = iccardInformationSql % tuple(paralist)
    elif len(paralist) > 0:
        iccardInformationSql = iccardInformationSql % paralist[0]
    iccardInformationSqlResult = DButil.conn_excu_sql(iccardInformationSql)
    cur = iccardInformationSqlResult[0]
    conn = iccardInformationSqlResult[1]
    result = cur.fetchall()
    cur.close()
    conn.close()
    table = self.form4.findChild(QTableWidget, 'tableWidget')
    rows = result
    row = len(result)  # 取得记录个数，用于设置表格的行数
    if row < 1:
        table.clearContents()
        return
    vol = len(rows[0])  # 取得字段数，用于设置表格的列数
    table.setRowCount(row)
    table.setColumnCount(vol)
    # table = QtWidgets.QTableWidget
    # 初始化加载页面时表格内容不可修改
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
    table.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
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
    branch = self.form4.findChild(QComboBox, "branch")  # 网点
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